from django.urls import path, include
from . import views
from . import api

app_name='job'



urlpatterns = [
    path('', views.job_list , name='job_list'),
    path('add', views.add_job , name='add_job'),
    path('<str:slug>', views.job_detail,name='job_detail'),

    path('api/jobs', api.joblistapi, name='joblistapi'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

]
