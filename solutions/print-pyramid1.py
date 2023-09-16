def pyramid1(rows):
    for x in range(rows):
        str = " " * (rows -x)
        for y in range(x *2 -1):
            str += "*"
        print(str)

if __name__ == "__main__":
    pyramid1(10)
