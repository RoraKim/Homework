# HomeWork
### Model 반영하기

`Django가 Model에 생긴 변화를 DB에 반영하는 방법` 을 뜻하는 용어를 작성하시오.

- migrate

### Model 변경사항 저장하기

```bash
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

1. 위에서 작성한 Model의 설계도를 저장하기 위한 명령어를 작성하시오.

```bash
#model의 변경사항으로 설계도를 만드는 명령어 
$ python manage.py makemigrations

#만들어진 설계도를 바탕으로 db에 반영 
$ python manage.py migrate {app_name} {migration_number}
```



1. 이로 인해 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과를 작성하시오. (app의 이름은 articles이다.)

```bash
$ python manage.py sqlmigrate articles(app_name) 0001
>>> CREATE TABLE "articles_article" ("id" intetger NOT NULL PRIMARY KEY AUTOINCREMENT
"title" varchar(10) NOT NULL, "content" text NOT NULL);
```



  

### Python Shell

Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때,
어떤 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.

```bash
$ python manage.py shell #기본 shell
$ python manage.py shell_plus #django-extensions 설치 후, settings.py에 django_extensions 설정
```



### Django Model Field

Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

```bash
from django.db import models

models.CharField
models.TextField
models.DateTimeField
models.IntergerField
models.fileField
```

