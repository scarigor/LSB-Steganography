from PIL import Image, ImageDraw
import numpy as np


# Common functions
def string_to_bin(string):
    result = []
    for c in string:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([str(b) for b in bits])
    return result


def bin_to_string(bin): return ''.join(format(ord(c), 'b') for c in bin)


def dec_to_bin(number): return bin(number)[2:].zfill(8)


def bin_to_decimal(number): return int(number, 2)


def get_bit(sequence, bit): return sequence[bit]


def change_bit(sequence, item, bit):
    return sequence[0:bit] + item + sequence[bit + 1:]


def read_message(message):
    text = open(message, "rt")
    text_content = text.read()
    text.close()
    binaryText = list(string_to_bin(text_content))
    return binaryText


def read_img(image):
    img = Image.open(image)
    return img

# Common functions end


def encode_lsb(img, msg, bit=1):  # max bit is 7
    # Set variables
    width, height = img.size
    imgFlat = list(np.array(img).flatten())
    imgBinary = list(map(dec_to_bin, imgFlat))
    msgLength = len(msg)
    imgLength = len(imgBinary)

    # Change LSB
    if msgLength > imgLength:
        print("Your message is too large to be encoded!")
        quit()
    else:
        for i in range(imgLength):
            if i <= msgLength - 1:
                if msg[i] != get_bit(imgBinary[i], bit):
                    imgBinary[i] = change_bit(imgBinary[i], msg[i], bit)
    print("Successfully encoded!")

    # To decimal:
    for i in range(imgLength):
        imgBinary[i] = bin_to_decimal(imgBinary[i])

    # Export result image
    finalImage = np.array(imgBinary).reshape(height, width, 3)
    im = Image.fromarray(finalImage.astype("uint8"), "RGB")
    im.save("output.bmp")
    im.close()


def decode_lsb(img, marker, bit=1):
    # Set variables
    output_file = open("output.txt", "w")
    imgFlat = list(np.array(img).flatten())
    imgBinary = list(map(dec_to_bin, imgFlat))
    lastBits = []

    # Extract last bits
    for i in range(len(imgBinary)):
        lastBits.append(get_bit(imgBinary[i], bit))

    # Fill array with null to size % 8 = 0
    leng = len(lastBits)
    while leng % 8 != 0:
        lastBits.append("0")
        leng += 1

    # Msg formatting
    msgBin = list(map(''.join, zip(*[iter(''.join(lastBits))]*8)))
    msgDec = list(map(bin_to_decimal, msgBin))
    msgChar = list(map(chr, msgDec))

    # Find end of text
    markerIndex = 0
    for i in range(len(msgBin)):
        if msgBin[i] == marker:
            markerIndex = i
            break

    # Concat final string
    p = "".join(msgChar)
    output_file.write(p[0:markerIndex])


encode_lsb(read_img("input.bmp"), read_message("input.txt"))
decode_lsb(read_img("output.bmp"), "01100000")