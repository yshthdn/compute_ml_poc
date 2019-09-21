# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.prediction import Prediction  # noqa: F401,E501
from swagger_server import util


class ComputeForecastResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, job_id: int=None, mem_request: str=None, cpu_request: str=None, time_request: date=None, project_id: str=None, project_desc: str=None, project_phase: str=None, design_block_id: str=None, design_block_desc: str=None, tool_used: str=None, tool_cmd: str=None, predictions: List[Prediction]=None):  # noqa: E501
        """ComputeForecastResponse - a model defined in Swagger

        :param job_id: The job_id of this ComputeForecastResponse.  # noqa: E501
        :type job_id: int
        :param mem_request: The mem_request of this ComputeForecastResponse.  # noqa: E501
        :type mem_request: str
        :param cpu_request: The cpu_request of this ComputeForecastResponse.  # noqa: E501
        :type cpu_request: str
        :param time_request: The time_request of this ComputeForecastResponse.  # noqa: E501
        :type time_request: date
        :param project_id: The project_id of this ComputeForecastResponse.  # noqa: E501
        :type project_id: str
        :param project_desc: The project_desc of this ComputeForecastResponse.  # noqa: E501
        :type project_desc: str
        :param project_phase: The project_phase of this ComputeForecastResponse.  # noqa: E501
        :type project_phase: str
        :param design_block_id: The design_block_id of this ComputeForecastResponse.  # noqa: E501
        :type design_block_id: str
        :param design_block_desc: The design_block_desc of this ComputeForecastResponse.  # noqa: E501
        :type design_block_desc: str
        :param tool_used: The tool_used of this ComputeForecastResponse.  # noqa: E501
        :type tool_used: str
        :param tool_cmd: The tool_cmd of this ComputeForecastResponse.  # noqa: E501
        :type tool_cmd: str
        :param predictions: The predictions of this ComputeForecastResponse.  # noqa: E501
        :type predictions: List[Prediction]
        """
        self.swagger_types = {
            'job_id': int,
            'mem_request': str,
            'cpu_request': str,
            'time_request': date,
            'project_id': str,
            'project_desc': str,
            'project_phase': str,
            'design_block_id': str,
            'design_block_desc': str,
            'tool_used': str,
            'tool_cmd': str,
            'predictions': List[Prediction]
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'mem_request': 'mem_request',
            'cpu_request': 'cpu_request',
            'time_request': 'time_request',
            'project_id': 'project_id',
            'project_desc': 'project_desc',
            'project_phase': 'project_phase',
            'design_block_id': 'design_block_id',
            'design_block_desc': 'design_block_desc',
            'tool_used': 'tool_used',
            'tool_cmd': 'tool_cmd',
            'predictions': 'predictions'
        }

        self._job_id = job_id
        self._mem_request = mem_request
        self._cpu_request = cpu_request
        self._time_request = time_request
        self._project_id = project_id
        self._project_desc = project_desc
        self._project_phase = project_phase
        self._design_block_id = design_block_id
        self._design_block_desc = design_block_desc
        self._tool_used = tool_used
        self._tool_cmd = tool_cmd
        self._predictions = predictions

    @classmethod
    def from_dict(cls, dikt) -> 'ComputeForecastResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComputeForecastResponse of this ComputeForecastResponse.  # noqa: E501
        :rtype: ComputeForecastResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self) -> int:
        """Gets the job_id of this ComputeForecastResponse.


        :return: The job_id of this ComputeForecastResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: int):
        """Sets the job_id of this ComputeForecastResponse.


        :param job_id: The job_id of this ComputeForecastResponse.
        :type job_id: int
        """

        self._job_id = job_id

    @property
    def mem_request(self) -> str:
        """Gets the mem_request of this ComputeForecastResponse.


        :return: The mem_request of this ComputeForecastResponse.
        :rtype: str
        """
        return self._mem_request

    @mem_request.setter
    def mem_request(self, mem_request: str):
        """Sets the mem_request of this ComputeForecastResponse.


        :param mem_request: The mem_request of this ComputeForecastResponse.
        :type mem_request: str
        """

        self._mem_request = mem_request

    @property
    def cpu_request(self) -> str:
        """Gets the cpu_request of this ComputeForecastResponse.


        :return: The cpu_request of this ComputeForecastResponse.
        :rtype: str
        """
        return self._cpu_request

    @cpu_request.setter
    def cpu_request(self, cpu_request: str):
        """Sets the cpu_request of this ComputeForecastResponse.


        :param cpu_request: The cpu_request of this ComputeForecastResponse.
        :type cpu_request: str
        """

        self._cpu_request = cpu_request

    @property
    def time_request(self) -> date:
        """Gets the time_request of this ComputeForecastResponse.


        :return: The time_request of this ComputeForecastResponse.
        :rtype: date
        """
        return self._time_request

    @time_request.setter
    def time_request(self, time_request: date):
        """Sets the time_request of this ComputeForecastResponse.


        :param time_request: The time_request of this ComputeForecastResponse.
        :type time_request: date
        """

        self._time_request = time_request

    @property
    def project_id(self) -> str:
        """Gets the project_id of this ComputeForecastResponse.


        :return: The project_id of this ComputeForecastResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: str):
        """Sets the project_id of this ComputeForecastResponse.


        :param project_id: The project_id of this ComputeForecastResponse.
        :type project_id: str
        """

        self._project_id = project_id

    @property
    def project_desc(self) -> str:
        """Gets the project_desc of this ComputeForecastResponse.


        :return: The project_desc of this ComputeForecastResponse.
        :rtype: str
        """
        return self._project_desc

    @project_desc.setter
    def project_desc(self, project_desc: str):
        """Sets the project_desc of this ComputeForecastResponse.


        :param project_desc: The project_desc of this ComputeForecastResponse.
        :type project_desc: str
        """

        self._project_desc = project_desc

    @property
    def project_phase(self) -> str:
        """Gets the project_phase of this ComputeForecastResponse.


        :return: The project_phase of this ComputeForecastResponse.
        :rtype: str
        """
        return self._project_phase

    @project_phase.setter
    def project_phase(self, project_phase: str):
        """Sets the project_phase of this ComputeForecastResponse.


        :param project_phase: The project_phase of this ComputeForecastResponse.
        :type project_phase: str
        """

        self._project_phase = project_phase

    @property
    def design_block_id(self) -> str:
        """Gets the design_block_id of this ComputeForecastResponse.


        :return: The design_block_id of this ComputeForecastResponse.
        :rtype: str
        """
        return self._design_block_id

    @design_block_id.setter
    def design_block_id(self, design_block_id: str):
        """Sets the design_block_id of this ComputeForecastResponse.


        :param design_block_id: The design_block_id of this ComputeForecastResponse.
        :type design_block_id: str
        """

        self._design_block_id = design_block_id

    @property
    def design_block_desc(self) -> str:
        """Gets the design_block_desc of this ComputeForecastResponse.


        :return: The design_block_desc of this ComputeForecastResponse.
        :rtype: str
        """
        return self._design_block_desc

    @design_block_desc.setter
    def design_block_desc(self, design_block_desc: str):
        """Sets the design_block_desc of this ComputeForecastResponse.


        :param design_block_desc: The design_block_desc of this ComputeForecastResponse.
        :type design_block_desc: str
        """

        self._design_block_desc = design_block_desc

    @property
    def tool_used(self) -> str:
        """Gets the tool_used of this ComputeForecastResponse.


        :return: The tool_used of this ComputeForecastResponse.
        :rtype: str
        """
        return self._tool_used

    @tool_used.setter
    def tool_used(self, tool_used: str):
        """Sets the tool_used of this ComputeForecastResponse.


        :param tool_used: The tool_used of this ComputeForecastResponse.
        :type tool_used: str
        """

        self._tool_used = tool_used

    @property
    def tool_cmd(self) -> str:
        """Gets the tool_cmd of this ComputeForecastResponse.


        :return: The tool_cmd of this ComputeForecastResponse.
        :rtype: str
        """
        return self._tool_cmd

    @tool_cmd.setter
    def tool_cmd(self, tool_cmd: str):
        """Sets the tool_cmd of this ComputeForecastResponse.


        :param tool_cmd: The tool_cmd of this ComputeForecastResponse.
        :type tool_cmd: str
        """

        self._tool_cmd = tool_cmd

    @property
    def predictions(self) -> List[Prediction]:
        """Gets the predictions of this ComputeForecastResponse.


        :return: The predictions of this ComputeForecastResponse.
        :rtype: List[Prediction]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions: List[Prediction]):
        """Sets the predictions of this ComputeForecastResponse.


        :param predictions: The predictions of this ComputeForecastResponse.
        :type predictions: List[Prediction]
        """

        self._predictions = predictions
