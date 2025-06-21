import pyqrcode
qr = qrcode.QRcode(version=1, box_size=10,border=5)
data=input("Enter any url you want as a QR code: ")
qr.add_data(data)
qr.make(fit=true)
img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")
