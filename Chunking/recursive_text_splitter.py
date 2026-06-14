from  langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader 
from langchain_core.documents import Document

def get_text_splitter() -> RecursiveCharacterTextSplitter:

    """
    Create and return a RecursiveCharacterTextSplitter instance.

     The splitter recursively attempts to split text using:
        Paragraphs -> Lines -> Words -> Characters

    Chunk overlap helps preserve context between adjacent chunks.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size = 100, 
        chunk_overlap = 30
    )



def chunking_with_split_text(text : str) -> list[str]:

    """
    Split raw text into chunks

    Input : str

    Output : list[str]
    """

    splitter = get_text_splitter()

    chunks = splitter.split_text(text)

    return chunks


    
def chunking_with_create_document(text : str) -> list[Document]:

    """
    Split text into Langchain document objects 
    and attach chunk numbers as metadata.

    Input : str

    Output : list[document]
    """

    splitter = get_text_splitter()

    chunks = splitter.create_documents([text])

    for i, doc in enumerate(chunks, start=1):

        doc.metadata["chunk_number"] = i 

    return chunks



def chunking_with_split_documents(documents : list[Document]) -> list[Document]:

    """
    Split LangChain Document objects into smaller 
    Document chunks while preserving metadata.

    Input : list[Document]

    Output : list[Document]
    """

    splitter = get_text_splitter()

    chunks = splitter.split_documents(documents)

    return chunks


def chunking_with_transform_documents(documents : list[Document]) -> list[Document]:

    """
    Transform LangChain Document objects into smaller 
    Document chunks while preserving metadata.

    Input : list[Document]

    Output : list[Document]
    """

    splitter = get_text_splitter()

    chunks = splitter.transform_documents(documents)

    return chunks
