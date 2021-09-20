from django.shortcuts import render, redirect
from .models import Participant
from .forms import ParticipantForm
from django.contrib import messages

# Create your views here.
def test_unicity_constraints(request, p):
    email = request.POST.get('email')
    o1 = p.objects.filter(email= email).count()

    username = request.POST.get('git_username')
    o2 = p.objects.filter(git_username= username).count()

    firstname = request.POST.get('first_name')
    o3 = p.objects.filter(first_name= firstname).count()
    
    lastname = request.POST.get('last_name')
    o4 = p.objects.filter(last_name= lastname).count()

    if(o3 > 0 and o4 > 0):
        messages.error(request, "Hmm... Looks like a user with this name is already registered.")
        return(0)
    elif(o1 > 0):
        messages.error(request, "Hmm... Looks like a user with this email is already registered.")
        return (0)
    elif(o2 > 0):
        messages.error(request, "Hmm... Looks like a user with this username is already registered.")
        return(0)
    
    return(1)

def participant_create_view(request):
    form = ParticipantForm(request.POST or None)  

    test_value = test_unicity_constraints(request, Participant)
    
    if(test_value == 0):
        return render(request, 'participant/register.html', {'form': form})
    else:
        if(form.is_valid()):
            form.save()
            form = ParticipantForm()
            messages.success(request, "You have registered successfully !")
            return redirect('/register/')

    return render(request, 'participant/register.html', {'form': form})