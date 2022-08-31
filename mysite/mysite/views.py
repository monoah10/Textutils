# I HAVE CREATED THIS FILE --- NOAH
from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    UPPERCASE=request.POST.get('UPPERCASE','off')
    removeextraspace=request.POST.get('removeextraspace','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount=request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if UPPERCASE=="on": 
        analyzed= ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
        djtext=analyzed

    if removeextraspace=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcount=="on":
        analyzed=('No. of characters given in the text are : '+str(len(djtext)))
        params = {'purpose': 'Charcter Counter', 'analyzed_text':analyzed}
        djtext=analyzed

    if removepunc == "off" and UPPERCASE=="off" and removeextraspace=="off" and newlineremover=="off" and charcount=="off":
        return HttpResponse('Please !!!! Select atleast one option')
    return render(request, 'analyze.html', params)