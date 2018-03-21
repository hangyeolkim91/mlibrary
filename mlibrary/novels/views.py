from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Bookcase, Novel
from .forms import BookcaseForm, NovelForm

# Create your views here.

def index(request):
    bookcase_list = Bookcase.objects.all()
    context = {
        'bookcase_list' : bookcase_list,
    }
    return render(request,'novels/index.html',context)

def make_bookcase(request):
    if request.method == 'POST':
        print('post')
        form = BookcaseForm(request.POST)
        if form.is_valid():
            bookcase = Bookcase(name=form.cleaned_data['bookcase_name'])
            bookcase.save()
            return HttpResponseRedirect('/')
    else:
        form = BookcaseForm()

    return render(request, 'novels/make_bookcase.html',{'form':form})

def upload_novel(request, bookcase_id):
    if request.method=='POST':
        print('upload_novel post bookcase_id' ,bookcase_id)
        form = NovelForm(request.POST,request.FILES)
        if form.is_valid():
            bookcase = Bookcase.objects.get(pk=bookcase_id)
            novel = Novel(file=request.FILES['file'])
            novel.bookcase = bookcase
            novel.author = form.cleaned_data['author']
            novel.title = form.cleaned_data['title']
            novel.published_date = form.cleaned_data['published_date']
            novel.save()

            return HttpResponseRedirect(f'/bookcase/{bookcase.id}')
    else:
        form = NovelForm()
        bookcase = get_object_or_404(Bookcase, pk=bookcase_id)
        context = {
            'bookcase':bookcase
        }
    print(context)
    return render(request, 'novels/upload_novel.html',{'form':form ,'bookcase':bookcase})

def detail_bookcase(request, bookcase_id):
    bookcase = get_object_or_404(Bookcase, pk=bookcase_id)
    return render(request, 'novels/detail_bookcase.html', {'bookcase':bookcase})

def detail_novel(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    return render(request, 'novels/detail_novel.html', {'novel':novel})

