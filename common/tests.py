import json
from test.support import EnvironmentVarGuard

from django.test import RequestFactory
from rest_framework.reverse import reverse
from django.test import TestCase

ACTIONS = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create',
}

METHODS = {
    'retrieve':'get',
    'list': 'get',
    'update': 'put',
    'partial_update': 'patch',
    'destroy': 'delete',
    'create': 'post',
}


class RestApiRequestFactory(RequestFactory):

    def __init__(self, basename, **defaults):
        super().__init__(**defaults)
        self.basename = basename

    def get_path(self, path, pk, **kwargs):
        if path is None:
            path = "list" if pk is None else "detail"
        if pk is not None:
            kwargs["pk"] = pk
        return reverse(f"{self.basename}-{path}", kwargs=kwargs)

    def get(self, path=None, data=None, pk=None, kwargs=None, **extra):
        if data is None:
            data = {}
        if kwargs is None:
            kwargs = {}
        return super().get(self.get_path(path=path, pk=pk, **kwargs), data, **extra)

    def post(self, path=None, data=None, pk=None, kwargs=None, **extra):
        if data is None:
            data = {}
        if kwargs is None:
            kwargs = {}
        return super().post(self.get_path(path=path, pk=pk, **kwargs), data, **extra)

    def patch(self, path=None, data=None, pk=None, kwargs=None, **extra):
        if data is None:
            data = {}
        if kwargs is None:
            kwargs = {}
        return super().patch(self.get_path(path=path, pk=pk, **kwargs), data, **extra)

    def put(self, path=None, data=None, pk=None, kwargs=None, **extra):
        if data is None:
            data = {}
        if kwargs is None:
            kwargs = {}
        return super().put(self.get_path(path=path, pk=pk, **kwargs), data, **extra)

    def delete(self, path=None, pk=None, kwargs=None, data='', content_type='application/octet-stream',
               **extra):
        if kwargs is None:
            kwargs = {}
        return super().delete(self.get_path(path=path, pk=pk, **kwargs), data, **extra)


class RestApiTestCase(TestCase):
    basename = None
    viewset = None

    @classmethod
    def setUpMoko(cls):
        cls.env = EnvironmentVarGuard()
        cls.env['AWS_ACCESS_KEY_ID'] = 'testing'
        cls.env['AWS_SECRET_ACCESS_KEY'] = 'testing'
        cls.env['AWS_SECURITY_TOKEN'] = 'testing'
        cls.env['AWS_SESSION_TOKEN'] = 'testing'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.setUpMoko()

    def request_factory(self):
        return RestApiRequestFactory(basename=self.basename)

    def action_test(self,
                    action="list",
                    pk=None,
                    data=None,
                    kwargs=None,
                    path=None,
                    method=None,
                    factory_data=None,
                    **extra):

        if kwargs is None:
            kwargs = {}

        if data is not None:
            factory_data = json.dumps(data)
            extra["content_type"] = 'application/json'

        if method == "get" and data is not None:
            factory_data = data.items()

        if method is None:

            action = ACTIONS[method]

            if method == "get" and pk is None:
                action = "list"

            if path is not None:
                action = path

        factory = self.request_factory()
        request = getattr(factory, method)(pk=pk, data=factory_data, path=path, kwargs=kwargs, **extra)
        view = self.viewset.as_view({method: action})
        return view(request, pk=pk)
