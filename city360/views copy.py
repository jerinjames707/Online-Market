from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime
import pycurl
from urllib.parse import urlencode
from .models import *

from ML import wage_pred


def sends_mail(mail,msg):

	crl = pycurl.Curl()
	crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
	data = {'email': mail,'msg':msg}
	pf = urlencode(data)

	# Sets request method to POST,
	# Content-Type header to application/x-www-form-urlencoded
	# and data to send in request body.
	crl.setopt(crl.POSTFIELDS, pf)
	crl.perform()
	crl.close()

def first(request):
    user = category.objects.all()
    return render(request,'index.html', {'result': user})

def index(request):
    user = category.objects.all()
    return render(request,'index.html', {'result': user})

def userreg(request):
    file=open("ML/mappings.txt","r")
    data_maps=eval(file.read())
    file.close()
    place=list(data_maps['District'].keys())
    return render(request,'userregister.html',{'res':place})


def wrkreg(request):
    file=open("ML/mappings.txt","r")
    data_maps=eval(file.read())
    file.close()
    print(data_maps.keys())
    data=dict()
    for i in list(data_maps.keys()):
        data[i]=list(data_maps[i].keys())
    #print(list(data_maps['District'].keys()))
    user = category.objects.all()
    return render(request,'w_register.html', {'result': user,'res':data})


def login(request):
    return render(request,'login.html')

def adduser(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        place=request.POST.get('place')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        status=request.POST.get('status')

        cus=userregg(name=name,email=email,place=place,phone=phone,password=password,status=status)
        cus.save()
        return render(request,'index.html', {'message1':'successfully Registered'})

def addworker(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        centre=request.POST.get('centre')
        gender=request.POST.get('gender')
        labour_category=request.POST.get('labour_category')
        labour_type=request.POST.get('labour_type')
        state=request.POST.get('state')
        district=request.POST.get('district')
        phone=request.POST.get('phone')
        category=request.POST.get('category')
        password=request.POST.get('password')
        status=request.POST.get('status')

        cus=wrkregg(name=name,email=email,gender=gender,labour_category=labour_category,district=district,labour_type=labour_type,state=state,centre=centre,phone=phone,category=category,password=password,status=status)
        cus.save()
        return render(request,'index.html', {'message1':'successfully Registered'})

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif userregg.objects.filter(email=email,password=password,status='approved').exists():
        userdetails=userregg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name

            request.session['uemail'] = email

            request.session['cus'] = 'cus'


            return render(request,'index.html')

    elif wrkregg.objects.filter(email=email,password=password,status='approved').exists():
        userdetails=wrkregg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['wid'] = userdetails.id
            request.session['wname'] = userdetails.name

            request.session['wemail'] = email
            request.session['category'] = userdetails.category



            return render(request,'index.html')

    else:
        return render(request, 'login.html')

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def viewusers(request):
    user = userregg.objects.all()
    return render(request, 'viewusers.html', {'result': user})

def viewworker(request):
    user = wrkregg.objects.all()
    return render(request, 'viewworkers.html', {'result': user})

def viewwrkrs(request):
    user = wrkregg.objects.all()
    return render(request, 'viewwrkr.html', {'result': user})

def prediction(request):
    file=open("ML/mappings.txt","r")
    data_maps=eval(file.read())
    file.close()
    print(data_maps.keys())
    data=dict()
    for i in list(data_maps.keys()):
        data[i]=list(data_maps[i].keys())
    return render(request, 'addpred.html',{'res':data})

def pred(request):
    if request.method=='POST':

    return render(request, 'result.html',{'res':result})


def wapprove(request,id):
    sel=wrkregg.objects.get(id=id)
    a=sel.name
    b=sel.email
    c=sel.password
    e=sel.phone
    f=sel.category
    upd=wrkregg(name=a,email=b,phone=e,password=c,category=f,status='approved',id=id)
    upd.save()
    sends_mail(b,'Your Request  Approved by Roadside Assistant Admin' )
    return redirect(viewwrkrs)
def wdelete(request,id):
    sel=wrkregg.objects.get(id=id)
    b=sel.email
    sends_mail(b,'Your Request  Rejected by Roadside Assistant Admin' )
    sel.delete()
    return redirect(viewwrkrs)



def uapprove(request,id):
    sel=userregg.objects.get(id=id)
    a=sel.name
    b=sel.email
    c=sel.password
    d=sel.place
    e=sel.phone
    upd=userregg(name=a,email=b,place=d,phone=e,password=c,status='approved',id=id)
    upd.save()
    print("sending.....")
    sends_mail(b,'Your Request  Approved by Roadside Assistant Admin' )
    print("mail Sent.....")
    return redirect(viewusers)

def udelete(request,id):
    sel=userregg.objects.get(id=id)
    b=sel.email
    sends_mail(b,'Your Request  Rejected by Roadside Assistant Admin' )
    sel.delete()
    return redirect(viewusers)

def cat(request):
    return render(request,'addcategory.html')

def addcat(request):
    if request.method=="POST":
        name=request.POST.get('cat')
        cus=category(name=name)
        cus.save()
        return render(request,'addcategory.html',{'status': 'Register Successfully'})

def subcat(request):
    user = category.objects.all()
    return render(request,'addsubcategory.html', {'result': user})

def addsubcat(request):
    if request.method=="POST":
        cname=request.POST.get('cat')
        sub_name=request.POST.get('subcat')
        cus=subcategory(cname=cname,sub_name=sub_name)
        cus.save()
        return render(request,'addsubcategory.html',{'status': 'Register Successfully'})

# def book(request,id):
#     data=wrkregg.objects.get(id=id)
#     return render(request,'bookservice.html',{'result':data})

def book(request):
    user = category.objects.all()
    return render(request,'bookservice.html', {'result': user})

def addbook(request):
    if request.method=="POST":
        uname=request.session['uname']
     
        date=request.POST.get('date')
        place=request.POST.get('place')
        phone=request.POST.get('phone')
        typee=request.POST.get('typee')
        issue=request.POST.get('issue')
        no_wrkr=request.POST.get('no_wrkr')
        rate=request.POST.get('rate')
        status=request.POST.get('status')


        cus=booking(uname=uname,wid='0',no_wrkr=no_wrkr,rate=rate,date=date,place=place,phone=phone,typee=typee,issue=issue,status=status)
        cus.save()
        user = category.objects.all()
       # return redirect(viewwrkrs)
    return render(request,'index.html', {'message2':'successfully Booked','result':user})

def viewbooking(request):
    uid=request.session['uname']
    fetch_booking = booking.objects.filter(uname=uid)
   
    return render(request,'viewbooking.html', {'result':fetch_booking})

def cancel(request,id):
    sel=booking.objects.get(id=id)
    sel.delete()
    return redirect(viewbooking)

def v_book(request):
    data=booking.objects.filter(typee=request.session['category'],status='pending')
    return render(request,'viewbook_w.html',{'result':data})

def confirm(request,id):
    sel=booking.objects.get(id=id)
    a=sel.uname
    b=sel.wid
    c=sel.date
    d=sel.place
    e=sel.phone
    f=sel.typee
    g=sel.issue
    h=sel.no_wrkr
    i=sel.rate
    
    upd=booking(uname=a,wid=b,place=d,phone=e,date=c,typee=f,issue=g,no_wrkr=h,rate=i,status='confirmed',id=id)
    upd.save()
    return redirect(v_book)

def reject(request,id):
    sel=booking.objects.get(id=id)
    a=sel.uname
    b=sel.wid
    c=sel.date
    d=sel.place
    e=sel.phone
    f=sel.typee
    g=sel.issue
    h=sel.no_wrkr
    i=sel.rate
    upd=booking(uname=a,wid=b,place=d,phone=e,date=c,typee=f,issue=g,no_wrkr=h,rate=i,status='rejected',id=id)
    upd.save()
    return redirect(v_book)

def report(request):
    
    data=booking.objects.filter(status='confirmed')
    return render(request,'report.html',{'result':data})

def gvreport(request,id):
    
    data=booking.objects.get(id=id)
    return render(request,'givereport.html',{'result':data})


def addreports(request):
    if request.method=="POST":
        bid=request.POST.get('bid')
        wid=request.session['wid']
        issue=request.POST.get('issue')
        uname=request.POST.get('uname')
        typee=request.POST.get('typee')
        status=request.POST.get('status')
        date=request.POST.get('date')
        amount=request.POST.get('amount')


        cus=reportss(bid=bid,wid=wid,issue=issue,uname=uname,typee=typee,status=status,date=date,amount=amount)
        cus.save()
        return redirect(report)

def viewwrkreport(request):
    name=request.session['uname']
    user = reportss.objects.filter(uname=name)
    return render(request, 'v_report.html', {'result': user})

def pay(request,id):
    data=reportss.objects.get(id=id)
    return render(request,'payment.html',{'result':data})

def addpayment(request):
    if request.method=="POST":
        rid=request.POST.get('rid')
        uname=request.POST.get('uname')
        typee=request.POST.get('typee')
        wid=request.POST.get('wid')
        amount=request.POST.get('amount')
        date=request.POST.get('date')
        c_num=request.POST.get('c_num')
   
        e_date=request.POST.get('e_date')
        cvv=request.POST.get('cvv')


        cus=payment(rid=rid,uname=uname,typee=typee,wid=wid,amount=amount,date=date,c_num=c_num,e_date=e_date,cvv=cvv)
        cus.save()
        user = category.objects.all()
        #return redirect(index)
        return render(request,'index.html', {'message':'successfully paid','result':user})

def viewbooking_admin(request):
     user1 = booking.objects.all()
     user3= wrkregg.objects.all()
     for i in user1:
        for j in user3:
            if str(i.wid)==str(j.id):
                i.wid=j.name
     user = payment.objects.all()
     user2= wrkregg.objects.all()
     for i in user:
        for j in user2:
            if str(i.wid)==str(j.id):
                i.wid=j.name

     return render(request, 'booking.html', {'result': user,'results': user1})

def ufeedback(request):
    return render(request,'u_feedback.html')

def adduserfdbk(request):
    if request.method=="POST":
        user=request.session['uname']
        feedback=request.POST.get('feedback')
        cus=user_feedback(uname=user,feedback=feedback)
        cus.save()
        return render(request,'u_feedback.html',{'status': 'Register Successfully'})

def wfeedback(request):
    return render(request,'w_feedback.html')

def addwrkrfdbk(request):
    if request.method=="POST":
        user=request.session['wname']
        feedback=request.POST.get('feedback')
        cus=wrkr_feedback(uname=user,feedback=feedback)
        cus.save()
        return render(request,'w_feedback.html',{'status': 'Register Successfully'})

def viewfeedbacks(request):
     user = user_feedback.objects.all()
     user1 = wrkr_feedback.objects.all()
     return render(request, 'viewfeedbacks.html', {'result': user,'results': user1})

