# Libraries
import os

from langchain_community.document_loaders import TextLoader

file_path = os.path.join("document_loaders", "2.txt")

# Txt file validation and text extraction
def txt_validation_and_text_extraction(file_path):

    validation_result = {
        "valid" : False,
        "exists" : True,
        "utf_8" : True,
        "empty" : False,
        "text" : "",
        "metadata" : None
    }

    # Check if file exists
    if not os.path.exists(file_path):

        validation_result["exists"] = False

        return validation_result
    
    # File loading and utf-8 check
    try: 

        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()

    except UnicodeDecodeError:

        validation_result["utf_8"] = False

        return validation_result

    # Text extraction
    text = docs[0].page_content.strip()

    # Empty file check
    if not text:

        validation_result["empty"] = True

        return validation_result

        
    validation_result["text"] = text

    # Valid file
    validation_result["valid"] = True
    validation_result["metadata"] = docs[0].metadata

    return validation_result



    
