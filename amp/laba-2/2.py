import getopt
import os
import sys

def print_ascii_table(file = None, columns = 16, start = 32):
    res = ''
    max = 255
    index = start
    i = 0
    rows = int((max - start) / columns + .5)
    while i < rows:
        j = int(start / columns)
        while j < columns and index <= max:
            if file is None and index >= 128 and index <= 160:
                res += ("{:4d} [ ] ".format(index))
                index += 1
                j += 1
                continue
            res += ("{:4d} [{:1c}] ".format(index, index))
            index += 1
            j += 1
        res += ("\n")
        i += 1
    res += ("\nLaba 2 \"Ascii table\" © 2023 Nikita Kostyr")
    print(res, file= file)
    return 0

if __name__ == "__main__":
    argv = sys.argv[1:]
    
    try:
        opts, args = getopt.getopt(argv, "f:h", ["file="])
    except Exception as e:
        print(e)
        print("Use -h flag to get help.")
        sys.exit(0xff)

    for opt, arg in opts:
        match opt:
            case "-h":
                print("This program prints out the table of ascii characters")
                print("from 32th to 255th to a file if its name were provided")
                print("or concole.")
                print("\n-------Options-------")
                print(" -h          : show this message")
                print(" -f, --file  : set output file name")
                print("\n----Return status----")
                print(" 0           : everything is ok")
                print(" 255         : smth went wrong")
                print("\nLaba 2 \"Ascii table\" © 2023 Nikita Kostyr")
                sys.exit(0)
            case "-f" | "--file":
                name = arg.split(".")[0] + "{}.txt"
                counter = 0
                while os.path.isfile(name.format(f"({counter})"))\
                or (os.path.isfile(name.format("")) and counter == 0):
                    counter += 1
                if counter == 0:
                    name = arg.split(".")[0] + ".txt"
                with open(name.format(f"({counter})"), "w", encoding="utf-8") as file:
                    ret = print_ascii_table(file)
                    sys.exit(ret)

    print("File name were not provided.")
    print("Use -h flag to get help.")
    print("\nPrinting table to console:")
    ret = print_ascii_table()
    sys.exit(ret)