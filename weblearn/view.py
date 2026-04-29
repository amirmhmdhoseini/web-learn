from django.http import HttpResponse

def test(request):
    return HttpResponse('<strong> this is a test</strong>')