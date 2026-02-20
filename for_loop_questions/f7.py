# find the missing number in a list containing numbers from 1 to N.

import logging

logging.basicConfig(
    filename="f7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

nums = [1, 2, 4, 5]
logging.info("Original list: %s", nums)

n = len(nums) + 1
logging.info("Calculated n value: %d", n)

expected_sum = n * (n + 1) // 2
logging.info("Expected sum (1 to n): %d", expected_sum)

actual_sum = sum(nums)
logging.info("Actual sum of list: %d", actual_sum)

missing_number = expected_sum - actual_sum
logging.info("Missing number calculated: %d", missing_number)

print("Missing number is:", missing_number)