import os
import subprocess
import sys

def main(convention, question):
    directory = "./{convention}/{question}".format(convention=convention, question=question)
    if os.path.exists(directory):
        os.chdir(directory)
        subprocess.run("pwd", shell=True)
        subprocess.run("oj t -c \"python3 {question}.py\"".format(question=question), shell=True)
        subprocess.run("cd -", shell=True)
    else:
        print("指定された大会名、問題名が正しくありません")
        print(directory)
        sys.exit()


if __name__ == "__main__":
    convention = sys.argv[1]
    question = sys.argv[2]
    main(convention, question)
