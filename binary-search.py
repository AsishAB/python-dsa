import time


# cards = [4,12,34,34,34,34,35,48,65,65,65,65,65,7,7,7,7,7,7,7,7]
cards = list(range(0,999999))
cards.sort()
# print(f"Cards = {cards} \n")
to_find = 6780
lo = 0
hi = len(cards) - 1
start_time = time.time()
def binary_search(lo, hi, cards):
    pos = -1
    # print(f"Initial Stage :- hi = {hi}, lo = {lo}")
    while hi >= lo: 
        pos = int((hi + lo) / 2)
        if cards[pos] == to_find:
            return pos
        else:
            # print(f"Cards value at {pos} = {cards[pos]}")
            if cards[pos] > to_find:
                hi = pos - 1
            elif cards[pos] < to_find:
                lo = pos + 1
    
def find_first_occurance(lo, hi, cards):
    position = binary_search(lo, hi, cards)
    if position == -1:
        return position
    while position !=0 and cards[position] <= cards[position - 1]:
        # if position !=0 and cards[position] == cards[position - 1]:
        if cards[position] == cards[position - 1]:
            position = position - 1

    return position
end_time = time.time()
execution_time = end_time - start_time
print(f"Position of {to_find} found at location {find_first_occurance(lo, hi, cards)}. Time taken = {end_time} - {start_time} =  {execution_time} seconds")

# cards = [7,7,7,7,7,7]
# cards = [7]
# cards = [4,12,34,35,48,65,7]



# Your function call




