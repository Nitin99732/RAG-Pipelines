"""
OpenAI Embeddings Configuration

This module demonstrates how to generate semantic embeddings using
OpenAI's embedding models through LangChain.

Supported customization options include:

- model:
    Specifies the embedding model to use (e.g.,
    'text-embedding-3-small' or 'text-embedding-3-large').

- dimensions:
    Controls the size of the returned embedding vector.
    Lower dimensions reduce storage requirements while higher
    dimensions may improve retrieval quality.

- api_key:
    Authentication credential used to access the OpenAI API.

- organization:
    Optional OpenAI organization identifier used for account
    and billing management when working with multiple organizations.

- base_url:
    Optional custom endpoint for OpenAI-compatible providers,
    Azure OpenAI deployments, or internal API gateways.

- max_retries:
    Maximum number of retry attempts for transient API failures.

- timeout:
    Maximum time (in seconds) to wait for an API response before
    raising a timeout exception.

The embedding model converts text into a numerical vector representation
that captures semantic meaning and can be used for similarity search,
retrieval, clustering, classification, and other NLP tasks.
"""


from langchain_openai import OpenAIEmbeddings

def openai_embeddings_with_embed_query(text : str) -> list[float]:

    """
    text-embedding-3-small

    Default dimensions: 1536

    Supports reduced dimensions via the dimensions parameter,
    up to a maximum of 1536.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        dimensions=1536,
        api_key="sk-...",
        max_retries=5,
        timeout=60
    )

    vector = embeddings.embed_query(text)

    return vector


def openai_embeddings_with_embed_documents(texts : list[str]) -> list[list[float]]:

    """
    text-embedding-3-large

    Default dimensions: 3072

    Supports reduced dimensions via the dimensions parameter,
    up to a maximum of 3072.    
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        dimensions=3072,
        api_key="sk-...",
        max_retries=5,
        timeout=60
    )

    vector = embeddings.embed_query(texts)

    return vector





"""
Asynchronous Embedding Methods

The aembed_query() and aembed_documents() methods are asynchronous
versions of embed_query() and embed_documents().

Unlike synchronous methods, asynchronous methods do not block the
current task while waiting for an API response. This allows multiple
embedding requests to run concurrently, improving throughput in
web applications, APIs, and large-scale document processing workflows.
"""


async def openai_embeddings_with_aembed_query(text: str) -> list[float]:

    """
    Convert a single text string into a semantic embedding vector asynchronously.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        dimensions=1536,
        api_key="sk-...",
        max_retries=5,
        timeout=60
    )

    vector = await embeddings.aembed_query(text)

    return vector


async def openai_embeddings_with_aembed_documents(texts: list[str]) -> list[list[float]]:
    
    """
    Convert a list of text strings into semantic embedding vectors asynchronously.

    Returns one embedding vector per input text.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        dimensions=3072,
        api_key="sk-...",
        max_retries=5,
        timeout=60
    )

    vectors = await embeddings.aembed_documents(texts)

    return vectors

