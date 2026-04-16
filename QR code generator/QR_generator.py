import qrcode as qrc
from PIL import Image

# simple way to create a QR Code
#img = qrc.make('Hello guys, this is a QR code generator using Python. You can create your own QR code by changing the text in the make() function. Enjoy!')
#img.save("qr_code.png")

qr = qrc.QRCode(version = 1, 
                   error_correction = qrc.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

qr.add_data(" ")

