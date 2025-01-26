from django.shortcuts import render
from events.models import Add_Event_Model
def home(request):

    # Use select_related to fetch category in a single query
    events = Add_Event_Model.objects.select_related('category').all()
    
    context = {
          'events':events
    }
    
    return render(request,'home.html',context)


    