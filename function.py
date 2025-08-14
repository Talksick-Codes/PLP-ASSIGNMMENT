##Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
def calculate_discount(price,discount_percent):
    if discount_percent>=0.2:
        final_price=price*(1-discount_percent)
    else:
        final_price=price
    return final_price
price=float(input("Input price: "))
discount_percent=float(input("Input discount percentage: "))
final_price=calculate_discount(price,discount_percent)
print(f"This is the final price:{final_price}")
