from django.shortcuts import render

def my_page(request):
    context = {
        "name": "Gregory",
        "city": "Johannesburg"
    }

    return render(request, 'my_page.html', context)

def base(request):
    context = {

    }

    return render(request, 'base.html', context)
