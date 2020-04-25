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

__all__ = ("m_conf",)


import simple_env_var


@simple_env_var.configuration
class MConf:

    @simple_env_var.section
    class CE:
        socket = "unix://var/run/docker.sock"

    @simple_env_var.section
    class Logger:
        level = "info"


m_conf = MConf()
