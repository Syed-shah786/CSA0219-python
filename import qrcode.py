# import the qrcode module
import qrcode

# define the data (url) you want to encode in the QR code
data = 'https://arms.sse.saveetha.com/Login.aspx?s=exp'

# generate a QR code imageusing the qrcode.make() function
img = qrcode.make(data)

# save the generated QR code image to a file named 'my_qr_code.png'
img.save('my_qr_code.png')