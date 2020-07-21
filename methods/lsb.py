from methods import BaseMethod
from utils import *


class LeastSignificantBit(BaseMethod):

    def __init__(self, image_path, message_path=None, least_bit=1):
        super(LeastSignificantBit, self).__init__(image_path, message_path, least_bit)

    def encode(self, save_path=None):
        if not self.message_path:
            raise ValueError('You need to specify path to message when instantiating.')

        img_binary = list(map(dec_to_bin, self.image_flatten))
        msg_len, img_len = len(self.message), len(img_binary)

        # Change LSB
        if msg_len > img_len:
            raise ValueError("Your message is too large to be encoded!")

        for i in range(img_len):
            if i <= msg_len - 1:
                if self.message[i] != img_binary[i][self.least_bit]:
                    img_binary[i] = change_bit(img_binary[i], self.message[i], self.least_bit)

        print("Successfully encoded!")

        if save_path:
            self.save_image(img_binary, save_path)

    def decode(self, marker, save_path=None):
        # Set variables
        image_binary = list(map(dec_to_bin, self.image_flatten))
        last_bits = list([image_binary[i][self.least_bit] for i in range(len(image_binary))])

        msg_chars, marker_idx = self.format_message(last_bits, marker)
        # Concat final string
        plain_text = ''.join(msg_chars)[0:marker_idx]
        if save_path:
            self.write_message(plain_text, save_path)
        else:
            print(f'Decoded message: {plain_text}')
