# your code goes here!
import time

def countdown(int):
    timer = int
    while timer > 0:
        print(f'{timer} SECOND(S)!')
        timer -= 1
    print("HAPPY NEW YEAR!")

countdown(20)

def countdown_with_sleep(int):
    timer = int
    while timer > 0:
        time.sleep(1)
        print(f'{timer} SECOND(S)!')
        timer -= 1
    print("HAPPY NEW YEAR!")