from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^checkName/',views.checkName),
    url(r'^login/',views.login,name='login'),
    url(r'^testmail/',views.testmail),
    url(r'^activeAccount/',views.activeAccount),
    url(r'^get_code/',views.get_code),
    url(r'^logout/',views.logout,name='logout')

]