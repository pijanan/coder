import random
clickes=11
boxes=[1,2,3,4,5,6,7,8,9,10,11,12]


def the_boxes_box():
    print(boxes[0:4])
    print(boxes[4:8])
    print(boxes[8:12])
    
def game ():
    global clickes,boxes
    imposter=random.choice(boxes)
    
    while clickes >0:
        print(the_boxes_box())
        theGuess=(int(input("which box want you open")))
        if boxes[theGuess-1]==imposter:
            boxes[theGuess-1]="#"
            print("you are out")
            break
            
        elif boxes[theGuess-1]=="#":
            clickes=clickes
           
        
        else:
            boxes[theGuess-1]="$"
            clickes = clickes-1
            continue
    else:
        print("you won 110$")
        
    
    
game()