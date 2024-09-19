import time

def timedown (startTime):
    while startTime > 0:
        startTime -=1
        print(startTime+1)
        time.sleep(1)
        
    else:
        print(" you time is finish")
        
        
startTime=int(input("wie viel sekundan?"))
timedown(startTime)