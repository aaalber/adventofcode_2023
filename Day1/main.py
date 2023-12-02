words_to_numbers = {
'one': 'on1ne',
'two': 'tw2wo',
'three': 'thr3ree',
'four': 'fou4our',
'five': 'fiv5ive',
'six': 'si6ix',
'seven': 'sev7ven',
'eight': 'eig8ght',
'nine': 'nin9ine'
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

        """ Part 2, comment 27-29 for Part 1 answer
        """
        for k,v in words_to_numbers.items():
            if k in line:
                line = line.replace(k,v)

        for char in line:
            if char.isnumeric():
                digits.append(int(char))

        if len(digits) == 1:
            full = int(str(digits[0]) + str(digits[0]))
        else:
            first = str(digits[0])
            last = str(digits[-1])
            full = int(first + last)

        answer = answer + full
        
    print(f'Answer: {answer}')

    f.close()
if __name__ == '__main__':
    main()

