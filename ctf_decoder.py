def solve_level_1():
    string_hex = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    byte_string = bytes.fromhex(string_hex)
    text = byte_string.decode("utf-8")
    return text

def solve_level_2():
    from base64 import b64decode
    string_64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
    data = b64decode(string_64)
    text = data.decode("utf-8")

    string = 664813035583918006462745898431981286737635929725
    length_string = (string.bit_length() + 7) // 8
    data_bytes = string.to_bytes(length_string, "big")
    text_2 = data_bytes.decode("utf-8")
    return text + text_2







def solve_level_3():
    return ""

def solve_level_4():
    return ""

def solve_level_5():
    return ""

def solve_level_6():
    return ""

def solve_level_7():
    return ""

def solve_level_8():
    return ""

def solve_level_9():
    return ""

def solve_level_10():
    return ""

def solve_level_11():
    return ""

def main():
    ...
