from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from app1.models import City


@registry.register_document
class CityDocument(Document):
    class Index:
        name = 'city'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = City
        fields = ["id", "name", "state_code", "state_name", "country_code", "country_name"]
