"""
Google Gemini Embeddings

Generate semantic embeddings using Google's Gemini embedding models
through LangChain.

Common customizable features:
    - model: Gemini embedding model name.
    - output_dimensionality: Size of the returned embedding vector.
    - google_api_key: Authentication key for the Gemini API.
    - task_type: Embedding optimization strategy for specific use cases.

Supports:
    - embed_query()
    - embed_documents()
    - aembed_query()
    - aembed_documents()

Gemini embeddings are conceptually similar to OpenAI embeddings, with
the addition of the `task_type` parameter that allows embeddings to be
optimized for retrieval, semantic similarity, clustering, and other tasks.
"""


from langchain_google_genai import GoogleGenerativeAIEmbeddings


def gemini_embeddings_with_embed_query(text: str) -> list[float]:
    """
    Convert a single text string into a semantic embedding vector.

    Features:
        - model: Selects the Gemini embedding model.
        - output_dimensionality: Controls the size of the output vector.
        - google_api_key: Authenticates API requests.
        - task_type: Optimizes embeddings for a specific task.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        output_dimensionality=3072,
        google_api_key="AIza...",
        task_type="RETRIEVAL_QUERY"
    )

    vector = embeddings.embed_query(text)

    return vector