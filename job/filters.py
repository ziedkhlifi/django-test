import  django_filters
from .models import job
class  JobFilter ( django_filters . FilterSet ):
    titre = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class  Meta :
         model  =job
         fields  = '__all__'
         exclude = ['published_at','image','salary','vacancy','owner','slug']