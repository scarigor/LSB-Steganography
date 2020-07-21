### Image Steganography

This project contains implementation of two image steganography methods.

### Installation

    pip install -r requirements.txt

### Usage

    python encode.py --image_path --message_path --method --least_bit --key_path --save_path
  
    --image_path: required=True, default=./images/input_1.bmp, type=str, Path to image to encode.
    --message_path: required=True, default=./input.txt, type=str, Path to message to encode.
    --method: required=True, default=LSB, type=str, choices=['LSB', 'PSI'], Steganography method.
    --least_bit: required=True, default=1, type=int, Least bit to change in image.
    --key_path: required=False, default=None, type=str, Path to key for PSI method.
    --save_path: required=False, default=./results/, type=str, Path where to save image.
    
    python decode.py --image_path --method --least_bit --key_path --save_path
    
    --image_path: required=True, default=./results/output.bmp, type=str, Path to image to decode.
    --method: required=True, default=LSB, type=str, choices=['LSB', 'PSI'], Steganography method.
    --least_bit: required=True, default=1, type=int, Least bit to change in image.
    --key_path: required=False, default=./key.txt, type=str, Path to key for PSI method.
    --save_path: required=False, default=./results/, type=str, Path where to save message.

### Example

    python encode.py --image_path ./images/input_1.bmp --message_path ./input.txt --method LSB --least_bit 1 --save_path ./results/
    
    python decode.py --image_path ./results.output.bmp --method LSB --least_bit 1 --save_path ./results/
