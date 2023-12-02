def main():
    f = open("input.txt", "r")
    all_games = {}
    lines = [x.replace("\n", "") for x in f.readlines()]

    for game in lines:
        
        # Garbage to clean up data
        game = game.split(":")
        key = game[0].split(" ")[-1]
        new = game[1].split(";")
        new_new = [y.lstrip() for y in new]
        all_games[key] = [x.split(",") for x in new_new]


    bad_games = []
    good_games = []

    total_power = 0
    for k,v in all_games.items():
        pull_no = 0 
        print(f'Game {k}: {v}')
        # [['6 blue', ' 9 green'], ['3 green', ' 6 blue'], ['5 blue', ' 1 red']]
        not_good = False


        red_number: int = None
        green_number: int = None
        blue_number: int = None

        for pull in v:  #['6 blue', ' 9 green']

            for color_num in pull:
                this_num = color_num.split(" ")
                this_num = [i for i in this_num if i]
                color = this_num[1]
                number = int(this_num[0])
                
                if color == "red":
                    if not red_number:
                        red_number = number
                    else:
                        if number > red_number:
                            red_number = number

                elif color == "green":
                    if not green_number:
                        green_number = number
                    else:
                        if int(number) > int(green_number):
                            green_number = number
                
                elif color == "blue":
                    if not blue_number:
                        blue_number = number
                    else:
                        if number > blue_number:
                            blue_number = number
                
        this_power = red_number * green_number * blue_number
        total_power = total_power + this_power
        """
                #  PART 1 
                if color == "red" and int(number) > 12:
                    not_good = True
                    break
                elif color == "green" and int(number) > 13:
                    not_good = True
                    break
                elif color == "blue" and int(number) > 14:
                    not_good = True
                    break
            if not_good == True:
                if k not in bad_games:
                    bad_games.append(k)
        pull_no = pull_no + 1
        """
    
    # PART 2
    print(total_power)
    """ 
    # PART 1
    good_games = [x for x in range(1,101) if str(x) not in bad_games]
    count = 0
    for num in good_games:
        count = count + num
    print(count)
    """
    
    f.close()



if __name__ == '__main__':
    main()

