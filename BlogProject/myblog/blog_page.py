from django.core.paginator import PageNotAnInteger, Paginator

# 通过页码返回相应的文章
def getblog_bypage(request,article_list):
    try:
        page_number = int(request.GET.get('page',''))  # 获取传递的页码参数
        paginator = Paginator(article_list,2)  # 实例化分页器对象
        page = paginator.page(page_number)  # 获取某一页的数据，以Page对象封装
    except:
        paginator = Paginator(article_list, 2)
        page = paginator.page(1)
    return page
