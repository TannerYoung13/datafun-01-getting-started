# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

import statistics
data_a = [10, 11, 14, 20, 20, 20, 22, 24, 28, 31]
data_b = [2, 9, 13, 14, 20, 20, 24, 26, 32, 40] 
mean_data_a = statistics.mean(data_a)
mean_data_b = statistics.mean(data_b)
median_data_a = statistics.median(data_a)
median_data_b = statistics.median(data_b)
mode_data_a = statistics.mode(data_a)
mode_data_b = statistics.mode(data_b)
logger.info(
    f"Mean, median, and mode for data a is ={mean_data_a} {median_data_a}, {mode_data_a}")
logger.info(
    f"Mean, median, and mode for data b is ={mean_data_b} {median_data_b}, {mode_data_b}"
)