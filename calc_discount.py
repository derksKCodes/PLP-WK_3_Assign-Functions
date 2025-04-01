# Function to calculate the discount price
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Main function that prompts user for input and prints the result
def main():
    # Input for original price and discount percentage
    price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price after discount
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price or original price if no discount is applied
    if final_price == price:
      #prints price in 2 decimal places
        print(f"The original price is: ${price:.2f}. No discount applied.")
    else:
        print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}.")

# Run the main function
main()
