price_of_product=float(input("Enter the price of the product: "))
discount_percentage="0%" if price_of_product<1000
discount_percentage="10%" if 1000<=price_of_product<5000
discount_percentage="20%" if price_of_product>=5000
print(f"The discount percentage for a product priced at {price_of_product} is: {discount_percentage}.")