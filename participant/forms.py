from django import forms 
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'git_username': 'Github Username',
            'experience': 'Do you have a past experience with coding?',
            'do_talk': 'Do you want to attend the FOS Talk?',
            'do_git': 'Do you want to attend the GIT/Github Workshop?',
            'do_fest': 'Do you want to attend OpenFest?',
            'conduct': 'Do you agree with the Code of Conduct of Hacktoberfest?'
        }


    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Handle Empty Labels
        self.fields['conduct'].required = True