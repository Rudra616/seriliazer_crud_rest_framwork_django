from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.models import Person  # Ensure correct capitalization
from app.serilizers import Peopleserializer

# @api_view(['GET','POST'])
# def index(request):
#     course ={
#         "course_name":"python",
#         "learns": ['flask','django','fastapi'],
#     }   
#     if request.method == 'GET':
#         print("you hit in get method")
#         return Response(course)
#     elif request.method =='POST':
#         data =request.data
#         print(data)
#         print("you hit in post methodd")
#         return Response(course)

@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def person_view(request):
    if request.method == 'GET':
            obj = Person.objects.all()
            serializer = Peopleserializer(obj, many=True)
            return Response(serializer.data)
        
    
    elif request.method == 'POST':
        data = request.data
        serializer = Peopleserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = Peopleserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id =data['id'])

        serializer = Peopleserializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': "person delete"})
