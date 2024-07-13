import re

def assess_password_strength(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digits': re.search(r'\d', password) is not None,
        'special': re.search(r'[\W_]', password) is not None,
    }
    score = sum(criteria.values())
    if score == 5:
        strength = 'Strong'
    elif score >= 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'
    feedback = []
    if not criteria['length']:
        feedback.append('Password should be at least 8 characters long.')
    if not criteria['uppercase']:
        feedback.append('Password should contain at least one uppercase letter.')
    if not criteria['lowercase']:
        feedback.append('Password should contain at least one lowercase letter.')
    if not criteria['digits']:
        feedback.append('Password should contain at least one digit.')
    if not criteria['special']:
        feedback.append('Password should contain at least one special character.')

    return strength, feedback

def main():
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
