"""
Demonstrate the implementation of a simple Countdown timer using recursion,
i.e.: stack-based iteration
"""
import time


def countdown(n):
    if n > 900:
        # Python stack is limited to 1000
        raise ValueError("Value to high")
    if n <= 0:
        print("Done")
        return
    print(n)
    time.sleep(0.25)
    countdown(n - 1)


def main():
    countdown(8)


if __name__ == "__main__":
    main()
