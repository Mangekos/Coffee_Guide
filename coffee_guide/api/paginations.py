from rest_framework.pagination import PageNumberPagination


class CafePagination(PageNumberPagination):
    page_size = 6
