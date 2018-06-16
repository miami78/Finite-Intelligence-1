from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response

class PageViews(TemplateView):
    ''''''
    template_name = "finite_finite/index.html"
    def index(self, request, *args, **kwargs):
        return render_to_response(self.template_name)
    def about(self, request, *args, **kwargs):
        return render_to_response('finite_finite/about.html')
    def services(self, request, *args, **kwargs):
        return render_to_response('finite_finite/services.html')

