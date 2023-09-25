from django.shortcuts import render

# Create your views here.
def menu(request):

    menu = [
        "창평순대국밥", "명동칼국수", "함박스테이크"
    ]
    
    hate_menu = "명동칼국수"

    context = {
        "menu" : menu,
        "hm" : hate_menu
    }

    return render(request, 'menus/menu.html', context)