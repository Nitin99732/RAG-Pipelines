from  langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def get_token_splitter() -> RecursiveCharacterTextSplitter:

    """
    Create and return a token-aware
    RecursiveCharacterTextSplitter.

    The splitter recursively attempts to split text using:
        Paragraphs -> Lines -> Words -> Characters
    
    Chunk size and chunk overlap are measured in tokens.

    Chunk overlap helps preserve context between adjacent chunks.
    """

    return RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size = 100, 
        chunk_overlap = 20
    )



def chunking_with_split_text(text : str) -> list[str]:

    """
    Split text into chunks 
    based on token count.

    Input : str

    Output : list[str]
    """


    splitter = get_token_splitter()

    chunks = splitter.split_text(text)

    return chunks


    
def chunking_with_create_document(text : str) -> list[Document]:

    """
    Split text into LangChain Document chunks
    based on token count and attach chunk
    numbers as metadata.

    Input : str

    Output : list[Document]
    """
    
    splitter = get_token_splitter()

    chunks = splitter.create_documents([text])

    for i, doc in enumerate(chunks, start=1):

        doc.metadata["chunk_number"] = i 

    return chunks



def chunking_with_split_documents(documents : list[Document]) -> list[Document]:

    """
    Split LangChain Document objects into smaller 
    Document chunks based on token count
    while preserving metadata.

    Input : list[Document]

    Output : list[Document]
    """

    splitter = get_token_splitter()

    chunks = splitter.split_documents(documents)

    return chunks


def chunking_with_transform_documents(documents : list[Document]) -> list[Document]:

    """
    Transform LangChain Document objects into smaller 
    Document chunks based on token count
    while preserving metadata.

    Input : list[Document]

    Output : list[Document]
    """

    splitter = get_token_splitter()

    chunks = splitter.transform_documents(documents)

    return chunks
