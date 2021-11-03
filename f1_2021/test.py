from packets import Parser


def main():
    for packet in Parser.from_file(filepath='../data/sample_10hz.90.bin'):
        print(type(packet).__name__)


if __name__ == '__main__':
    main()
