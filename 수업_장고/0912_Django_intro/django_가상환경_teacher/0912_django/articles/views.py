from django.shortcuts import render

# Create your views here.
def index(request):
    # 어떤 화면을 보여줄지 return
    return render(request, "articles/index.html")