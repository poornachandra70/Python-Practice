starting_number = int(input())
ending_number = int(input())

count = 0

# visit every number the values divisible by 3
for i in range(starting_number, ending_number + 1):
    if i % 3 == 0:
        count += 1

print(f"Divisible by 3 : {count}")