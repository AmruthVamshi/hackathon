from django.shortcuts import render,redirect
from .forms import NotesForm
from .models import Notes
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
	form=NotesForm()
	notes=Notes.objects.filter(author=request.user)
	context={'form':form,'notes':notes}
	return render(request,"notes/home.html",context)
def formsave(request):
	form=NotesForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.author=request.user
		instance.save()
	return redirect('notes:home')
def delete(request,post_pk):
	delete=Notes.objects.get(pk=post_pk)
	delete.delete()
	return redirect('notes:home')