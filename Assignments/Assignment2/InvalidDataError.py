class InvalidDataError(Exception):
    """
    Exception for invalid data.
    """
    def __init__(self, msg):
        """
        Initializes InvalidDataError.
        :param msg: message to store in object
        """
        msg = "Could not process order, data was corrupted, " + msg
        super(InvalidDataError, self).__init__(msg)
