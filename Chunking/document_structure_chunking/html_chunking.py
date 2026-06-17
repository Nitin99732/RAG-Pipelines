from langchain_text_splitters import HTMLHeaderTextSplitter
from langchain_core.documents import Document



def get_html_splitter() -> HTMLHeaderTextSplitter:
    """
    Create and return HTMLHeaderTextSplitter.

    Split HTML documents based on:
        h1 -> h2 -> h3
    """

    return HTMLHeaderTextSplitter(
        headers_to_split_on=[
            ("h1", "Header 1"),
            ("h2", "Header 2"),
            ("h3", "Header 3")
        ]
    )

def html_chunking(html_text : str) -> list[Document]:
    """
    Split html text into structured 
    Document chunks.

    Input : str

    Output : list[Document]
    """

    splitter = get_html_splitter()

    chunks = splitter.split_text(html_text)

    return chunks