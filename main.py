# main.py
from messages import WELCOME_PREFIX, WELCOME_NAME
from utils import compose

def main():
    msg = compose(WELCOME_PREFIX, WELCOME_NAME, "!")
    # ensure exact expected output (no extra spaces)
    print(msg)

if __name__ == "__main__":
    main()
