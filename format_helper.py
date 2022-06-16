def to_str(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str
    return bytes_or_str.encode('utf-8')