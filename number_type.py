#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this program tells the number type


def main():
    # this function tells the number type

    type = int(input("Enter an integer: "))

    if type > 0:
        print("{} is a positive number".format(type))
        print("")
    elif type < 0:
        print("{} is a negative number".format(type))
        print("")
    else:
        print("0 is just zero!")
        print("")

    print("Done.")


if __name__ == "__main__":
    main()
