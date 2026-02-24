def online_bill_payment(name, price, discount=10/100):
    total = sum(price)
    discount_amount = (discount / 100) * total
    final_price = total - discount_amount
    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Discount: {discount_amount}")
    print(f"Final Price: {final_price}")
online_bill_payment("Vivek", [100, 200, 300])

