
def transform_to_nmea_sentence(key, value):
    sentence = f"POV,{key},{value}"

    # Generate the checksum as required by the OpenVario Protocol.
    packet = str(bytes(sentence, encoding="utf-8"))
    checksum = 0
    for bt in packet:
        checksum ^= ord(bt)

    # Return the entire NMEA record.
    return f"${sentence}*{hex(checksum)}"