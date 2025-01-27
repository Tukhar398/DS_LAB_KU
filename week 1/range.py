number = int(input("Enter a number: "))
start = 10
end = 50
if start <= number <= end:
    print(f"{number} is in the range between {start} and {end}.")
else:
    print(f"{number} is not in the range between {start} and {end}.")
