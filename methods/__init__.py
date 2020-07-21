from utils import *
import numpy as np
import os


class BaseMethod:

    def __init__(self, image_path, message_path=None, least_bit=1):
        self.image_path = image_path
        self.message_path = message_path

        self.image = read_img(self.image_path)
        self.width, self.height = self.image.size
        if self.message_path:
            self.message = read_message(self.message_path)
        else:
            self.message = None

        if 0 > least_bit > 7:
            raise ValueError('Least bit can be only in [0..7] range.')

        self.least_bit = least_bit

    @property
    def image_flatten(self):
        return np.array(self.image).flatten().tolist()

    def save_image(self, img_binary, save_path):
        img_binary = list(map(bin_to_decimal, img_binary))

        save_path = save_path if save_path.endswith('/') else save_path + '/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        final_image = np.array(img_binary).reshape((self.height, self.width, 3))
        im = Image.fromarray(final_image.astype("uint8"), "RGB")
        im.save(save_path + "output.bmp")
        im.close()

    @staticmethod
    def write_message(plain_text, save_path):
        save_path = save_path if save_path.endswith('/') else save_path + '/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        with open(save_path + 'output.txt', 'w') as f:
            f.write(plain_text)

    @staticmethod
    def format_message(last_bits, marker):
        while len(last_bits) % 8 != 0:
            last_bits.append("0")

        msg_binary = list(map(''.join, zip(*[iter(''.join(last_bits))] * 8)))
        msg_decimal = list(map(bin_to_decimal, msg_binary))
        msg_char = list(map(chr, msg_decimal))

        marker_idx = 0
        for i, c in enumerate(msg_binary):
            if c == marker:
                marker_idx = i
                break

        return msg_char, marker_idx

    def encode(self, **kwargs):
        raise NotImplementedError

    def decode(self, **kwargs):
        raise NotImplementedError
