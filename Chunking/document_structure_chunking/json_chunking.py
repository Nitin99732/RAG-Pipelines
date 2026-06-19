import json

from langchain_core.documents import Document


def json_chunking(json_text: str) -> list[Document]:

    """
    Split JSON using top-level keys.
    """

    data = json.loads(json_text)

    chunks = []

    for key, value in data.items():

        chunks.append(
            Document(
                page_content=json.dumps(
                    value,
                    indent=2
                ),
                metadata={
                    "key": key
                }
            )
        )

    return chunks