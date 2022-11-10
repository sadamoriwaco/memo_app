from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator

from .models import Custmer,Message

from .forms import CustmerForm,MessageForm
from .forms import FindForm
from .forms import CheckForm


def index(request,num=1):
    data=Custmer.objects.all()
    page=Paginator(data,3)
    params={
        'title':'memo',
        'message':'',
        'data':page.get_page(num),
    }
    return render(request,'memo/index.html',params)

# def index(request):
#     data = Custmer.objects.all()
#     re1=Custmer.objects.aggregate(Count('age'))
#     re2=Custmer.objects.aggregate(Sum('age'))
#     re3=Custmer.objects.aggregate(Avg('age'))
#     re4=Custmer.objects.aggregate(Min('age'))
#     re5=Custmer.objects.aggregate(Max('age'))
#     msg='count:'+str(re1['age__count'])+\
#         '<br>Sum:'+str(re2['age__sum'])+\
#         '<br>Average:'+str(re3['age__avg'])+\
#         '<br>Min:'+str(re4['age__min'])+\
#         '<br>Max:'+str(re5['age__max'])
#     params = {
#         'title':'Memo',
#         'message':msg,
#         'data':data,
#     }
#     return render(request,'memo/index.html',params)

# def index(request):
#     data = Custmer.objects.all().order_by('age')
#     # 逆の順の場合「.reverse()」
#     # data = Custmer.objects.all().order_by('age').reverse()
#     params = {
#         'title':'Memo',
#         'message':'',
#         'data':data,
#     }
#     return render(request,'memo/index.html',params)
    
def create(request):    
    if(request.method == 'POST'):
        obj=Custmer()
        custmer=CustmerForm(request.POST,instance=obj)
        custmer.save()
        return redirect(to='/memo')
    params = {
        'title':'Memo',
        'form':CustmerForm(),
    }
    return render(request,'memo/create.html',params)
    
def edit(request,num):
    obj=Custmer.objects.get(id=num)
    if(request.method == 'POST'):
        custmer=CustmerForm(request.POST,instance=obj)
        custmer.save()
        return redirect(to='/memo')
    params={
        'title':'memo',
        'id':num,
        'form':CustmerForm(instance=obj),
    }
    return render(request,'memo/edit.html',params)

def delete(request,num):
    custmer=Custmer.objects.get(id=num)
    if(request.method == 'POST'):
        custmer.delete()
        return redirect(to='/memo')
    params={
        'title':'Memo',
        'id':num,
        'obj':custmer,
    }
    return render(request,'memo/delete.html',params)

# def find(request):
#     if(request.method == 'POST'):
#         msg='serch result:'
#         form=FindForm(request.POST)
#         str=request.POST['find']

#         # name mail検索
#         data=Custmer.objects.filter(Q(name__contains=str)|Q(mail__contains=str))

#         # よりも小さい
#         # val=str.split()
#         # data=Custmer.objects.filter(age__lte=int(str))

#         # ＊＊以上＊＊以下
#         # data=Custmer.objects.filter(age__gte=val[0],age__lte=val[1])

#         # data=Custmer.objects.filter(name__contains=str)

#         # 書いた名前全部検索
#         # list=str.split()
#         # data=Custmer.objects.filter(name__in=list)

#     else:
#         msg='serch words..'
#         form=FindForm()
#         data=Custmer.objects.all()
#     params={
#         'title':'Memo',
#         'message':msg,
#         'form':form,
#         'data':data
#     }
#     return render(request,'memo/find.html',params)

def find(request):
    if(request.method == 'POST'):
        msg=request.POST['find']
        form=FindForm(request.POST)
        sql='select * from memo_custmer'
        if(msg != ''):
            sql += 'where' + msg
        data=Custmer.objects.raw(sql)
        msg=sql
    else:
        msg='search words...'
        form=FindForm()
        data=Custmer.objects.all()
    params={
        'title':'Memo',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'memo/find.html',params)

def check(request):
    params={
        'title':'Memo',
        'message':'check validation.',
        'form':CheckForm(),
    }   
    if(request.method=='POST'):
        obj=Custmer()
        form=CustmerForm(request.POST,instance=obj)
        params['form']=form
        if(form.is_valid()):
            params['message']='OK!'
        else:
            params['message']='no good.'
    return render(request,'memo/check.html',params)


def message(request,page=1):
    if(request.method=='POST'):
        obj=Message()
        form=MessageForm(request.POST,instance=obj)
        form.save()
    data=Message.objects.all().reverse()
    paginator=Paginator(data,5)
    params={
        'title':'Message',
        'form':MessageForm(),
        'data':paginator.get_page(page),
    }
    return render(request,'memo/message.html',params)