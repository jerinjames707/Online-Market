from django.db import models



class userregg(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

class sellerregg(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    file=models.FileField(max_length=150)

class product(models.Model):
    item_name=models.CharField(max_length=150)
    price=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    disc=models.CharField(max_length=150)
    file=models.FileField(max_length=150)
    seller_id=models.CharField(max_length=150)

class CartItem(models.Model):
    item_name = models.CharField(max_length=100)
    p_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cart_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()  # Add this line to include the 'quantity' field
    description = models.TextField()
    total = models.TextField()
    user_id = models.IntegerField()
    # Add any other fields as needed

class payment(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    total_price = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    card_no =models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

class auctionpayment(models.Model):
    item_name = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    card_no =models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    seller_id = models.CharField(max_length=100)

class auction(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    disc = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    seller_id =models.CharField(max_length=100)
    user_id =models.CharField(max_length=100)


class order_tbl(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=150) 
    status=models.CharField(max_length=150)   
    user_id=models.CharField(max_length=150)   
    
class returnitem(models.Model):
    item_name = models.CharField(max_length=100)
    total_price = models.CharField(max_length=100)
    date = models.CharField(max_length=150) 
    return_reasons=models.CharField(max_length=150) 
    status = models.CharField(max_length=150)
    user_id=models.CharField(max_length=150)      
    
        
class user_feeback(models.Model):
    feedback=models.CharField(max_length=150)
    user_id=models.CharField(max_length=150)

class selr_feedback(models.Model):
    feedback=models.CharField(max_length=150)
    seller_id=models.CharField(max_length=150)

class ratings(models.Model):
    p_id=models.CharField(max_length=100)
    star=models.CharField(max_length=100)
    u_id=models.CharField(max_length=100)
