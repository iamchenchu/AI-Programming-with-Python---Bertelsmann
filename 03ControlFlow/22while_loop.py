"""For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. 
This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, 
which is what happens in a while loop. Here's an example of a while loop."""

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

## adds the last element of the card_deck list to the hand list
## until the values in hand add up to 17 or more
while sum(hand)  <= 17:
    hand.append(card_deck.pop())
print(hand)