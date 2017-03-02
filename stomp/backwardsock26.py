"""
Python2.6 (and greater) specific versions of various networking (ipv6) functions used by stomp.py
"""
from __future__ import print_function

import socket


def get_socket(host, port, timeout=None,
               proxy_host=None, proxy_port=None,
               proxy_user=None, proxy_password=None):
    """
    Return a socket connection.

    :param str host: the hostname to connect to
    :param int port: the port number to connect to
    :param timeout: if specified, set the socket timeout
    :param proxy_host: if specified, the http proxy to connect through
    :param proxy_host: if specified, the http proxy port
    :param proxy_user: if specified, the username for authenticating to proxy
    :param proxy_password: if specified, the password for authenticating to proxy
    """
    if proxy_host:
        import socks
        s = socks.socksocket()
        s.settimeout(timeout)
        s.set_proxy(socks.HTTP, proxy_host, proxy_port, True, username=proxy_user, password=proxy_password)
        s.connect((host, port))
        return s
    else:
        return socket.create_connection((host, port), timeout)
