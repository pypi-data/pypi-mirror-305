#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : HuiQing Yu
# @Date   : 2024/10/30


import json
import logging
import urllib
import urllib.parse

import allure
import requests


class Http:
    logger = logging.getLogger()

    def __init__(self, open_allure=False):
        self.headers = {
            "Accept": "application/json",
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            "Accept-language": "zh-CN",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
        }
        self.timeout = 60
        self.open_allure = open_allure

    def get(self, url, params, add_to_headers=None):
        self.headers.update({"Content-type": "application/x-www-form-urlencoded"})
        if add_to_headers:
            self.headers.update(add_to_headers)
        try:
            self.logger.info(f"Request URL=【GET】 {url}")
            self.logger.info(f"request Header = {self.headers}")
            self.logger.info(f"Request Params = {params if params else None}")
            if params:
                if 'json' in self.headers['Content-type']:
                    response = requests.get(url=url, params=params, headers=self.headers, timeout=self.timeout)
                else:
                    response = requests.get(url=url, params=urllib.parse.urlencode(params), headers=self.headers, timeout=self.timeout)
            else:
                response = requests.get(url, headers=self.headers, timeout=self.timeout)
            self.logger.info(f"Response = {response.text}")
            if self.open_allure:
                info = (
                    f"Request Params = {params}\n"
                    f"Response = {response.text}"
                )
                allure.attach(body=info, name=f"【GET】Request URL {url}", attachment_type=allure.attachment_type.TEXT)
            if response.status_code != 200:
                return {"status": "fail", "msg": f"httpPost failed, status code:{response.status_code}"}
            return response.json()
        except Exception as e:
            self.logger.error(f"httpGet failed, detail is:{e}")
            return {"status": "fail", "msg": "%s" % e}

    def post(self, url, params, add_to_headers=None):
        if add_to_headers:
            self.headers.update(add_to_headers)
        post_data = json.dumps(params)
        try:
            self.logger.info(f"request URL= 【POST】 {url}")
            self.logger.info(f"request Header = {self.headers}")
            self.logger.info(f"Request Params = {params if params else None}")
            response = requests.post(url, post_data, headers=self.headers, timeout=self.timeout)
            self.logger.info(f"Response = {response.text}")
            if self.open_allure:
                info = (
                    f"Request Params = {params}\n"
                    f"Response = {response.text}"
                )
                allure.attach(body=info, name=f"【POST】Request URL {url}", attachment_type=allure.attachment_type.TEXT)
            if response.status_code != 200:
                return {"status": "fail", "msg": f"httpPost failed, status code:{response.status_code}"}
            return response.json()
        except Exception as e:
            self.logger.error(f"httpPost failed, detail is:{e}")
            return {"status": "fail", "msg": "%s" % e}
