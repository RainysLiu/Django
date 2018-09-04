from BlogProject import settings
from myblog.models import *

def global_setting(request):
    BLOG_NAME = settings.BLOG_NAME  # 读取项目配置文件中的BLOG_NAME对应的变量值
    BLOG_DESC = settings.BLOG_DESC  # 读取项目配置文件中的BLOG_DESC对应的变量值
    category_list = Category.objects.all()
    articles_orderby_click = Article.objects.order_by('-click_count')[:6]
    def GetArticles_orderby_comment():
        articles = Article.objects.all()
        commentnumber_artcile_dic={}
        for article in articles:
            commentnumber_artcile_dic[article] = article.comment_set.all().count()
        sorted_commentnumber_artcile_dic=sorted(commentnumber_artcile_dic.items(), key=lambda d:d[1],reverse=True)
        articles_orderby_comment=[]
        for items in sorted_commentnumber_artcile_dic:
            articles_orderby_comment.append(items[0])
        articles_orderby_comment=articles_orderby_comment[:6]
        return articles_orderby_comment
    articles_orderby_comment = GetArticles_orderby_comment()
    return locals()




