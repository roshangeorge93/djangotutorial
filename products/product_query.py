from products.models import Product,Brand,Catageory

# list all products
q0=Product.objects.values_list('P_name',flat=True)
print(q0)

# list all products And filter based on cat_id
q1=Product.objects.filter(Cat_id='20').values('P_name','Cat_id')
print(q1)