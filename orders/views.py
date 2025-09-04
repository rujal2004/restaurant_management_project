from django.shortcuts import render

# Create your views here.
class ReservationsView(View):
    def get(self,request):
        return render(request,"reservations.htmll")