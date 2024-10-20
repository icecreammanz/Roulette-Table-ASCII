from colorama import Fore, Back, Style, init

init(autoreset=True)

def firstrow():
    firstrows = []
    skip_next = False
    for x in range(3, 37):
        if x % 3 == 0 and not skip_next:
            firstrows.append(Back.BLACK + str(x))
            skip_next = True
        elif x % 3 == 0 and skip_next:
            firstrows.append(Back.RED + str(x))
            skip_next = False
    return "   ".join(firstrows)

def secondrow():
    secondrows = []
    start = 2
    while start < 36:
        if start % 2 == 0:
            secondrows.append(Back.RED + str(start))
        else:
            secondrows.append(Back.BLACK + str(start))
        start += 3
    return "   ".join(secondrows)

def thirdrow():
    thirdrows = []
    start = 1
    while start < 35:
        if start % 2 == 0:
            thirdrows.append(Back.RED + str(start))
        else:
            thirdrows.append(Back.BLACK + str(start))
        start += 3
    return "   ".join(thirdrows)

def tableshow(firstrow, secondrow, thirdrow):
    print("+-----+--------------------------------------------------------+")
    print("|     |               Roulette Table                           |")
    print("+-----+--------------------------------------------------------+")
    print(f"|     | {firstrow} |")  # Display the first row
    print(f"|  0  | {secondrow} |")  # Display the second row
    print(f"|     | {thirdrow} |")  # Display the third row
    print("+-----+--------------------------------------------------------+")
    print("|     |     1ST12      |       2ND12       |       3RD12       |")
    print("+-----+--------------------------------------------------------+")
    print("|     | 1TO18 |  EVEN  |   RED   |  BLACK  |  ODD   |  19TO36  |")
    print("+-----+--------------------------------------------------------+")

def main():
    firstrows = firstrow()
    secondrows = secondrow()
    thirdrows = thirdrow()
    tableshow(firstrows, secondrows, thirdrows)

if __name__ == '__main__':
    main()

