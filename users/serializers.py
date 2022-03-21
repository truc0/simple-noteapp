from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers

from notes.models import Note


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'notes')


# add a serializer for documentation
class LogoutSerializer(serializers.Serializer):
    ...


class RegisterSerializer(serializers.Serializer):
    """
    Register serializer that provides password validation and 
    """
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def validate(self, data):
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already token')
        return super().validate(data)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    """
    ChangePassword serializer provides validation of old password
    """

    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)

    def _get_user(self, *args, **kwargs):
        user = self.context.get('user', None)
        if user:
            return user
        else:
            raise serializers.ValidationError('A user should be provided as context for changing password')

    def validate_old_password(self, value):
        """
        Make sure user is logged in and old_password is correct
        """
        user = self._get_user()
        if not user.check_password(value):
            raise serializers.ValidationError('The old password is incorrect')

    def save(self):
        """
        Override the save method to save password
        """
        user = self._get_user()
        user.set_password(self.validated_data['new_password'])
