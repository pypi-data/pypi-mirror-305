#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Time    : 2024/10/25 14:33
Author  : ren
"""
import ipaddress
import urllib.parse
from collections import OrderedDict

import netifaces
from nacos import NacosClient
from sanic import Sanic
from sanic.log import logger
from sanic_ext import Extension


class NacosExt(Extension):
    name = "SanicNacos"

    bootstrap_cfg = {
        "NACOS_SERVER_ADDR": "127.0.0.1:8848",
        "NACOS_ENABLE": True,
        "NACOS_AK": None,
        "NACOS_SK": None,
        "NACOS_USERNAME": None,
        "NACOS_PASSWORD": None,

        "NACOS_NAMESPACE": "public",
        "NACOS_GROUP": "DEFAULT",
        "NACOS_CLUSTER_NAME": "DEFAULT",

        "NACOS_PREFER_SUBNET": "192.0.0.0/8",

        "NACOS_SERVICE_NAME": None,
        "NACOS_SERVER_IP": None,
        "NACOS_SERVER_PORT": None,
        "NACOS_HB_INTERVAL": 30,
    }

    _client: NacosClient = None

    def startup(self, bootstrap) -> None:
        self.bootstrap_cfg.update(self.app.config)
        if not self.bootstrap_cfg['NACOS_ENABLE']:
            logger.warning("nacos registry is not enabled")
            return
        if not hasattr(self.app.ctx, "NACOS_CLIENT"):
            self.app.ctx.NACOS_CLIENT = self._client = NacosClient(self.bootstrap_cfg['NACOS_SERVER_ADDR'],
                                                                   namespace=self.bootstrap_cfg['NACOS_NAMESPACE'],
                                                                   ak=self.bootstrap_cfg['NACOS_AK'],
                                                                   sk=self.bootstrap_cfg['NACOS_SK'],
                                                                   username=self.bootstrap_cfg['NACOS_USERNAME'],
                                                                   password=self.bootstrap_cfg['NACOS_PASSWORD'],
                                                                   )
        else:
            self._client = self.app.ctx.cNACOS_CLIENT
        self._registry()

    def label(self):
        return "SanicNacos"

    def _registry(self):
        if self.bootstrap_cfg['NACOS_ENABLE']:
            self.app.before_server_start(self.add_naming_instance)
            self.app.after_server_start(self.add_naming_instance)
        else:
            logger.warning("nacos discovery is disabled")

    def add_naming_instance(self, app: Sanic, *args):
        self.bootstrap_cfg['NACOS_SERVICE_NAME'] = self.bootstrap_cfg['NACOS_SERVICE_NAME'] or self.app.name
        self.bootstrap_cfg['NACOS_SERVER_IP'] = (self.bootstrap_cfg['NACOS_SERVER_IP'] or
                                                 get_ip_addresses_with_subnet(
                                                     self.bootstrap_cfg['NACOS_PREFER_SUBNET']))
        assert self.bootstrap_cfg['NACOS_SERVER_IP'] is not None
        self.bootstrap_cfg['NACOS_SERVER_PORT'] = self.bootstrap_cfg['NACOS_SERVER_PORT'] or \
                                                  get_server_port(app)
        if self.bootstrap_cfg['NACOS_SERVER_PORT'] is not None:
            if self._client.add_naming_instance(
                    self.bootstrap_cfg['NACOS_SERVICE_NAME'],
                    self.bootstrap_cfg['NACOS_SERVER_IP'],
                    self.bootstrap_cfg['NACOS_SERVER_PORT'],
                    cluster_name=self.bootstrap_cfg['NACOS_CLUSTER_NAME'],
                    heartbeat_interval=self.bootstrap_cfg['NACOS_HB_INTERVAL'],
                    group_name=self.bootstrap_cfg['NACOS_GROUP'],
                    metadata={"__registry_by__": self.name},
            ):
                logger.info(f"add nacos instance success, {self.bootstrap_cfg}")
            else:
                logger.error("add nacos instance failed")
        else:
            logger.warning("nacos server port is not found")


def get_ip_addresses_with_subnet(prefer_subnet: str = "192.0.0.0/8"):
    ip_info = OrderedDict()
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for addr in addresses[netifaces.AF_INET]:
                ip_info[addr["addr"]] = addr["addr"]
                prefer = ipaddress.ip_network(prefer_subnet)
                if ipaddress.ip_address(addr["addr"]) in prefer:
                    ip_info[addr["addr"]] = addr["addr"]
                    ip_info.move_to_end(addr["addr"], last=False)
                    break
    logger.info(f"find ip {ip_info}")
    return ip_info.popitem(last=False)[0]


def get_server_port(app: Sanic):
    if app.state.port:
        return app.state.port
    if app.serve_location:
        return urllib.parse.urlparse(app.serve_location).port
