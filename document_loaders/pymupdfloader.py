from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from pathlib import Path


def pdf_loader(file_path: str) -> list[Document]:
    """
    Load a pdf and return a list of LangChain Document objects.
    """
    
    # Validate that file exists
    if not file_path.exists():

        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate the file extension 
    if file_path.suffix.lower() != ".pdf":

        raise ValueError(f"Expected a pdf file, got'{file_path.suffix}' instead.")
    
    # Load the pdf
    loader = PyMuPDFLoader(file_path)

    try: 
        docs = loader.load()
    except Exception as e:
        raise RuntimeError(f"Failed to laod PDF: {e}") from e
    
    # Validate that pages were extracted
    if not docs:

        raise ValueError("The pdf contains not extractable pages.")
    

    return docs


file_path = Path("book.pdf")

loader = pdf_loader(file_path)

    