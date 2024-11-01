# coding: UTF-8
import sys
bstack11l111l_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11l1lll_opy_ = 7
def bstack111l1l_opy_ (bstack1lllll1_opy_):
    global bstack11111ll_opy_
    bstack1llll_opy_ = ord (bstack1lllll1_opy_ [-1])
    bstack11lll1_opy_ = bstack1lllll1_opy_ [:-1]
    bstack1lll111_opy_ = bstack1llll_opy_ % len (bstack11lll1_opy_)
    bstack11ll_opy_ = bstack11lll1_opy_ [:bstack1lll111_opy_] + bstack11lll1_opy_ [bstack1lll111_opy_:]
    if bstack11l111l_opy_:
        bstack11lllll_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack11111l1_opy_ + bstack1llll_opy_) % bstack11l1lll_opy_) for bstack11111l1_opy_, char in enumerate (bstack11ll_opy_)])
    else:
        bstack11lllll_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack11111l1_opy_ + bstack1llll_opy_) % bstack11l1lll_opy_) for bstack11111l1_opy_, char in enumerate (bstack11ll_opy_)])
    return eval (bstack11lllll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llll11ll11_opy_
bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
def bstack1lll1111111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1lll11111l1_opy_(bstack1lll1111l11_opy_, bstack1lll111111l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1lll1111l11_opy_):
        with open(bstack1lll1111l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1lll1111111_opy_(bstack1lll1111l11_opy_):
        pac = get_pac(url=bstack1lll1111l11_opy_)
    else:
        raise Exception(bstack111l1l_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᗦ").format(bstack1lll1111l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111l1l_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᗧ"), 80))
        bstack1lll1111l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1lll1111l1l_opy_ = bstack111l1l_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᗨ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1lll111111l_opy_, bstack1lll1111l1l_opy_)
    return proxy_url
def bstack11l1l1l1l_opy_(config):
    return bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᗩ") in config or bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᗪ") in config
def bstack11lll1l11l_opy_(config):
    if not bstack11l1l1l1l_opy_(config):
        return
    if config.get(bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᗫ")):
        return config.get(bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᗬ"))
    if config.get(bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᗭ")):
        return config.get(bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᗮ"))
def bstack11l11ll1l_opy_(config, bstack1lll111111l_opy_):
    proxy = bstack11lll1l11l_opy_(config)
    proxies = {}
    if config.get(bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᗯ")) or config.get(bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᗰ")):
        if proxy.endswith(bstack111l1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᗱ")):
            proxies = bstack1lll11l111_opy_(proxy, bstack1lll111111l_opy_)
        else:
            proxies = {
                bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᗲ"): proxy
            }
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬᗳ"), proxies)
    return proxies
def bstack1lll11l111_opy_(bstack1lll1111l11_opy_, bstack1lll111111l_opy_):
    proxies = {}
    global bstack1ll1lllllll_opy_
    if bstack111l1l_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩᗴ") in globals():
        return bstack1ll1lllllll_opy_
    try:
        proxy = bstack1lll11111l1_opy_(bstack1lll1111l11_opy_, bstack1lll111111l_opy_)
        if bstack111l1l_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢᗵ") in proxy:
            proxies = {}
        elif bstack111l1l_opy_ (u"ࠣࡊࡗࡘࡕࠨᗶ") in proxy or bstack111l1l_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣᗷ") in proxy or bstack111l1l_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤᗸ") in proxy:
            bstack1lll11111ll_opy_ = proxy.split(bstack111l1l_opy_ (u"ࠦࠥࠨᗹ"))
            if bstack111l1l_opy_ (u"ࠧࡀ࠯࠰ࠤᗺ") in bstack111l1l_opy_ (u"ࠨࠢᗻ").join(bstack1lll11111ll_opy_[1:]):
                proxies = {
                    bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᗼ"): bstack111l1l_opy_ (u"ࠣࠤᗽ").join(bstack1lll11111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᗾ"): str(bstack1lll11111ll_opy_[0]).lower() + bstack111l1l_opy_ (u"ࠥ࠾࠴࠵ࠢᗿ") + bstack111l1l_opy_ (u"ࠦࠧᘀ").join(bstack1lll11111ll_opy_[1:])
                }
        elif bstack111l1l_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦᘁ") in proxy:
            bstack1lll11111ll_opy_ = proxy.split(bstack111l1l_opy_ (u"ࠨࠠࠣᘂ"))
            if bstack111l1l_opy_ (u"ࠢ࠻࠱࠲ࠦᘃ") in bstack111l1l_opy_ (u"ࠣࠤᘄ").join(bstack1lll11111ll_opy_[1:]):
                proxies = {
                    bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᘅ"): bstack111l1l_opy_ (u"ࠥࠦᘆ").join(bstack1lll11111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᘇ"): bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᘈ") + bstack111l1l_opy_ (u"ࠨࠢᘉ").join(bstack1lll11111ll_opy_[1:])
                }
        else:
            proxies = {
                bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᘊ"): proxy
            }
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧᘋ"), bstack1llll11ll11_opy_.format(bstack1lll1111l11_opy_, str(e)))
    bstack1ll1lllllll_opy_ = proxies
    return proxies