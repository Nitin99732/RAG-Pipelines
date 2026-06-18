import xml.etree.ElementTree as ET

from langchain_core.documents import Document


def xml_chunking(xml_text: str) -> list[Document]:

    """
    Split XML using tags.
    """

    root = ET.fromstring(xml_text)

    chunks = []

    for child in root:

        chunks.append(
            Document(
                page_content=ET.tostring(
                    child,
                    encoding="unicode"
                ),
                metadata={
                    "tag": child.tag
                }
            )
        )

    return chunks