"""
Llama Parse handles 130+ document formats.

Pipeline
--------
Upload File
    ↓
Layout Analysis
    ↓
Native Text Extraction
OCR (only when needed)
Table Parsing
Chart Parsing
    ↓
Document Reconstruction
    ↓
Markdown / Metadata / Items
"""

from llama_cloud import LlamaCloud

# Instantiate client (reads LLAMA_CLOUD_API_KEY from environment by default)
client = LlamaCloud()

upload_file = client.files.create(file="doc.pdf", purpose="parse")

result = client.parsing.parse(
    file_id=upload_file.id,

    # fast < cost_effective < agentic (recommended) < agentic_plus
    tier="agentic",

    # Pin a specific version in production if reproducibility is required
    version="latest",

    # Reuse previous parsing result
    disable_cache=False,

    # Parse only required pages
    # Limit how many maximum pages to parse
    # Remove this block to parse the entire document
    page_ranges={
        "target_pages": "1, 2, 5-10",
        "max_pages": 10,
    },

    # OCR & Processing
    processing_options={

        # OCR languages
        # Only affects scanned pages/images
        # Native PDF text is extracted directly
        "ocr_parameters": {
            "languages": ["en"]
        },

        # High OCR accuracy (Default: False)
        "high_res_ocr": True,

        # Better borderless table detection (Default: False)
        "aggressive_table_extraction": True,

        # Better chart and graph understanding
        "specialized_chart_parsing": True,
    },

    # Output returns
    expand=[

        # Main input for chunking and embeddings
        "markdown",

        # Page numbers, document info
        "metadata",

        # Structured document elements
        "items",
    ],

    # Output formatting
    output_options={

        # Markdown formatting
        "markdown": {

            # Preserve hyperlinks
            "annotate_links": True,

            # Keep images separate
            # Better for RAG than inline Base64 images
            "inline_images": False,

            # Table formatting
            "tables": {

                # Merge tables spanning multiple pages
                "merge_continued_tables": True,

                # Produce cleaner Markdown tables
                "compact_markdown_tables": True,
            },
        },

        # Preserve document layout
        "spatial_text": {

            # Preserve multi-column reading order
            "do_not_unroll_columns": True,

            # Preserve layout consistency across pages
            "preserve_layout_alignment_across_pages": True,
        },

        # Save images
        "images_to_save": [
        "embedded",
        "screenshot",
        ],
    },
)

# Parsed outputs
markdown = result.markdown
metadata = result.metadata
items = result.items
