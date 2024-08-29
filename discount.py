def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - ((discount_percent / 100) * price)
    else:
        final_price = price
    return final_price

def main():
    price = int(input("Enter The Original Price: "))
    discount_percent = int(input("Enter The discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after discount is: {final_price}")

main()
