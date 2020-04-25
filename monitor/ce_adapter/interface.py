"""
   Copyright 2020 Yann Dumont

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

__all__ = ("Interface", "ContainerState", "CEAdapterError", "EngineAPIError", "NotFound")


import abc
import typing


class CEAdapterError(Exception):
    pass


class EngineAPIError(CEAdapterError):
    pass


class NotFound(CEAdapterError):
    pass


class ContainerState:
    running = "active"
    stopped = "inactive"


class Interface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAbsolut(self, c_name: str, lines: int) -> str:
        pass

    @abc.abstractmethod
    def getRelative(self, c_name: str, since: typing.Optional[int] = None, until: typing.Optional[int] = None) -> str:
        pass
