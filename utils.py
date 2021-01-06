
def transform_to_nmea_sentence(data):
    sentence = f"POV,{data}"

    # Generate the checksum as required by the OpenVario Protocol.
    packet = str(bytes(sentence, encoding="utf-8"))
    checksum = 0
    for bt in packet:
        checksum ^= ord(bt)

    # Return the entire NMEA record.
    checksum = str(hex(checksum)[2:]).upper()

    return f"${sentence}*{checksum}"
