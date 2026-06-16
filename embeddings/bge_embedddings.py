"""
BGE Embeddings

Generate semantic embeddings using BAAI's open-source BGE embedding
models through LangChain and Hugging Face.

Common customizable features:
    - model_name: Specifies the BGE embedding model.
    - model_kwargs: Configures device settings (CPU/GPU).
    - encode_kwargs: Controls embedding generation behavior.

Supports:
    - embed_query()
    - embed_documents()

Popular BGE models:
    - BAAI/bge-small-en-v1.5  (384 dimensions)
    - BAAI/bge-base-en-v1.5   (768 dimensions)
    - BAAI/bge-large-en-v1.5  (1024 dimensions)
    - BAAI/bge-m3             (1024 dimensions)

BGE models are free, open-source, and can be run locally without
requiring an API key.

Unlike OpenAI and Gemini embedding models, BGE embeddings do not
support configurable output dimensions. Each model has a fixed
embedding size determined by the model architecture.
"""



from langchain_huggingface import HuggingFaceEmbeddings


def bge_embeddings_with_embed_query(text: str) -> list[float]:
    """
    Convert a single text string into a semantic embedding vector.

    Features:
        - model_name: Selects the BGE embedding model.
        - model_kwargs: Configures execution device.
        - encode_kwargs: Controls embedding behavior.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    vector = embeddings.embed_query(text)

    return vector




def bge_embeddings_with_embed_documents(texts: list[str]) -> list[list[float]]:
    """
    Convert a list of text strings into semantic embedding vectors.

    Features:
        - model_name: Selects the BGE embedding model.
        - model_kwargs: Configures execution device.
        - encode_kwargs: Controls embedding behavior.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    vectors = embeddings.embed_documents(texts)

    return vectors