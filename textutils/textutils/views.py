from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>HOME</h1>
    #<a href="https://www.google.com"> Django Google</a>
    #<a href="https://en-gb.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C318504236042%7Ce%7Cfacebook%27%7C&placement&creative=318504236042&keyword=facebook%27&partner_id=googlesem&extra_2=campaignid%3D1653993517%26adgroupid%3D63066387003%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-362360550869%26loc_physical_ms%3D1007809%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIr5j3tsfy7AIVCGoqCh3b-QCHEAAYASAAEgIJg_D_BwE"> Django Facebook</a>
    #<a href="https://www.youtube.com"> Django YouTube</a>
    #<a href="https://twitter.com/?lang=en"> Django Twitter</a>''')

#def about(request):
#    return HttpResponse("About tayyib")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    charcount = request.GET.get('charcount','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    print(removepunc)
    print(djtext)
    #Analyze the text
     #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            if char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To Upper', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose':'Remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)
    elif (charcount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
        params = {'purpose':'Total Charcter count', 'analyzed_text': len(analyzed)}
        return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse("Error")

def aboutus(request):
    return render(request, 'aboutus.html')