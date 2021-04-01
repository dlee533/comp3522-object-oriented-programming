python crypto.py abcd1234 -s "Test Data to be encrypted"

python crypto.py abcd1234 -f "inputFile.txt"

python crypto.py -f "inputFile.txt" abcd1234

python crypto.py abcd1234 --file "inputFile.txt"

python crypto.py abcd1234 -f "inputFile.txt" -m en

python crypto.py abcd1234 -f "inputFile1.txt" -m de

python crypto.py abcd1234 -f "inputFile1.txt" -m de --output print

python crypto.py abcd1234 -s b'\xe6\xad\xdf#\x895T\xbe\xd5\xcb\xf9\x17\x8d\xb3T\x01\xcf\x80\xc8QF\x9f\xf8FWO\xef`\xc2\xeaJ\xd9' -m de --output "output.txt"
