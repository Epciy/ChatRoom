from django.contrib.auth import login 
from django.shortcuts import render,redirect
from .forms import SignUpForm


# Create your views here.
def frontpage(request):
    return render(request,"core/frontpage.html")


#la creation de  la page d'inscription de l'utilisateur. 
def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)

        if form.is_valid(): #  si username et password son valide
           user=form.save()

           login(request,user) # on va utiliser la methode login importer from  django.contrib.auth  pour que l'utilisateur se connecte 
           return redirect("frontpage") # methode pour rederiger l'utilisateur vers frontpage
    else:
        form=SignUpForm()
    return render(request,'core/signup.html',{"form":form})