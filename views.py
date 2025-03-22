from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from fitapp.models import Customer 
from fitapp.forms import CustomerForm 
from django.contrib import messages 
#from django.http import request 

# Create your views here.
def index(request):
    return render (request,"fitapp/index.html")

def features(request):
    return render (request,"fitapp/features.html")

def diet_plan(request):
    return render (request,"fitapp/dietplan.html")

def contact(request):
    return render (request,"fitapp/contact.html")

def maleworkout(request):
    return render (request,"fitapp/maleworkout.html")

def femaleworkout(request):
    return render (request,"fitapp/femaleworkout.html")

def pt_info(request):
    return render (request,"fitapp/pt_info.html")

def pt_gym(request):
    return render (request,"fitapp/pt_gym.html")

def pt_online(request):
    return render (request,"fitapp/pt_online.html")

def pt(request):
    return render (request,"fitapp/pt.html")

def mchest(request):
    return render (request,"fitapp/mchest.html")

def mback(request):
    return render (request,"fitapp/mback.html")

def marms(request):
    return render (request,"fitapp/marms.html")

def mshoulder(request):
    return render (request,"fitapp/mshoulder.html")

def mabs(request):
    return render (request,"fitapp/mabs.html")

def mlegs(request):
    return render (request,"fitapp/mlegs.html")

def fchest(request):
    return render (request,"fitapp/fchest.html")

def fback(request):
    return render (request,"fitapp/fback.html")

def farms(request):
    return render (request,"fitapp/farms.html")

def fshoulder(request):
    return render (request,"fitapp/fshoulder.html")

def fabs(request):
    return render (request,"fitapp/fabs.html")

def flegs(request):
    return render (request,"fitapp/flegs.html")

def save(request):
    f1=CustomerForm (request.POST)
    if f1.is_valid():
        f1.save()
    else:
        f1=CustomerForm()    
    return render (request,"fitapp/pt.html",{'form':f1})


class CustomerCreate(CreateView):
    # specify the model for create view
    model = Customer
    # specify the fields to be displayed
    fields = '__all__'
    def form_valid(self, form):
        messages.success(self.request, 'Enquiry form has been sent Successfully..!')
        return super().form_valid(form)
    success_url ='/pt'

class CustomerList(ListView):
    # specify the model for list view
    model = Customer

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'
    success_url ="/pt/"

class CustomerDelete(DeleteView):
    model = Customer
    success_url ="/list/"

class CustomerDetail(DetailView):
    model = Customer