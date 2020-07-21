from methods.lsb import LeastSignificantBit
from methods.psi import PSI

from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--image_path', default='./results/output.bmp', type=str, help='Path to image to decode.')
    parser.add_argument('--method', default='LSB', type=str, choices=['LSB', 'PSI'], help='Steganography method.')
    parser.add_argument('--least_bit', default=1, type=int, help='Least bit to change in image.')
    parser.add_argument('--key_path', default='./key.txt', type=str, help='Path to key for PSI method.')
    parser.add_argument('--save_path', default='./results/', type=str, help='Path where to save message.')
    args = parser.parse_args()

    if args.method == 'LSB':
        decoder = LeastSignificantBit(args.image_path, least_bit=args.least_bit)
    elif args.method == 'PSI':
        decoder = PSI(args.image_path, key_path=args.key_path, least_bit=args.least_bit)
    else:
        raise ValueError('Method you passed is unsupported')

    decoder.decode('01100000', args.save_path)
