from django.shortcuts import render
from .models import Product
from django.db.models import Q

# filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

def filtering(products, list, query):
    if list != []:
        for i in list:
            products = products.filter(
                    (Q(prdlstNm__icontains=query) |
                    Q(prdkind__icontains=query)) &
                    ~Q(allergy__icontains=i)
                )
            list.remove(i)
            return filtering(products, list, query)
    return products


def searchResult(request):
    # global query
    if ('kw' in request.GET) and ('afilter' in request.GET):
        query = request.GET.get('kw')
        afilter = request.GET.getlist('afilter')
        list = afilter.copy()
        products = Product.objects.all()
        products = filtering(products, list, query)
        return render(request, 'search.html', {'query':query, 'afilter':afilter, 'products':products} )
    
    elif ('kw' in request.GET):
        query = request.GET.get('kw')
        products = Product.objects.all().filter(
            Q(prdlstNm__icontains=query) |
            Q(prdkind__icontains=query)
        )
        return render(request, 'search.html', {'query':query, 'products':products} )
