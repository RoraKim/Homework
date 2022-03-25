# HomeWork
### MTV

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의
약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는
역할을 간략히 서술하시오.

- model(데이터 베이스를 관리) - model 
  - 어플리케이션의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리(조회, 생성, 수정, 삭제)
- template(인터페이스, 화면) - View
  - 파일의 구조나 레이아웃을 정의 
  - 실제 사용자에게 보여줄 화면
- View(중심 컨트롤러) - controller
  - HTTP 요청을 수신, HTTP 응답을 반환
  - Model을 통해서 사용자의 요청을 충족시키는 데이터에 접근
  - 템플릿에 응답의 서식 설정을 맡김



### URL

__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
의미한다. __(a)__는 무엇인지 작성하시오.

- variable routing

  

### Django template path

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다.
__(a)__에 들어갈 폴더 이름을 작성하시오.

- templates