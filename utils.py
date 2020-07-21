from PIL import Image


def str_to_bin(s):
    result = []
    for c in s:
        result += [str(b) for b in '00000000'[len(bin(ord(c))[2:]):] + bin(ord(c))[2:]]

    return result


def bin_to_string(b): return ''.join(format(ord(c), 'b') for c in b)


def dec_to_bin(number): return bin(number)[2:].zfill(8)


def bin_to_decimal(number): return int(number, 2)


def get_bit(sequence, bit): return sequence[bit]


def change_bit(sequence, item, bit):
    return sequence[0:bit] + item + sequence[bit + 1:]


def read_message(message_path):
    with open(message_path) as f:
        return list(str_to_bin(f.read()))


def read_img(image_path):
    return Image.open(image_path)
