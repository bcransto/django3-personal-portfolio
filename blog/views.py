from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import JsonResponse
from django.core import serializers
from .forms import BlogForm

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})

def indexView(request):
    form = BlogForm()
    blogs = Blog.objects.all()
    return render(request, "blog/index.html", {"form": form, "blogs": blogs})

def postBlog(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = BlogForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)