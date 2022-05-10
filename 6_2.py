# import random 
# print("random", random)
# print("dir", dir(random))

import random 

# elements = [
#     "earth",
#     "air",
#     "fire",
#     "water" 
# ]
# taking an item out of the list randomly
# print("choice ===", random.choice(elements)) 

# takes a sample out of the original list 
# print("sample ===>", random.sample(elements, 2))

# shuffle the order of the items within the specified list
# random.shuffle(elements)
# print("shuffle ===>", elements)

# returns a number from 0 to 5 randomly
# print("randint ===>", random.randint(0, 5))

# def main():
#     print("from main")
#     spin()

# def spin():
#     print("from spin")

# main()

def main():
    for i in range(3): # i is the iterator
        print("i", i)
        outcome = spin()
        print(outcome, end=" ")

def spin():
    n = random.randint(1, 20)
    # print("Random number generated: ", n)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Mellon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"

main()


