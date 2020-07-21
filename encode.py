from methods.lsb import LeastSignificantBit
from methods.psi import PSI

from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--image_path', default='./images/input_1.bmp', type=str, help='Path to image to encode.')
    parser.add_argument('--message_path', default='./input.txt', type=str, help='Path to message to encode.')
    parser.add_argument('--method', default='LSB', type=str, choices=['LSB', 'PSI'], help='Steganography method.')
    parser.add_argument('--least_bit', default=1, type=int, help='Least bit to change in image.')
    parser.add_argument('--key_path', default=None, type=str, help='Path to key for PSI method.')
    parser.add_argument('--save_path', default='./results/', type=str, help='Path where to save image.')
    args = parser.parse_args()

    if args.method == 'LSB':
        encoder = LeastSignificantBit(args.image_path, args.message_path, args.least_bit)
    elif args.method == 'PSI':
        encoder = PSI(args.image_path, args.message_path, args.key_path, args.least_bit)
    else:
        raise ValueError('Method you passed is unsupported')

    encoder.encode(args.save_path)
