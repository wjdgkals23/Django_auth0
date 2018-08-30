from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    # post로 넘어오는 모든 주소를 잡는다.
    # ?P<pk> 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻
    # /d+ 숫자가 여러 개 붙을 수 있다는 표
    # /$ 마지막에 /가 오고 마무리한다는 뜻
]