import argparse
import interpreter

parser = argparse.ArgumentParser(
    description='Encode a brainfuck file in the cancro language and encode a cancro file in the brainfuck language.'
)

parser.add_argument("--file", "-f", help="The file to encode")
parser.add_argument("--output", "-o", help="The output file", default="out")
parser.add_argument("--decode", "-d", help="Decode a cancro file", action="store_true")
parser.add_argument("--run", "-r", help="Run the file", action="store_true")

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


def encode(data: str) -> str:
    return data.translate(encode_map)


def decode(data: str) -> str:
    for key, value in decode_map.items():
        data = data.replace(key, value)
    return data


if __name__ == '__main__':
    args = parser.parse_args()
    if args.run:
        if args.decode:
            interpreter.BrainfuckInterpreter(open(args.file, "rb")).run()
        else:
            interpreter.BrainfuckInterpreter(interpreter.CancroReader(open(args.file, "rb"))).run()
    else:
        with open(args.file, 'r') as f:
            content = f.read()
        if args.decode:
            content = decode(content)
        else:
            content = encode(content)
        with open(args.output, 'w') as f:
            f.write(content)

