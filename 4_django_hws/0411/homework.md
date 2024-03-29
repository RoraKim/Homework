# HomeWork
### Django User Model

- Django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다.

  ```python
  from django.contrib.auth.models import User
  ```

-  아래의 Django 공식 github에서 User 모델이 정의된 코드를 찾아 작성하시오.
  https://github.com/django/django

```python
어느 폴더 어느 파일의 어느 메서드인지

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
```

![image-20220412091432573](homework.assets/image-20220412091432573.png)



### Create user by ModelForm

새 유저를 생성하는 Django 내부에 정의된 ModelForm을 사용하기 위한 import 구문을 작성하시오.

```python
from django.contrib.auth.forms import usercreationForm
```



### Django sessions

Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다.
그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다.
(a)와 (b)에 알맞은 값을 작성하시오.

a : django_session

b : sessionid



