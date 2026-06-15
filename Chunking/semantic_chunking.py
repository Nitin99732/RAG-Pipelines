from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


def get_semantic_chunker() -> SemanticChunker:

    """
    Create and return SemanticChunker.

    The splitter groups sentences together
    based on semantic similarity.

    Topic changes are detected using
    sentence embeddings and cosine similarity.
    """

    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding
    )


def get_semantic_chunker_with_percentile() -> SemanticChunker:

    """
    Create chunk boundaries based on
    large drops in semantic similarity.
    """
    
    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding,
        breakpoint_threshold_type="percentile"
    )


def get_semantic_chunker_with_standard_deviation() -> SemanticChunker:
    
    """
    Split chunks based on 
    similarity that are 
    unusually low.

    Threshold = Mean - k(sd)
    """

    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding,
        breakpoint_threshold_type="standard_deviation"
    )


def get_semantic_chunker_with_interquartile() -> SemanticChunker:
    
    """
    Split chunks based on 
    Q1, Q3 and IQR.

    More robust for outliers
    """

    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding,
        breakpoint_threshold_type="interquartile"
    )


def get_semantic_chunker_with_gradient() -> SemanticChunker:
    
    """
    Split chunks based on 
    sudden change in similarity.
    """

    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding,
        breakpoint_threshold_type="gradient"
    )


def get_semantic_chunker_with_thres_amount() -> SemanticChunker:

    """
    Control chunking sensitivity by adjusting
    the breakpoint threshold amount.

    Higher values create fewer chunks.
    Lower values create more chunks.    
    """

    embedding = OpenAIEmbeddings()

    return SemanticChunker(
        embedding,
        breakpoint_threshold_amount=90
    )


def get_semantic_chunker_with_num_chunks() -> SemanticChunker:

    """
    Attempt to create approximately
    the specified number of chunks.
    """

    embedding = OpenAIEmbeddings()


    return SemanticChunker(
        embedding,
        number_of_chunks=10
    )


def chunking_with_split_text(text : str) -> list[str]:

    """
    Split text into semantically 
    meaningful chunks.

    Input : str

    Output : list[str]
    """

    splitter = get_semantic_chunker()

    chunks = splitter.split_text(text)

    return chunks


def chunking_with_create_documents(text : str) -> list[Document]:

    """
    Split text into semantic 
    LangChain Document chunks.

    Input : str
    
    Output : list[Document]
    """

    splitter = get_semantic_chunker()

    docs = splitter.create_documents([text])

    for i, doc in enumerate(docs, start=1):

        doc.metadata["chunk_number"] = i

    return docs


def chunking_with_transform_documents(documents : list[Document]) -> list[Document]:

    """
    Split LangChain Documents into 
    semantic Document chunks.

    Input : list[Document]
    
    Output : list[Document]
    """

    splitter = get_semantic_chunker()

    docs = splitter.transform_documents(documents)

    return docs

