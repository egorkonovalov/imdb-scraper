"""Offline WSGI checks for the image endpoint and its /imdb alias."""
import json
from io import BytesIO
from urllib.parse import urlencode
from wsgiref.util import setup_testing_defaults

import bottle
import pytest

import routes
from imdb import fetch


def get(path, **params):
    environ = {}
    setup_testing_defaults(environ)
    environ.update(PATH_INFO=path, QUERY_STRING=urlencode(params),
                   **{"wsgi.input": BytesIO()})
    response = {}

    def start_response(status, headers, exc_info=None):
        response.update(status=int(status.split()[0]), headers=dict(headers))

    body = b"".join(bottle.default_app()(environ, start_response))
    assert response["headers"]["Content-Type"].startswith("application/json")
    return response["status"], json.loads(body)


@pytest.mark.parametrize("path", ["/title/images", "/imdb/title/images"])
def test_images_route(monkeypatch, path):
    def fake_graphql(query, variables, country="US"):
        assert variables == {"id": "tt0111161", "first": 50, "after": "CURSOR+/="}
        assert country == "DK"
        return {"title": {"id": "tt0111161", "titleText": {"text": "A film"},
                          "images": {"total": 0, "edges": []}}}

    monkeypatch.setattr(fetch, "fetch_graphql", fake_graphql)
    status, body = get(path, title_id="https://www.imdb.com/title/tt0111161/",
                       cursor="CURSOR+/=", country="dk")
    assert status == 200
    assert body["count"] == 0
    assert body["results"] == []
    assert body["country"] == "DK"
    assert body["pagination"] == {"total": 0, "has_more": False, "next_cursor": None}


@pytest.mark.parametrize("params", [{}, {"title_id": " "}, {"title_id": "bad"},
                                    {"title_id": "tt0111161", "country": "USA"}])
def test_images_bad_parameters(monkeypatch, params):
    def unexpected_fetch(*args, **kwargs):
        pytest.fail("Invalid input must not reach IMDb")

    monkeypatch.setattr(fetch, "fetch_graphql", unexpected_fetch)
    status, body = get("/title/images", **params)
    assert status == 400
    assert body["error"]


@pytest.mark.parametrize("error,status", [(fetch.ImdbNotFound("missing"), 404),
                                         (fetch.ImdbBadRequest("bad cursor"), 400),
                                         (fetch.ImdbUpstreamError("unavailable"), 500)])
def test_images_errors(monkeypatch, error, status):
    def failing_fetch(*args, **kwargs):
        raise error

    monkeypatch.setattr(fetch, "fetch_graphql", failing_fetch)
    actual_status, body = get("/title/images", title_id="tt0111161")
    assert actual_status == status
    assert body["error"]


def test_health_lists_images():
    status, body = get("/health")
    assert status == 200
    assert "/title/images" in body["endpoints"]
