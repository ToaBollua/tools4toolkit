import sys
import subprocess

try:
    import barcode
    from barcode.writer import ImageWriter
    from PIL import Image
except ImportError:
    print("python-barcode or Pillow library is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode", "Pillow"])
    print("python-barcode and Pillow libraries installed successfully!")
    import barcode
    from barcode.writer import ImageWriter
    from PIL import Image

def generate_barcode():
    user_input = input("Enter the data to generate a barcode: ")
    EAN = barcode.EAN13(user_input, writer=ImageWriter())
    filename = EAN.save(user_input)

    print(f"Barcode generated and saved as {filename}")

if __name__ == "__main__":
    generate_barcode()