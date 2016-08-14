from django.shortcuts import render

import iShop.models

# Create your views here.
def view_shop(request):
    #posts = BlogArticle.objects.all()
    return render(request, 'default.html', {})
