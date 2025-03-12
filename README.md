# Diceware Generator

A simple Diceware password generator written in Python.

## Description

This project generates a secure passphrase using the Diceware method. The passphrase is created by rolling dice to generate a sequence of numbers, which are then mapped to words from a word list.

## Features

- Generates a passphrase with a specified number of words.
- Uses a secure random number generator.
- Logs the process for debugging purposes.

## Requirements

- Python 3.x

## Installation

- Clone the repository:
    ```sh
    git clone https://github.com/JamesHinson/diceware-generator.git
    cd diceware-generator
    ```

## Usage

1. Run the script:
    ```sh
    python diceware.py
    ```

2. Follow the prompts to generate a passphrase.

## Files

- `diceware.py`: The main script for generating the passphrase.
- `eff_large_wordlist.txt`: The word list used for generating the passphrase.
- - Not included in the repository, download from [EFF Diceware Wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt).
- `diceware.log`: The log file for debugging.

## License

This project is licensed under the MIT License.