from django.shortcuts import render
from .forms import PastebinForm
from .models import Pastebin as Paste
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	inipage="home.html"
	form = PastebinForm(request.POST)
	context = {
		"form" : form

	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		instance.save()
		textboxname = instance.pasteurl

		paste = Paste.objects.get(pasteurl=textboxname)
		return HttpResponseRedirect("/%s" %(paste.pasteurl))
		
	return render(request,inipage,context)

def retrieve(request,url):
	paste = Paste.objects.get(pasteurl=url)

	context = {

		"name" : paste.name,
		"code" : paste.textpaste
	}
	return render(request,"result.html", context)

#def request_page(request):
 # if(request.GET.get('pastebtn')):
  #  mycode.get( int(request.GET.get('mytextbox')) )
#return render_to_response('myApp/templateHTML.html')