
import fitz

import os

from document_loaders.ocr import extract_text_with_ocr

file_path = os.path.join("document_loaders", "1.pdf")

# PDF Validation and Text Extraction
def pdf_validation_and_text_extraction(file_path):

    validation_result = {
        "valid" : False,
        "exists" : True,
        "corrupted" : False,
        "encrypted" : False,
        "empty" : False,
        "page_count" : 0,
        "page_metadata" : []
    }

    # Existence Check:
    if not os.path.exists(file_path):
        
        validation_result["exists"] = False

        return validation_result
    
    # Corruption Check
    try:
        
        doc = fitz.open(file_path)
    
    except Exception as e:

        validation_result["corrupted"] = True

        return validation_result
    
    # Encrytped Check
    if  doc.needs_pass:
        
        validation_result["encrypted"] = True
    
        doc.close()

        return validation_result
    
    # Page count 
    page_count = doc.page_count

    if page_count == 0:

        validation_result["empty"] = True

        doc.close()

        return validation_result
    
    else:

        validation_result["page_count"] = page_count

    # Empty pdf detection flag
    has_any_text = False

    # Loop through doc
    for page_number, page in enumerate(doc, start=1):

        page_text = ""

        use_ocr = False

        has_images = bool(page.get_images())


        if has_images:

            use_ocr = True

            page_text = extract_text_with_ocr(page)
        
        else:

            use_ocr = False

            page_text = page.get_text().strip()

        # Check if any text exists in the document
        if page_text.strip():

            has_any_text = True
        

        validation_result["page_metadata"].append({
            "page_number" : page_number,
            "text" : page_text,
            "ocr" : use_ocr
        }) 

        

    # Empty Pdf Check
    if not has_any_text:

        validation_result["empty"] = True

        doc.close()

        return validation_result
    
    validation_result["valid"] = True

    doc.close()

    return  validation_result



