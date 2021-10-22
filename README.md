# ★우정퀴즈★

한국외대 AI융합전공 소프트웨어 공학 11조

## 📲 설치

### 1. 프로젝트 파일 다운받기(git clone 혹은 그냥 다운로드)

터미널(명령 프롬프트)키시고 하시면 댑니다

```shell
# 프로젝트를 다운받을 해당 디렉토리로 이동한 후
cd 특정디렉토리
git clone https://github.com/MaxKim-J/friendship-quiz
```

### 2. pip, python 버전 확인 => 최신으로 업데이트

```shell
python3 -m pip install --upgrade pip
```

### 3. Django(2.0.0대 버전) 전역으로 설치

```shell
pip install django~=2.0.0
```

가상환경 키기 전에 전역으로 설치해야 합니다

### 4. 가상환경 생성, 실행

```shell
# 윈도우
C:\Python35\python -m venv myvenv # 생성
myvenv\Scripts\activate # 실행

# 맥 OS
python3 -m venv myvenv # 생성
source myvenv/bin/activate # 실행
```

해당 프로젝트 디렉토리로 이동한 후 위 명령어를 실행해야 합니다  
[가상환경이란?](https://velog.io/@hanmin_ss/Django-01.-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD%EA%B3%BC-%EC%9E%A5%EA%B3%A0%EC%84%A4%EC%B9%98)  
가상환경이 성공적으로 실행되고 나면 명령 프롬프트 새로운 라인 첫 부분에 `(myvenv)` 이런 식으로 표시될 것입니다.

### 5. 의존성 설치

개발을 하는 모든 사람들이 같은 프로젝트의 같은 의존성, 같은 버전임을 명시할 수 있게 설치한 의존성의 목록은 requirement.txt에 기록됩니다. 아래 명령어를 실행시키면 requirement.txt에 있는 의존성이 가상환경에 깔립니다.

```shell
pip install -r requirements.txt
```

여기까지가 설치 과정인데 잘 안되시면 아래 링크들도 참조해 주세요

[Django :: 장고 설치하기, 가상 환경 설정 (윈도우, Window 10)](https://hongku.tistory.com/258)  
[[윈도우] 파이썬 가상환경 설치와 장고 프로젝트 생성](https://kis6473.tistory.com/49)  
[장고걸스 - 설치하기](https://tutorial.djangogirls.org/ko/installation/)

## ⚙️ 구동

설치를 끝내고 편리한 웹 개발을 위한 개발 서버를 구동하는 과정입니다.

### DB 마이그레이션

앱의 models.py에 맞는 데이터베이스 스키마를 만들어 DB를 생성합니다. DB를 몽땅 날리고 초기화할때도 사용합니다.

```shell
python manage.py migrate
```

### 웹 서버 시작하기

이거 입력하고 `http://127.0.0.1:8000/`에 웹사이트가 나오면 성공입니다. 그 다음에는 개발을 진행해주시면 되겠습니다.

```shell
python manage.py runserver
```
