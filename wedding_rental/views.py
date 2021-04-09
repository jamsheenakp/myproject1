from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from .models import branch, branch_manager, login, category, subcategory, item


# Create your views here.
def adm_add_branch(request):
    if request.method=="POST":
        branchname=request.POST['branch_name']
        place=request.POST['place']
        city= request.POST['city']
        phone=request.POST['phone_no']
        image=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        print(filename)

        branch_obj=branch()
        branch_obj.branch_name=branchname
        branch_obj.branch_place=place
        branch_obj.branch_city=city
        branch_obj.branch_phone=phone
        branch_obj.branch_image=fs.url(filename)
        branch_obj.save()


    return render(request,"adm/add_ branch.html")

def adm_add_branch_manager(request):
    if request.method=="POST":
        branch_id=request.POST['branches']
        b=branch.objects.get(pk=branch_id)





        managername=request.POST['manager_name']
        housename=request.POST['house_name']
        place=request.POST['place']
        city=request.POST['city']
        phoneno=request.POST['phone_no']
        age=request.POST['age']
        email=request.POST['email']
        image=request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)

        login_obj = login()
        login_obj.username =email
        login_obj.password="12"
        login_obj.usertype="branchmanager"
        login_obj.save()

        manager_obj=branch_manager()
        manager_obj.name= managername
        manager_obj.house_name=housename
        manager_obj.place=place
        manager_obj.city=city
        manager_obj.phone=phoneno
        manager_obj.age=age
        manager_obj.email=email
        manager_obj.BRANCH_ID=b
        manager_obj.LOGIN_ID=login_obj
        manager_obj.image=fs.url(filename)
        manager_obj.save()


    branch_obj=branch.objects.all()
    return render(request,"adm/add_branch_manager.html" ,{'data' : branch_obj})

def adm_add_category(request):
    if request.method=="POST":
        categoryname=request.POST['category']

        category_obj=category()
        category_obj.category_name=categoryname
        category_obj.save()

    return render(request,"adm/add_category.html")


def adm_add_Add_item(request):
    if request.method=="POST":
        itemname=request.POST['item_name']
        itemprice=request.POST['item_price']
        itemquantity=request.POST['item_quantity']
        image = request.FILES['item_image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        # category_id = request.POST['category']
        # c  =item.objects.filter(CATEGORY_ID=category.objects.get(pk=category_id))

        subcategory_id=request.POST['subcategory']
        sub_cat_obj = subcategory.objects.get(pk=subcategory_id)
        item_obj = item()
        item_obj.item_name = itemname
        item_obj.item_price = itemprice
        item_obj.item_quantity = itemquantity
        item_obj.item_image = fs.url(filename)
        item_obj.SUBCATEGORY_ID =sub_cat_obj
        item_obj.save()

    subcategory_obj=subcategory.objects.all()
    category_obj = category.objects.all()
    return render(request, "adm/Add_item.html", {'data': subcategory_obj, 'data1': category_obj})


def adm_add_subcategory(request):
    if request.method=="POST":
        subcategoryname=request.POST['subcategory']
        category_id=request.POST['category']
        c=category.objects.get(pk=category_id)

        subcategory_obj=subcategory()
        subcategory_obj.subcategory_name=subcategoryname
        subcategory_obj.CATEGORY_ID=c
        subcategory_obj.save()

    category_obj=category.objects.all()
    return render(request,"adm/add_subcategory.html" ,{'data': category_obj})

def adm_change_password(request):
    return render(request,"adm/change_password.html")

def adm_edit_branch(request,id):
    branch_obj=branch.objects.get(id=id)
    return render(request,"adm/edit_branch.html",{'data':branch_obj})

def adm_updatetbranch(request):
    branchname=request.POST['branch_name']
    bplace=request.POST['place']
    bcity=request.POST['city']
    phone=request.POST['phone_no']
    id=request.POST['hid']

    branch_obj=branch.objects.get(id=id)
    branch_obj.branch_name = branchname
    branch_obj.branch_place = bplace
    branch_obj.branch_city = bcity
    branch_obj.branch_phone = phone
    if 'branch_image' in request.FILES:
        image=request.FILES['branch_image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        branch_obj.image=fs.url(filename)
    branch_obj.save()
    branch_obj=branch.objects.all()
    return render(request, "adm/view_branch.html",{'data' : branch_obj})

def adm_edit_branchmanager(request,id):
    manager_obj=branch_manager.objects.get(id=id)
    branch_obj=branch.objects.all()
    return render(request,"adm/edit_branchmanager.html",{'data' : manager_obj,'data1':branch_obj})

def adm_updatemanager(request):
    managername=request.POST['name']
    housename=request.POST['house_name']
    place=request.POST['place']
    city=request.POST['city']
    phone_no=request.POST['phone_no']
    Dob=request.POST['Dob']
    email=request.POST['email']
    id = request.POST['hid']

    manager_obj=branch_manager.objects.get(id=id)
    manager_obj.name=managername
    manager_obj.house_name=housename
    manager_obj.place=place
    manager_obj.city=city
    manager_obj.phone=phone_no
    manager_obj.email=email
    manager_obj.dob=Dob
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        manager_obj.image = fs.url(filename)
    manager_obj.save()
    manager_obj=branch_manager.objects.all()
    return render(request, "adm/view_branch_manager.html", {'data': manager_obj})


def adm_edit_category(request,id):
    category_obj=category.objects.get(id=id)
    return render(request,"adm/edit_category.html" ,{ 'data' : category_obj})

def adm_updatecategory(requset):
    categorynm=requset.POST['category']
    id = requset.POST['hid']


    category_obj=category.objects.get(id=str(id))
    category_obj.category_name=categorynm
    category_obj.save()
    category_obj=category.objects.all()
    return render(requset,"adm/view_category.html", {'data': category_obj})


def adm_edit_item(request,id):
    item_obj=item.objects.get(id=id)
    category_obj=category.objects.all()
    subcategory_obj=subcategory.objects.all()
    return render(request,"adm/edit_item.html" ,{'data' : item_obj ,'data1':category_obj,'data2' : subcategory_obj})

def adm_updateitem(request):
    itemn=request.POST['item_name']
    print('item_name')
    price=request.POST['item_price']
    qty=request.POST['item_quantity']
    subcategory_id = request.POST['subcategory']
    id = request.POST['hid']
    item_obj = item.objects.get(id=str(id))
    item_obj.item_name=itemn
    item_obj.item_price=price
    item_obj.item_quantity=qty
    item_obj.save()
    return redirect('myapp:adm_view_item')



def adm_edit_subcategory(request,id):
    subcategory_obj=subcategory.objects.get(id=id)
    category_obj=category.objects.all()
    # subcategory_obj=subcategory.objects.all()
    print(category_obj)
    return render(request,"adm/edit_subcategory.html" ,{'data': subcategory_obj ,'data1': category_obj})

def adm_updatesubcategory(request):
    subcategoryname=request.POST['subcategory']
    id = request.POST['hid']

    subcategory_obj = subcategory.objects.get(id=id)
    subcategory_obj.subcategory_name=subcategoryname
    subcategory_obj.save()
    subcategory_obj=subcategory.objects.all()
    category_obj=category.objects.all()
    return render(request, "adm/view_subcategory.html", {'data': subcategory_obj ,'data1' :category_obj})



def adm_Login(request):
    return render(request,"adm/Login.html")

def adm_purchased_item(request):
    return render(request,"adm/purchased_item.html")

def adm_review(request):
    return render(request,"adm/review.html")

def adm_view_branch(request):
    if request.method=="POST":
        branchsearch=request.POST['branch_name']
        branch_obj=branch.objects.filter(branch_name__contains= branchsearch)
        return render(request, "adm/view_branch.html", {'data': branch_obj})
    branch_obj=branch.objects.all()
    return render(request,"adm/view_branch.html",{'data':branch_obj})

def adm_deletebranch(request,id):
    branch_obj=branch.objects.get(id=id)
    branch_obj.delete()
    return adm_view_branch(request)




def adm_view_branch_managerpost(request):
    if request.method=="POST":
        branchsearch=request.POST['branch']
        manager_obj=branch_manager.objects.filter(BRANCH_ID__branch_name__contains=branchsearch)
        return render(request,"adm/view_branch_manager.html", {'data' : manager_obj})

def adm_view_branch_manager(request):


        manager_obj=branch_manager.objects.all()
        return render(request,"adm/view_branch_manager.html", {'data' : manager_obj})
def adm_deletemanager(request,id):
    branch_manager_obj=branch_manager.objects.get(id=id)
    branch_manager_obj.delete()
    return adm_view_branch_manager(request)

def adm_view_category(request):
    if request.method=="POST" :
        pass

    catall=category.objects.all()
    return render(request,"adm/view_category.html",{'data': catall})

def adm_deletecategory(request,id):
    category_obj=category.objects.get(id=id)
    category_obj.delete()
    return adm_view_category(request)

def adm_view_item(request):
    if request.method=="POST":
         btn=request.POST['button']
         if btn=="Search":

               subcatid=request.POST['subcategory']
               subcategory_obj=subcategory.objects.get(id=subcatid)
               item_obj=item.objects.filter(SUBCATEGORY_ID=subcategory_obj)
         else :
            itemname=request.POST['item']
            item_obj=item.objects.filter(item_name__contains=itemname)
         category_obj = category.objects.all()
         subcategory_obj = subcategory.objects.all()
         return render(request, "adm/view_item.html", {'data': category_obj, 'data1': subcategory_obj, 'data2': item_obj})

    category_obj = category.objects.all()
    subcategory_obj = subcategory.objects.all()

    item_obj = item.objects.all()
    return render(request,"adm/view_item.html"  ,{'data' :category_obj ,'data1':subcategory_obj , 'data2' : item_obj})

def adm_deleteitem(request,id):
    item_obj= item.objects.get(id=id)
    item_obj.delete()
    return adm_view_item(request)

def adm_view_order_details(request):
    return render(request,"adm/view_order_details.html")



def adm_view_rating(request):
    return render(request,"adm/view_rating.html")

def adm_view_subcategory(request):
    if request.method=="POST":
        categoryid=request.POST['category']
        subcategory_obj=subcategory.objects.filter(CATEGORY_ID=category.objects.get(pk=categoryid))
        category_obj=category.objects.all()
        return render(request,"adm/view_subcategory.html" ,{'data' : subcategory_obj, 'data1' :category_obj})
    subcategory_obj=subcategory.objects.all()
    category_obj=category.objects.all()
    return render(request, "adm/view_subcategory.html", {'data': subcategory_obj,'data1': category_obj})
def adm_deletesubcategory(request,id):
    subcategory_obj = subcategory.objects.get(id=id)
    subcategory_obj.delete()
    return adm_view_subcategory(request)


def adm_home(request):
    return render(request,"adm/homepage.html")

def adt(request):
    return render(request,"index.html")