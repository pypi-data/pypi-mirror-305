def validation_message(message):
    return {
        'status': False,
        'message': message,
        'title': "Validation Message",
        'icon': "warning",
    }


def success_message(message):
    return {
        'status': True,
        'message': message,
        'title': "Congratulations!",
        'icon': "success",
    }

def error_message(message):
    return {
        'status': False,
        'message': message,
        'title': "Ooops!",
        'icon': "error",
    }


def warning_message(message):
    return {
        'status': False,
        'message': message,
        'title': "Hey wait !",
        'icon': "warning",
    }


def info_message(message):
    return {
        'status': False,
        'message': message,
        'title': "Did you know that!",
        'icon': "info",
    }