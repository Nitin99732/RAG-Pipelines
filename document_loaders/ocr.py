# Libraries
import numpy as np
from PIL import Image

import os

os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

from paddleocr import PaddleOCR

# OCR Model
ocr_model = PaddleOCR(lang="en")


# OCR Function
def extract_text_with_ocr(page):

    # Convet PDF Page to Image
    pix = page.get_pixmap(dpi=300)

    # Convert Pixmap to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Convet PIL Image to NumPy Array
    img_array = np.array(img)

    # Run OCR
    result = ocr_model.predict(img_array)

    # Extract Text
    extracted_text = ""

    if result:

        texts = result[0]["rec_texts"]

        for text in texts:

            extracted_text += text + "\n"

    return extracted_text.strip()