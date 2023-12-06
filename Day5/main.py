
def main():
    f = open("sample_input.txt", "r")
    lines = [x.replace("\n", "") for x in f.readlines()]
    
    for line in lines:
        print(line)


    f.close()



if __name__ == '__main__':
    main()