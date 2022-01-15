가상환경 진입 후 진행하기

- 장고 설치

```python
pip install django===3.1.3
```

- pip upgrade warning

```python
python -m pip install --upgrade pip
```

- 프로젝트 생성하기

```python
# .은 현재 디렉토리를 의미
django-admin startproject config . 
```

- 웹 사이트 구동하기

```
python manage.py runserver
```

- 앱 생성하기

```python
django-admin startapp "앱이름"
```

- 앱이 필요로 하는 테이블 생성하기

```
python manage.py migrate
```

- 모델이 신규로 생성되거나 변경되면 makemigrations 명령을 수행 후 migrate명령을 수행해야 함

```
python manage.py makemigrations
```

- 슈퍼유저 생성

```
python manage.py createsuperuser
```



### Model 예시

- 생성

```python
from pybo.models import Question, Answer
from django.utils import timezone

q = Question(subject='pybo가 무엇인가요?', content = 'pybo에 대해 알고 싶습니다', create_date=timezone.now())
q.save()
```

- 조회

```python
Question.objects.all() # 모든 Question 데이터를 조회
Question.objects.filter(id=1) # 조건에 해당하는 데이터 모두 리턴
Question.objects.get(id=1) # 한건만 리턴
Question.objects.filter(subject__contains='장고') # subject에 장고가 포함된 데이터만 조회 
```

- 수정

```python
q = Question.objects.get(id=2)
q.subject = 'Django Model Question'
q.save()
```

- 삭제

```python
q = Question.objects.get(id=1)
q.delete()
```



### 정리

- config/urls.py은 앱이 아닌 프로젝트 성격의 파일이므로 이곳에는 프로젝트 성격의 URL 매핑만 추가되어야 한다.
- 앱을 INSTALLED_APPS 항목에 추가하지 않으면 DB 관련 작업을 할 수 없다.
- makemigrations, migrate
  - 명령은 장고가 테이블 작업을 수행하기 위한 작업파일을 생성하는 명령어로  모델을 생성하거나 변화가 있을 경우 실행 -> 실제 테이블 생성은 migrate 명령을 통해서만 가능
  - 모델의 메서드가 추가될 경우에는 수행할 필요 없으며 모델의 속성이 변경되었을 때만 사용
- 