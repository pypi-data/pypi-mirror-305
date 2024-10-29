from enum import StrEnum, unique
from http.client import HTTPResponse
from typing import Union
from urllib.error import HTTPError
import urllib.request

from multiformats import CID

from ot.identifier import read_content


@unique
class IPFSNode(StrEnum):
    Gateway = "gateway"
    Local = "local"


def get(cid, node: IPFSNode = IPFSNode.Gateway):
    """
    Fetch the contents from an IPFS node given a CID.

    :param cid: the CID of the content to fetch
    :param node: whether to use a local or a gateway node
        one of IPFSNode.Gateway or IPFSNode.Local
    """
    assert CID.decode(cid=cid)

    content = {
        IPFSNode.Gateway: fetch_from_gateway,
        IPFSNode.Local: fetch_from_local_ipfs_node,
    }[node](cid)

    return read_content(content)


def fetch_from_local_ipfs_node(
    cid, node_address="http://127.0.0.1:8080/ipfs"
) -> HTTPResponse:
    url = f"{node_address}/{cid}"
    return request(url)


def fetch_from_gateway(cid, gateway_base="w3s.link") -> HTTPResponse:
    url = f"https://{cid}.ipfs.{gateway_base}/"
    return request(url)


def request(url) -> Union[HTTPResponse, HTTPError]:
    try:
        with urllib.request.urlopen(url) as response:
            return response.read()
    except HTTPError as http_error:
        return http_error
