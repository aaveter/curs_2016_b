

7.

+, -, *, /, **, %, ^, //

8.

max, min, sum, math.sqrt, abs()

9.

# coding: cp1251
- кодировка файла

10.

if __name__=='__main__':
    pass

11.

12.

14.


def func(x, y, z=0, *args, t=7, **kwargs):
    print(z, t)


func(10, 20, 30, 13, t=100)