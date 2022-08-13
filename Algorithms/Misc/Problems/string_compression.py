
long_string = "AAAABBBCCCCCCCCCDD"

def string_compression(compress: str):
    last_char = compress[0]
    char_count = 1
    result_str = ''
    for i in range(1, len(compress)):
        current_char = compress[i]
        if current_char != last_char:
            result_str += last_char + str(char_count)
            char_count = 1
        else:
            char_count += 1
        last_char = current_char

    result_str += last_char + str(char_count)
    return result_str

print(string_compression(long_string))


