from django.shortcuts import render
from .models import User
from .forms import FormName

# Create your views here.

def user(request):
    my_context = {'my_data': User.objects.order_by('first_name')}
    return render(request, 'second_app/users.html', context=my_context)


def index(request):
    return render(request, 'second_app/index.html')

def form(request):

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'second_app/signup.html', context={'form': FormName})

