from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from app1.documents import CityDocument


class CityDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CityDocument
        fields = "__all__"
