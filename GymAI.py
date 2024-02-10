import random

# Define a list of workout exercises
exercises = [
    "Push-ups",
    "Sit-ups",
    "Jumping jacks",
    "Squats",
    "Plank",
    "Lunges",
    "Bicep curls",
    "Tricep dips",
]

# Define a dictionary of workout categories
exercise_categories = {
    "Upper Body": ["Push-ups", "Bicep curls", "Tricep dips"],
    "Lower Body": ["Squats", "Lunges"],
    "Core": ["Sit-ups", "Plank"],
    "Cardio": ["Jumping jacks"],
}

def recommend_workout():
    print("Welcome to the Gym AI Assistant!")
    print("Here are some workout options:")
    
    # Print exercise categories
    for category, exercises_in_category in exercise_categories.items():
        print(f"{category}: {', '.join(exercises_in_category)}")

    # Get user input for the preferred exercise category
    user_category = input("Enter your preferred workout category: ").capitalize()

    # Check if the entered category is valid
    if user_category in exercise_categories:
        recommended_exercise = random.choice(exercise_categories[user_category])
        print(f"We recommend doing {recommended_exercise} today!")
    else:
        print("Invalid category. Please choose a valid workout category.")

if __name__ == "__main__":
    recommend_workout()
