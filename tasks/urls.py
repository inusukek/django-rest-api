"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskList),
    path('tasks/<int:id>', views.TaskDetail),

    # path('api/tasks', views.TaskDetail.as_view()),  #Show all data
    # path('api/tasks/<int:pk>', views.TaskDetail.as_view()),  #Edit/Update/Delete Data with id
    # path('api-auth/', include('rest_framework.urls'))
]
urlpatterns = format_suffix_patterns(urlpatterns)

#หลักการทำงาน

# HTTP requests will be matched by Url Patterns and passed to the Views
#เมื่อมีการ Http request จะทำงานตาม Path ที่กำหนดไว้ และ ส่งการทำงานต่อไปที่ Views  

# Views processes the HTTP requests and returns HTTP responses (with the help of Serializer)
#ตัว View จะทำรับข้อมูล และ ส่งตอบกลับข้อมูล โดยอาศัย Seializer(ประมวลผลข้อมูล) 

# Serializer serializes/deserializes data model objects
# Serializer ทำการแปลงรูปแบบข้อมูลระหว่าง Dict(ข้อมูลรูปแบบภาษา python) เป็น JSON เพื่อส่งต่อไป Model(ติดต่อ Database)/ส่ง Response กลับ 

# Models contains essential fields and behaviors for CRUD Operations with Database
# Models ทำหน้าที่จัดเรียงข้อมูลให้ตรงกับ field Database และทำการแก้ไข/ดึงข้อมูลจาก Database อาศัยการทำงาน CRUD Operations

#CRUD stands for Create, Read, Update & Delete. 
# These are the four basic operations which are executed on Database Models. 
# We are developing a web app which is capable of performing these operations.