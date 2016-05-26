
import os

def listing(path):
    filenames = os.listdir(path)
    print(filenames)
    for fi in sorted(filenames):
        if fi == '.idea':
            continue
        fileway = os.path.abspath(os.path.join(path, fi))

        if os.path.isdir(fileway) and fi[0]!=".":
            print('DIR:', fileway)
            listing(fileway)
        elif os.path.isfile(fileway):
            print(fileway)

if __name__=='__main__':
    listing(path='.')