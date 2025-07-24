numbers = input("enter the numbers: ")
nums = [int(s) for s in numbers.split()]

even_numbers = []
for n in nums:
	if n % 2 == 0:
		even_numbers.append(n)

with open(evenn_numbers.txt", "w") as f:
	for num in even_numbers:
		f.write(str(num) + "\n")

print("Even numbers saved in 'even_numbers.txt'")
