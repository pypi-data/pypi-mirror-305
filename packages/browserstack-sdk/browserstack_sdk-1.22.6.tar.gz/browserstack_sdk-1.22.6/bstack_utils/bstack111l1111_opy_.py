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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack1111l1l1l1_opy_, bstack111ll11l1_opy_, bstack1ll111l11_opy_, bstack1l1ll1ll_opy_, \
    bstack1111111lll_opy_
def bstack11ll1l1l_opy_(bstack1ll1ll11111_opy_):
    for driver in bstack1ll1ll11111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1llll_opy_(driver, status, reason=bstack111l1l_opy_ (u"࠭ࠧᙁ")):
    bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
    if bstack1l1ll111_opy_.bstack11l11l1l11_opy_():
        return
    bstack1ll11llll_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᙂ"), bstack111l1l_opy_ (u"ࠨࠩᙃ"), status, reason, bstack111l1l_opy_ (u"ࠩࠪᙄ"), bstack111l1l_opy_ (u"ࠪࠫᙅ"))
    driver.execute_script(bstack1ll11llll_opy_)
def bstack11llll11l_opy_(page, status, reason=bstack111l1l_opy_ (u"ࠫࠬᙆ")):
    try:
        if page is None:
            return
        bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
        if bstack1l1ll111_opy_.bstack11l11l1l11_opy_():
            return
        bstack1ll11llll_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᙇ"), bstack111l1l_opy_ (u"࠭ࠧᙈ"), status, reason, bstack111l1l_opy_ (u"ࠧࠨᙉ"), bstack111l1l_opy_ (u"ࠨࠩᙊ"))
        page.evaluate(bstack111l1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᙋ"), bstack1ll11llll_opy_)
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣᙌ"), e)
def bstack111l1l11l_opy_(type, name, status, reason, bstack11ll1l1ll_opy_, bstack1lll1l11l_opy_):
    bstack1ll111ll_opy_ = {
        bstack111l1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᙍ"): type,
        bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᙎ"): {}
    }
    if type == bstack111l1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᙏ"):
        bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᙐ")][bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᙑ")] = bstack11ll1l1ll_opy_
        bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᙒ")][bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨᙓ")] = json.dumps(str(bstack1lll1l11l_opy_))
    if type == bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᙔ"):
        bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᙕ")][bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᙖ")] = name
    if type == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᙗ"):
        bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᙘ")][bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᙙ")] = status
        if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᙚ") and str(reason) != bstack111l1l_opy_ (u"ࠦࠧᙛ"):
            bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᙜ")][bstack111l1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᙝ")] = json.dumps(str(reason))
    bstack111llll11_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᙞ").format(json.dumps(bstack1ll111ll_opy_))
    return bstack111llll11_opy_
def bstack1111l111_opy_(url, config, logger, bstack1lll11l1ll_opy_=False):
    hostname = bstack111ll11l1_opy_(url)
    is_private = bstack1l1ll1ll_opy_(hostname)
    try:
        if is_private or bstack1lll11l1ll_opy_:
            file_path = bstack1111l1l1l1_opy_(bstack111l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᙟ"), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᙠ"), logger)
            if os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᙡ")) and eval(
                    os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᙢ"))):
                return
            if (bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᙣ") in config and not config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᙤ")]):
                os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᙥ")] = str(True)
                bstack1ll1l1lllll_opy_ = {bstack111l1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪᙦ"): hostname}
                bstack1111111lll_opy_(bstack111l1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᙧ"), bstack111l1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨᙨ"), bstack1ll1l1lllll_opy_, logger)
    except Exception as e:
        pass
def bstack1l11l1l11l_opy_(caps, bstack1ll1l1lll1l_opy_):
    if bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᙩ") in caps:
        caps[bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᙪ")][bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬᙫ")] = True
        if bstack1ll1l1lll1l_opy_:
            caps[bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᙬ")][bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᙭")] = bstack1ll1l1lll1l_opy_
    else:
        caps[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧ᙮")] = True
        if bstack1ll1l1lll1l_opy_:
            caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᙯ")] = bstack1ll1l1lll1l_opy_
def bstack1ll1llll111_opy_(bstack11l1l1l1ll_opy_):
    bstack1ll1l1llll1_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᙰ"), bstack111l1l_opy_ (u"ࠬ࠭ᙱ"))
    if bstack1ll1l1llll1_opy_ == bstack111l1l_opy_ (u"࠭ࠧᙲ") or bstack1ll1l1llll1_opy_ == bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᙳ"):
        threading.current_thread().testStatus = bstack11l1l1l1ll_opy_
    else:
        if bstack11l1l1l1ll_opy_ == bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᙴ"):
            threading.current_thread().testStatus = bstack11l1l1l1ll_opy_