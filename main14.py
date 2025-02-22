def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Main code
if __name__ == "__main__":
    try:
        # Ask the user for a number
        num = int(input("Enter a number to check if it's odd or even: "))
        # Call the function
        check_odd_even(num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
How the Code Works:
