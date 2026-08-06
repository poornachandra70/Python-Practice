number = int(input())
sum_of_digits = 0
while(number > 0):
dig = number % 10
sum_of_digits += dig
number = number//10
# Extract and add each digit using a whi
print(f"Sum of Digits: {sum_of_digits}")