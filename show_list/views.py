from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
# from show_list.models import do_list
from show_list import models
import datetime
import random
import time
# Create your views here.
def delete(request,pid = None):
    ###刪除事項
    if pid:
        try:
            item = models.do_list.objects.get(id=pid)
        except:
            item = None
        if item:
            item.delete()

    items = models.do_list.objects.all().order_by('deadline')
    # items = models.do_list.objects.get(id=17)
    return render(request,"show_list/index.html",locals())

def update(request,item_id):
    # time.sleep(5)
    if request.method == 'POST':
        item = get_object_or_404(models.do_list, pk=item_id)
        # item = models.do_list.objects.get(id=item_id)
        item.title = request.POST.get(f'title')
        item.description = request.POST.get(f'message')
        # item.description = f'海豐海鮮餐廳海景廳午宴{random.randint(1, 100)}'
        item.save()
        items = models.do_list.objects.all().order_by('deadline')
        return JsonResponse({'title': item.title, 'description': item.description})


    
    # return render(request,"show_list/index.html",locals())
    # return JsonResponse({'error': 'Invalid request'}, status=400)



def first(request):
    # return HttpResponse("第一個Django專案")
    # aaa = 1

    try:
        if request.POST['add'] == "新增":
            add_title = request.POST['title']
            add_date = request.POST['date']
            add_date = add_date.replace("/","-")
            add_message = request.POST['description']
            if add_title != None and add_date != None and add_message != None:
                add_todolist = models.do_list.objects.create(title = add_title,description=add_message,deadline=add_date)
                add_todolist.save()
                note = "新增成功"
    except:
        aaa = 3

    items = models.do_list.objects.all().order_by('deadline')
    # items = models.do_list.objects.get(id=17)
    return render(request,"show_list/index.html",locals())


