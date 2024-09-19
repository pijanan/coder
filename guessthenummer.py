import random
nummerlist=[1,2,3,4,5,6,7,8,9,10]
nummer=random.choice(nummerlist)

x=3
while x >= 1:
    guest_nummer=int(input("guesss the nummer"))
    print(guest_nummer)
    if guest_nummer == nummer:
        print("you find the nummer")
        break
    elif guest_nummer > nummer:
        print("try a little bit low")
        x -= 1
        print(f"you have {x} lifes")
        
    elif guest_nummer < nummer:
        print("try a little bit high")
        x -= 1
        print(f"you have {x} lifes")

    else:
        print("try again")
        x -= 1
        print(f"you have {x} lifes")
else:
    print("You don't have any life more")

   
    
