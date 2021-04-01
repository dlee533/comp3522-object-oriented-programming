import os
import abc
import des
import ast


class BaseCryptoHandler(abc.ABC):
    """
    Abstract base class for all handlers that handle encryption or decryption requests.
    """
    def __init__(self, next_handler=None):
        """
        :param next_handler: a BaseCryptoHandler
        """
        self._next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request):
        """
        Handles a request. Handling will vary according to the particular
        concrete handler implementation.
        :param request: a Request object
        :return: None (abstract method), concrete methods will invoke handle request method
        for next handler (if any)
        """
        pass

    def set_handler(self, handler):
        """
        Set the next handler in the chain.
        :param handler: a BaseCryptoHandler
        """
        self._next_handler = handler


class EncryptionHandler(BaseCryptoHandler):
    """
    Handles the encryption of data in the request.
    """
    def handle_request(self, new_request):
        """
        Encrypts the data in the request.
        :param new_request: a Request object
        :return: a tuple where the first element is a string that indicates successful handling of the
        request or not, or if there is a next handler, invokes the next handler to handle the request
        """
        des_key = des.DesKey(b"%b" % new_request.key.encode('utf8'))
        if new_request.data_input:
            new_request.result = des_key.encrypt(bytes(new_request.data_input, 'utf8'), padding=True)
        else:
            with open(new_request.input_file, mode='r') as file:
                data = file.read()
                new_request.result = des_key.encrypt(bytes(data, 'utf8'), padding=True)
        if not self._next_handler:
            return "", True
        return self._next_handler.handle_request(new_request)


class DecryptionHandler(BaseCryptoHandler):
    """
    Concrete handler to decrypt request data.
    """
    def handle_request(self, new_request):
        """
        Decrypts the data in the request.
        :param new_request: a Request object
        :return: a tuple where the first element is a string that indicates successful handling of the
        request or not, or if there is a next handler, invokes the next handler to handle the request
        """
        des_key = des.DesKey(b"%b" % new_request.key.encode('utf8'))
        if new_request.data_input:
            new_request.result = des_key.decrypt(ast.literal_eval(new_request.data_input), padding=True)
        else:
            with open(new_request.input_file, mode='rb') as file:
                data = file.read()
                new_request.result = des_key.decrypt(data, padding=True)
        if not self._next_handler:
            return "", True
        return self._next_handler.handle_request(new_request)


class KeyHandler(BaseCryptoHandler):
    """
    Concrete handler to validate encryption/decryption key.
    """
    def handle_request(self, new_request):
        """
        Checks to see if the key is valid.
        :param new_request: Request
        """
        valid_length = (8, 16, 24)
        if len(new_request.key) in valid_length:
            return ("", True) if not self._next_handler else self._next_handler.handle_request(new_request)
        else:
            return "Length of the key is invalid", False


class ValidateInputHandler(BaseCryptoHandler):
    """
    Concrete handler to validate input to encryption/decryption.
    """
    def handle_request(self, new_request):
        """
        Checks if the input file/data is valid.
        :param new_request: Request
        """
        if new_request.data_input is None or new_request.input_file is None:
            if (new_request.data_input is not None) or (new_request.input_file is not None
                                                        and os.path.isfile(new_request.input_file)):
                return ("", True) if not self._next_handler else self._next_handler.handle_request(new_request)
        return "The input is invalid", False


class OutputHandler(BaseCryptoHandler):
    """
    Concrete handler to output the result.
    """
    def handle_request(self, new_request):
        """
        output the result based on the output value.
        :param new_request: Request
        """
        message = ""
        if new_request.output == "print":
            print(new_request.result)
        else:
            with open(new_request.output, mode="bw") as file:
                file.write(new_request.result)
                message = "Check '" + new_request.output + "'"
        return message, True
