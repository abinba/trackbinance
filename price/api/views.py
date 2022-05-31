from rest_framework import viewsets

from price.api.serializers import PriceSerializer
from price.models import Price


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """

    serializer_class = PriceSerializer

    def get_queryset(self):
        symbol = self.request.query_params.get("symbol")
        return Price.objects.filter(symbol__name=symbol).order_by("-created_at")
        # may be added later in the future: .select_related("symbol")
