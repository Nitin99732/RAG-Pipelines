def fixed_chara_splitter(text, chunk_size, chunk_overlap):

    """
    Split the text in a list of small chunks 
    based on chunks size and chunk overlap.

    Stores the metadata:
    - Chunk id
    - Start
    - End
    - Chunk length 
    """

    # Check valid chunk_overlap size
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        actual_end = min(end, len(text))

        chunks.append({
            "page_content" : chunk,
            "metadata" : {
                "chunk_id" : len(chunks),
                "start" : start,
                "end" : actual_end,
                "chunk_length" : len(chunk)
                }
        })

        start += (chunk_size - chunk_overlap)

    
    return chunks
