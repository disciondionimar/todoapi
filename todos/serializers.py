
# third-party imports
from rest_framework.serializers import ModelSerializer


# local imports
from todos.models import Todo


class TodoSerializer(ModelSerializer):

    class Meta():
        model = Todo
        fields = ('id', 'title', 'description', 'is_complete')