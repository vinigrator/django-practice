import datetime

from django.db.models import Max, Min, Count
from django.shortcuts import render

from iShop.models import Shop, Seller, Goods

# Create your views here.
def view_shop(request):
    #posts = BlogArticle.objects.all()
    return render(request, 'default.html', {})

def view_shop_ex(request):
    all_shops = Shop.objects.all()
    all_goods = Goods.objects.all()
    all_sellers = Seller.objects.all()

    sh_good = {}
    sh_sell = {}
    for curShop in Shop.objects.all():
        sh_good[curShop.name] = Goods.objects.filter(shops=curShop)
        sh_sell[curShop.name] = Seller.objects.filter(shop=curShop)

    midate = Seller.objects.aggregate(Min('date_start'))

    madate = Seller.objects.aggregate(Max('date_start'))
    shellback = Seller.objects.get(date_start=midate['date_start__min'])
    young_boy = Seller.objects.get(date_start=madate['date_start__max'])

    popular_goods = Goods.objects.values('name').annotate(cnt_sh=Count('shops')).order_by('-cnt_sh')[0]['name']

    return render(request, 'default.html', {"sh":all_shops, "gd":all_goods, "se":all_sellers, "sh_gd":sh_good, "sh_se":sh_sell, "sb":shellback, "yb":young_boy, "pg":popular_goods})


def view_shop_add(request):
    #shop = Shop("First", "Moscow", 9.9)
    #shop.save()
    #posts = BlogArticle.objects.all()
    shops = Shop.objects.all()
    for sh in shops:
        sh.delete()
    args = {'name': "First", 'address': "Moscow", 'rate': 9.9}
    shop1 = Shop(**args)
    shop1.save()
    args = {'name': "Second", 'address': "Moscow", 'rate': 8.9}
    shop2 = Shop(**args)
    shop2.save()
    args = {'name': "Third", 'address': "St.Peterburg", 'rate': 9.3}
    shop3 = Shop(**args)
    shop3.save()
    args = {'name': "Fourth", 'address': "Bologoe", 'rate': 6.9}
    shop4 = Shop(**args)
    shop4.save()

    goods = Goods.objects.all()
    for gd in goods:
        gd.delete()
    args = {'name': "iGvozd", 'count':10000, 'price':2}
    good1 = Goods(**args)
    good1.save()
    good1.shops.add(shop1,shop4)
    good1.save()
    args = {'name': "iMolotok", 'count':152, 'price':200}
    good2 = Goods(**args)
    good2.save()
    good2.shops.add(shop1, shop2, shop3)
    good2.save()
    args = {'name': "iTopor", 'count':666, 'price':1313}
    good3 = Goods(**args)
    good3.save()
    good3.shops.add(shop1, shop3)
    good3.save()

    sellers = Seller.objects.all()
    for sl in sellers:
        sl.delete()
    args = {'name': "Ivanov", 'characteristic': "", 'salary': 35000, "date_start": datetime.datetime.strptime("24.01.2015 12:00", "%d.%m.%Y %H:%M"), "shop": shop1}
    seller1 = Seller(**args)
    seller1.save()
    args = {'name': "Witch", 'characteristic': "Grand Witch", 'salary': 66613,
            "date_start": datetime.datetime.strptime("06.06.2666 13:13", "%d.%m.%Y %H:%M"), "shop": shop1}
    seller2 = Seller(**args)
    seller2.save()
    args = {'name': "Petrov", 'characteristic': "", 'salary': 30000,
            "date_start": datetime.datetime.strptime("20.05.2005 20:05", "%d.%m.%Y %H:%M"), "shop": shop3}
    seller3 = Seller(**args)
    seller3.save()

    return render(request, 'default.html', {})