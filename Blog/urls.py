from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from rest_framework.generics import CreateAPIView
from Blogapp.views import DelatePost
from Blogapp.views import CreatePost,anPost,PostList,PostViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


doc_view = get_schema_view(
    openapi.Info(
        title = "Blog",
        default_version = "v1",
        description="( REST API) Clone of Blog using Django Rest Framework",
        contact = openapi.Contact("Izzatillo Olimjonov <olimjonovizzatillo1999@gmail.com>"),

    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register('post1',PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path("post/", PostList.as_view()),
    path("poct/<int:pk>", anPost.as_view()),
    path('posts/', CreatePost.as_view()),
    path('udalit/<int:pk>',DelatePost.as_view()),
    path('doc/',doc_view.with_ui("swagger", cache_timeout=0), name="swagger_doc"),
    path('redoc/',doc_view.with_ui("redoc", cache_timeout=0), name="redoc_doc"),
]