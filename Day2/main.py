
def main():
    f = open("input.txt", "r")
    all_games = {}
    lines = [x.replace("\n", "") for x in f.readlines()]

    for game in lines:

        game = game.split(":")
        this_key = game[0].split(" ")[-1]

        new = game[1].split(";")
        print(new)



    f.close()



if __name__ == '__main__':
    main()

