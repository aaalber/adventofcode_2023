
words_to_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 9
}


def main():
    f = open("input.txt", "r")
    
    lines = [x.replace("\n", "") for x in f.readlines()]
    answer: int = 0 
    
    for line in lines:
        digits: list = []
        first: int = 0
        last: int = 0 
        full: int = 0

        """ Part 2, comment 30-32 for Part 1 answer
        """
        print(line)
        for k,v in words_to_numbers.items():

            if k in line:
                print(k)
                line = line.replace(k,str(v))
        #print(line)
        print(line)


        for char in line:
            if char.isnumeric():
                digits.append(int(char))

        if len(digits) == 1:
            full = int(str(digits[0]) + str(digits[0])) 
        else:
            first = str(digits[0])
            last = str(digits[-1])
            full = int(first + last) 
        print(digits)
        print(full)

        print(answer, full)
        answer = answer + full
        print()
    f.close()

    print(f'Answer: {answer}')

if __name__ == '__main__':
    main()

