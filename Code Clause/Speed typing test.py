import time

def typing_speed_test():
    print("Welcome to the typing speed test!")
    time.sleep(1)
    print("You will be given a sentence to type. Ready?")
    time.sleep(1)
    
    sentence = "The quick brown fox jumps over the lazy dog"
    print(sentence)
    
    start_time = time.time()
    user_input = input("Type the sentence above and press Enter to finish:\n")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    speed = words_typed / time_taken
    
    print(f"\nYou typed {words_typed} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is {speed:.2f} words per second.")
    
    if user_input == sentence:
        print("Congratulations! You typed the sentence correctly.")
    else:
        print("Oops! You made a mistake while typing.")
        
typing_speed_test()
