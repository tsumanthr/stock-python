from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import stock

# Create your views here.


def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # login authentication
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if username == 'admin':
                login(request, user)
                return render(request, 'stockentry_manager.html')
            else:
                login(request, user)
                return render(request, 'stockentry_user.html')
        else:
            messages.success(request, 'invalid details')
            return redirect('login')


def returnstockmanger_page(request):
    return render(request, 'stockentry_manager.html')


def stockentrymanager_page(request):
    if request.method == 'POST':
        arriveddate = request.POST['date']
        if stock.objects.filter(arriveddate=arriveddate).exists():
            messages.error(request, "Date already present!")
            return render(request, "stockentry_manager.html")
        else:
            stocks = [[1,  request.POST.get('date'), "SUGAR",     request.POST.get('Q1'), request.POST.get('P1')],
                      [2,  request.POST.get('date'), "APPLE",     request.POST.get(
                          'Q2'), request.POST.get('P2')],
                      [3,  request.POST.get('date'), "SALT",      request.POST.get(
                          'Q3'), request.POST.get('P3')],
                      [4,  request.POST.get('date'), "WHEAT",     request.POST.get(
                          'Q4'), request.POST.get('P4')],
                      [5,  request.POST.get('date'), "RAGI",      request.POST.get(
                          'Q5'), request.POST.get('P5')],
                      [6,  request.POST.get('date'), "RICE",      request.POST.get(
                          'Q6'), request.POST.get('P6')],
                      [7,  request.POST.get('date'), "PASTA",     request.POST.get(
                          'Q7'), request.POST.get('P7')],
                      [8,  request.POST.get('date'), "GRAPES",    request.POST.get(
                          'Q8'), request.POST.get('P8')],
                      [9,  request.POST.get('date'), "PERFUMES",  request.POST.get(
                          'Q9'), request.POST.get('P9')],
                      [10, request.POST.get('date'), "DAIRYMILK", request.POST.get(
                          'Q10'), request.POST.get('P10')],
                      [11, request.POST.get('date'), "HONEY",     request.POST.get(
                          'Q11'), request.POST.get('P11')],
                      [12, request.POST.get('date'), "MANGO",     request.POST.get(
                          'Q12'), request.POST.get('P12')],
                      [13, request.POST.get('date'), "ORANGE",    request.POST.get(
                          'Q13'), request.POST.get('P13')],
                      [14, request.POST.get('date'), "ALMONDS",   request.POST.get(
                          'Q14'), request.POST.get('P14')],
                      [15, request.POST.get('date'), "KIVI",      request.POST.get('Q15'), request.POST.get('P15')]]
            for s in stocks:
                stock(
                    sno=s[0],
                    arriveddate=s[1],
                    productName=s[2],
                    productQ=s[3],
                    productP=s[4]
                ).save()

            return render(request, "stockentry_manager.html")


def stockentryuser_page(request):
    if request.method == 'POST':
        arriveddate = request.POST['date']
        if stock.objects.filter(arriveddate=arriveddate).exists():
            messages.error(request, "Date already present!")
            return render(request, "stockentry_user.html")
        else:
            stocks = [[1,  request.POST.get('date'), "SUGAR",     request.POST.get('Q1'), request.POST.get('P1')],
                      [2,  request.POST.get('date'), "APPLE",     request.POST.get(
                          'Q2'), request.POST.get('P2')],
                      [3,  request.POST.get('date'), "SALT",      request.POST.get(
                          'Q3'), request.POST.get('P3')],
                      [4,  request.POST.get('date'), "WHEAT",     request.POST.get(
                          'Q4'), request.POST.get('P4')],
                      [5,  request.POST.get('date'), "RAGI",      request.POST.get(
                          'Q5'), request.POST.get('P5')],
                      [6,  request.POST.get('date'), "RICE",      request.POST.get(
                          'Q6'), request.POST.get('P6')],
                      [7,  request.POST.get('date'), "PASTA",     request.POST.get(
                          'Q7'), request.POST.get('P7')],
                      [8,  request.POST.get('date'), "GRAPES",    request.POST.get(
                          'Q8'), request.POST.get('P8')],
                      [9,  request.POST.get('date'), "PERFUMES",  request.POST.get(
                          'Q9'), request.POST.get('P9')],
                      [10, request.POST.get('date'), "DAIRYMILK", request.POST.get(
                          'Q10'), request.POST.get('P10')],
                      [11, request.POST.get('date'), "HONEY",     request.POST.get(
                          'Q11'), request.POST.get('P11')],
                      [12, request.POST.get('date'), "MANGO",     request.POST.get(
                          'Q12'), request.POST.get('P12')],
                      [13, request.POST.get('date'), "ORANGE",    request.POST.get(
                          'Q13'), request.POST.get('P13')],
                      [14, request.POST.get('date'), "ALMONDS",   request.POST.get(
                          'Q14'), request.POST.get('P14')],
                      [15, request.POST.get('date'), "KIVI",      request.POST.get('Q15'), request.POST.get('P15')]]
            for s in stocks:
                stock(
                    sno=s[0],
                    arriveddate=s[1],
                    productName=s[2],
                    productQ=s[3],
                    productP=s[4]
                ).save()

            return render(request, "stockentry_user.html")


def report_page(request):
    totaldata = stock.objects.all()
    return render(request, 'report.html', {"data": totaldata})


def showreport_page(request):
    date = request.POST.get('date')
    filterdata = stock.objects.filter(arriveddate=date)
    return render(request, 'report.html', {'data': filterdata})
