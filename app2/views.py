from django.shortcuts import render

def gallery(request):
    return render(request, 'app2/gallery.html')

def services(request):
    return render(request, 'app2/services.html')

def team(request):
    return render(request, 'app2/team.html')
