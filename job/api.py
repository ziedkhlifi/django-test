
from .serializers import  JobSerializer
from .models import job
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def joblistapi(request):
    all_jobs = job.objects.all()
    data = JobSerializer(all_jobs,many=True).data
    return Response({'data': data})
@api_view(['GET'])
def job_detail_api(request, id ):
    job_detail = job.objects.get(id=id)
    data = JobSerializer(job_detail,).data
    return Response({'data': data})
