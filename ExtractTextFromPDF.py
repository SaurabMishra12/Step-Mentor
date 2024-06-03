import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import fitz
import pytesseract
from PIL import Image
import io
import pandas as pd
import re


# Specify the teseract patH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extractTxtFromPdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = []

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text_page = page.get_text("text")
        text.append(text_page)

        # Extracting images for OCR
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(r'C:\Users\msaur\Downloads')

            # Use Tesseract to do OCR on the image
            ocr_text = pytesseract.image_to_string(image)
            text.append(ocr_text)

    return text


def clean_text(text):
    # Basic cleaning: remove extra spaces, line breaks, etc.
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def text_to_csv(text, csv_path):
    # Create a DataFrame from the text
    df = pd.DataFrame({"Page": range(1, len(text) + 1), "Content": text})

    # Save DataFrame to CSV
    df.to_csv(csv_path, index=False)


# Path to your PDF file
pdf_path = r'C:\Users\msaur\Documents\projects python\GUI\2020 jeeData.pdf'
text_content = extractTxtFromPdf(pdf_path)

# Clean extracted text
cleaned_text = [clean_text(page) for page in text_content]

# Path to save the CSV file
csv_path = 'userdevelopment.csv'
text_to_csv(cleaned_text, csv_path)

# Print cleaned text (optional)
for page_num, page_text in enumerate(cleaned_text):
    print(f"Page {page_num + 1}:\n{page_text}\n")
