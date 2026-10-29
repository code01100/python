# # # for token_numbers in range(1, 11):
# # #     print(f"Serving chai to Token number: #{token_numbers}")


# # for batch_number in range(1, 5):
# #     print(f"Serving batch number: #{batch_number}")

# names_list = ["mint", "ginger", "cardamom", "clove", "cinnamon"]

# for name in names_list:
#     print(f"Serving chai with {name} flavor")

# menu = ["mint", "ginger", "cardamom", "clove", "cinnamon"]

# for m in menu:
#     print(f"Serving chai with {m} flavor")

# names = ["Bob", "Alice", "Eve", "Charlie"]

# amounts = [100, 200, 300, 400]

# j= 0

# for i in names:
#     print(f"Serving chai to {i} with amount {amounts[j]}")
#     j += 1

# for names, amounts in zip(names, amounts):
#     print(f"Serving chai to {names} with amount {amounts}")


#***While loops***
# temp = 40
# while temp < 100:
#     temp += 15
#     print(f"Temperature is {temp} degrees Celsius")


# print("Tea is ready to boil")

# flavors = ["mint", "Out of Stock", "cardamom", "Discontinued", "cinnamon"]

# for flavor in flavors:
#     if flavor == "Out of Stock":
#         print(f"Sorry, {flavor} flavor is currently unavailable.")
#         continue
#     elif flavor == "Discontinued":
#         print(f"Sorry, {flavor} flavor has been discontinued.")
#         break
#     else:
#         print(f"Serving chai with {flavor} flavor")

# staff = [("Alice", 16), ("Bob", 17), ("Charlie", 18)]
# for name, age in staff:
#     if age <= 18:
#         print(f"{name} is eligible to manage the staff")
#         break
#     else:
#         print(f"No one is eligible to manage the staff")

#***Walrus operator***
# value = 13
# if (remainder := value % 5):
#     print(f"{value} is not divisible by 5, remainder is {remainder}")

# available_sizes = ["small", "medium", "large", "extra large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Sorry, {requested_size} size is not available.")

# flavors = ["mint", "ginger", "cardamom", "clove", "cinnamon"]

# while (requested_flavor := input("Enter your chai flavor: ")) not in flavors:
#     print(f"Sorry, {requested_flavor} flavor is not available.")

# print(f"You choose {requested_flavor} flavor. Serving your chai now!")

# coupon discount program
# users = [
#     {"id": 1,"total": 100, "coupon": "P20"},
#     {"id": 2,"total": 200, "coupon": "F30"},    
#     {"id": 3,"total": 80, "coupon": "P50"},
#     {"id": 4,"total": 850, "coupon": "P100"},]

# discounts = {
#     "P20": (0.2,0),
#     "F30": (0.5,0),
#     "P50": (0.3,0),
#     "P100": (0.0,10)
# }

# for user in users:
#     percent,fixed = discounts.get(user["coupon"],(0,0))
#     discount_amount = user["total"] * percent + fixed
#     print(f"User ID: {user['id']}, Total: {user['total']}, Coupon: {user['coupon']}, Discount Amount: {discount_amount}")


