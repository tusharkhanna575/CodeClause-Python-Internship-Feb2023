import time
import random

def random_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey"
    ]
    return random.choice(quotes)


def typing_speed_test():
    quote = random_quote()
    print("Type the following text as quickly and accurately as possible:")
    print(quote)
    input("Press Enter to begin...")

    start_time = time.time()

    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time

    words_typed = len(user_input.split())
    error_count = sum(1 for i, j in zip(user_input, quote) if i != j)

    wpm = words_typed / (elapsed_time / 60)
    accuracy = ((len(quote) - error_count) / len(quote)) * 100

    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

typing_speed_test()
