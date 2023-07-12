# -*- coding: utf-8 -*-

from flask import request

from base_cls import BaseCls
from submodules.utils.protobuf_helper import ProtobufHelper
from view.errors import PopupError


class BaseCtrl(BaseCls):

    POST = "POST"
    GET = "GET"
    HEAD = "HEAD"
    DELETE = "DELETE"
    PUT = "PUT"

    @property
    def operate(self):
        method = request.method
        if method == self.POST:
            return self._operate
        if method == self.GET:
            return f"{self._operate}_GET"
        if method == self.DELETE:
            return f"{self._operate}_DELETE"
        if method == self.PUT:
            return f"{self._operate}_PUT"
        if method == self.HEAD:
            return f"{self._operate}_HEAD"
        raise PopupError("Method Not Supported")

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.PH = ProtobufHelper
        self._operate = kargs.get('operate', None)
        self.request = request
        self._manager = None
        self._init(*args, **kargs)

    def _init(self, *args, **kargs):
        """子类要有自己的初始化工作就重载此函数."""
        pass

    def __getattr__(self, name):
        if request.method == self.POST:
            return request.get_json().get(name)
        if request.method == self.GET:
            return request.args.get(name)

    def get_header_param(self, key, default=None):
        return request.headers.get(key, default)

    def do_operate(self):
        if self.operate is None:
            raise PopupError(f"操作未实现: {self.operate}")
        if self.operate.startswith("_"):
            raise PopupError(f"操作未实现: {self.operate}")
        cls = self.__class__
        if self.operate not in cls.__dict__:
            raise PopupError(f"操作未实现: {self.operate}")
        return cls.__dict__[self.operate](self)
