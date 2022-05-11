import random


# функция перевода строки в биты
def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode("utf-8", "surrogatepass"), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# функция перевода битов в строку
def text_from_bits(bits):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode("utf-8", "surrogatepass") or '\0'


# функция для создания случайного бинарника
def make_bin_file():
    f = open(f'dump.bin', 'wb')
    some_list = "abcdefghijklmnopqrstuvwxyz"
    for item in some_list:
        bt = text_to_bits(item * (random.randint(1, 250))).encode()
        f.write(bt)
    f.close()


# рле кодирование
def rle_encode(some_string):
    result = ''
    prev_char = ''
    count = 1

    if not some_string:
        return ''

    for char in some_string:
        if char != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        result += str(count) + prev_char

    return result


# рле декодирование
def rle_decode(some_string):
    result = ''
    count = ''

    for char in some_string:
        if char.isdigit():
            count += char
        else:
            result += char * int(count)
            count = ''
    return result


# читаем файл и кодируем его
def rle_compression():
    f = open(f'dump.bin', 'rb')
    bytes = f.read()
    symbs = text_from_bits(bytes)
    encode_text = rle_encode(symbs)
    fb = open(f'encode.bin', 'wb')
    fb.write(text_to_bits(encode_text).encode())
    fb.close()
    f.close()


# читаем файл и декодируем его
def rle_decompression():
    f = open(f'encode.bin', 'rb')
    bytes = f.read()
    symbs = text_from_bits(bytes)
    decode_text = rle_decode(symbs)
    fb = open(f'decode.bin', 'wb')
    fb.write(text_to_bits(decode_text).encode())
    fb.close()
    f.close()


make_bin_file()
rle_compression()
rle_decompression()

#dump и decode весят 25 кб, а encode - 1 кб!