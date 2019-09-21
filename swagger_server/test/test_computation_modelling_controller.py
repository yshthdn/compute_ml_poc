# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.compute_forecast_response import ComputeForecastResponse  # noqa: E501
from swagger_server.models.config import Config  # noqa: E501
from swagger_server.test import BaseTestCase


class TestComputationModellingController(BaseTestCase):
    """ComputationModellingController integration test stubs"""

    def test_compute_forecast_post(self):
        """Test case for compute_forecast_post

        
        """
        body = Config()
        response = self.client.open(
            '/v1/compute_forecast',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_compute_forecast_put(self):
        """Test case for compute_forecast_put

        
        """
        body = Config()
        response = self.client.open(
            '/v1/compute_forecast',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
