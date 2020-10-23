from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    nl = request.POST.get('newlineremover','off')
    esr = request.POST.get('extraspaceremover','off')
    low = request.POST.get('lower','off')
    cap = request.POST.get('capital','off')
    prefix = request.POST.get('pre','off')
    suffix = request.POST.get('suf','off')
    chcount = request.POST.get('chcount','off')
    wcount = request.POST.get('wcount','off')
    show = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        show+= "Removed Punctuations : "
        params = {'purpose':show, 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        show+= "Upper Cased : "
        params = {'purpose' : show, 'analyzed_text': analyzed}
        djtext = analyzed
 
    if nl =="on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed = analyzed+char
        show+="New Lines Removed : "
        params = {'purpose' : show , 'analyzed_text': analyzed}
        djtext = analyzed

    if esr == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        show+="Extra spaces removed : "
        params = {'purpose': show, 'analyzed_text': analyzed}
        djtext = analyzed

    if low == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed+ char.lower()
        show+="Lower Cased Text : "
        params = {'purpose':show , 'analyzed_text': analyzed}
        djtext = analyzed

    if cap == 'on':
        analyzed = djtext.capitalize()
        show+="Capitalized Text : "
        params = {'purpose': show, 'analyzed_text': analyzed}
        djtext = analyzed

    if prefix == 'on':
        analyzed = 'www.'+djtext
        show+="Prefixed Text with www. : "
        params = {'purpose':show , 'analyzed_text': analyzed}
        djtext = analyzed

    if suffix =='on':
        analyzed = djtext+'.com'
        show+="Suffixed Text with .com : "
        params = {'purpose':show , 'analyzed_text': analyzed}
        djtext = analyzed

    if chcount =='on':
        analyzed = ""
        for i in djtext:
            if i!=" ":
                analyzed+=i
        j = len(analyzed)
        show+= "Character count : "
        params = {'purpose':show , 'analyzed_text': j}
        djtext = j

    if wcount == 'on':
        analyzed = len(djtext.split())
        show+= "Word Count : "
        params = {'purpose':show , 'analyzed_text': analyzed}
        

    if(removepunc != "on" and nl!="on" and esr!="on" and fullcaps!="on" and low!='on' and prefix!='on' and suffix!='on' and cap!='on' and chcount!='on' and wcount!='on'):
        return HttpResponse("please select any operation and try again")

    
    return render(request, 'analyze.html', params)
    
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')   
