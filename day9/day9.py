def get_yn(prompt, yes_values={"y", "yes"}, no_values={"n", "no"}):
    
    while True:
        response = input(prompt).strip().lower()
        if response in yes_values:
            return True
        elif response in no_values:
            return False

def get_int(prompt, lo=None, hi=None):
   
    while True:
        try:
            value = int(input(prompt))
            if (lo is None or lo <= value) and (hi is None or value <= hi):
                return Value
        except ValueError:
            pass

def get_one_of(prompt, values):
    
    while True:
        value = input(prompt).strip().lower()
        if value in values:
            return value

def main():
    print(
        "Guessing Game\n"
        "\n"
        "Think of a number in [1..100],\n"
        "and I will try to guess \n"
    )

    if get_yn("Are you ready? (y/n): "):
        lo, hi = 1, 100
        got_it = False
        for attempt in range(1, 8):
            guess = (lo + hi) // 2
            print("I guess {}!".format(guess))
            res = get_one_of("Was this [L]ow, [H]igh, or [C]orrect? ", {"l", "h", "c"})            
            if res == "l":
                lo = guess + 1
            elif res == "h":
                hi = guess - 1
            else:  
                got_it = True
                break
            if lo > hi:
                break
        if got_it:
            print("Ha! Got it in {} guesses!".format(attempt))
        else:
            print("Something smells in the state of Denmark...")
    else:
        print("Bye!")

if __name__=="__main__":
    main()