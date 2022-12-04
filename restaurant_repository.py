def get_all_restaurants():
    return {
        [
            {
                "id": 1,
                "logo_url": "https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg",
                "restaurant_name": "Bastard Burgers",
                "color": "#e47200"
            }
        ],
        [
            {
                "id": 2,
                "logo_url": "https://www.max.se/build/svg/logo-max.svg",
                "restaurant_name": "Max Burgers",
                "color": "#f11823"
            }
        ]
        }

def get_meal_from_restaurant(id):
    if id == 1:
        return f"https://order.bastardburgers.com/se/sv-se/products/131/config?menuType=takeaway&categoryId=323&storeId=168&hash=&itemId=&choice=&quantity=1&returnCategoryId=322&returnUrl=%2Fse%2Fsv-se%2Fcategories%3FmenuType%3Dtakeaway%26categoryId%3D322%26storeId%3D168"
    if id == 2:
        return f"https://order.max.se/se/sv-se/products/11541/config?menuType=takeaway&categoryId=14950&storeId=329&hash=&itemId=&choice=&quantity=1&returnCategoryId=14332&returnUrl=%2Fse%2Fsv-se%2Fcategories%3FmenuType%3Dtakeaway%26categoryId%3D14332%26storeId%3D329"