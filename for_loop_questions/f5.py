# reverse a string using a for loop (no slicing.)

import logging

logging.basicConfig(
    filename="f5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def reverse_string(s: str) -> str:
    logging.info("reverse_string function started")

    rev = ""

    for i in range(len(s)-1, -1, -1):
        logging.info("Adding character: %s", s[i])
        rev += s[i]

    logging.info("Function completed. Reversed string: %s", rev)
    return rev


s: str = input("Enter a string: ")
logging.info("User entered string: %s", s)

rev: str = reverse_string(s)

logging.info("Final output: %s", rev)
print("reversed string:", rev)