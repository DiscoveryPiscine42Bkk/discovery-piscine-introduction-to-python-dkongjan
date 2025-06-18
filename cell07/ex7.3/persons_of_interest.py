
def famous_births(figures_dict):
    """
    Takes a dictionary where each key is an identifier and each value is a dictionary
    with keys ':name' and ':date_of_birth' (format YYYY-MM-DD).
    Sorts by birth date and displays each figure.
    """
    # Sort by the ':date_of_birth' value
    sorted_figures = sorted(
        figures_dict.values(),
        key=lambda entry: entry[':date_of_birth']
    )

    for figure in sorted_figures:
        print(f"{figure[':name']} was born on {figure[':date_of_birth']}")

def main():
    historical_figures = {
        1: {':name': "Isaac Newton", ':date_of_birth': "1643-01-04"},
        2: {':name': "Albert Einstein", ':date_of_birth': "1879-03-14"},
        3: {':name': "Marie Curie", ':date_of_birth': "1867-11-07"},
        4: {':name': "Ada Lovelace", ':date_of_birth': "1815-12-10"}
    }

    famous_births(historical_figures)

if __name__ == "__main__":
    main()