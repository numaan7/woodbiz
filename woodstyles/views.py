from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def newsletter(email):
    
    if Newsletter.objects.filter(email=email).exists():
        return redirect('/')
    else:
        newsletter=Newsletter(email=email)
        newsletter.save()
        return redirect('/')

def index(request):
    woods=Wood.objects.all().order_by('-date')
    
    if request.method=="POST":
        email=request.POST.get('email')
        newsletter(email)
    if request.method=='GET':
        sort=request.GET.get('sort')
        if sort=='atoz':
            woods=Wood.objects.all().order_by('title')
        if sort=='ztoa':
            woods=Wood.objects.all().order_by('-title')
        if sort=='newest':
            woods=Wood.objects.all().order_by('-date')
        if sort=='oldest':
            woods=Wood.objects.all().order_by('date')
        

        try:
            category=request.GET.get('category')
            cat=get_object_or_404(Categorie,name=category)
            woods=Wood.objects.filter(category=cat)
        except:
            pass
        try:
            search=request.GET.get('s')
            woods=Wood.objects.filter(title__icontains=search)
        except:
            pass
    paginator = Paginator(woods, 10) # 10 posts in each page
    page = request.GET.get('page')
    try:
        woods = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        woods = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        woods = paginator.page(paginator.num_pages)

        
    
    category=Categorie.objects.all()
    return render(request,'index.html',{'woods':woods,'categories':category, page:'pages'})
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        return redirect('/')
    category=Categorie.objects.all()
    return render(request,'contact.html',{'categories':category})
def about(request):
    category=Categorie.objects.all()
    return render(request,'about.html',{'categories':category})

        

