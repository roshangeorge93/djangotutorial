
# products:app

# SELECT
# 	products.product_id,
# 	products.product_name,
# 	products.product_price,
# 	products.product_rating,
# 	brand.brand_name,
# 	brand.brand_id,
# 	category.category_name
# FROM
# 	products
# 	JOIN brand ON products.brand_id = brand.brand_id
# 	JOIN category ON category.category_id = products.category_id;

# ----DJANGO EQUIVALENT-------
products=Product.objects.select_related('category','brand').values('id','name','price','rating','brand__name','brand__id','category__name')
for product in products:
   print(product)

# ----------------------------------------------------------------------------------------------------------------------
# -- list all products
# select * from products;

# ----DJANGO EQUIVALENT-------
all_products=Product.objects.all().values()
for product in all_products:
        print(product)

# ----------------------------------------------------------------------------------------------------------------------
# -- given a category_id ,list the products
# select * from products left join category on products.category_id=category.category_id  where category.category_id='c_id1';

# ----DJANGO EQUIVALENT-------
products=Product.objects.select_related('category').filter(category_id__id=1).values()
for product in products:
         print(product)

# ----------------------------------------------------------------------------------------------------------------------
# --list all products and filter based on cat_name
# select * from products left join category on products.category_id=category.category_id where category.category_name='c_name1';

# ----DJANGO EQUIVALENT-------
products=Product.objects.select_related('category').filter(category_id__name='category4').values()
for product in products:
         print(product)

# ----------------------------------------------------------------------------------------------------------------------
# -- list all categories and their products
# select * from category left join products on products.category_id=category.category_id;

# ----DJANGO EQUIVALENT-------
categories=Category.objects.prefetch_related('product_set').all().values()

# ----------------------------------------------------------------------------------------------------------------------
# -- list all products and print their brand name
# SELECT * from products left join brand on brand.brand_id=products.brand_id;

# ----DJANGO EQUIVALENT-------
products=Product.objects.select_related('brand').all().values('id','name','brand__name')
for product in products:
         print(product)

# ----------------------------------------------------------------------------------------------------------------------
# -- list all sub_categories under a category(based on cat_id)
# select * from category where category.parent_category_id='pc_id5';

# ----DJANGO EQUIVALENT-------
sub_categories=Category.objects.filter(parent_category_id=1).values()
for category in sub_categories:
     print(category)

# ----------------------------------------------------------------------------------------------------------------------
# -- list all sub_categories under a list of categories(based on id)
# SELECT * FROM category
# WHERE category.parent_category_id IN ('pc_id1','pc_id5','pc_id2');

# ----DJANGO EQUIVALENT-------
sub_categories=Category.objects.filter(parent_category_id__in=[1,2]).values()
for category in sub_categories:
     print(category)
# ----------------------------------------------------------------------------------------------------------------------
# -- list all sub_category under a category(based on name):using self join
# select  c.category_id as sub_categories from category c  join category p on c.parent_category_id=p.category_id where p.category_name='c_name2';

# ----DJANGO EQUIVALENT-------
parent_category=Category.objects.get(name='category1')

if parent_category:
       subcategories=Category.objects.filter(parent_category_id=parent_category.id)
else:
       subcategories=Category.objects.none()

for subcategory in subcategories:
       print(subcategory.name)
# ----------------------------------------------------------------------------------------------------------------------
