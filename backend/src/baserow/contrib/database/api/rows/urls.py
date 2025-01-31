from django.urls import re_path

from .views import (
    BatchDeleteRowsView,
    BatchRowsView,
    RowAdjacentView,
    RowMoveView,
    RowNamesView,
    RowsView,
    RowView,
)

app_name = "baserow.contrib.database.api.rows"

urlpatterns = [
    re_path(r"table/(?P<table_id>[a-z0-9_]+)/$", RowsView.as_view(), name="list"),
    re_path(
        r"table/(?P<table_id>[a-z0-9_]+)/(?P<row_id>[0-9]+)/$",
        RowView.as_view(),
        name="item",
    ),
    re_path(
        r"table/(?P<table_id>[a-z0-9_]+)/(?P<row_id>[0-9]+)/adjacent/$",
        RowAdjacentView.as_view(),
        name="adjacent",
    ),
    re_path(
        r"table/(?P<table_id>[a-z0-9_]+)/batch/$",
        BatchRowsView.as_view(),
        name="batch",
    ),
    re_path(
        r"table/(?P<table_id>[a-z0-9_]+)/batch-delete/$",
        BatchDeleteRowsView.as_view(),
        name="batch-delete",
    ),
    re_path(
        r"table/(?P<table_id>[a-z0-9_]+)/(?P<row_id>[0-9]+)/move/$",
        RowMoveView.as_view(),
        name="move",
    ),
    re_path(
        r"names/$",
        RowNamesView.as_view(),
        name="names",
    ),
]
