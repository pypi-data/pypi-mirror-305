def check_perms(request, perms):
    # Initialize result dictionary
    result = {
        'has_all_perms': False,
        'has_some_perms': False,
        'has_no_perms': False
    }

    # List to store which permissions the user has
    user_perms = []

    # Check each permission
    for perm in perms:
        if request.user.has_perm(perm):
            user_perms.append(perm)

    # Determine the result based on the permissions the user has
    if len(user_perms) == len(perms):
        result['has_all_perms'] = True
    elif len(user_perms) > 0:
        result['has_some_perms'] = True
    else:
        result['has_no_perms'] = True

    return result
