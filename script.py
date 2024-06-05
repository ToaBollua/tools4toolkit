import sys
import subprocess

try:
    import qrcode
except ImportError:
    print("qrcode library is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode"])
    print("qrcode library installed successfully!")
    import qrcode

def generate_qr_code():
    user_input = input("Enter the text or URL to generate a QR code: ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    print("QR code generated and saved as qr_code.png")

if __name__ == "__main__":
    generate_qr_code()