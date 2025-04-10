from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null=True, related_name='+')

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotion = models.ManyToManyField(Promotion)

class Customer(models.Model):
    Membership_Bronz = 'B'
    Membership_Silver = 'S'
    Membership_Gold = 'G'

    Membership_choices = [
        (Membership_Bronz,'Bronz'),
        (Membership_Silver,'Silver'),
        (Membership_Gold,'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=Membership_choices,default=Membership_Bronz) 

class Order(models.Model):
    Pyment_Status_Pending = 'P'
    Pyment_Status_Complete = 'C'
    Pyment_Status_Failed = 'F'

    Pyment_Status_Choices = [
        (Pyment_Status_Pending, 'Pending'),
        (Pyment_Status_Complete, 'Complete'),
        (Pyment_Status_Failed, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    pyment_Status = models.CharField(max_length=1, choices = Pyment_Status_Choices, default=Pyment_Status_Pending) 
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key=True)
    zip = models.CharField(max_length=255)