# count how many vowels are present in a given string.

import logging

# Configure logging
logging.basicConfig(
    filename="f1.log",      
    level=logging.INFO,          
    format="%(asctime)s - %(levelname)s - %(message)s"
)

s: str = str(input("Enter a string: "))

logging.info("User entered string: %s", s)

count: int = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
        logging.info("Found vowel: %s", ch)

logging.info("Total vowels: %d", count) 