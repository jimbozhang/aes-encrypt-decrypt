import argparse
from pathlib import Path
from cryptographic import encrypt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password", help="password string", type=str)
    parser.add_argument("input", help="input filename", type=str)
    parser.add_argument("output", help="output filename", type=str)
    args = parser.parse_args()

    Path(args.output).parent.mkdir(exist_ok=True)
    encrypt(args.input, args.output, args.password)


if __name__ == "__main__":
    main()
