from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NoteModelForm
# Create your views here.
from .models import Note

#CRUD

def create_view(request):
    form=None
    if request.method=='POST':
        form=NoteModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('/')
    else:
        form=NoteModelForm()
    return render(request, "notepad/create.html",{'form': form})

#def list_view(request):
#    notes=Note.objects.all()
#    return render(request, "notepad/list.html",{'object_list':notes})