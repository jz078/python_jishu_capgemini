# print the frequency of each character in a string.
import logging

logging.basicConfig(
    filename="f2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def function(s: str) -> dict:
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
            logging.info("Incremented count of '%s' to %d", ch, freq[ch])
        else:
            freq[ch] = 1
            logging.info("Added new character '%s' with count 1", ch)

    logging.info("Function completed")

    return freq



s: str = input("Enter a string: ")
logging.info("User entered string: %s", s)

dict1 = function(s)

logging.info("Final frequency dictionary: %s", dict1)
print(dict1)