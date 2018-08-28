#Django Auth0 Practice

***

### Reference link
- https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/

---

###Day 1 파이썬 가상환경 설정 및 장고(Django) 토이 프로젝트 셋팅

- 파이썬 가상환경 설정하기(mac os using homebrew)
    - 가상환경 tool 설치 및 설정
        - brew install pyenv
        - brew install pyenv-virtualenv
        
    - terminal setting(vi ~/.bash_proflie)
        - export PYENV_ROOT=/usr/local/Cellar/pyenv
        - if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
        - if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
    
    - 파이썬 설치
        - pyenv install version(3.7.0)
        - pyenv global 3.7.0 (설치버전을 주 사용 파이썬으로 설정)
        
    - 가상환경 생성
        - mkdir djangoprojects / mkdir tutorials (프로젝트 폴더 생성)
        - pyenv virtualenv 3.7.0 django_env(장고 관련 개발 가상 환경 생성)
        - cd djangoprojects/tutorials
        - pyenv local django_env
    
    - 장고환경 생성 및 프로젝트 실행 (가상환경 실행 상태)
        - pip3(pip) install django
        - django-admin startproject config
        - mv config app

***

- django 프로젝트 구조

***

- JWT 이해하기

    - 토큰 기반 인증 시스템
        - session 데이터를 이용하는 Stateful 서버의 반대개념
        - 상태를 저장하지 않고, 서버는 클라이언트측의 요청만을 처리한다 -> 서버확장성 증가
        - 작동 원리
            1. 로그인 처리
            2. 계정정보 검증
            3. 계정정보 일치 시 signed 토큰 발급
            4. 발급된 토큰은 클라이언트측에 저장되고, 서버요청시 함께 전달된다.
            5. 서버는 토큰을 검증하고, 요청에 응답
            
    - JWT 웹 표준 JSON 기반 토큰 인증 시스템
        - 특징
            1. 자가 수용적 (기본정보, 전달할 정보, 토큰 검증증명 sign)
            2. http를 통해 쉽게 전달 가능
        - 생김새
            - 헤더.내용.서명
            - 헤더 : 토큰타입, 해싱알고리즘 지정
            - 내용(정보)
                - registered : 토큰에 대한 정보를 담는 클레임
                - public : 충돌이 방지된 이름 ? 역할 의문??
                - private : 실제정보 -> 일반 객체 형태
            - 서명 : 헤더와 내용을 인코딩한 값을 합치 주어진 비밀키로 해쉬하여 생