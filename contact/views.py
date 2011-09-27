# Create your views here.
from contact.forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
	if request.method=="POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			return HttpResponse("<p>Thank You!</p>")
	else:
			form = ContactForm()
	return render(request, "contact.html", {"form":form})
