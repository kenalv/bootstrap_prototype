from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from Province.models import Canton,Distric
# Create your views here.

def index(request):
   
    cantonsList = Canton.objects.all()
    form = forms.SearchForm()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(cantonsList, 10) # Show 10 elements per page, change to the number for more elements
    
    try:
        cantons = paginator.page(page)
    except PageNotAnInteger:
        cantons = paginator.page(1)
    except EmptyPage:
        cantons = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
            
        if form.is_valid():
           
            if form.cleaned_data['search_options'] == '2':
                print(form.cleaned_data['search_name'])
                if form.cleaned_data['search_name'] is not '':
                        districsList = Distric.objects.filter(name = form.cleaned_data['search_name'] )
                        paginator = Paginator(districsList, 10) # Show 10 elements per page, change to the number for more elements
                        try:
                            districs = paginator.page(page)
                        except PageNotAnInteger:
                            districs = paginator.page(1)
                        except EmptyPage:
                            districs = paginator.page(paginator.num_pages)
                        return render(request,'test.html',{'districs':districs,'searchForm':form})
               
                districsList = Distric.objects.all()
                paginator = Paginator(districsList, 10) # Show 10 elements per page, change to the number for more elements
                try:
                    districs = paginator.page(page)
                except PageNotAnInteger:
                    districs = paginator.page(1)
                except EmptyPage:
                    districs = paginator.page(paginator.num_pages)
                return render(request,'test.html',{'districs':districs,'searchForm':form})

            if form.cleaned_data['search_options'] == '1': 
                print('SEARCH NAME')
                print(form.cleaned_data['search_name'])
                print('SEARCH NAME')
                if form.cleaned_data['search_name'] is not '':
                        cantonsList = Canton.objects.all()
                        paginator = Paginator(cantonsList, 10) # Show 10 elements per page, change to the number for more elements

                        try:
                            cantons = paginator.page(page)
                        except PageNotAnInteger:
                            cantons = paginator.page(1)
                        except EmptyPage:
                            cantons = paginator.page(paginator.num_pages)
                        return render(request,'test.html',{'cantons':cantons,'searchForm':form})

                cantonsList = Canton.objects.all()
                paginator = Paginator(cantonsList, 10) # Show 10 elements per page, change to the number for more elements

                try:
                    cantons = paginator.page(page)
                except PageNotAnInteger:
                    cantons = paginator.page(1)
                except EmptyPage:
                    cantons = paginator.page(paginator.num_pages)
                return render(request,'test.html',{'cantons':cantons,'searchForm':form})
            
        #elif form.is_valid():

    if request.method == 'GET' and request.GET:
        print(request.GET.get('pk'))
        if request.GET.get('pk') is not None:
            data = request.GET.get('pk') ## [0] = model  -  [1] = model_pk
            data_pk = data.split('-') 
            if request.GET.get('option') == 'del' and  data_pk[0] == 'canton':
            
                data_to_del = Canton.objects.get(id =  data_pk[1])
                data_to_del.delete()
                        
                form = forms.SearchForm(request.POST)
                cantonsList = Canton.objects.all()
                return render(request,'test.html',{'cantons':cantonsList,'searchForm':form}) 

            if request.GET.get('option') == 'del' and  data_pk[0] == 'distric':

                data_to_del = Distric.objects.get(id =  data_pk[1])
                data_to_del.delete()
                        
                form = forms.SearchForm()
                districList = Distric.objects.all()
                return render(request,'test.html',{'districs':districList,'searchForm':form}) 

    return render(request,'test.html',{'cantons':cantons,'searchForm':form})
    
def myMaker(request):

    formCanton = forms.CantonForm()
    formDistric = forms.DistricForm()

    if request.method == 'POST':
        if request.POST.get('canton'):
            new_dictric = Distric.objects.create(canton=request.POST.get('canton'),name=request.POST.get('name'),code=request.POST.get('code'))
            new_dictric.save
            #messages.info(request, 'Your distric has been added successfully!')
            return render(request,'new_data.html',{'formDistric':formDistric,'formCanton':formCanton,'message':'Your distric has been added successfully!'})
    
        if(request.POST.get('province')):   
            new_canton = Canton.objects.create(province=request.POST.get('province'),name=request.POST.get('name'),code=request.POST.get('code'))
            new_canton.save
            #messages.add_message(request, messages.INFO, 'Your canton has been added successfully!')
            return render(request,'new_data.html',{'formCanton':formCanton,'formDistric':formDistric,'message':'Your canton has been added successfully!'})
       

        


    return render(request,'new_data.html',{'formCanton':formCanton, 'formDistric':formDistric})

