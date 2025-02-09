from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect
from expence.models import Transaction


# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        print(type(description), amount)

        if  description is  str:
            messages.info(request, "no description provided")
            return redirect('/')
        try:
            amount=float(amount)
        except Exception as e:
            messages.info(request, "should be number")
            return redirect('/')
        Transaction.objects.create(description=description, amount=amount)
    tran=Transaction.objects.all()
    balance=Transaction.objects.all().aggregate(balance=Sum('amount'))['balance'] or 0
    income=Transaction.objects.filter(amount__gte = 0).aggregate(income=Sum('amount'))['income'] or 0
    expence=Transaction.objects.filter(amount__lte = 0).aggregate(expence=Sum('amount'))['expence'] or 0

    return render(request,'index.html',
                  {'transactions':tran,
                   'income':income, 'expence':expence,'balance':balance})

def delete(request,uuid):
    Transaction.objects.filter(uuid=uuid).delete()
    return redirect('/')
