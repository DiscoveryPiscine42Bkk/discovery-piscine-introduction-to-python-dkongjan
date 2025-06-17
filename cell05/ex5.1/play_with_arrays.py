def main():
    # Define the original array of numbers
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # Create a new array by adding 2 to each element in the original array
    new_array = [x + 2 for x in original_array]

    # Display both arrays
    print("Original array:", original_array)
    print("New array     :", new_array)