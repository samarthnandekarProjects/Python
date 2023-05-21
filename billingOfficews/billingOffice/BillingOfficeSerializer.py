from rest_framework import serializers  
from billingOffice.models import BillingOffice
  
class BillingOfficeSerializer(serializers.ModelSerializer):
  
    class Meta:  
        model = BillingOffice
        fields = ('__all__')  