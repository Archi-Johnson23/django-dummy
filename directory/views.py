from django.shortcuts import render
from django.http import HttpResponse

from directory.models import Author

def show_author_view(request):
    # возвращение книг
    autho=Author.objects.all()
    # response = HttpResponse("Возвращение книги".encode())
    context ={'autho':autho}
    return render(request, template_name="directory/show_author.html",context=context)