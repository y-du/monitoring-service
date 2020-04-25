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

__all__ = ("Log", )


from .ce_adapter import Interface, CEAdapterError, NotFound
import falcon
import time
import datetime


class Log:
    __abs_parameters = ("lines", )
    __rel_parameters = ("since", "until")

    def __init__(self, ce_adapter: Interface):
        self.__ce_adapter = ce_adapter

    def on_get(self, req: falcon.request.Request, resp: falcon.response.Response, name):
        try:
            if req.params:
                params = req.params.copy()
                if set(params).issubset(self.__rel_parameters):
                    utc_tstp_format = "%Y-%m-%dT%H:%M:%SZ"
                    for key in params:
                        params[key] = int(datetime.datetime.strptime(params[key], utc_tstp_format).replace(tzinfo=datetime.timezone.utc).timestamp())
                    resp.body = self.__ce_adapter.getRelative(name, **params)
                elif set(params).issubset(self.__abs_parameters):
                    for key in params:
                        params[key] = int(params[key])
                    resp.body = self.__ce_adapter.getAbsolut(name, **params)
                else:
                    raise TypeError("unknown arguments")
            else:
                resp.body = self.__ce_adapter.getRelative(name)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        except (TypeError, ValueError):
            resp.status = falcon.HTTP_400
        except NotFound:
            resp.status = falcon.HTTP_404
        except CEAdapterError:
            resp.status = falcon.HTTP_500
