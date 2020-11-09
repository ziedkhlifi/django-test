from django.core.paginator import Paginator
from django.shortcuts import render
from .models import job
from .form import ApplyForm
# Create your views here.
def job_list (request):
    job_list = job.objects.all()
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj }
    return render(request,'job/job_list.html', context)

def job_detail (request, slug):
    job_detail = job.objects.get(slug= slug)
    if request.method =='POST':
        form =ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    context = {'job': job_detail,'form1':form }
    return render(request,'job/job_detail.html',context)

def add_job(request):
    return render(request,'job/add_job.html',{})
