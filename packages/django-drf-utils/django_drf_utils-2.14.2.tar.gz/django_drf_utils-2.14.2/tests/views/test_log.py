import logging
import os
from unittest import mock
from unittest.mock import MagicMock

from django.conf import ENVIRONMENT_VARIABLE
from django.test import RequestFactory
from rest_framework import status

from django_drf_utils.views import LogView


class TestWithAuth:
    def test_log_ok(self):
        os.environ[ENVIRONMENT_VARIABLE] = "blurb"
        username = "chucknorris"
        mock_user = MagicMock(is_authenticated=True, username=username)
        request = RequestFactory().get("/")
        request.data = {
            "message": "404 Page not found",
            "level": "error",
            "stack": "frontend",
        }
        request.user = mock_user
        view = LogView()
        view.setup(request)

        with mock.patch("django_drf_utils.views.log.logger.log") as log:
            response = view.create(request)
            assert response.status_code == status.HTTP_200_OK
            assert response.data == {"detail": "ok"}
            log.assert_called_once()
            assert log.call_args.args == (logging.ERROR, request.data["message"])
