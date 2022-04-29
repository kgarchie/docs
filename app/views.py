from django.shortcuts import render
from .models import docs

# Create your views here.

def index(request):
    doc_all = docs.objects.all()
    context = {
        'docs': doc_all 
    }
    return render(request, 'index.html', context)


def doc(request, id):
    doc = docs.objects.get(id=id)
    context = {
        'doc': doc
    }
    return render(request, 'doc.html', context)
