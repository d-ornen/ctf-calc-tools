def main(hex_value):
    hex_value = hex_value.lstrip("0x")
    hex_value = ensure_even_length(hex_value)
    convert(hex_value)


def ensure_even_length(hexstr):
    if len(hexstr) % 2 == 0:
        return hexstr
    else:
        return "0"+hexstr


def convert(sanitized_hex):
    translated_hex_string = ""
    current_offset = 0
    max_offset = len(sanitized_hex) // 2
    while True:
        if current_offset < max_offset:
            char_pair = sanitized_hex[current_offset*2:current_offset*2+2]
            translated_hex_string += chr(int(char_pair, 16))
            current_offset += 1
        else:
            print(translated_hex_string)
            return 0


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
