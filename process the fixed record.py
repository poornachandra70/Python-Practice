product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Create the fixed product record as a tuple (excluding reorder_level)
product_record = (product_id, product_name, category, unit_price, quantity)

# Access the product ID and product name using indexes (as required, though available in tuple)
_pid = product_record[0]
_pname = product_record[1]

# Unpack the complete tuple into separate variables
p_id, p_name, p_cat, p_price, p_qty = product_record

# Calculate the total stock value
stock_value = p_price * p_qty

# Determine the stock status using the available quantity and reorder level
if p_qty == 0:
    stock_status = "Out of Stock"
elif p_qty <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the complete processed product record
print(f"Product ID: {p_id}")
print(f"Product Name: {p_name}")
print(f"Category: {p_cat}")
print(f"Unit Price: {p_price:.2f}")
print(f"Available Quantity: {p_qty}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")