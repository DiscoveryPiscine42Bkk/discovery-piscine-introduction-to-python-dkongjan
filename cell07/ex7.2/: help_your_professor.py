def average(scores_dict):
    """
    Takes a dictionary associating student first names with their assignment scores.
    Returns the average score of the class.
    """
    if not scores_dict:
        return 0  # Avoid division by zero if dictionary is empty
    
    total_score = sum(scores_dict.values())
    number_of_students = len(scores_dict)
    avg = total_score / number_of_students
    return avg

def main():
    # Example student scores
    student_scores = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Diana": 92,
        "Eve": 88
    }

    class_average = average(student_scores)
    print(f"Class average: {class_average:.2f}")

if __name__ == "__main__":
    main()