# -*- coding: utf-8 -*-
from requests import Request, Response
from mitmproxy import ctx


# def request(flow):
#     # flow.request.headers['User-Agent'] = 'MitmProxy'
#     # ctx.log.info(str(flow.request.headers))
#     # ctx.log.debug(str(flow.request.headers))
#     # ctx.log.error(str(flow.request.headers))
#     # ctx.log.alert(str(flow.request.headers))
#     # ctx.log.warn(str(flow.request.headers))
#     # request = flow.request
#     # info = ctx.log.info
#     # info(request.url)
#     # info(str(request.headers))
#     # info(str(request.cookies))
#     # info(request.host)
#     # info(request.method)
#     # info(str(request.port))
#     # info(request.scheme)
#     url = 'https://httpbin.org/get'
#     flow.request.url = url


def response(flow):
    response = flow.response
    info = ctx.log.info
    info(str(response.status_code))
    info(str(response.headers))
    info(str(response.cookies))
    info(str(response.text))
    # info(str(response.url))
    # info(str(response.request))

