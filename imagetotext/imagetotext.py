import pytesseract as tess
from pyzbar.pyzbar import decode
from PIL import Image
import csv

data = decode(Image.open("qr.jpg"))
# if len(data) > 1:
print(data[0].data.decode())
# Set the path to the Tesseract executable
tess.pytesseract.tesseract_cmd = r'C:\Users\Ravi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Open the image using PIL (Pillow)
img = Image.open('qr.jpg')

# Use pytesseract to extract text from the image
extracted_text = tess.image_to_string(img)

# Define the CSV file path where you want to save the extracted text
csv_file_path = 'extracted_text.csv'

# Split the extracted text into lines (assuming each line represents a row in the CSV)
lines = extracted_text.split('\n')

# Write the extracted text to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    for line in lines:
        # Write each line as a row in the CSV file
        csv_writer.writerow([line])

print(f"Extracted text has been saved to '{csv_file_path}'")