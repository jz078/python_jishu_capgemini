# find the second largest element in a list using a for loop.

import logging

logging.basicConfig(
    filename="f3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(list1):
    logging.info("Function second_largest started")

    largest = float('-inf')
    second = float('-inf')

    for num in list1:
        logging.info("Checking number: %d", num)

        if num > largest:
            logging.info("New largest found: %d", num)
            second = largest
            largest = num

        elif num > second and num != largest:
            logging.info("New second largest found: %d", num)
            second = num

    logging.info("Function completed. Second largest: %s", second)
    return second


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
logging.info("User entered numbers: %s", numbers)

result = second_largest(numbers)

logging.info("Final result: %s", result)
print("Second largest:", result)