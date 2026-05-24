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
    from base64 import b64decode
    string_64 = "NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q="
    data_bytes = b64decode(string_64)
    text_hex = data_bytes.decode("utf-8")
    string_hex = bytes.fromhex(text_hex)
    text = string_hex.decode("utf-8")
    return text

def solve_level_4():
    from base64 import b64decode
    string_64 = "Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0="
    for i in range(2):
        string_64 = b64decode(string_64)
        #print(string_64)
    text = string_64.decode("utf-8")
    return text

def solve_level_5():
    string_hex = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    data_bytes = bytes.fromhex(string_hex)
    data_bytes_inverted = data_bytes[::-1]
    text = data_bytes_inverted.decode("utf-8")
    return text

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
    print("=== CTF DECODER ===")
    print(f"Level 1: {solve_level_1()}")
    print(f"Level 2: {solve_level_2()}")
    print(f"Level 3: {solve_level_3()}")
    print(f"Level 4: {solve_level_4()}")
    print(f"Level 5: {solve_level_5()}")

main()
