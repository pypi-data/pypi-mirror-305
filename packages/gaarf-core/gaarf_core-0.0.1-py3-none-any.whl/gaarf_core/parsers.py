# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for defining various parsing strategy for GoogleAdsRow elements.

GoogleAdsRowParser parses a single GoogleAdsRow and applies different parsing
strategies to each element of the row.
"""

from __future__ import annotations

import abc
import functools
import operator
from collections.abc import Mapping
from typing import Union

from typing_extensions import TypeAlias, override

from gaarf_core import api_clients, exceptions, query_editor

ApiRowElement: TypeAlias = Union[int, float, str, bool, list, None]


class BaseParser(abc.ABC):
  @abc.abstractmethod
  def parse_response(
    self, response: api_clients.GaarfApiResponse
  ) -> list[list[ApiRowElement]]:
    """Parses response."""


class ListParser(BaseParser):
  @override
  def parse_response(
    self,
    response: api_clients.GaarfApiResponse,
    query_specification: query_editor.BaseQueryElements,
  ) -> list[list[ApiRowElement]]:
    del query_specification
    return response.results


class DictParser(BaseParser):
  @override
  def parse_response(
    self,
    response: api_clients.GaarfApiResponse,
    query_specification: query_editor.BaseQueryElements,
  ) -> list[list[ApiRowElement]]:
    if not isinstance(response.results[0], Mapping):
      return GaarfParserError
    results = []
    for result in response.results:
      row = []
      for field in query_specification.fields:
        row.append(self.get_nested_field(result, field))
      results.append(row)
    return results

  def get_nested_field(self, dictionary, key):
    key = key.split('.')
    return functools.reduce(operator.getitem, key, dictionary)


class GaarfParserError(exceptions.GaarfError):
  """Incorrect data format for parser."""
