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


__all__ = ("DockerAdapter", )


from ..logger import getLogger
from ..configuration import m_conf
from .interface import Interface, ContainerState, EngineAPIError, NotFound, CEAdapterError
import docker
import docker.errors
import docker.types
import typing


logger = getLogger(__name__.split(".", 1)[-1])


error_map = {
    docker.errors.APIError: EngineAPIError,
    docker.errors.NotFound: NotFound
}


class DockerAdapter(Interface):
    def __init__(self):
        self.__client = docker.DockerClient(base_url=m_conf.CE.socket)

    def getAbsolut(self, c_name: str, lines: int) -> str:
        try:
            container = self.__client.containers.get(c_name)
            return container.logs(tail=lines).decode()
        except Exception as ex:
            logger.error("can't get logs for {} - {}".format(c_name, ex))
            raise error_map.setdefault(ex, CEAdapterError)(ex)

    def getRelative(self, c_name: str,  since: typing.Optional[int] = None, until: typing.Optional[int] = None) -> str:
        try:
            container = self.__client.containers.get(c_name)
            kwargs = dict()
            if all((since, until)):
                kwargs["since"] = since
                kwargs["until"] = until
            elif since:
                kwargs["since"] = since
            elif until:
                kwargs["until"] = until
            return container.logs(**kwargs).decode()
        except Exception as ex:
            logger.error("can't get logs for {} - {}".format(c_name, ex))
            raise error_map.setdefault(ex, CEAdapterError)(ex)
