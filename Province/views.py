from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from Province.models import Canton,Distric
from Province.serializers import CantonSerializer,DistricSerializer
# Create your views here.
def get_search_by_provinces(place):
        
    place_canton = str(place.canton).split(' ')
    place_canton.pop(0)
    temp = ''
    print( temp.join(place_canton))
    #{"canton": temp.join(place_canton),"name":place.name,"code":place.code }
    return {"canton": temp.join(place_canton),"name":place.name,"code":place.code }
        
def get_filtred_provinces(places,filt):
    
    return list(filter(lambda place: str(place['canton']) == str(filt), list(places)))    
    
     


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
            print('FILTROOOOOOO')
            if form.cleaned_data['search_by_province'] is True:
                
                if form.cleaned_data['search_options'] == '2':
                     
                    if form.cleaned_data['search_name'] != '':
                        ## ERROR AQUÍ no hace el filtro, debería de realizarce 
                        print(form.cleaned_data['search_name'])
                        ## pasando correctamente la variable de busqueda.
                        districsList = Distric.objects.filter(canton='Alajuela') #'form.cleaned_data['search_name']')
                        ## pero no obtiene datos
                        print(list(districsList))
                        paginator = Paginator(districsList, 10) # Show 10 elements per page, change to the number for more elements
                        try:
                                districs = paginator.page(page)
                        except PageNotAnInteger:
                                districs = paginator.page(1)
                        except EmptyPage:
                                districs = paginator.page(paginator.num_pages)
                        return render(request,'test.html',{'districs':districs,'searchForm':form})
                        
                    

                if form.cleaned_data['search_options'] == '1': 
                    if form.cleaned_data['search_name'] is not '':
                        cantonsList = Canton.objects.filter(province = form.cleaned_data['search_name'] )
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

            print('FILTROOOOOOO')
           #############################################################################
            if form.cleaned_data['search_options'] == '2':
            
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
                if form.cleaned_data['search_name'] is not '':
                        cantonsList = Canton.objects.filter(name=form.cleaned_data['search_name'])
                        serializer = CantonSerializer(cantonsList)
                        print(serializer.data)
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
            try:
                c = Canton.objects.get(name = request.POST.get('canton'))
                cc= Canton.objects.get(id = request.POST.get('province'))
                new_dictric = Distric.objects.create(
                    province=cc,
                    canton=c,
                    name=request.POST.get('name'),code=request.POST.get('code'))
                new_dictric.save
            except:
                print('An error occured.')
           
            #messages.info(request, 'Your distric has been added successfully!')
            return render(request,'new_data.html',{'formDistric':formDistric,'formCanton':formCanton,'message':'Your distric has been added successfully!'})
    
        if(request.POST.get('province')):   

            new_canton = Canton.objects.create(province=request.POST.get('province'),name=request.POST.get('name'),code=request.POST.get('code'))
            new_canton.save
            #messages.add_message(request, messages.INFO, 'Your canton has been added successfully!')
            return render(request,'new_data.html',{'formCanton':formCanton,'formDistric':formDistric,'message':'Your canton has been added successfully!'})
       

        


    return render(request,'new_data.html',{'formCanton':formCanton, 'formDistric':formDistric})

