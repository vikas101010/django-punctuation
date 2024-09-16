# This is my first file  --vikas
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    # Get the text
    djtext=request.GET.get('text','default')
    # check box values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    print(removepunc)
    print(djtext)
    #checj which checkbox is on
    if removepunc == "on":
    # analyzed = djtext
       punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
       analyzed=""
       for char in djtext:
           if char not in punctuation:
            analyzed=analyzed+char

       param={'purpose':'Removepunctuation','analyzed_text':analyzed}
    # Analyze the text
       return render(request,'analyze.html',param)

    elif (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        param={'purpose':'change to uppercase','analyzed_text':analyzed}
    # Analyze the text
        return render(request,'analyze.html',param)
    elif(newlineremover=="on"):
          analyzed=""
          for char in djtext:
             if char!="\n":
               analyzed = analyzed + char
          param={'purpose':'newlineremover','analyzed_text':analyzed}
    # Analyze the text
          return render(request,'analyze.html',param)
    
    else:
        return HttpResponse("Error: Please Check the box ")
from django.shortcuts import render
#  count characters 
# def analyze(request):
#     # Check if the form has been submitted
#     if request.method == 'GET' and 'text' in request.GET:
#         # Get the text from the form
#         djtext = request.GET['text']
        
#         # Initialize the analyzed text
#         analyzed = ""
        
#         # Check if countchar is 'on' in the request
#         if request.GET.get('countchar') == 'on':
#             # Count characters
#             charcount = len(djtext)
#             analyzed = charcount  # Directly use the character count
            
#             # Prepare parameters for the template
#             param = {'purpose': 'countchar', 'analyzed_text': analyzed}
            
#             # Render the result in the HTML template
#             return render(request, 'analyze.html', param)
    
#     # In case the 'countchar' is not 'on' or other cases
#     return render(request, 'analyze.html', {'purpose': 'No operation', 'analyzed_text': ''})


# def navbar(request):
#     nav = """
#     <h1>HOME</h1>
#     <ul>
#     <iframe src="https://www.youtube.com/embed/eOGSFd2J3wY"title="Dil hai ki manta nhi" allow="autoplay;encrypted-media"></iframe>
#     <iframe src="https://www.youtube.com/embed/iu1i2KviJaE"title="Dil hai ki manta nhi" allow="autoplay;encrypted-media"></iframe>
#     <iframe src="https://www.youtube.com/embed/hhXDoofch9I"title="Dil hai ki manta nhi" allow="autoplay;encrypted-media"></iframe>
#     </ul>
#     <button onclick="window.location.href='your server link';">
# Back
# </button>'
#     """
#     return HttpResponse(nav)

