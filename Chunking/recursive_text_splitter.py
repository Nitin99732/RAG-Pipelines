from  langchain_text_splitters import RecursiveCharacterTextSplitter

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


    
def chunking_with_create_document(text):

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

