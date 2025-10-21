from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import QuerySet, F
from django_filters import rest_framework as filters

from posts.models import Post, Comment


class PostFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name="owner__username")
    search = filters.CharFilter(method="search_filter", label="Search")
    created_lt = filters.DateTimeFilter(field_name="created_at", lookup_expr="lt")
    created_gt = filters.DateTimeFilter(field_name="created_at", lookup_expr="gt")

    class Meta:
        model = Post
        fields = ["owner", "search", "created_lt", "created_gt"]

    @staticmethod
    def search_filter(queryset: QuerySet[Post], name: str, value: str):
        """
        Полнотекстовый поиск для postgres
        """
        value = value.strip()
        if not value:
            return queryset

        if len(value) < 3:
            similar = TrigramSimilarity("title", value) + TrigramSimilarity("content", value)
            return (
                queryset.annotate(similarity=similar)
                .filter(similarity__gt=0.3)
                .order_by("-similarity", "-created_at")
            )

        # полнотекстовый поиск
        vector = SearchVector("title", weight="A", config="russian") + SearchVector(
            "content", weight="B", config="russian"
        )
        query = SearchQuery(value, config="russian", search_type="websearch")

        queryset = (
            queryset.annotate(vector=vector, rank=SearchRank(F("vector"), query))
            .filter(vector=query, rank__gte=0.3)
            .order_by("-rank", "-created_at")
        )
        print(queryset.query)
        return queryset


class CommentFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name="owner__username")
    text = filters.CharFilter(lookup_expr="icontains")
    created_lt = filters.DateTimeFilter(field_name="created_at", lookup_expr="lt")
    created_gt = filters.DateTimeFilter(field_name="created_at", lookup_expr="gt")

    class Meta:
        model = Comment
        fields = ["text", "post", "owner", "created_lt", "created_gt"]
