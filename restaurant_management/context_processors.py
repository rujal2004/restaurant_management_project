import datetime

def current_year(request):
    return{
      "year":datetime.date.today().year  
    }