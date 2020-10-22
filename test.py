import os
import subprocess
import string
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
    return argparser.parse_args()

def main(args):
    if not args.convention:
        print("大会名が与えられていません")
        sys.exit()
    if not args.question in string.ascii_lowercase[:6]:
        print("問題の名前が正しくありません")
        sys.exit()
    directory = "./{convention}/{question}".format(convention=args.convention, question=args.question)
    if os.path.exists(directory):
        os.chdir(directory)
        subprocess.run("pwd", shell=True)
        subprocess.run("oj t -c \"python3 {question}.py\"".format(question=args.question), shell=True)
        subprocess.run("cd -", shell=True)
    else:
        print("指定された大会名、問題名が正しくありません")
        print(directory)
        sys.exit()


if __name__ == "__main__":
    args = get_option()
    main(args)
