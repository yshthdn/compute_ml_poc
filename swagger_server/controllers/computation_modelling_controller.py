import connexion
import six
import json

from swagger_server.models.compute_forecast_response import ComputeForecastResponse  # noqa: E501
from swagger_server.models.config import Config  # noqa: E501
from swagger_server import util


def compute_forecast_post(body):  # noqa: E501
    """

     # noqa: E501

    :param body: Computation config needs to be added
    :type body: dict | bytes

    :rtype: ComputeForecastResponse
    """
    if connexion.request.is_json:
        body = Config.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    # import ipdb;ipdb.set_trace()
    cfr = ComputeForecastResponse.from_dict(connexion.request.get_json()).attribute_map
    # return json.dumps(cfr)
    return cfr



def compute_forecast_put(body):  # noqa: E501
    """

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: ComputeForecastResponse
    """
    if connexion.request.is_json:
        body = Config.from_dict(connexion.request.get_json())  # noqa: E501
    return body
