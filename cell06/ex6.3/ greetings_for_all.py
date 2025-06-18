def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print("Error: Name must be a string.")

# Example usage:
if __name__ == "__main__":
    greetings()                  # Should print: Welcome, noble stranger!
    greetings("Alice")           # Should print: Welcome, Alice!
    greetings(42)                # Should print: Error: Name must be a string.