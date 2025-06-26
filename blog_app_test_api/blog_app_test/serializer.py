from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Article
        fields = ['id', 'title', 'publish_date', 'category_name']




class RegisterSerializer(serializers.ModelSerializer):
    """
    Used only for user signup.
    Includes the extra fields your CustomUserManager expects: name, mobile_number.
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model  = User
        fields = [
            'username',
            'email',
            'password',
            'name',
            'mobile_number',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Explicitly pass all required fields to `create_user()` so the custom
        manager doesn’t complain about missing arguments.
        """
        return User.objects.create_user(
            username       = validated_data['username'],
            email          = validated_data['email'],
            password       = validated_data['password'],
            name           = validated_data['name'],
            mobile_number  = validated_data['mobile_number'],
        )


class UserSerializer(serializers.ModelSerializer):
    """
    Used for profile view/update.
    Includes `name` and `mobile_number` so the client can read & modify them.
    """
    class Meta:
        model  = User
        fields = [
            'id',
            'username',
            'email',
            'name',
            'mobile_number',
        ]
        read_only_fields = ['id', 'username', 'email']  # email & username immutable
