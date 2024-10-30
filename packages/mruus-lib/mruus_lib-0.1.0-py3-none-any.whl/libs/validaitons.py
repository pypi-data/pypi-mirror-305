import re


def validate(value, extra=[], fields=[None, '' , 'null' , 'undefined']):
    fields = fields
    fields.extend(extra)
    return value in fields


def is_valid_email(email):
    email_regex = re.compile(
        r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    )
    
    # Use the regex to check if the email matches the pattern
    return re.match(email_regex, email) is not None