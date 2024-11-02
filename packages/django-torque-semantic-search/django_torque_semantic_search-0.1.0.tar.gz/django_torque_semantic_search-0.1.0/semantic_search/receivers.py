from django.conf import settings
from django.db import transaction
from django.db.models import ExpressionWrapper, F, FloatField, Q, Sum, Value, Window
from django.db.models.functions import DenseRank
from django.dispatch import receiver
from pgvector.django import CosineDistance
import orjson

from torque import models as torque_models
from torque.signals import search_filter, search_index_rebuilt, update_cache_document

from semantic_search.llm import llm
from semantic_search.models import SemanticSearchCacheDocument
from semantic_search.utils import build_semantic_summary


@receiver(update_cache_document)
def update_semantic_cache_document(sender, **kwargs):
    cache_document = kwargs["cache_document"]
    filtered_data = kwargs["filtered_data"]
    document_dict = kwargs["document_dict"]

    with transaction.atomic():
        SemanticSearchCacheDocument.objects.filter(
            search_cache_document=cache_document
        ).delete()

        semantic_summary = build_semantic_summary(document_dict, filtered_data)

        embeddings = llm.get_embeddings(semantic_summary)

        semantic_search_cache_documents = [
            SemanticSearchCacheDocument(
                search_cache_document=cache_document,
                data=semantic_summary,
                data_embedding=embedding,
            )
            for embedding in embeddings
        ]

        SemanticSearchCacheDocument.objects.bulk_create(semantic_search_cache_documents)


@receiver(search_index_rebuilt)
def rebuild_semantic_search_index(sender, **kwargs):
    wiki_config = kwargs["wiki_config"]

    with transaction.atomic():
        semantic_sc_documents = []

        for scd in torque_models.SearchCacheDocument.objects.filter(
            wiki_config=wiki_config
        ):
            document_dict = orjson.loads(
                torque_models.DocumentDictCache.objects.get(
                    document=scd.document, wiki_config=wiki_config
                ).dictionary
            )["fields"]
            semantic_summary = build_semantic_summary(document_dict, scd.filtered_data)
            embeddings = llm.get_embeddings(semantic_summary)

            for embedding in embeddings:
                semantic_sc_documents.append(
                    SemanticSearchCacheDocument(
                        search_cache_document=scd,
                        data_embedding=embedding,
                        data=semantic_summary,
                    )
                )

        SemanticSearchCacheDocument.objects.bulk_create(semantic_sc_documents)


@receiver(search_filter)
def semantic_filter(sender, **kwargs):
    similarity = getattr(settings, "SEMANTIC_SEARCH_SIMILARITY", 0.7)

    cache_documents = kwargs["cache_documents"]
    qs = kwargs.get("qs")

    if qs:
        embeddings = llm.get_embeddings(qs, prompt_name="query")

        distances = {
            f"distance_{i}": CosineDistance(
                "semantic_documents__data_embedding", embedding
            )
            for i, embedding in enumerate(embeddings)
        }

        filter_q = Q()
        for i in range(len(embeddings)):
            filter_q |= Q(**{f"distance_{i}__lte": similarity})

        results = (
            cache_documents.annotate(**distances)
            .filter(filter_q)
            .order_by("distance_0")  # sorted by the first query's distance
        )

        return results
