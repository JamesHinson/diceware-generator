import logging
import secrets

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Change to DEBUG to start logging
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def roll_dice() -> str:
    total_rolls = ""
    for _ in range(5):
        dice_roll = secrets.randbelow(6) + 1
        logger.debug(f"You rolled a {dice_roll}")
        total_rolls += str(dice_roll)
    total_rolls = str(int(total_rolls) )
    return total_rolls


def load_word_list() -> dict:
    with open("eff_large_wordlist.txt") as f:
        return {line.split('\t')[0].strip(): line.split('\t')[1].strip() for line in f.readlines()}


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
    print("Welcome to Diceware!")
    num_words = int(input("How many words would you like to generate? "))
    print("Your passphrase is: ", generate_passphrase(num_words))


if __name__ == '__main__':
    main()
