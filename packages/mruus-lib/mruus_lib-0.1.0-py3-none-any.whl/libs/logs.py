from accounts.models import ErrorLogs, AuditTrials
import httpagentparser, traceback, sys

def sendException(request, error, is_web=True):
    user = None
    if request.user.is_authenticated:
        user = request.user

    ip = request.META.get('REMOTE_ADDR')
    get_client_agent = request.META['HTTP_USER_AGENT']

    if is_web:
        detect_os = httpagentparser.detect(
            get_client_agent)['os']['name']
        browser = httpagentparser.detect(get_client_agent)[
            'browser']['name']
    else:
        detect_os = request.data['os']
        browser = request.data['browser']

    trace_err = traceback.format_exc()
    Expected_error = str(sys.exc_info()[0])
    field_error = str(sys.exc_info()[1])
    line_number = str(sys.exc_info()[-1].tb_lineno)
    error_logs = ErrorLogs(
        user=user,
        ip_address=ip,
        browser=browser,
        expected_error=Expected_error,
        field_error=field_error,
        trace_back=str(trace_err),
        line_number=line_number,
        os=detect_os,
    )

    error_logs.save()


def sendAudit(request, module, action, is_web=True):
    user = None

    if request.user.is_authenticated:
        user = request.user

    ip = request.META.get('REMOTE_ADDR')
    get_client_agent = request.META['HTTP_USER_AGENT']

    if is_web:
        detect_os = httpagentparser.detect(
            get_client_agent)['os']['name']
        browser = httpagentparser.detect(get_client_agent)[
            'browser']['name']
    else:
        detect_os = request.data['os']
        browser = request.data['browser']

    action = action
    module = module

    audit_trails = AuditTrials(
        user=user,
        Actions=action,
        path=request.path,
        Module=module,
        operating_system=detect_os,
        ip_address=ip,
        browser=browser,
    )

    audit_trails.save()

    return {
        'title': "Audit Trials Saved Successfully!!",
    }


def get_audit_data(prev_data, current_data, instance=True):
    # Changes
    changes = []
    for field, old_value in prev_data.items():
        if instance:
            new_value = getattr(current_data, field)
        else:
            new_value = current_data[field]
            
        if old_value != new_value:
            changes.append(
                f'{field.replace("_", " ").title()}: {old_value} -into- {new_value}')

    changes = "\n".join(changes) if len(changes) > 0 else "---"
    return changes