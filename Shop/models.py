from django.db import models

# Create your models here. 
class Product(models.Model):  

    def __str__(self): 
        return self.product_name 
    
    product_id = models.AutoField 
    product_name = models.CharField(max_length=50) 
    category = models.CharField(max_length=50,default="") 
    subCategory = models.CharField(max_length=50,default="")  
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)  
    pub_date = models.DateField()  
    image = models.ImageField(upload_to="Shop/Images",default="")

class Contact(models.Model):  

    def __str__(self): 
        return self.name 
    
    msg_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500,default="")  

class Order(models.Model):  

    def __str__(self): 
        return self.name  
    
    order_id = models.AutoField(primary_key=True) 
    items_json = models.CharField(max_length=5000) 
    name = models.CharField(max_length=150) 
    email = models.CharField(max_length=150)  
    phone = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=300) 
    city = models.CharField(max_length=200) 
    state = models.CharField(max_length=200) 
    zip_code = models.CharField(max_length=200)  


