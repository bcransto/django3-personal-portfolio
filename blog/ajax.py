import json
from django.http import Http404, HttpResponse

def add_blog(request):
    if request.is_ajax():
        blog_items = ['title 1','entry a','date 1']
        data = json.dumps(blog_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404