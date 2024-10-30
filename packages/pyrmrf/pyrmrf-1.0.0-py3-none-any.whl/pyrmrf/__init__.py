import sys
import shutil


def main():
    try:
        shutil.rmtree(sys.argv[1])
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
