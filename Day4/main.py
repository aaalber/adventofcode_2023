
def main():

    with open("input.txt") as f:
        all_cards = f.read().splitlines()

    total = 0
    total_cards = 0

    new_list_of_cards = []
    
    winners = {}

    index = 0

    for card in all_cards:

        total_cards +=1 

        this_card = card.split(':')
        all_numbers = this_card[1].lstrip().split('|')
        my_numbers = all_numbers[1].split()
        winning_numbers = all_numbers[0].split()
        winning_numbers[0] = winning_numbers[0].lstrip()

        num_winners = 0
        points = 0

        new_list_of_cards.append(card)

        for num in my_numbers:
            if num in winning_numbers:
                num_winners += 1
                
                if points > 1:
                    points = points * 2
                else:
                    points += 1
        
        winners[card] = num_winners
        
        for x in range(num_winners):
            x += 1

            if card in new_list_of_cards:
                number_of_times = new_list_of_cards.count(card)
            
            for z in range(number_of_times):
                new_list_of_cards.append(all_cards[index+x])

        total += points
        
        index += 1


        # Part 1
        total_cards = total_cards + num_winners

    # Part 2
    print(len(new_list_of_cards))

if __name__ == '__main__':
    main()