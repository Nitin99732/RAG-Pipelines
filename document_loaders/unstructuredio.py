"""
Production-Ready Document Parsing with Unstructured

Pipeline
--------
Upload Document
        ↓
Partition Document
        ↓
Filter Elements
        ↓
Clean Elements
        ↓
Return Clean Elements

Supports:
- PDF
- DOCX
- PPTX
- HTML
- TXT
- Images
- CSV
- XML
- Emails
"""

from pathlib import Path

from unstructured.partition.auto import partition
from unstructured.documents.elements import (
    Title,
    NarrativeText,
    ListItem,
    Table,
    Image,
)
from unstructured.cleaners.core import (
    clean_extra_whitespace,
    replace_unicode_quotes,
    group_broken_paragraphs,
)

# ==========================================================
# Configuration
# ==========================================================

KEEP_ELEMENTS = (
    Title,
    NarrativeText,
    ListItem,
    Table,
    Image
)


# ==========================================================
# Step 1 - Parse Document
# ==========================================================

def parse_document(file_path: str):
    """
    Parse a document using Unstructured.

    Returns:
        List[Element]
    """

    return partition(

        # Uploaded document
        filename=str(Path(file_path)),

        # auto | fast | hi_res | ocr_only
        strategy="auto",

        # Preserve table rows & columns
        infer_table_structure=True,

        # OCR languages
        languages=["eng"],

        # Insert PageBreak elements
        include_page_breaks=False,

        # Multimodal RAG

        # Extract images
        extract_image_block_types=["Image"],

        # Store images as Base64
        extract_image_block_to_payload=True,

        # Return raw elements
        chunking_strategy=None,
    )


# ==========================================================
# Step 2 - Inspect Elements
# ==========================================================

def inspect_elements(elements):
    """
    Print the first few parsed elements.
    """

    print(f"\nTotal Elements: {len(elements)}\n")

    for element in elements[:10]:
        print("-" * 80)
        print("Category :", element.category)
        print("Page     :", element.metadata.page_number)
        print("Text     :", element.text[:120])


# ==========================================================
# Step 3 - Filter Elements
# ==========================================================

def filter_elements(elements):
    """
    Keep only useful elements for RAG.
    """

    return [
        element
        for element in elements
        if isinstance(element, KEEP_ELEMENTS)
    ]


# ==========================================================
# Step 4 - Clean Elements
# ==========================================================

def clean_elements(elements):
    """
    Clean extracted text.
    """

    for element in elements:

        element.apply(replace_unicode_quotes)

        element.apply(clean_extra_whitespace)

        if isinstance(element, NarrativeText):
            element.apply(group_broken_paragraphs)

    return elements


# ==========================================================
# Step 5 - Example Usage
# ==========================================================

if __name__ == "__main__":

    FILE_PATH = "book.pdf"

    # Parse
    elements = parse_document(FILE_PATH)

    # Inspect
    inspect_elements(elements)

    # Filter
    filtered_elements = filter_elements(elements)

    # Clean
    cleaned_elements = clean_elements(filtered_elements)

    print(f"\nClean Elements: {len(cleaned_elements)}")