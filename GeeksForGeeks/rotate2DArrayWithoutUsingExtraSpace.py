def main():
    count = int(input())
    
    for _ in range(count):
        size = int(input())
        arrIn = input().split(" ")
        retStr = ""

        for y in range(size):
            for x in range(size):
                retStr += arrIn[ ((size-1) - x) * size + y ]
                retStr += " "
        
        print(retStr)
        


if __name__ == "__main__":
    main()