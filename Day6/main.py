

def main():
    f = open("input.txt", "r")
    lines = [x.replace("\n", "") for x in f.readlines()]

    time_line = [ x for x in lines[0].split(" ")[1:] if x]
    distance_line = [ x for x in lines[1].split(" ")[1:] if x]

################ PART 2 ########################

    all_winners = []

    temp_time_str = ""
    for x in time_line:
        temp_time_str += (str(x))
    part_2_time = int(temp_time_str)

    temp_distance_str = ""
    for y in distance_line:
        temp_distance_str += (str(y))
    part_2_distance = int(temp_distance_str)

    count = 0
    time = part_2_time
    record = part_2_distance

    for hold in range(int(time + 1)):
        hold = int(hold)

        distance = (time - hold) * hold

        if distance > record:
            count += 1

    print(f'Part 2: {count}')

################# PART 1 #######################
    
    all_winners = []

    for race_num in range(4):

        count = 0
        time = int(time_line[race_num])
        record = int(distance_line[race_num])

        for hold in range(int(time + 1)):
            hold = int(hold)

            distance = (time - hold) * hold

            if distance > record:
                count += 1

        all_winners.append(count)


    # Part 1
    result = 1
    for x in all_winners:
        result = result * x

    print(f'Part 1: {result}')

    f.close()



if __name__ == '__main__':
    main()

