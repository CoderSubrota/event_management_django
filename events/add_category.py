
from django import forms
from events.models import Category_Model
class Add_Category (forms.ModelForm):
    class Meta:
        model = Category_Model
        fields = ['name','description']
        
        widgets={
            'name':forms.TextInput(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter category name'
            }),
            'description':forms.Textarea(attrs={
                'class':'py-3 ps-2 rounded-xl flex w-full my-4 h-56 flex-col ring-2 ring-indigo-500',
                'placeholder':'Enter category description'
            }),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            
            