import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Your password should be at least 8 characters long.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 2
    else:
        feedback.append("Your password should include at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 2
    else:
        feedback.append("Your password should include at least one lowercase letter.")

    # Digit check
    if any(char.isdigit() for char in password):
        score += 2
    else:
        feedback.append("Your password should include at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Your password should include at least one special character (e.g., @, #, $).")

    return score, feedback

# Step 1: Get user input
password = input(" Enter a password: ")

# Step 2: Evaluate password
strength_score, messages = check_password_strength(password)

# Step 3: Display results
if strength_score == 10:
    print(" Your password is **strong!** ")
else:
    print(f"Password strength: {strength_score}/10")
    for msg in messages:
        print(f" {msg}")

# Bonus: Suggest password improvement
if strength_score < 10:
    print("🔹 Try making your password longer and including a mix of uppercase, lowercase, numbers, and symbols for better security.")
