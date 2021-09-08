# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:02:31 2021

@author: santosh.sharma
"""
from django.shortcuts import render


def index(request):
    params = {'name': 'harry', 'place': 'meerut'}
    return render(request, 'index.html', params)

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')
    #Check Checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove','off')
    charcount = request.POST.get('charcount', 'off')
    #Check which checkbox is on
    if removepunc=="on":

        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'RemovePuntuation','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    if newlineremove=='on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext=analyzed
    if charcount == 'on':
        analyzed=[]
        for char in djtext:
            analyzed.append(char)
        charc = len(analyzed)
        params={'purpose':'Character Count','analyzed_text':charc}
        
    if removepunc!='on' and fullcaps!='on' and newlineremove!='on' and charcount!='on':
        return HttpResponse("Error")


def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')