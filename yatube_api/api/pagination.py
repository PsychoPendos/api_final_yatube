from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        limit = self.request.GET.get('limit')
        offset = self.request.GET.get('offset')
        if not (limit and offset):
            return Response(data)
        return Response({
            'links': {},
            'count': self.page.paginator.count,
            'response': data
        })
