from re import A
import re
from ssl import HAS_TLSv1_1
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from  .models import Gallery, LatestDept, McaAdmission, McaCourse, McaEbook, McaNotice, McaResult, McaSemister1, McaSemister2, McaSemister3, McaSemister4, McaSemister5, McaSemister6, StatisticAdmission, StatisticEbook, StatisticNotice, StatisticResult, StatisticSemister1, StatisticSemister2, StatisticSemister3, StatisticSemister4, StatisticSemister5, StatisticSemister6, StudentBlog,ContactUs,McaFaculty,McaSubject,StatisticsFaculty,Carousel
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

def home(request):
    cr=Carousel.objects.all()
    return render(request,'home.html',context={'carousel':cr})
# depatment notice
def mcanotice(request):
    mn=McaNotice.objects.all()    
    return render(request,'mcanotice.html',context={"mca_notice":mn})

def statisticnotice(request):
    sn=StatisticNotice.objects.all()    
    return render(request,'statisticnotice.html',context={"statistis_notice":sn})

# department admission
def mcaadmission(request):
    ma=McaAdmission.objects.all()
    return render(request,'mcaadmission.html',context={"mca_admission":ma})

def statisticadmission(request):
    sa=StatisticAdmission.objects.all()
    return render(request,'statisticadmission.html',context={"statistic_admission":sa})

#department results
def mcaresult(request):
    mr=McaResult.objects.all()    
    return render(request,'mcaresult.html',context={"mca_result":mr})

def statisticresult(request):
    sr=StatisticResult.objects.all()
    return render(request,'statisticresult.html',context={"statistic_result":sr})

#lastest dept update
def latestdept(request):
    id=LatestDept.objects.all()
    return render(request,'latestdept.html',context={"latestdept":id})

def mcacourse(request):
    mcacourse=McaCourse.objects.last()      
    return HttpResponse( "<a href='{{% mcacoursse.file.url %}}'>download</a>")

# department faculty
def mcafaculty(request): 
    mca=McaFaculty.objects.all()       
    return render(request,'mcafaculty.html',context={'mca':mca})

def statisticfaculty(request):
    stats=StatisticsFaculty.objects.all()
    return render(request,'statisticfaculty.html',context={'stats':stats})
def mcaebook(request):
    mb=McaEbook.objects.all()
    return render(request,'mcaebook.html',context={'mcaebook':mb})

def statisticebook(request):
    sb=StatisticEbook.objects.all()
    return render(request,'statisticebook.html',context={'statisticebook':sb})

def mcaebook(request):
    meb=McaEbook.objects.all()
    return render(request,'mcaebook.html',context={'mcaebook':meb})
def statisticebook(request):
    seb=StatisticEbook.objects.all()
    return render(request,'statisticebook.html',context={'statisticebook':seb})

def mcasemister1(request):
    ms=McaSemister1.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem1':ms})
def mcasemister2(request):
    ms=McaSemister2.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem2':ms})
def mcasemister3(request):
    ms=McaSemister3.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem3':ms})
def mcasemister4(request):
    ms=McaSemister4.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem4':ms})
def mcasemister5(request):
    ms=McaSemister5.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem5':ms})
def mcasemister6(request):
    ms=McaSemister6.objects.all()
    return render(request,'mcasemister1.html',context={'mcasem6':ms})
def statisticsemister1(request):
    ss=StatisticSemister1.objects.all()
    return render(request,'mcasemister1.html',context={'statsem1':ss})
def statisticsemister2(request):
    ss=StatisticSemister2.objects.all()
    return render(request,'mcasemister1.html',context={'statsem2':ss})
def statisticsemister3(request):
    ss=StatisticSemister3.objects.all()
    return render(request,'mcasemister1.html',context={'statsem3':ss})
def statisticsemister4(request):
    ss=StatisticSemister4.objects.all()
    return render(request,'mcasemister1.html',context={'statsem4':ss})
def statisticsemister5(request):
    ss=StatisticSemister5.objects.all()
    return render(request,'mcasemister1.html',context={'statsem5':ss})
def statisticsemister6(request):
    ss=StatisticSemister6.objects.all()
    return render(request,'mcasemister1.html',context={'statsem6':ss})

def gallery(request):
    g=Gallery.objects.all()
    return render(request,'gallery.html',context={'gallery':g})

def studentblog(request):
   
    s=StudentBlog.objects.all()
    paginator=Paginator(s,2)
    page_number = request.GET.get('page')
    st = paginator.get_page(page_number) 
    total_no=[n+1 for n in range(st.paginator.num_pages)]    
    p=request.GET.get('filter')  
    if request.method=='GET':     
        if p:
            se=StudentBlog.objects.get(pk=p) 

            data={'studentfilter':se,'total':total_no,'post':st}        
            return render(request,'studentblog.html',context={'data':data})       
        else:
            data={'studentblog':st,'total':total_no}               
            return render(request,'studentblog.html',context={'data':data}) 
    if request.method=='POST':
        search=StudentBlog.objects.filter(title__contains=request.POST.get('search'))  
        data={'studentfilter':search,'total':total_no,'post':st}
        return render(request,'studentblog.html',context={'data':data})

def aboutus(request):
    return render(request,'aboutus.html')

def rightinfo(request):
    return render(request,'rightinfo.html')

def antiragging(request):
    return render(request,'antiragging.html')
@csrf_exempt
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('textarea')
        files=request.FILES.get('file')                    
        c=ContactUs(name=name,email=email,query=query,file=files)
        c.save()        
    return JsonResponse({"status":200})
@csrf_exempt
def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('userid')       
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)        
        if user is not None:                       
            login(request, user) 
            print("imran") 
            return JsonResponse({'status':202})                 
        else:
           return JsonResponse({'status':511})

def adminpanel(request):
    return render(request,'admin/admin.html')   

def add_mca_notice(request):
    return render(request,'admin/mcaaddnotice.html')
