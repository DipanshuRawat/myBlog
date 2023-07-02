from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from blog.models import Post


def blogHome(request):
    allPosts= Post.objects.all()
    print(allPosts)
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)
    # return HttpResponse("Hello, world. You're at the polls blogHome.")

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)   
 # return HttpResponse(f"This is blogPost: {slug}")


