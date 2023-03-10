from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
  mymembers = Member.objects.all().values()
  #template = loader.get_template('myfirst.html')
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing1(request):
  mydata = Member.objects.all()
  mydata_values_list = Member.objects.values_list("firstname")
  # mydata_filter_firstname = Member.objects.filter(firstname='Hafsa').values() | Member.objects.filter(firstname='Foysal',id='2').values()
  mydata_filter_firstname = Member.objects.filter(Q(firstname__startswith='f')| Q(id='5')).values()
  mydata_order_by = Member.objects.all().order_by('-firstname','id').values()

  template = loader.get_template('childtemplate.html')
  context = {
    'mydata': mydata,
    'mydata_values_list':mydata_values_list,
    'mydata_filter_firstname':mydata_filter_firstname,
    'mydata_order_by':mydata_order_by
  }
  return HttpResponse(template.render(context, request))


def testing(request):
  mymembers = Member.objects.all().values()
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry','Orange','Coconut',],
    'firstname': 'Hafsa',
    'mymembers': mymembers,
    'mydata': mydata,
    'greeting': 1,
    'mycar':{'brand':'Ford', 'model':'Mustang', 'year':'1964',},


  }
  return HttpResponse(template.render(context, request))

def string_builder(request,name):
  template = loader.get_template('New_test.html')
  context = {
    'Name': name,
    'Id': 20,
    'firstname': 'Hafsa',
    'mylist': [1, 1,8, 1, 2, 2, 7,2, 2, 3, 3, 3, 3, 4, 5],
    'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
  }
  return HttpResponse(template.render(context, request))
