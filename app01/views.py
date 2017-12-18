from django.shortcuts import render, redirect
from utils.pager import Pagination

HOST_LIST = []
for i in range(1, 1904):
    HOST_LIST.append("c%s.com" % i)


def hosts(request):
    pager_obj = Pagination(request.GET.get('page', 1), len(HOST_LIST), request.path_info, request.GET)
    host_list = HOST_LIST[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    list_condition = request.GET.urlencode()
    print(list_condition)
    from django.http import QueryDict
    params = QueryDict(mutable=True)
    params['_list_filter'] = request.GET.urlencode()
    list_condition = params.urlencode()
    print(params)
    print(list_condition)
    return render(request, 'hosts.html', {'list_condition': list_condition, 'host_list': host_list, "page_html": html})


USER_LIST = []
for i in range(1, 1040):
    USER_LIST.append("bb%s" % i)


def users(request):
    pager_obj = Pagination(request.GET.get('page', 1), len(USER_LIST), request.path_info)
    users_list = USER_LIST[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render(request, 'users.html', {'host_list': users_list, "page_html": html})


# def get_page(request):
#     try:
#        current_page=int(request.GET.get("page"))
#     except Exception as e:
#         current_page=1
#     per_page_count=10
#     start=(current_page-1)*per_page_count
#     end=current_page*per_page_count
#     host_list=HOST_LIST[start:end]
#     total_count=len(HOST_LIST)
#     max_page_num,div=divmod(total_count,per_page_count)
#     if div:
#         max_page_num+=1
#     # half_mager
#     max_pager_count=11
#     page_html_list=[]
#     for i in range(1,max_page_num+1):
#         if current_page==i:
#             temp='<a class="active" href="/hosts/?page=%s">%s</a>'%(i,i)
#         else:
#             temp = '<a  href="/hosts/?page=%s">%s</a>' % (i, i)
#         page_html_list.append(temp)
#     page_html=''.join(page_html_list)
#     return   render(request,'hosts.html',{'host_list':host_list,'page_html':page_html})
def edit(request,pk):
    if request.method == 'GET':
        return render(request, 'edit.html')
    elif request.method == "POST":
        # print(request.POST)
        url='/hosts/?%s'%(request.GET.get("_list_filter"))
        print(url)
        return redirect(url)

