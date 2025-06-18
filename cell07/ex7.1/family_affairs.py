def find_the_redheads(family_dict):
    """
    Takes a dictionary of family members with first names as keys
    and hair colors as values. Returns a list of first names of
    those with red hair using the filter function.
    """
    redheads = list(filter(lambda name: family_dict[name].lower() == 'red', family_dict))
    return redheads

def main():
    # Example family dictionary
    family = {
        "Alice": "blonde",
        "Bob": "red",
        "Charlie": "brown",
        "Diana": "red",
        "Eve": "black"
    }

    redheads = find_the_redheads(family)
    print("Red-haired family members:")
    for name in redheads:
        print(name)

if __name__ == "__main__":
    main()