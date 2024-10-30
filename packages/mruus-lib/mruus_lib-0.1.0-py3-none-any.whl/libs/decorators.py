from functools import wraps
from django.shortcuts import render
from django.http import JsonResponse

# _library imports
from libs import messages, logs


def handle_exceptions(error_display="page"):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                return view_func(request, *args, **kwargs)
            except Exception as e:
                # Log the exception
                logs.sendException(request, e)
                print(e)

                # Decide the return based on a condition, e.g., a request parameter
                if error_display == 'alert':
                    return JsonResponse(messages.error_message("Exception has been caught, contact the admins!"), status=500)
                else:
                    context = {'error_message': str(e)}
                    return render(request, 'pages/404.html', context, status=500)

        return _wrapped_view
    return decorator
