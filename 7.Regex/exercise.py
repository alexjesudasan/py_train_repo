import re

def validate_email(email):
    # Basic pattern for validating an email
    pattern = r'^[\w\.]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Examples
print(validate_email("abc.def@gmail.com"))
print(validate_email("alex.bn@gmail"))