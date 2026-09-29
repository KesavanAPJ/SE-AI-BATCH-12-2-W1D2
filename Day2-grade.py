def calculate_grade(mark):
    """Returns the letter grade for a given mark based on the assignment scale."""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'E'

def main():
    user_input = input("Enter your mark (0-100): ")
    
    try:
        # Convert input to a float to handle potential decimal marks
        mark = float(user_input)
        
        # Check if the mark is within the valid 0-100 range
        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
        else:
            # Format to integer if there are no decimal places for a cleaner output
            if mark.is_integer():
                mark = int(mark)
                
            grade = calculate_grade(mark)
            print(f"Mark: {mark} -> Grade: {grade}")
            
    except ValueError:
        # Catch non-numeric input to prevent the program from crashing
        print("Error: Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()