from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PostedUrls
from .scraper import scrape
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'url-list/',
        'Detail': 'url-detail/<str:pk>',
        'Create': 'url-create/',
        'Delete': 'url-delete/<str:pk>',
        'Update': 'url-update/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def urlList(request):
    urls_data = PostedUrls.objects.all()
    urls_dictionary = {'urls': [], 'titles': []}
    for i in urls_data:
        title = scrape(i.url)
        urls_dictionary['urls'].append(i.url)
        urls_dictionary['titles'].append(title)
    return Response(urls_dictionary)

@csrf_exempt
@api_view(['POST'])
def urlCreate(request):
    urls_list = []
    if request.data:
        for count, value in enumerate(request.data):
            title = scrape(value)
            temp_dict = {"url": value, "title": title}
            urls_list.append(temp_dict)
    return Response(urls_list)
