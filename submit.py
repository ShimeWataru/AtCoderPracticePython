import pathlib
import string
import subprocess
import sys
from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()
    argparser.add_argument(
        "convention", type=str, default="", help="Convention Name"
    )
    argparser.add_argument(
        "question", type=str, default="", help="Alphabet of question"
    )
    argparser.add_argument(
        "-t", "--type", type=str, default="", help="Question format number or alphabet"
    )

    return argparser.parse_args()


def main(args):
    if not args.convention:
        print("大会名が与えられていません")
        sys.exit()
    if not args.question in string.ascii_lowercase[:6]:
        print("問題の名前が正しくありません")
        sys.exit()
    alphabet_index = string.ascii_lowercase.find(args.question)
    url_suffix = args.question if not args.type else string.digits[1:][alphabet_index]

    file_path = "{convention}/{question}/{question}.py".format(
        convention=args.convention, question=args.question
    )
    url = (
        "https://atcoder.jp/contests/{convention}/tasks/{convention}_{question}".format(
            convention=args.convention, question=url_suffix
        )
    )
    subprocess.run(
        "oj s {url} {file_path}".format(url=url, file_path=file_path), shell=True
    )


if __name__ == "__main__":
    args = get_option()
    main(args)
