# I Created it
from django.http import HttpResponse            #importing function HttpResponse    #HttpResponse used here to display in the webpage
from django.shortcuts import render             #importing function render

def index(request):
    #return HttpResponse("Hello World -- Homepage")
    #params = {'name':'Jake' , 'place':'Jupiter'}        #params is parameter and is optional-- means we are just passing it
    return render(request, 'index.html')#, params)        #redirecting to the template index.html


def go(request):
    #print(request.GET.get('entered_text', 'default'))

    #get the text
    djtext = request.POST.get('entered_text', 'default')         #djtext is the variable we created, this stores the value we enter in the textarea in index page
    #if we replace GET with POST, the entered text will not be shown in url
    #also, we have to replace all GET with POST in this python file


    #check checkbox values (whether on or off)
    removepunc = request.POST.get('removepunc', 'off')
    capitalize_all = request.POST.get('cap_all' , 'off')
    rmnewline = request.POST.get('rmline','off')
    countchr = request.POST.get('countchr' , 'off')
    #=we have replaced all GET with POST in above 4 lines



    # print("Button is : ",removepunc)                            #this prints the removepunc value in the terminal
    #print(djtext)                                               #this prints the djtext value in the terminal



    analyzed = djtext
    the_punctuations =  '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''      
    #analyzed = ""       #this will store analyzed text means --- it will check for punctutions in the djtext in the for loop
    

                                    #Now we are doing all with analyzed (processing it)
    #check which checkbox is on

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in the_punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed ,'djtxt':djtext}

    if capitalize_all == "on":
        analyzed = analyzed.upper()
        params = {'purpose':'Capitalize All', 'analyzed_text': analyzed,'djtxt':djtext }

    if rmnewline == "on":
        removed = ''
        for i in analyzed:
            if i!="\n" and i!="\r":     # \n and \r both are needed to be checked to remove next line
                removed = removed+i
            analyzed = removed
        params = {'analyzed_text': analyzed,'djtxt':djtext }


    if countchr == "on":
        temp = 0
        for char in analyzed:
            if char != " ":
                temp+=1

        op = "\nTotal Characters: "+str(temp)
        if capitalize_all == "off" and removepunc == "off" and rmnewline == "off":
            params = {'counter':op ,'djtxt':djtext}
        else:
            params = {'analyzed_text': analyzed, 'counter':op,'djtxt':djtext}

    if removepunc == "off" and capitalize_all == "off" and countchr == "off" and rmnewline == "off":
        analyzed = "The Checkbox is unchecked, please check it for Desired Output"
        params = {'analyzed_text': analyzed }



    
    #return render(request, 'analyze.html', params)      #params is parameters we are passing to analyze.html
    return render(request, 'index.html', params)      #params is parameters we are passing to index.html


    #analyze the text


# def about(request):
#     return HttpResponse("<h1>I am Piyush</h1> <a href = '/'> Back </a>")     #Inside the " " , we can enter html tags

# def links(request):
#     return HttpResponse('''Hello, These are the Links: <br><br> <a href = "https://www.facebook.com"><font color = 'red'> Facebook </font> </a>''')

# def rempunc(request):
#     #print(request.GET.get('entered_text', 'default'))

#     #get the text
#     djtext = request.GET.get('entered_text', 'default')         #djtext is the variable we created, this stores the value we enter in the textarea in index page
#     print(djtext)                                               #this prints the djtext value in the terminal
#     #analyze the text


#     return HttpResponse("Removing Punctuations")

# def capfirst(request):
#     return HttpResponse('''Capitalize First <br><br><a href = "http://127.0.0.1:8000/">HOME</a> <a href = "http://127.0.0.1:8000/rempunc">REMOVE PUNCTUATIONS</a>
#     <a href = "http://127.0.0.1:8000/charcount">COUNT CHARACTER</a>''')

# def charcount(request):
#     return HttpResponse('''Count Charcters <br><br><a href = "http://127.0.0.1:8000/">HOME</a> <a href = "http://127.0.0.1:8000/rempunc">REMOVE PUNCTUATIONS</a>
#     <a href = "http://127.0.0.1:8000/capfirst">CAPITALIZE FIRST</a>''')