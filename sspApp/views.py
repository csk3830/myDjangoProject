from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 Support Solution Portal에 오신 걸 환영합니다.")

