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
        "-i", "--initial", type=str, default="a", help="First problem alphabet"
    )
    argparser.add_argument(
        "-n", "--number", type=int, default=6, help="Number of questions"
    )
    argparser.add_argument(
        "-t", "--type", type=str, default="", help="Question format number or alphabet"
    )
    return argparser.parse_args()


def main(args):
    if not args.convention:
        print("大会名が与えられていません")
        sys.exit()
    initial_index = string.ascii_lowercase.find(args.initial)
    questions_range = string.ascii_lowercase[
        initial_index : initial_index + args.number
    ]
    url_suffix = questions_range if not args.type else string.digits[1:]

    for i in range(args.number):
        directory = "{convention}/{question}".format(
            convention=args.convention, question=questions_range[i]
        )
        url = "https://atcoder.jp/contests/{convention}/tasks/{convention}_{question}".format(
            convention=args.convention, question=url_suffix[i]
        )
        subprocess.run("mkdir -p ./{dir}/test".format(dir=directory), shell=True)
        subprocess.run("touch ./{dir}/{question}.py".format(dir=directory, question=questions_range[i]), shell=True)
        subprocess.run("oj d -d {dir}/test {url}".format(dir=directory, url=url), shell=True)


if __name__ == "__main__":
    args = get_option()
    main(args)
