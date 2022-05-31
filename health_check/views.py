from django.http import HttpResponse


def health_check(request):  # noqa
    return HttpResponse("ok", status=200)
