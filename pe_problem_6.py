#! /usr/bin/python

## sum_of_squareum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
## The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum 

square_of_sum = 0
counter = 0
sum_counter = 0
diff_of_soq_and_sos = 0
sum_of_square = 0
square_of_sum = 0

for counter in range(1, 101):
  sum_of_square += (counter * counter)
  sum_counter += counter
  print (str(counter) + "  " + str(sum_of_square) + "   " + str(sum_counter))

square_of_sum = sum_counter * sum_counter
diff_of_soq_and_sos = square_of_sum - sum_of_square

print ("Sum of Square : " + str(sum_of_square))
print ("Square of Sum : " + str(square_of_sum))

print ("The difference between the square of sum and the sum of square is: " + str(diff_of_soq_and_sos))


