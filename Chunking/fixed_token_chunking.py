import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

def fixed_token_splitting(text, chunk_size, chunk_overlap):

    """
    First convert text into tokens, split tokens
    into fixed-size chunks with overlap, then decode 
    each chunk back into text.

    Stores the metadata:
    - chunk id
    - start token
    - end token
    - tokens count
    """

    if chunk_size <= 0:

        raise ValueError(
            "chunk_size must be greater than 0"
        )

    if chunk_size <= chunk_overlap:

        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )


    tokens = encoding.encode(text)

    chunks = []

    start = 0

    while start < len(tokens):

        end = start + chunk_size

        tokens_chunk = tokens[start : end]

        text_chunk = encoding.decode(tokens_chunk)

        chunks.append({
            "page_content" : text_chunk,
            "metadata" : {
                "chunk_id" : len(chunks),
                "start_token" : start,
                "end_token" : min(end, len(tokens)),
                "token_count" : len(tokens_chunk)
                }
        })

        start += (chunk_size - chunk_overlap)


    return chunks