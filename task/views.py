from django.shortcuts import render
from django.http import HttpResponse

def front(request):
    return render (request,"page1.html") 


def back(request):
    sentence = request.POST.get('sentence','default')
    removepunct = request.POST.get('removepunc','off')
    counter = request.POST.get('counter','off')
    capital = request.POST.get('capital','off')
    spaceremove = request.POST.get('spaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')
    titleviews = request.POST.get('titleviews','off')

    # This is for remove punctuation
    if(removepunct == 'on'):
        puntuation = """(,.;:''""?}]{”“’’/[_-!<>)\|"""
        checking =""
        for char in sentence:
            if (char not in puntuation):
                checking = checking+char
        solve = {'purpose':'Remove punctuations','workdone':checking}
        sentence = checking
        
    
    if (counter == 'on'):
        checking = ''
        for index,char in enumerate (sentence):
            if not(sentence[index] == " "):
                checking = checking + char
        checking = len(checking)
        solve = {'purpose':'Grammer Correctness','workdone':checking}
        sentence = checking
        
    
    if (spaceremove == 'on'):
        checking = ''
        for index,char in enumerate (sentence):
            if not(sentence[index] == " "):
                checking = checking + char
        solve = {'purpose':'Grammer Correctness','workdone':checking}
        sentence = checking
        
    
    if(capital == 'on'):
        checking = sentence.capitalize()
        solve = {'purpose':'Grammer Correctness','workdone':checking}
        sentence = checking
        
    
    if(newlineremove == 'on'):
        checking =""
        for char in sentence:
            if char != '\n' and char !='\r':
                checking = checking + char
        solve = {'purpose':'Grammer Correctness','workdone':checking}
        sentence = checking
    
    if(titleviews == 'on'):
        checking = sentence.title()
        solve = {'purpose' : 'Grammer Correctness','workdone':checking}

        

    if (removepunct != 'on'and counter != 'on' and spaceremove != 'on'and capital != 'on' and newlineremove != 'on' and titleviews != 'on'):
        return HttpResponse("Page not found 404")
    
    return render (request,"page2.html",solve)

# Create your views here.
