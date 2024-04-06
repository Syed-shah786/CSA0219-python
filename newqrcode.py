# Import the qrcode module
import qrcode

# Define the data (URL) you want to encode in the QR code
data = 'https://agrodirection1.wordpress.com/'

# Create a QRCode instance with specified version, box_size, and border parameters
qr = qrcode.QRCode(version=10, box_size=20, border=5)

# Add the data to the QRCode instance
qr.add_data(data)

# Generate the QR code using the make() method with fit=True
qr.make(fit=True)

# Create an image of the QR code with specified fill_color and back_color
img = qr.make_image(fill_color='GREEN', back_color='WHITE')

# Save the generated QR code image to a file named 'my_qr_code.png'
img.save('my_qr_code.png')
