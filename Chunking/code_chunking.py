from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def get_code_splitter() -> RecursiveCharacterTextSplitter:

    """
    Create and return Python-aware
    RecursiveCharacterTextSplitter.

    The splitter attempts to split code using:
       Classes -> Functions -> Methods

    Chunk overlap helps preserve context 
    between adjacent chunks.

    Support multiple programming languages:
    Language.PYTHON
    Language.JS
    Language.TS
    Language.JAVA
    Language.CPP
    Language.GO
    Language.RUST
    Language.PHP
    Language.CSHARP
    ...
    """

    return RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=500,
        chunk_overlap=100
    )



def code_chunking(code : str) -> list[str]:
    """
    Split python code into chunks.

    The underlying splitter also supports:
    - create_documents()
    - split_documents()
    - transform_documents()
    """

    splitter = get_code_splitter()

    chunks = splitter.split_text(code)

    return chunks