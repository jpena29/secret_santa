from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Information

# Create your views here.
def index(request):
	template = loader.get_template('secret/index.html')
	return HttpResponse(template.render())
