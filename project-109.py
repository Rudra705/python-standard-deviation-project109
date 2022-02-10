import statistics
import csv
import pandas as pd 

file = pd.read_csv("StudentsPerformance.csv")
reading_score = file["reading score"].to_list()
writing_score = file["writing score"].to_list()
math_score = file["math score"].to_list()

# Mean of all scores
mean_of_reading_score = statistics.mean(reading_score)
print("The mean of the reading score is:", mean_of_reading_score)

mean_of_writing_score = statistics.mean(writing_score)
print("The mean of the writing score is:", mean_of_writing_score)

mean_of_math_score = statistics.mean(math_score)
print("The mean of the math score is:", mean_of_math_score,"\n")

# Mode of all scores
mode_of_reading_score = statistics.mode(reading_score)
print("The mode of the reading score is:", mode_of_reading_score)

mode_of_writing_score = statistics.mode(writing_score)
print("The mode of the writing score is:", mode_of_writing_score)

mode_of_math_score = statistics.mode(math_score)
print("The mode of the math score is:", mode_of_math_score, "\n")

# Median of all scores
median_of_reading_score = statistics.median(reading_score)
print("The median of the reading score is:", median_of_reading_score)

median_of_writing_score = statistics.median(writing_score)
print("The median of the writing score is:", median_of_writing_score)

median_of_math_score = statistics.mean(math_score)
print("The median of the math score is:", median_of_math_score, "\n")

# Standard Deviation of all scores
standard_deviation_of_reading_score = statistics.stdev(reading_score)
print("The standard deviation of the reading score is:", standard_deviation_of_reading_score)

standard_deviation_of_writing_score = statistics.stdev(writing_score)
print("The standard deviation of the writing score is:", standard_deviation_of_writing_score)

standard_deviation_of_math_score = statistics.stdev(math_score)
print("The standard deviation of the math score is:", standard_deviation_of_math_score, "\n")

# 1,2 and 3 standard deviation percentage calculation of reading score
first_sd_start_reading ,first_sd_end_reading = mean_of_reading_score - standard_deviation_of_reading_score, mean_of_reading_score + standard_deviation_of_reading_score
second_sd_start_reading ,second_sd_end_reading = mean_of_reading_score - (2 * standard_deviation_of_reading_score), mean_of_reading_score + (2 * standard_deviation_of_reading_score)
third_sd_start_reading , third_sd_end_reading = mean_of_reading_score - (3 * standard_deviation_of_reading_score), mean_of_reading_score + (3 * standard_deviation_of_reading_score)

numbers_in_first_sd_reading = [result for result in reading_score if result > first_sd_start_reading and result < first_sd_end_reading  ]
percentage_in_first_sd_reading = (len(numbers_in_first_sd_reading) *100 / len(reading_score))
print("{}% of data lies between first standard deviatoin in reading score".format((len(numbers_in_first_sd_reading) *100 / len(reading_score))))

numbers_in_second_sd_reading = [result for result in reading_score if result > second_sd_start_reading and result < second_sd_end_reading  ]
percentage_in_second_sd_reading = (len(numbers_in_second_sd_reading) *100 / len(reading_score))
print("{}% of data lies between second standard deviatoin in reading score".format((len(numbers_in_second_sd_reading) *100 / len(reading_score))))

numbers_in_third_sd_reading = [result for result in reading_score if result > third_sd_start_reading and result < third_sd_end_reading  ]
percentage_in_third_sd_reading = (len(numbers_in_third_sd_reading) *100 / len(reading_score))
print("{}% of data lies between third standard deviatoin in reading score \n".format((len(numbers_in_third_sd_reading) *100 / len(reading_score))))

# 1,2 and 3 standard deviation percentage calculation of writing score
first_sd_start_writing ,first_sd_end_writing = mean_of_writing_score - standard_deviation_of_writing_score, mean_of_writing_score + standard_deviation_of_writing_score
second_sd_start_writing ,second_sd_end_writing = mean_of_writing_score - (2 * standard_deviation_of_writing_score), mean_of_writing_score + (2 * standard_deviation_of_writing_score)
third_sd_start_writing , third_sd_end_writing = mean_of_writing_score - (3 * standard_deviation_of_writing_score), mean_of_writing_score + (3 * standard_deviation_of_writing_score)

numbers_in_first_sd_writing = [result for result in writing_score if result > first_sd_start_writing and result < first_sd_end_writing  ]
percentage_in_first_sd_writing = (len(numbers_in_first_sd_writing) *100 / len(writing_score))
print("{}% of data lies between first standard deviatoin in writing score".format((len(numbers_in_first_sd_writing) *100 / len(writing_score))))

numbers_in_second_sd_writing = [result for result in writing_score if result > second_sd_start_writing and result < second_sd_end_writing  ]
percentage_in_second_sd_writing = (len(numbers_in_second_sd_writing) *100 / len(writing_score))
print("{}% of data lies between second standard deviatoin in writing score".format((len(numbers_in_second_sd_writing) *100 / len(writing_score))))

numbers_in_third_sd_writing = [result for result in writing_score if result > third_sd_start_writing and result < third_sd_end_writing  ]
percentage_in_second_sd_writing = (len(numbers_in_third_sd_writing) *100 / len(writing_score))
print("{}% of data lies between third standard deviatoin in writing score \n".format((len(numbers_in_third_sd_writing) *100 / len(writing_score))))


# 1,2 and 3 standard deviation percentage calculation of reading score
first_sd_start_math ,first_sd_end_math = mean_of_math_score - standard_deviation_of_math_score, mean_of_math_score + standard_deviation_of_math_score
second_sd_start_math ,second_sd_end_math = mean_of_math_score - (2 * standard_deviation_of_math_score), mean_of_math_score + (2 * standard_deviation_of_math_score)
third_sd_start_math , third_sd_end_math = mean_of_math_score - (3 * standard_deviation_of_math_score), mean_of_math_score + (3 * standard_deviation_of_math_score)

numbers_in_first_sd_math = [result for result in math_score if result > first_sd_start_math and result < first_sd_end_math  ]
percentage_in_first_sd_math = (len(numbers_in_first_sd_math) *100 / len(math_score))
print("{}% of data lies between first standard deviatoin in math score".format((len(numbers_in_first_sd_math) *100 / len(math_score))))

numbers_in_second_sd_math = [result for result in math_score if result > second_sd_start_math and result < second_sd_end_math  ]
percentage_in_second_sd_math = (len(numbers_in_second_sd_math) *100 / len(math_score))
print("{}% of data lies between second standard deviatoin in math score".format((len(numbers_in_second_sd_math) *100 / len(math_score))))

numbers_in_third_sd_math = [result for result in math_score if result > third_sd_start_math and result < third_sd_end_math  ]
percentage_in_second_sd_math = (len(numbers_in_third_sd_math) *100 / len(math_score))
print("{}% of data lies between third standard deviatoin in math score \n".format((len(numbers_in_third_sd_math) *100 / len(math_score))))
