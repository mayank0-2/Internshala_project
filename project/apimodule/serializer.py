from rest_framework import serializers
from . models import apiModel
from django.contrib.auth.models import User

class model_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = apiModel
        fields = '__all__'
        
        
class UserRegistrationSerializer(serializers.Serializer):
    choices = ['admin', 'employee']
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices)
    

    
    def create(self, validated_data) :
        role = validated_data['role']
        pas = validated_data['password']
        temp = User.objects.create(
            username = validated_data['username'],
            is_superuser= True if role == 'admin' else False
        )
        temp.set_password(pas)
        temp.save()
        return temp