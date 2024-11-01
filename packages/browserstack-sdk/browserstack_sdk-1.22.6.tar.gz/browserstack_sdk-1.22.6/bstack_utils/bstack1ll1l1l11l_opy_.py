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
import logging
import os
import threading
from bstack_utils.helper import bstack11ll111l_opy_
from bstack_utils.constants import bstack111l111lll_opy_
logger = logging.getLogger(__name__)
class bstack1111lll1l_opy_:
    bstack1ll1ll1ll1l_opy_ = None
    @classmethod
    def bstack1llll1l11l_opy_(cls):
        if cls.on():
            logger.info(
                bstack111l1l_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ៚").format(os.environ[bstack111l1l_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠤ៛")]))
    @classmethod
    def on(cls):
        if os.environ.get(bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬៜ"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭៝")] == bstack111l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ៞"):
            return False
        return True
    @classmethod
    def bstack1ll11l11111_opy_(cls, bs_config, framework=bstack111l1l_opy_ (u"ࠢࠣ៟")):
        if framework == bstack111l1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ០"):
            return bstack11ll111l_opy_(bs_config.get(bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭១")))
        bstack1ll111ll1l1_opy_ = framework in bstack111l111lll_opy_
        return bstack11ll111l_opy_(bs_config.get(bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ២"), bstack1ll111ll1l1_opy_))
    @classmethod
    def bstack1ll111lllll_opy_(cls, framework):
        return framework in bstack111l111lll_opy_
    @classmethod
    def bstack1ll11l1llll_opy_(cls, bs_config, framework):
        return cls.bstack1ll11l11111_opy_(bs_config, framework) is True and cls.bstack1ll111lllll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ៣"), None)
    @staticmethod
    def bstack11ll1lll1l_opy_():
        if getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ៤"), None):
            return {
                bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ៥"): bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࠬ៦"),
                bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ៧"): getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭៨"), None)
            }
        if getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ៩"), None):
            return {
                bstack111l1l_opy_ (u"ࠫࡹࡿࡰࡦࠩ៪"): bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ៫"),
                bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭៬"): getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ៭"), None)
            }
        return None
    @staticmethod
    def bstack1ll111lll1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1111lll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11l1l1l111_opy_(test, hook_name=None):
        bstack1ll111ll1ll_opy_ = test.parent
        if hook_name in [bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭៮"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ៯"), bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ៰"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭៱")]:
            bstack1ll111ll1ll_opy_ = test
        scope = []
        while bstack1ll111ll1ll_opy_ is not None:
            scope.append(bstack1ll111ll1ll_opy_.name)
            bstack1ll111ll1ll_opy_ = bstack1ll111ll1ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1ll111llll1_opy_(hook_type):
        if hook_type == bstack111l1l_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥ៲"):
            return bstack111l1l_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥ៳")
        elif hook_type == bstack111l1l_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦ៴"):
            return bstack111l1l_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣ៵")
    @staticmethod
    def bstack1ll111lll11_opy_(bstack1lll11ll1l_opy_):
        try:
            if not bstack1111lll1l_opy_.on():
                return bstack1lll11ll1l_opy_
            if os.environ.get(bstack111l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢ៶"), None) == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣ៷"):
                tests = os.environ.get(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣ៸"), None)
                if tests is None or tests == bstack111l1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ៹"):
                    return bstack1lll11ll1l_opy_
                bstack1lll11ll1l_opy_ = tests.split(bstack111l1l_opy_ (u"࠭ࠬࠨ៺"))
                return bstack1lll11ll1l_opy_
        except Exception as exc:
            print(bstack111l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣ៻"), str(exc))
        return bstack1lll11ll1l_opy_