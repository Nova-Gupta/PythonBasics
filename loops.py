#for loop example
for i in range(5):
    print("Iteration:", i)

#while loop equivalent
i = 0
while i < 5:
    print("Count:", i)
    i += 1

#loop with break and continue
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num > 7:
        break  # Stop the loop if number is greater than 7
    print("Odd number less than 8:", num)