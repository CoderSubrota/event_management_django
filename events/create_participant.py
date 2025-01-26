
from django import forms
from events.models import Create_Participant_Model
class Create_Participant_Form (forms.ModelForm):
    class Meta:
        model = Create_Participant_Model
        fields = ['event_assign','name','email']
        
        widgets={
            'name':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter participant name'
            }),
            'email':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter participant email'
            }),
           'event_assign':forms.CheckboxSelectMultiple(),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            
            