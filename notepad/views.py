from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NoteModelForm
# Create your views here.
from .models import Note

#CRUD

def create_view(request):
    form=NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user=request.user
        form.save()
        return redirect('/')

    context={
        'form':form
    }

    return render(request, "notepad/create",context)