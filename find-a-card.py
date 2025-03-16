# cards = [1,2,4,5,6,7,8,4,2,1,2,43,54,6,76,878,9]
cards = []
to_find = 8
import logging

logger = logging.getLogger(__name__)
logger.info("dmsfbkrbgi")
def find_position(cards, number_to_find):
    logger.info("dmsfbkrbgi")
    pos = f"{number_to_find} is Not found"
    for i in range(len(cards)):
        if cards[i] == number_to_find:
            pos = f"Number {number_to_find} found in position = i"
        
    return pos


print(find_position(cards, to_find))
