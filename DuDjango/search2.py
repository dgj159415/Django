# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse



# 接收POST请求数据
from web.models import UserInfo
def search_post(request):
    ctx={}
    response = UserInfo.objects.get(id=1)
    ctx['a'] ='您搜索的姓名为：'+response.username
    return HttpResponse(ctx)
