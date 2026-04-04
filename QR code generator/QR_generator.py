import qrcode as qr
img = qr.make('Hello guys, this is a QR code generator using Python. You can create your own QR code by changing the text in the make() function. Enjoy!')
img.save("qr_code.png")