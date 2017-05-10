import os
import sys


def main(wd, nb_name):
    lesson_template = '~/Desktop/GA/DSI-SF-5/utils/lesson_template.ipynb'
    os.system('cp ' + lesson_template + ' ' + wd + '/' + nb_name + '.ipynb')
    os.system('jupyter notebook ' + wd + '/' + nb_name + '.ipynb')

if __name__ == '__main__':
    wd, nb_name = sys.argv[1:]
    main(wd, nb_name)
