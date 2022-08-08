from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from shopapp.models import Shop
#前后端分离，传json
def get_json(request):
    shop = Shop.objects.all()
    data = list(shop.values())
    print(data)
    return JsonResponse({'code':200,'msg':'获取手机列表成功','data':data})
def shop_info(request):
    shop_phones = Shop.objects.all()
    return render(request, 'shop_info.html', {'shop_phones': shop_phones})
def getall(request):#取所有的值
    shop_phones = Shop.objects.all()
    return render(request,'shop_phones.html',{'shop_phones':shop_phones})
def save_form(request):
    return render(request,"phone_save.html")
def save(request):
    shop_phone = Shop(
        title=request.POST.get('title'),
        id=request.POST.get('id'),
        click=request.POST.get('click'),
        phone_img=request.POST.get('phone_img'),
        market_price=request.POST.get('market_price'),
        sell_price=request.POST.get('sell_price'),
        stock_quantity=request.POST.get('stock_quantity'),
        disposition=request.POST.get('disposition'),
        release_time=request.POST.get('release_time')
    )
    shop_phone.save()
    print("手机发售成功")
    return redirect('/shop/getall/')
def delete(request):
    dtitle=request.GET.get("title")
    Shop.objects.filter(title=dtitle).delete()
    print('删除成功！')
    return redirect('/shop/getall/')#重定向
def update(request):
    utitle = request.GET.get("title")
    shop_phone = Shop.objects.get(title=utitle)
    if request.method=="GET":
        return render(request, "update.html", {"shop_phone":shop_phone})
    shop_phones = Shop(
        title=request.POST.get('title'),
        id=request.POST.get('id'),
        click=request.POST.get('click'),
        phone_img=request.POST.get('phone_img'),
        market_price=request.POST.get('market_price'),
        sell_price=request.POST.get('sell_price'),
        stock_quantity=request.POST.get('stock_quantity'),
        disposition=request.POST.get('disposition'),
        release_time=request.POST.get('release_time')
    )
    Shop.objects.filter(title=utitle).update(title=shop_phones.title,
                                             id=shop_phones.id,
                                             click=shop_phones.click,
                                             phone_img=shop_phones.phone_img,
                                             market_price=shop_phones.market_price,
                                             sell_price=shop_phones.sell_price,
                                             stock_quantity=shop_phones.stock_quantity,
                                             disposition=shop_phones.disposition,
                                             release_time=shop_phones.release_time)
    return redirect('/shop/getall/')  #重定向