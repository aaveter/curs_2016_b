# coding: utf-8
import os

PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'results'
)

def students_gen():
    for filename in os.listdir(PATH):
        files = [os.path.join(PATH, filename)]
        if os.path.isdir(files[0]):
            files = [ os.path.join(files[0], a) for a in os.listdir(files[0]) if a.endswith('.py') ]
        else:
            if not filename.endswith('.py'):
                continue
        yield filename.replace('rabota_', ''), files


def ocenki():
    i = 0
    for stud, files in students_gen():
        i += 1
        pluses = calc_files(files)
        o = int(round(pluses / 2.5))
        if o > 5:
            o = 5
        if o > 2:
            print('{:2}) {:25}: {}'.format(i, stud, o))

def calc_files(files):
    pluses = 0
    for fi in files:
        #print(fi)
        for line in open(fi, encoding='utf-8'):
            mass = line.split('##')
            if len(mass) > 1:
                pluses += mass[1].count('+')
    return pluses


if __name__=='__main__':
    ocenki()
