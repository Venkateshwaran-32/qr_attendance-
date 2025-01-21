# Import library for QR code generation
import pyqrcode

# Define the URL of the web app
url = "http://127.0.0.1:5000"  # Replace with your deployed web app URL later

# Generate the QR code
qr_code = pyqrcode.create(url)
qr_code.png("qr_code.png", scale=6)  # Save the QR code as an image
print("QR Code generated successfully! Check qr_code.png.")
