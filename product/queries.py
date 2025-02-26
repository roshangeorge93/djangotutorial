# Products and Categories

# 1) SELECT * FROM product WHERE category_id = 'cat1'

from product.models import Product
products = Product.objects.filter(category_id='1')
products.values()


# 2)SELECT
# 	product.product_name 
# FROM product
# LEFT JOIN category ON product.category_id = category.category_id
# WHERE category.category_id='cat1';


from product.models import Product, Category
category_id = 'cat1'
product_names = Product.objects.filter(category_id=category_id).values_list('product_name', flat=True)


# 3) SELECT
# 	*
# FROM category
# LEFT JOIN product ON product.category_id = category.category_id

from product.models import Category
categories_with_products = Category.objects.prefetch_related('product_set').all()


# 4) -- list all sub_category under a category(based on name):using self join

