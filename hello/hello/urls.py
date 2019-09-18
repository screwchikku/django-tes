"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from polls.models import Fruits
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static

# Serializers define the API representation.
class FruitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruits
        fields = ['name', 'image', 'price']

# ViewSets define the view behavior.
class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'fruits', FruitViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('admin/',admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)