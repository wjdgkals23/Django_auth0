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
        