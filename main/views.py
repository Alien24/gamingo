from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def zgadnij_liczbe(request):
    return render(request, 'main/zgadnij_liczbe.html')

def kolko_i_krzyzyk(request):
    return render(request, 'main/kolko_i_krzyzyk.html')

def sudoku(request):
    return render(request, 'main/sudoku.html')