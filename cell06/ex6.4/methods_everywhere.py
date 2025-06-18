def shrink(text):
    """Displays the first eight characters of the provided string."""
    if isinstance(text, str):
        print(text[:8])
    else:
        print("Error: Input must be a string.")

def main():
    # Example usages of shrink()
    shrink("OpenAI GPT-4")        # Should print: OpenAI G
    shrink("Hi")                  # Should print: Hi
    shrink(12345)                 # Should print: Error: Input must be a string

if __name__ == "__main__":
    main()