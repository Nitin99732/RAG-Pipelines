from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

def markdown_chunking(text : str) -> list[Document]:

    """
    Split markdown text bases 
    on header structure.

    Input : str

    Output : list[Document]
    """

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2")
    ]

    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )

    docs = splitter.split_text(text)

    return docs

sample_markdown = """
# Artificial Intelligence

AI is transforming technology.

## Machine Learning

Machine Learning is a subset of AI.

## Deep Learning

Deep Learning uses neural networks.

# Retrieval Augmented Generation

RAG combines retrieval and generation.
"""

for doc in markdown_chunking(sample_markdown):
    print(doc.metadata)
    print(doc.page_content)