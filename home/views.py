from django.shortcuts import render

# Create your views here.


def index(request):
    """    A view to Render the Index/home page.  """

    return render(request, 'home/index.html')
