
import imp
from django.shortcuts import render
#models의 어떤 내용을 필요로 하는지 모르니 일단 다 받아오자 
#현재 폴더의 models로부터 article을 받아오라느뜻
from . models import Article
from . forms.articles.comment import commentForm


# Create your views here.

def index(request):

    '''
    모든 게시글 정보 조회
    ORM
    Model.manager.query API
    '''

    articles = Article.objects.all() #반환 받아온 값 쓰기 
    context = {
        'articles' : articles
        
        }

    #print(dir(request))
    #print(request)
    #render의 두번째 인자에 적히는 건 파일 경로 
    #원래는 그냥 index.html이라고 적었겠지만, 같은 이름의 경로들을 방지하기 위해 
    #templates폴더 안에 articles폴더 안의 index.html을 반환
    return render(request, 'articles/index.html')

    
def new(request):
    return render(request, 'articles/new.html')