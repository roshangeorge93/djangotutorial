from products.models import Product,Brand,Catageory

# list all products
q0=Product.objects.values_list('P_name',flat=True)
print(q0)

# list all products And filter based on cat_id  or given a catgeory id ,list all the products
q1=Product.objects.filter(Cat_id='20').values('P_name','Cat_id')
print(q1)


# list all products and filtrer based on cat_name
q2=Product.objects.filter(Cat__Cat_name='android').values('P_name','Cat__Cat_name')
print(q2)

# list all category and their products
q3=Product.objects.select_related('Cat_id').values('P_name','Cat__Cat_name')
print(q3)

