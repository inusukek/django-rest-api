from asyncio.windows_events import NULL
from urllib import request
from django.http import JsonResponse
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, status

@api_view(['GET', 'POST'])
def TaskList(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse({'tasks': serializer.data})

    if request.method == 'POST':    
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#ส่งข้อมูลที่มากับbody/params แสดงผลข้อมูลที่ได้รับ


@api_view(['GET', 'PUT', 'DELETE'])
def TaskDetail(request, id, format=None):
    
    try:
        tasks = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #เรียกดู Task Detail where ตาม ID 
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)

    elif request.method == 'PUT': #อัพเดตข้อมูล where ตาม ID
        serializer = TaskSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': #ลบข้อมูลตาม where id หรือ ถ้าไม่มี id จะเป็นลบทั้งหมด
        tasks = Task.objects.get(pk=id)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        # try:
        #     print("Have ID")
        #     taks= Task.objects.get(id= 5)
        #     taks.delete()
        # except :
        #     taks= Task.objects.all()
            # taks.delete()

        # NoneType = type(None)
        # if type(id) == NoneType:
        #     print(id)
        # #     return Response(status=status.HTTP_204_NO_CONTENT)
        # elif type(id) != NoneType:
        #     print("null")
        # #     return Response(status=status.HTTP_204_NO_CONTENT)

#=====================================================================================================================================#

#ดึงข้อมูลทั้งหมด
#แปลงข้อมูลจาก dict เป็น JSON
#return JSON output

# ประกาศแบบ class
# ประกาศview เพื่อดึงข้อมูลจาก Serailzer
# class TaskList(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     # permission_classes = [permissions.IsAuthenticated] #สิทธิ์ในการเข้าถึงข้อมูล/login ในระบบ django

# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#=====================================================================================================================================#

