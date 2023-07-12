# -*- coding: utf-8 -*-

from flask import Blueprint
from view.unify_response import UnifyResponse
from view.view_helper import ViewHelper

name = "view-port"
_view_port = Blueprint(name, name, url_prefix="/<string:source>")

view_helper = ViewHelper("ctrl")


@_view_port.route("/<string:operate>", methods=["POST", "GET", "DELETE", "PUT", "HEAD"])
def view_port(source, operate):
    """视图层."""
    if '-' in operate:
        operate = operate.replace('-', '_')
    if '-' in source:
        source = source.replace('-', '_')
    ctrl = view_helper.ctrls[source](operate=operate)
    result = ctrl.do_operate()
    return UnifyResponse.R(result)


view_helper.load_ctrl()
