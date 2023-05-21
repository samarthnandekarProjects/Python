from django.shortcuts import render,get_object_or_404    
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from billingOffice.models import BillingOffice
from billingOffice.BillingOfficeSerializer import BillingOfficeSerializer
# Create your views here.  
  
class BillingOfficeView(APIView):
  
    def get(self, request, id=None):  
        if id:  
            result = BillingOffice.objects.get(id=id)
            serializers = BillingOfficeSerializer(result)
            return Response({'success': 'success', "billingOffice":serializers.data}, status=200)
  
        result = BillingOffice.objects.all()
        serializers = BillingOfficeSerializer(result, many=True)
        return Response({'status': 'success', "billingOffice":serializers.data}, status=200)
  
    def post(self, request):  
        serializer = BillingOfficeSerializer(data=request.data)
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

    def put(self, request,id):
        result = BillingOffice.objects.get(id=id)
        serializer = BillingOfficeSerializer(result, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):  
        result = BillingOffice.objects.get(id=id)
        serializer = BillingOfficeSerializer(result, data = request.data, partial=True)
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):  
        result = get_object_or_404(BillingOffice, id=id)
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})