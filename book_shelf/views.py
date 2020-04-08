from django.shortcuts import render

# Create your views here.
def shelf_itself(request):
    return render(request, 'book_shelf/shelf_itself.html', {})
