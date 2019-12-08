products = [{"product_name":"test"}]


for product in products:
    category_name = product["maincategory"]

    category = session.query(Category).filter(Category.name==category_name)
    if not category:
        category = Category(name=category_name)

    p = Product(product_name=product["product_name"])

    for store_name in product[stores].split():

        store = session.query(Store).filter(Store.name==store_name)
        if not store:
            store = Store(name=store_name)

        p.stores.append(store)

    session.add(p)
session.commit()


    
        
