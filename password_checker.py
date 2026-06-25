import string

password = input("Enter password: ")
score = 0
suggestions = []

if len(password) >= 10:
    score += 1
else:
    suggestions.append("Make it at least 10 characters long.")

if any(c.isupper() for c in password):
    score += 1
else:
    suggestions.append("must have atleat one uppercase letter.")

if any(c.islower() for c in password):
    score += 1
else:
    suggestions.append("must have atleat one lowercase letter.")

if any(c.isdigit() for c in password):
    score += 1
else:
    suggestions.append("must have atleat one digit.")

if any(c in string.punctuation for c in password):
    score += 1
else:
    suggestions.append("must have atleat one special character.")

if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Medium password")
else:
    print("Strong password")

print("password score: ", score, "/5")

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)