import getopt
import sys

def right_triangle(rows = 3):
    i = 1
    while i <= rows:
        print('@ ' * (rows - i), '* ' * i, sep="")
        i += 1
    return 0

def left_triangle(rows = 3):
    i = rows
    while i > 0:
        print('* ' * i,'@ ' * (rows - i), sep="")
        i -= 1
    return 0

if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "r:l:h")
    except Exception as e:
        print(e)
        print("Use -h flag to get help.")
        sys.exit(0xff)

    for opt, arg in opts:
        match opt:
            case "-h":
                print("Help")
                sys.exit(0)
            case "-r":
                res = right_triangle(int(arg))
                sys.exit(res)
            case "-l":
                res = left_triangle(int(arg))
                sys.exit(res)
    
    res = right_triangle()
    sys.exit(res)