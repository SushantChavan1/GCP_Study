import re

text = "Contact of sushant: 123-456-7890"
cleaned = re.sub(r'\D', '', text)  # Remove non-digit characters
print("Cleaned Text:", cleaned)
