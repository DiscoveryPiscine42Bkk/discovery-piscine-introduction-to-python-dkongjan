def array_of_names(name_dict):
    """
    Takes a dictionary of first names as keys and last names as values,
    returns a list of full names with the first letter of each name capitalized.
    """
    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

def main():
    # Example dictionary
    names = {
        "john": "doe",
        "jane": "smith",
        "alEx": "joHNsOn"
    }

    result = array_of_names(names)
    print("Formatted full names:")
    for name in result:
        print(name)

if __name__ == "__main__":
    main()