from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
from django.db.models import Q
import datetime
import pycurl
from urllib.parse import urlencode
from .models import *
from datetime import datetime, timedelta
from django.contrib import messages
from datetime import date
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
   #ser = category.objects.all()
    return render(request,'index.html')

'''def index(request):
    user = category.objects.all()
    return render(request,'index.html', {'result': user})'''
    
def index(request):
    #categories = request.session['category'].split(',')  # Split the category values by comma
    #data=booking.objects.filter(typee__in=categories,place=request.session['place'],status='pending')
    #data=booking.objects.filter(~Q(place__in=request.session['place']),typee__in=categories,status='pending')
    return render(request,'index.html')
    
def userreg(request):
    file=open("ML/mappings.txt","r")
    data_maps=eval(file.read())
    file.close()
    place=list(data_maps['District'].keys())
    return render(request,'userregister.html',{'res':place})
    
def payments(request,id):
    ser = CartItem.objects.get(id=id)
    return render(request,'payment.html',{'res':ser})    

def v_payment(request):
    sel=payment.objects.all()
    return render(request,'viewpayment.html',{'res':sel})
    
def v_payments(request):
    user_id = request.session['uid']
    sell = payment.objects.filter(user_id=user_id)
    context = {'result': sell, 'user_id': user_id}
    return render(request, 'viewpayment2.html', context)


def rating(request, id):
    if request.method == 'POST':
        p_id = request.POST.get('p_name')
        u_id = request.session['uname']
        star = request.POST.get('star')

        # Check if the customer has already rated the product
        existing_rating = ratings.objects.filter(p_id=p_id, u_id=u_id).first()
        if existing_rating:
            # Update the existing rating
            existing_rating.star = star
            existing_rating.save()
        else:
            # Create a new rating
            ins = ratings(p_id=p_id, u_id=u_id, star=star)
            ins.save()

    return render(request, 'index.html', {'message': 'Successfully rated'})
    
    
def add_payment(request,id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        total_price = request.POST.get('total_price')
        date = request.POST.get('date')
        card_name = request.POST.get('card_name')
        card_type = request.POST.get('card_type')
        card_no = request.POST.get('card_no')
        cvv = request.POST.get('cvv')

        # Retrieve any other necessary fields
        
        addpayment = payment(item_name=item_name,quantity=quantity,total_price=total_price, date=date,card_name=card_name,card_type=card_type,card_no=card_no,cvv=cvv,user_id=request.session['uid'])
        addpayment.save()
        
        ser = CartItem.objects.get(id=id)
        ser.delete()
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'payment.html')    

def bid(request,id):
    ser = product.objects.get(id=id)
    return render(request,'add_auction.html',{'res':ser})   

def ad_auction(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        disc = request.POST.get('disc')
        file = request.POST.get('file')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Retrieve any other necessary fields
        
        addauction = auction(item_name=item_name,price=price,disc=disc,file=file,start_date=start_date,end_date=end_date,seller_id=request.session['wid'])
        addauction.save()
        
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'index.html')


def v_auction(request):
    sel = auction.objects.all()

    # Calculate remaining time for each auction item
    for item in sel:
        start_date_str = item.start_date
        end_date_str = item.end_date

        # Convert start_date and end_date strings to datetime objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%dT%H:%M")

        # Calculate remaining time
        remaining_time = end_date - datetime.now()

        # Remove seconds from the remaining time
        remaining_time = remaining_time - timedelta(seconds=remaining_time.seconds % 60)

        # Check if time is over
        if remaining_time <= timedelta(seconds=0):
            remaining_time = "Time Over"

        item.remaining_time = remaining_time

    return render(request, 'viewauction.html', {'res': sel})
    
    
def load_bid(request,id):
    ser = auction.objects.get(id=id)
    return render(request,'add_bidprice.html',{'res':ser}) 
    
from django.contrib import messages

def update(request, id):
    if request.method == "POST":
        auc = auction.objects.get(id=id)
        current_price = int(auc.price)
        price = int(request.POST.get("price"))

        if price > current_price:
            auc.price = price
            auc.user_id = request.session['uid']
            auc.save()
        else:
            messages.warning(request, "Please enter a higher amount than the current price.")

    return redirect(v_auction)

def view_mypro(request):
    u_id=request.session['uid']
    sel=auction.objects.filter(user_id=u_id, end_date__lt=date.today())
    return render(request,'view_mypro.html',{'res':sel})

def buyaucpro(request,id):
    ser = auction.objects.get(id=id)
    return render(request,'aucpayment.html',{'res':ser})  

def add_aucpayment(request,id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_id = request.POST.get('item_id')
        seller_id = request.POST.get('seller_id')
        total_price = request.POST.get('total_price')
        date = request.POST.get('date')
        card_name = request.POST.get('card_name')
        card_type = request.POST.get('card_type')
        card_no = request.POST.get('card_no')
        cvv = request.POST.get('cvv')

        # Retrieve any other necessary fields
        
        addpayment = auctionpayment(item_name=item_name,price=total_price,item_id=item_id,seller_id=seller_id, date=date,card_name=card_name,card_type=card_type,card_no=card_no,cvv=cvv,user_id=request.session['uid'])
        addpayment.save()
        
        # ser = auction.objects.get(id=item_id)
        # ser.delete()
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'index.html')   

def v_book(request):
    sel=product.objects.all()
    return render(request,'viewbook_w.html',{'res':sel})
       
def check_out(request):
    user_id = request.session['uid']
    sell = CartItem.objects.filter(user_id=user_id)
    context = {'result': sell, 'user_id': user_id}
    return render(request, 'checkout.html', context)
 
 
def viewrating(request,item_name):
    sel=ratings.objects.filter(p_id=item_name)
    return render(request,'viewrating.html',{'res':sel})



 

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        p_id = request.POST.get('p_id')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        total = int(price)*int(quantity)
        image = request.POST.get('file')
        # Retrieve any other necessary fields
        
        cart_item = CartItem(item_name=item_name,image=image,p_id=p_id, price=price,total=total,quantity=quantity,description=description,user_id=request.session['uid'])
        cart_item.save()
        
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'index.html')

def v_product(request):
    user = product.objects.filter(seller_id=request.session['wid'])
    return render(request, 'view_sproduct.html', {'result': user})




def login(request):
    return render(request,'login.html')

def adduser(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        status=request.POST.get('status')

        cus=userregg(name=name,email=email,phone=phone,password=password,status=status)
        cus.save()
    return render(request,'index.html', {'message1':'successfully Registered'})

def addseller(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        status=request.POST.get('status')
        myfile=request.FILES['file']
        fs= FileSystemStorage()
        myfile=fs.save(myfile.name,myfile)

        cus=sellerregg(name=name,file=myfile,email=email,phone=phone,password=password,status=status)
        cus.save()
    return render(request,'w_register.html', {'message1':'successfully Registered'})



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

    elif sellerregg.objects.filter(email=email,password=password,status='approved').exists():
        userdetails=sellerregg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['wid'] = userdetails.id
            request.session['wname'] = userdetails.name

            request.session['wemail'] = email



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
    user = sellerregg.objects.all()
    return render(request, 'viewworkers.html', {'result': user})

def viewsellers(request):
    user = sellerregg.objects.all()
    return render(request, 'viewwrkr.html', {'result': user})


def wapprove(request,id):
    sel=sellerregg.objects.get(id=id)
    a=sel.name
    b=sel.email
    c=sel.password
    e=sel.phone
    m=sel.file
    upd=sellerregg(name=a,email=b,phone=e,file=m,password=c,status='approved',id=id)
    upd.save()
    sends_mail(b,'Your Request  Approved by Roadside Assistant Admin' )
    return redirect(viewsellers)
    
def wdelete(request,id):
    cel=sellerregg.objects.get(id=id)
    cel.delete()
    return redirect(viewsellers)

def cdelete(request,id):
    sel=CartItem.objects.get(id=id)
    sel.delete()
    return redirect(check_out)

def uapprove(request,id):
    sel=userregg.objects.get(id=id)
    a=sel.name
    b=sel.email
    c=sel.password
    e=sel.phone
    upd=userregg(name=a,email=b,phone=e,password=c,status='approved',id=id)
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



def addbook(request):
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        date = request.POST.get('date')
        disc = request.POST.get('disc')
        myfile=request.FILES['file']
        fs= FileSystemStorage()
        myfile=fs.save(myfile.name,myfile)

        us = product(item_name=item_name, price=price, date=date, disc=disc,file=myfile,seller_id=request.session.get('wid'))
        us.save()
        #user = category.objects.all()
        # return redirect(viewwrkrs)
    return render(request,'addproduct.html', {'message1':'successfully Registered'})




def viewbooking(request):
    uid=request.session['uname']
    fetch_booking = booking.objects.filter(uname=uid,)
   
    return render(request,'viewbooking.html', {'result':fetch_booking})
    
def amount(request):
    a = reportss.objects.get(amount=wid)
    return render(request,'viewbooking.html', {'res': a})    

def cancel(request,id):
    sel=booking.objects.get(id=id)
    sel.delete()
    return redirect(viewbooking)

def viewwrker(request,wid):
    sel=wrkregg.objects.get(name=wid)
    
    return render(request,'viewwrkprf.html', {'result':sel})

def uprofile(request):
    #a= request.session['uid']
    sel=userregg.objects.get(id=request.session['uid'])
    return render(request,'userprf.html', {'sel':sel})

def wprofile(request):
    #a= request.session['uid']
    sel=sellerregg.objects.get(id=request.session['wid'])
    return render(request,'sellerprf.html', {'sel':sel})


def v_book(request):
    sel3=product.objects.all()
    return render(request,'viewbook_w.html',{'res':sel3})   



def confirm(request,id):
    sel=product.objects.get(id=id)
    a=sel.item_name
    c=sel.price
    d=sel.date
    e=sel.disc
    f=sel.seller_id
    #i=sel.rate
    upd=product(item_name=a,date=d,disc=e,price=c,seller_id=f,status='confirmed',id=id)
    upd.save()
    return redirect(v_book)

def reject(request,id):
    sel=product.objects.get(id=id)
    a=sel.item_name
    c=sel.price
    d=sel.date
    e=sel.disc
    f=sel.seller_id
   # i=sel.rate
    upd=product(item_name=a,date=d,disc=e,price=c,seller_id=f,status='rejected',id=id)
    upd.save()
    return redirect(v_book)


def u_feeback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')    
        ufeed = user_feeback(feedback=feedback,user_id=request.session['uid'])
        ufeed.save()
        
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'usr_feeback.html')

def s_feeback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')    
        ufeed = selr_feedback(feedback=feedback,seller_id=request.session['wid'])
        ufeed.save()
        
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
        
    return render(request, 'slr_feedback.html')

def v_userfeed(request):
    user = user_feeback.objects.all()
    return render(request, 'v_userfeedback.html', {'result': user})
    
def v_sellerfeed(request):
    user = selr_feedback.objects.all()
    return render(request, 'v_sellerfeedback.html', {'result': user})  
    
def return_pro(request,id):
    ser = payment.objects.get(id=id)
    return render(request,'returnproduct.html',{'res':ser})    
    
def addreturn(request,id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        total_price = request.POST.get('total_price')
        date = request.POST.get('date')
        return_reasons = request.POST.get('return_reasons')
        status=request.POST.get('status')

        # Retrieve any other necessary fields
        
        returnitem(item_name=item_name,total_price=total_price,date=date,return_reasons=return_reasons,status=status,user_id=request.session['uid']).save()
        

        return redirect(index)
        # Redirect to the cart page or any other desired page
        #return redirect(cart)  # Assuming you have a named URL for the cart page
    
def v_return(request):
    user = returnitem.objects.all()
    return render(request, 'v_return.html', {'result': user})  



def approve(request,id):
    sel=returnitem.objects.get(id=id) 
    sel.status='approved'
    sel.save()

    return redirect(v_return)

def reject(request,id):
    sel=returnitem.objects.get(id=id) 
    sel.status='Rejected'
    sel.save()

    return redirect(v_return)