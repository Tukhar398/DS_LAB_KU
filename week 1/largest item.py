user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(item) for item in user_list]
largest_item = max(user_list)
print(f"The largest item in the list is: {largest_item}")
