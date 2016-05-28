
# import sys
# sys.argv # все входные параметры приложения
#
# print(sys.argv)
#
# for a in sys.argv[1:]:
#     if a.startswith('car='):
#         value = a.split('=')[1]
#         print( 'marka:', value )


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

parser.add_argument('--color', default=None)

args = parser.parse_args()
#print(args.accumulate(args.integers))

if args.color:
    print( 'color:', args.color )