# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "ModuleData"
"""
  * @File    :   ModuleData.py
  * @Time    :   2023/04/26 15:02:59
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

import xy_web_server
from importlib_resources import files


class ModuleData:
    def __init__(self) -> None:
        self.path = files(xy_web_server.__name__).joinpath("data")

        self.template_path = self.path.joinpath("template")

        self.nginx_path = self.template_path.joinpath("nginx")

        self.nginx_servers_conf_path = self.nginx_path.joinpath(
            "nginx_servers_conf.template"
        )
        self.nginx_server_conf_path = self.nginx_path.joinpath(
            "nginx_server_conf.template"
        )
        self.nginx_location_conf_path = self.nginx_path.joinpath(
            "nginx_location_conf.template"
        )

        self.nginx_servers_json_path = self.nginx_path.joinpath("nginx_servers.json")
        self.nginx_server_json_path = self.nginx_path.joinpath("nginx_server.json")
        self.nginx_location_json_path = self.nginx_path.joinpath("nginx_location.json")

        self.runner_path = self.template_path.joinpath("runner")
        self.runner_py_path = self.runner_path.joinpath("runner_py.template")

        self.site_path = self.template_path.joinpath("site")
        self.site_application_path = self.site_path.joinpath("application")
        self.site_application_tornado_path = self.site_application_path.joinpath(
            "tornado"
        )
