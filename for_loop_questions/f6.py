# remove duplictate elements from a list while preserving order.

import logging

logging.basicConfig(
    filename="f6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
logging.info("Original list: %s", numbers)

unique_list = []

for item in numbers:
    logging.info("Checking item: %d", item)

    if item not in unique_list:
        unique_list.append(item)
        logging.info("Added %d to unique_list", item)
    else:
        logging.warning("Duplicate found: %d", item)

logging.info("Final unique list: %s", unique_list)

print(unique_list)