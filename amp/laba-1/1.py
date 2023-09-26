import sys
import getopt
import re

X = None
Y = None

def get_quarter_info(X, Y):
    if  (int(X) == 0 and int(Y) == 0):
        print("We are in [0:0] point")
        return 0
    elif (int(X) > 0 and int(Y) > 0):
        print("We are in 1'st quarter")
        return 1
    elif (int(X) < 0 and int(Y) > 0):
        print("We are in 2'nd quarter")
        return 2
    elif (int(X) < 0 and int(Y) < 0):
        print("We are in 3'rd quarter")
        return 3
    elif (int(X) > 0 and int(Y) < 0):
        print("We are in 4'th quarter")
        return 4
    elif (int(X) != 0 and int(Y) == 0):
        print("We are on the 0X axis")
        return 5
    elif (int(X) == 0 and int(Y) != 0):
        print("We are on the 0Y axis")
        return 6
    # print("Are we in cosmos?")
    return 0xff

# main section
if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hx:y:")
    except:
        print("Something went wrong :(")
        print("Use -h flag to get help.")
        sys.exit(0xff)

    for opt, arg in opts:
        match opt:
            case "-x": 
                X = arg
            case "-y": 
                Y = arg
            case "-h":
                print("This is a help section so listen carefully:")
                print("This program displays where point is located on coordinate plane.")
                print("Coordinates of this point are provided by user input.")
                print("\n--------Options:")
                print(" -x       : set X value from number")
                print(" -y       : set X value from number")
                print(" -h       : print this message")
                print("\n--------Return status:")
                print(" [0-6]    - everything is ok")
                print(" 0        - [0:0] point or help section exit")
                print(" [1-4]    - quarters")
                print(" [5,6]    - axes 0X and 0Y")
                print(" 255      - smth went wrong")
                sys.exit(0)

    if X is None or Y is None:
        print("X and/or Y were not provided.")
        print("Use -h flag to get help.")
        sys.exit(0xff)

    # роботу цих перевірок пояснив у звіті в теоретичній частині 
    if re.match("^[-+]?[0-9]*$", X) is None:
        print("X must be integer")
        print("Use -h flag to get help.")
        sys.exit(0xff)

    if re.match("^[-+]?[0-9]*$", Y) is None:
        print("Y must be integer")
        print("Use -h flag to get help.")
        sys.exit(0xff)

    # for i in X:
    #     if i not in "-+0123456789":
    #         print(f"{i} is not allowed symbol for X")
    #         print("X must be integer")
    #         print("Use -h flag to get help.")
    #         sys.exit(0xff)

    # for i in Y:
    #     if i not in "-+0123456789":
    #         print(f"{i} is not allowed symbol for Y")
    #         print("Y must be integer")
    #         print("Use -h flag to get help.")
    #         sys.exit(0xff)

    res = get_quarter_info(X, Y)
    sys.exit(res)