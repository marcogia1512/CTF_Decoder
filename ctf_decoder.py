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
    string_hex = "0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    byte_string =  bytes.fromhex(string_hex)
    text = byte_string.decode("utf-16-be")
    return text

def solve_level_7():
    from base64 import b64decode
    first_string_hex = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"
    string_64 = bytes.fromhex(first_string_hex)
    second_string_hex = b64decode(string_64)
    third_string_hex = second_string_hex.decode("utf-8")
    data_bytes = bytes.fromhex(third_string_hex)
    text = data_bytes.decode("utf-8")
    return text

def solve_level_8():
    from base64 import b64decode
    set_strings = "666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ=="
    splitting_set_strings = set_strings.split("|")
    clear_set_strings = [string.strip() for string in splitting_set_strings]
    result = b""
    for string in clear_set_strings:
        if "=" in string:
            string_64 = b64decode(string)
            result += string_64
        else:
            string_hex = bytes.fromhex(string)
            result += string_hex
    return result.decode("utf-8")

def solve_level_9():
    from base64 import b64decode
    string_64 = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="
    encrypted_string = b64decode(string_64)
    text = encrypted_string.decode("utf-8")
    result = ""
    for char in text:
        if char.isalpha():
            decrypted_char = chr(ord(char) - 7)
            result += decrypted_char
        else:
            result += char
    return result

def solve_level_10():
    from base64 import b64decode
    string_64 = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI="
    data = b64decode(string_64)
    print(data[0]) ##output 164
    print(164 ^ 102) #output 194
    #return ""

solve_level_10()

def main():
    print("=== CTF DECODER ===")
    print(f"Level 1: {solve_level_1()}")
    print(f"Level 2: {solve_level_2()}")
    print(f"Level 3: {solve_level_3()}")
    print(f"Level 4: {solve_level_4()}")
    print(f"Level 5: {solve_level_5()}")
    print(f"Level 6: {solve_level_6()}")
    print(f"Level 7: {solve_level_7()}")
    print(f"Level 8: {solve_level_8()}")
    print(f"Level 9: {solve_level_9()}")

#main()
