from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
from .serializers import SongSerializer
from .models import Song
import ipdb


class CustomSongPagination(PageNumberPagination):
    page_size = 1


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomSongPagination

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer: Song):
        return serializer.save(album_id=self.kwargs["pk"])
