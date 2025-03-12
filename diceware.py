import logging
import secrets

logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def roll_dice() -> str:
    return "".join(str(secrets.randbelow(6) + 1) for _ in range(5))


def load_word_list() -> dict:
    try:
        with open("eff_large_wordlist.txt") as f:
            return {line.split(maxsplit=1)[0]: line.split(maxsplit=1)[1].strip() for line in f}
    except FileNotFoundError:
        print("Word list file not found. Ensure 'eff_large_wordlist.txt' is in the working directory.")
        logger.error("Word list file not found. Ensure 'eff_large_wordlist.txt' is in the working directory.")
        exit(1)


def generate_word(word_list: dict) -> str:
    return word_list[roll_dice()]


def generate_passphrase(num_words: int) -> str:
    word_list = load_word_list()
    passphrase = []
    for i in range(num_words):
        logger.debug(f"Generating word {i + 1}")
        passphrase.append(generate_word(word_list))
    return " ".join(passphrase)


def main():
    logging.basicConfig(filename='diceware.log', level=logging.DEBUG, format=FORMAT)
    # logger.setLevel(logging.DEBUG)  # Uncomment to start logging
    print("Welcome to Diceware!")
    try:
        num_words = int(input("How many words would you like to generate? "))
        if num_words <= 0:
            raise ValueError("Number of words must be greater than zero.")
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        print("Please enter a valid positive integer.")
        return

    print("Your passphrase is:", generate_passphrase(num_words))


if __name__ == '__main__':
    main()
