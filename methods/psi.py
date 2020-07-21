from methods import BaseMethod
from utils import *
import numpy as np


class PSI(BaseMethod):

    def __init__(self, image_path, message_path=None, key_path=None, least_bit=1):
        super(PSI, self).__init__(image_path, message_path, least_bit)

        self.key_path = key_path

        if not self.key_path:
            print('Secret key will be generated.')
            self._key = np.random.randint(1, 50, 16).tolist()
            with open('./key.txt', 'w') as f:
                f.write(','.join([str(i) for i in self._key]))

        else:
            with open(self.key_path) as f:
                self._key = list([int(i) for i in f.read().strip().split(',')])

    def encode(self, save_path=None):
        if not self.message_path:
            raise ValueError('You need to specify path to message when instantiating.')

        # Set variables
        image_binary = list(map(dec_to_bin, self.image_flatten))

        # Change LSBp
        if len(self.message) > len(image_binary):
            raise ValueError("Your message is too large to be encoded!")

        next_idx, count = 0, 0
        for i in range(len(self.message)):
            if count > len(self._key) - 1:
                count = 0

            next_idx += self._key[count]
            if next_idx > (len(image_binary) - max(self._key)):
                break
            else:
                image_binary[next_idx] = change_bit(image_binary[next_idx], self.message[i], self.least_bit)
                count += 1

        if save_path:
            self.save_image(image_binary, save_path)

    def decode(self, marker, save_path=None):
        # Set variables
        image_binary = list(map(dec_to_bin, self.image_flatten))
        last_bits, next_idx, count = [], 0, 0

        for i in range(len(image_binary)):
            if count > len(self._key) - 1:
                count = 0

            next_idx += self._key[count]
            if next_idx > (len(image_binary) - max(self._key)):
                break
            else:
                last_bits.append(image_binary[next_idx][self.least_bit])
            count += 1

        msg_char, marker_idx = self.format_message(last_bits, marker)
        plain_text = ''.join(msg_char)[0:marker_idx] if marker_idx else ''.join(msg_char)

        if save_path:
            self.write_message(plain_text, save_path)
        else:
            print(f'Decoded plain text: {plain_text}')
