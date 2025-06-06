import chardet

def convert_to_utf8_sig(file_path: str):
    """
    Converte qualquer arquivo CSV para UTF-8-SIG.
    """
    with open(file_path, "rb") as raw_file:
        raw = raw_file.read()
        result = chardet.detect(raw)
        detected_encoding = result["encoding"]

    if detected_encoding.lower() in ["utf-8", "utf-8-sig"]:
        return  # já está em encoding correto

    decoded_text = raw.decode(detected_encoding)
    with open(file_path, "w", encoding="utf-8-sig") as out_file:
        out_file.write(decoded_text)
