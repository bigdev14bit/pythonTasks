"""
1. collect input from users
2.
"""
purchase = int(input("Enter Purchase Amount: "))

if purchase < 1000:
    print("No Discount")
elif purchase <= 1000 and purchase >= 10000:
     discount = purchase * 0.05
     new_price = purchase - discount
     print("The Discounted Price Is: ", discount, " and your new price is ", new_price)

elif purchase <= 10000 and purchase >= 50000:
     discount = purchase * 0.1
     new_price = purchase - discount
     print("The Discounted Price Is: ", discount," and your new price is ", new_price )

else:
    discount = purchase * 0.2
    new_price = purchase - discount
    print("The Discounted Price Is: ", discount," and your new price is ", new_price )
