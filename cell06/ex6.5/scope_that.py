def add_one(x):
    x += 1
    return x

def main():
    number = 10
    print("Before calling add_one:", number)
    
    add_one(number)  # This changes a *copy* of `number`, not the original.
    
    print("After calling add_one:", number)

if __name__ == "__main__":
    main()