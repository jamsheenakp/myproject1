from django.db import models

# Create your models here.
class login (models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)



class category (models.Model):
    category_name=models.CharField(max_length=50)

class subcategory (models.Model):
    subcategory_name=models.CharField(max_length=50)
    CATEGORY_ID = models.ForeignKey(category, on_delete=models.CASCADE)

class branch (models.Model):
    branch_name=models.CharField(max_length=50)
    branch_place=models.CharField(max_length=50)
    branch_city=models.CharField(max_length=50)
    branch_phone=models.CharField(max_length=50)
    branch_image=models.CharField(max_length=300)

class branch_manager (models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    house_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    BRANCH_ID = models.ForeignKey(branch, on_delete=models.CASCADE)
    LOGIN_ID = models.ForeignKey(login, on_delete=models.CASCADE)


class item (models.Model):
    SUBCATEGORY_ID = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50)
    item_price=models.CharField(max_length=50)
    item_quantity=models.CharField(max_length=50)
    item_image=models.CharField(max_length=300)

class customer (models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    LOGIN_ID = models.ForeignKey(login, on_delete=models.CASCADE)


class order_master (models.Model):
    date=models.DateField(max_length=50)
    status=models.CharField(max_length=50)
    total_amount=models.CharField(max_length=50)
    return_date=models.DateField(max_length=50)
    no_of_days=models.CharField(max_length=50)
    CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.CASCADE)

class order_sub (models.Model):
    quantity=models.CharField(max_length=50)
    ORDER_MASTER_ID=models.ForeignKey(order_master,on_delete=models.CASCADE)
    ITEM_ID = models.ForeignKey(item, on_delete=models.CASCADE)



class stock (models.Model):
    ITEM_ID = models.ForeignKey(item, on_delete=models.CASCADE)
    BRANCH_ID = models.ForeignKey(branch, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)


class complaint(models.Model):
    CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    replay=models.CharField(max_length=100)
    date=models.DateField(max_length=50)


class rating(models.Model):
    ITEM_ID = models.ForeignKey(item, on_delete=models.CASCADE)
    CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.CASCADE)
    rating=models.CharField(max_length=50)
    review=models.CharField(max_length=100)


class cart(models.Model):
    ITEM_ID = models.ForeignKey(item, on_delete=models.CASCADE)
    CUSTOMER_ID = models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)


class damage(models.Model):
    order_sub_ID = models.ForeignKey(order_sub, on_delete=models.CASCADE)
    ITEM_ID = models.ForeignKey(item, on_delete=models.CASCADE)
    damage=models.CharField(max_length=50)

class cash_entry(models.Model):
    ORDER_MASTER_ID = models.ForeignKey(order_master, on_delete=models.CASCADE)
    DAMAGE_ID = models.ForeignKey(damage, on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    date=models.DateField(max_length=50)