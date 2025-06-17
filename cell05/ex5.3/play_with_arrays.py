def main():
    # Define the original array of numbers
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # Use a set to keep track of seen values and avoid duplicates
    seen = set()
    new_array = []

    for x in original_array:
        if x > 5:
            new_value = x + 2
            if new_value not in seen:
                new_array.append(new_value)
                seen.add(new_value)

    # Display both arrays
    print("Original array:", original_array)
    print("New array (values > 5 + 2, no duplicates):", new_array)