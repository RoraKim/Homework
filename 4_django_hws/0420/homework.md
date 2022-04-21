# HomeWork
### RESTful API

아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.

  True 

- HTTP Method는 GET과 POST 두 종류 뿐이다.

  False

- ‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.

  False

```p
1. 지원 행위에 대한 내용은 HTTP Method 로 나타낸다 

   -> https://www.fifa.com/wordcup/teams/team/43822/

2. 계층 관계를 명확히 해야한다.
-> https://www.fifa.com/wordcup/teams/43822/
```



### status code

다음의 HTTP status code의 의미를 간략하게 작성하시오.

- 200 - 성공
- 400 - 잘못된 요청
- 401 - 인증 안됨
- 403 - 권한 없음
- 404 - 페이지 없음
- 500 - 서버 에러
- 405 - 허용되지 않음 네서드 
- 201 - 생성됨
- 204 - 응답한 정보 없음



### ModelSerializer

아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class student(models.model):
    name = models.TextField()
    age = models.CharField(max_length=20)
    address = models.TextField()
```

```python
from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```



### Django REST Fraomework

Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.



시리얼라이저는 쿼리 세트와 모델 인스턴스와 같은 복잡한 데이터를 네이티브 파이썬 데이터 형으로 변환하여JSON, XML 또는 기타 콘텐츠 유형으로 쉽게 렌더링 할 수 있게 한다. 직렬화기는 또한 들어오는 데이터의 유효성을 먼저 확인한 후 파싱된 데이터를 복잡한 형식으로 다시 변환할 수 있도록 역직렬화를 제공한다. 

