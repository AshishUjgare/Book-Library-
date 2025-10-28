from django.shortcuts import render
from sixth_app.form import BookForm

# Create your views here.
def book_view(request) :
    form = BookForm()
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    return render (request , "book_form.html" , {'form' : form})
