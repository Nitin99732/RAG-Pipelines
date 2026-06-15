from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def get_parent_splitter() -> RecursiveCharacterTextSplitter:

    """
    Create and return a parent splitter.

    Parent chunks are larger chunks
    that peserve broader context.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )


def get_child_splitter() -> RecursiveCharacterTextSplitter:

    """
    Create and return a child splitter.

    Child chunks are smaller chunks
    used for fine-grained retrieval.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )


def create_parent_chunks(text : str) -> list[Document]:

    """
    Split text into
    parent chunks

    Input : str

    Output : list[Document]
    """

    splitter = get_parent_splitter()

    parents = splitter.create_documents([text])

    for i, parent in enumerate(parents, start=1):

        parent.metadata["parent_id"] = i

    return parents


def create_child_chunks(parents : list[Document]) -> list[Document]:

    """
    Split parent chunks into child chunks 
    and attach parent-child relationships.

    Input : list[Document]

    Ouptut : list[Document]
    """

    splitter = get_child_splitter()

    childern = []

    child_id = 1

    for parent in parents:

        parent_id = parent.metadata["parent_id"]

        child_docs = splitter.create_documents([parent.page_content])

        for child in child_docs:

            child.metadata["child_id"] = child_id

            child.metadata["parent_id"] = parent_id

            childern.append(child)

            child_id += 1

    return childern


def hierarhical_chunking(text : str) -> tuple[list[Document], list[Document]]:

    """
    Create parent and child chunks

    Input : str 

    Output : tuple[parent_chunks, child_chunks]
    """

    parents = create_parent_chunks(text)

    childern = create_child_chunks(parents)

    return parents, childern