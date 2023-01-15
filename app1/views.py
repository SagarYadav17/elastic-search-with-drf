from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend
from elasticsearch.exceptions import NotFoundError

from app1.documents import CityDocument
from app1.serializers import CityDocumentSerializer
from rest_framework.exceptions import NotFound


class CityDocumentView(BaseDocumentViewSet):
    document = CityDocument
    serializer_class = CityDocumentSerializer

    filter_backends = [CompoundSearchFilterBackend]

    # Define search fields
    search_fields = {
        'name': {'fuzziness': 'AUTO'},
    }

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except NotFoundError:
            raise NotFound(f"{self.index} index not found")
