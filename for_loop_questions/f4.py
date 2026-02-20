# check whether a list is sorted in ascending order.

import logging

logging.basicConfig(
    filename="f4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

numbers = [1, 3, 5, 7, 9]
logging.info("Checking list: %s", numbers)

is_sorted = True

for i in range(len(numbers) - 1):
    logging.info("Comparing %d and %d", numbers[i], numbers[i + 1])

    if numbers[i] > numbers[i + 1]:
        logging.warning(
            "List is not sorted because %d > %d",
            numbers[i],
            numbers[i + 1]
        )
        is_sorted = False
        break

if is_sorted:
    logging.info("List is sorted in ascending order")
    print("List is sorted in ascending order")
else:
    logging.info("List is NOT sorted in ascending order")
    print("List is NOT sorted in ascending order")