from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):

	#set up session variables:
	
	if 'word' not in request.session:
		request.session['word'] = ''
		request.session['color'] = ''
		request.session['font_weight'] = ''
		request.session['dt_time'] = ''
		request.session['content'] = []
	return render(request, "session_words/index.html")
	
def clearSession(request):
	request.session.clear()
	return redirect('/session_words')
		
	
def add_word(request):
	if request.method=="POST":
		word = request.POST.get('word', "")
		color = request.POST.get('color', "red")
		size = request.POST.get('size', "False")
		if size=="True":
			font_weight = "30"
		else:
			font_weight = "10"
		dt_time = datetime.strftime(datetime.now(), '%B-%d-%Y %I:%M:%S')
		content = {"word":word, "color":color,"font_weight": font_weight,  "dt_time": dt_time}
		request.session['word'] = word
		request.session['color'] = color
		request.session['font_weight'] = font_weight
		request.session['dt_time'] = dt_time
		request.session['content'].append(content)
		return redirect('/session_words')

