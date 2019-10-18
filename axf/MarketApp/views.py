from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):

    typeid = request.GET.get('typeid','104749')

    foodtypes = AxfFoodType.objects.all()
    # typeid,typename,childtypenames,typesort

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    # print(childtypenames)
    # 全部分类: 0  # 进口水果:103534#国产水果:103533

    childtype_list = childtypenames.split('#')

    # print(childtype_list)
    # ['全部分类:0', '进口水果:103534', '国产水果:103533']

    typename_list=[]

    for childtype in childtype_list:
        typename = childtype.split(':')
        # print(typename)
        # 全部分类
        # 进口水果
        # 国产水果
        typename_list.append(typename)

    goods_list = AxfGoods.objects.filter(categoryid=typeid)

    childcid=request.GET.get('childcid','')

    if childcid and childcid !='0':
        goods_list = goods_list.filter(childcid=childcid)

    sort_num=request.GET.get('sort_num','0')

    if sort_num =='1':
        goods_list=goods_list.order_by('price')
    elif sort_num=='2':
        goods_list=goods_list.order_by('-price')
    elif sort_num=='3':
        goods_list=goods_list.order_by('productnum')
    elif sort_num=='4':
        goods_list=goods_list.order_by('-productnum')

    allgoods=AxfGoods.objects.all()


    sort_list=[['综合排序','0'],['价格升序','1'],['价格降序','2'],['销量升序','3'],['销量降序','4']]

    context={
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'typename_list':typename_list,
        'childcid':childcid,
        'sort_num':sort_num,
        'sort_list':sort_list,
        'allgoods':allgoods,

    }
    return render(request,'axf/main/market/market.html',context=context)