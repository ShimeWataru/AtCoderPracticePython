import os
import sys
import pathlib

dir_names = sys.argv[1:]
questions = ["a", "b", "c"]

for i in range(len(dir_names)):
    os.mkdir(dir_names[i])
    for j in range(len(questions)):
        mk_file = pathlib.Path(
            '{dir}/{file}.py'.format(dir=dir_names[i], file=questions[j]))
        mk_file.touch()
