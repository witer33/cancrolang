import argparse

parser = argparse.ArgumentParser(
    description='Encode a brainfuck file in the cancro language and encode a cancro file in the brainfuck language.'
)

parser.add_argument("--file", "-f", help="The file to encode")
parser.add_argument("--output", "-o", help="The output file", default="out")
parser.add_argument("--decode", "-d", help="Decode a cancro file", action="store_true")

chars_map = {
    '>': 'Cancro',
    '<': 'cAncro',
    '+': 'caNcro',
    '-': 'canCro',
    '.': 'cancRo',
    ',': 'cancrO',
    '[': 'CAncro',
    ']': 'cANcro'
}

encode_map = str.maketrans(chars_map)
decode_map = {v: k for k, v in chars_map.items()}

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        content = f.read()
    if args.decode:
        for key, value in decode_map.items():
            content = content.replace(key, value)
    else:
        content = content.translate(decode_map)
    with open(args.output, 'w') as f:
        f.write(content)

