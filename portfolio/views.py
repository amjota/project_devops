from django.views import View
from django.shortcuts import get_object_or_404, render, redirect

class IndexView(View):
    def get(self, request):
        return render(request, 'portfolio/index.html')
