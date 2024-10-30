from datetime import datetime, date, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import ssl
import string
from django.contrib.humanize.templatetags import humanize


def getCurrentDatetime():
    return datetime.now()


def getCurrentDate():
    return date.today()


def get_strftime(str='%y%m%d'):
    today = date.today()
    return today.strftime(f'{str}')


def sendEmail(request, email_sender, email_recierver, email_password, email_subject, email_message):
    sender_email = email_sender
    receiver_email = email_recierver
    password = email_password

    message = MIMEMultipart("alternative")
    message["Subject"] = email_subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = email_message

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    try:
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        return True
    except Exception as error:
        username = request.user.username
        name = request.user.first_name + ' ' + request.user.last_name
        # sendException(
        #     request, username, name, error)
        message = {
            'isError': True,
            'title': "Server Error",
            'type': "error",
            'Message': 'On Error Occurs . Please try again or contact system administrator'
        }
        return False


def generate_verification_code(length=6):
    """Generate a random verification code."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def delete_session(request, key: str):
    """Delete a session value by its key."""
    if key in request.session:
        del request.session[key]
    return True


def formatNumber(number):
    # Format a number with commas
    return humanize.intcomma(number)


def check_file_format(file, size=2, file_type="image"):
    # Allowed file extensions and maximum file size (5MB)
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    if file_type == "document":
        ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

    if file_type == "both":
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx', 'doc'}

    MAX_FILE_SIZE = size * 1024 * 1024  # 5 MB

    # Get the file extension
    extention = file.name.split(".")[-1]
    extention = extention.lower()

    ext_string = " , ".join(ALLOWED_EXTENSIONS)

    if not extention in ALLOWED_EXTENSIONS:
        return f"This field only supports {ext_string}"

    if file.size > MAX_FILE_SIZE:
        return f"{file.name} file is more than {size}MB size'"

    return ''


def humanize_time_difference(past_time):
    """
    Returns a human-readable string representing the time difference between the current time and the given past time.

    Args:
    - past_time (datetime): The past time to compare against the current time.

    Returns:
    - str: A string representing the time difference in a human-readable format.
    """
    now = datetime.now(timezone.utc) if past_time.tzinfo else datetime.now()
    diff = now - past_time

    years = diff.days // 365
    months = (diff.days % 365) // 30
    weeks = diff.days // 7
    days = diff.days % 7
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    milliseconds = diff.microseconds // 1000

    if years > 0:
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif months > 0:
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif weeks > 0:
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif days > 0:
        return f"{days} day{'s' if days > 1 else ''} ago"
    elif hours > 0:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif minutes > 0:
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif seconds > 0:
        return f"{seconds} second{'s' if seconds > 1 else ''} ago"
    else:
        return f"{milliseconds} millisecond{'s' if milliseconds > 1 else ''} ago"
