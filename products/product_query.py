from products.models import Product,Brand,Catageory

# list all products
q0=Product.objects.values_list('P_name',flat=True)
print(q0)

