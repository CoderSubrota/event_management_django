
from django import forms
from events.models import Add_Event_Model,Category_Model
class Add_Event (forms.ModelForm):
    class Meta:
        model = Add_Event_Model
        fields = ['name','description','date','time','location','category']
        
        widgets={
            'name':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter participant name'
            }),
            'description':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter participant description'
            }),
            'date':forms.SelectDateWidget(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
            }),
            'time':forms.TimeInput(attrs={
                 'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                 'placeholder':'Follow this formate HH:MM'
            }),
            'location':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                
                'placeholder':'Enter participant location'
            }),
           'category':forms.CheckboxSelectMultiple(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col',
            })
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self.fields['category'].queryset = Category_Model.objects.all()
            