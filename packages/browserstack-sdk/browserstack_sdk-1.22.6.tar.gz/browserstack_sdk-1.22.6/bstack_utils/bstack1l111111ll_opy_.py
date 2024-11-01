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
import logging
import os
import datetime
import threading
from bstack_utils.helper import bstack111lll1ll1_opy_, bstack111lll111l_opy_, bstack1ll1ll111_opy_, bstack11l1l1ll1l_opy_, bstack1111l11lll_opy_, bstack11111ll11l_opy_, bstack1111l1llll_opy_, bstack1l1ll11l_opy_
from bstack_utils.bstack1ll1ll1ll1l_opy_ import bstack1ll1ll11lll_opy_
import bstack_utils.bstack111llll1_opy_ as bstack1ll11l11_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from bstack_utils.bstack1lllll1lll_opy_ import bstack1lllll1lll_opy_
from bstack_utils.bstack11ll11l1l1_opy_ import bstack11l1llllll_opy_
bstack1ll11l1lll1_opy_ = bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᚴ")
logger = logging.getLogger(__name__)
class bstack1l1l1ll1l_opy_:
    bstack1ll1ll1ll1l_opy_ = None
    bs_config = None
    bstack1111lll1_opy_ = None
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def launch(cls, bs_config, bstack1111lll1_opy_):
        cls.bs_config = bs_config
        cls.bstack1111lll1_opy_ = bstack1111lll1_opy_
        try:
            cls.bstack1ll11l1ll11_opy_()
            bstack111llll11l_opy_ = bstack111lll1ll1_opy_(bs_config)
            bstack111llll111_opy_ = bstack111lll111l_opy_(bs_config)
            data = bstack1ll11l11_opy_.bstack1ll11l1l1ll_opy_(bs_config, bstack1111lll1_opy_)
            config = {
                bstack111l1l_opy_ (u"ࠪࡥࡺࡺࡨࠨᚵ"): (bstack111llll11l_opy_, bstack111llll111_opy_),
                bstack111l1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᚶ"): cls.default_headers()
            }
            response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠬࡖࡏࡔࡖࠪᚷ"), cls.request_url(bstack111l1l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭ᚸ")), data, config)
            if response.status_code != 200:
                bstack1ll1l111l11_opy_ = response.json()
                if bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᚹ")] == False:
                    cls.bstack1ll11llllll_opy_(bstack1ll1l111l11_opy_)
                    return
                cls.bstack1ll1l11l111_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᚺ")])
                cls.bstack1ll11ll1lll_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᚻ")])
                return None
            bstack1ll1l11l11l_opy_ = cls.bstack1ll1l111ll1_opy_(response)
            return bstack1ll1l11l11l_opy_
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣᚼ").format(str(error)))
            return None
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def stop(cls, bstack1ll11ll111l_opy_=None):
        if not bstack1111lll1l_opy_.on() and not bstack1l1l1lll_opy_.on():
            return
        if os.environ.get(bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᚽ")) == bstack111l1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᚾ") or os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᚿ")) == bstack111l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᛀ"):
            logger.error(bstack111l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫᛁ"))
            return {
                bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛂ"): bstack111l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᛃ"),
                bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᛄ"): bstack111l1l_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪᛅ")
            }
        try:
            cls.bstack1ll1ll1ll1l_opy_.shutdown()
            data = {
                bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᛆ"): bstack1l1ll11l_opy_()
            }
            if not bstack1ll11ll111l_opy_ is None:
                data[bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫᛇ")] = [{
                    bstack111l1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᛈ"): bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧᛉ"),
                    bstack111l1l_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪᛊ"): bstack1ll11ll111l_opy_
                }]
            config = {
                bstack111l1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᛋ"): cls.default_headers()
            }
            bstack1111llll1l_opy_ = bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭ᛌ").format(os.environ[bstack111l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦᛍ")])
            bstack1ll11llll1l_opy_ = cls.request_url(bstack1111llll1l_opy_)
            response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠧࡑࡗࡗࠫᛎ"), bstack1ll11llll1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111l1l_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢᛏ"))
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨᛐ") + str(error))
            return {
                bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛑ"): bstack111l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᛒ"),
                bstack111l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᛓ"): str(error)
            }
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack1ll1l111ll1_opy_(cls, response):
        bstack1ll1l111l11_opy_ = response.json()
        bstack1ll1l11l11l_opy_ = {}
        if bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"࠭ࡪࡸࡶࠪᛔ")) is None:
            os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛕ")] = bstack111l1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᛖ")
        else:
            os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛗ")] = bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"ࠪ࡮ࡼࡺࠧᛘ"), bstack111l1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᛙ"))
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᛚ")] = bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᛛ"), bstack111l1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᛜ"))
        if bstack1111lll1l_opy_.bstack1ll11l1llll_opy_(cls.bs_config, cls.bstack1111lll1_opy_.get(bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩᛝ"), bstack111l1l_opy_ (u"ࠩࠪᛞ"))) is True:
            bstack1ll1l111lll_opy_, bstack1l1l1l1111_opy_, bstack1ll11lll1l1_opy_ = cls.bstack1ll11l1ll1l_opy_(bstack1ll1l111l11_opy_)
            if bstack1ll1l111lll_opy_ != None and bstack1l1l1l1111_opy_ != None:
                bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᛟ")] = {
                    bstack111l1l_opy_ (u"ࠫ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠧᛠ"): bstack1ll1l111lll_opy_,
                    bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᛡ"): bstack1l1l1l1111_opy_,
                    bstack111l1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᛢ"): bstack1ll11lll1l1_opy_
                }
            else:
                bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᛣ")] = {}
        else:
            bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᛤ")] = {}
        if bstack1l1l1lll_opy_.bstack111ll1l1l1_opy_(cls.bs_config) is True:
            bstack1ll1l1111l1_opy_, bstack1l1l1l1111_opy_ = cls.bstack1ll11ll11ll_opy_(bstack1ll1l111l11_opy_)
            if bstack1ll1l1111l1_opy_ != None and bstack1l1l1l1111_opy_ != None:
                bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᛥ")] = {
                    bstack111l1l_opy_ (u"ࠪࡥࡺࡺࡨࡠࡶࡲ࡯ࡪࡴࠧᛦ"): bstack1ll1l1111l1_opy_,
                    bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᛧ"): bstack1l1l1l1111_opy_,
                }
            else:
                bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᛨ")] = {}
        else:
            bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᛩ")] = {}
        if bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᛪ")].get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ᛫")) != None or bstack1ll1l11l11l_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᛬")].get(bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ᛭")) != None:
            cls.bstack1ll1l111111_opy_(bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"ࠫ࡯ࡽࡴࠨᛮ")), bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᛯ")))
        return bstack1ll1l11l11l_opy_
    @classmethod
    def bstack1ll11l1ll1l_opy_(cls, bstack1ll1l111l11_opy_):
        if bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᛰ")) == None:
            cls.bstack1ll1l11l111_opy_()
            return [None, None, None]
        if bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᛱ")][bstack111l1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᛲ")] != True:
            cls.bstack1ll1l11l111_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᛳ")])
            return [None, None, None]
        logger.debug(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᛴ"))
        os.environ[bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᛵ")] = bstack111l1l_opy_ (u"ࠬࡺࡲࡶࡧࠪᛶ")
        if bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"࠭ࡪࡸࡶࠪᛷ")):
            os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᛸ")] = bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠨ࡬ࡺࡸࠬ᛹")]
            os.environ[bstack111l1l_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭᛺")] = json.dumps({
                bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ᛻"): bstack111lll1ll1_opy_(cls.bs_config),
                bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭᛼"): bstack111lll111l_opy_(cls.bs_config)
            })
        if bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ᛽")):
            os.environ[bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ᛾")] = bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ᛿")]
        if bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᜀ")].get(bstack111l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᜁ"), {}).get(bstack111l1l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᜂ")):
            os.environ[bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬᜃ")] = str(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᜄ")][bstack111l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧᜅ")][bstack111l1l_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᜆ")])
        return [bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠨ࡬ࡺࡸࠬᜇ")], bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᜈ")], os.environ[bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᜉ")]]
    @classmethod
    def bstack1ll11ll11ll_opy_(cls, bstack1ll1l111l11_opy_):
        if bstack1ll1l111l11_opy_.get(bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᜊ")) == None:
            cls.bstack1ll11ll1lll_opy_()
            return [None, None]
        if bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᜋ")][bstack111l1l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᜌ")] != True:
            cls.bstack1ll11ll1lll_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᜍ")])
            return [None, None]
        if bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᜎ")].get(bstack111l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᜏ")):
            logger.debug(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᜐ"))
            parsed = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᜑ"), bstack111l1l_opy_ (u"ࠬࢁࡽࠨᜒ")))
            capabilities = bstack1ll11l11_opy_.bstack1ll11lll11l_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᜓ")][bstack111l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ᜔")][bstack111l1l_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ᜕ࠧ")], bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᜖"), bstack111l1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ᜗"))
            bstack1ll1l1111l1_opy_ = capabilities[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩ᜘")]
            os.environ[bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ᜙")] = bstack1ll1l1111l1_opy_
            parsed[bstack111l1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ᜚")] = capabilities[bstack111l1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᜛")]
            os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ᜜")] = json.dumps(parsed)
            scripts = bstack1ll11l11_opy_.bstack1ll11lll11l_opy_(bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᜝")][bstack111l1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ᜞")][bstack111l1l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᜟ")], bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜠ"), bstack111l1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࠧᜡ"))
            bstack1lllll1lll_opy_.bstack111ll1l111_opy_(scripts)
            commands = bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᜢ")][bstack111l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜣ")][bstack111l1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠪᜤ")].get(bstack111l1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᜥ"))
            bstack1lllll1lll_opy_.bstack111ll11l11_opy_(commands)
            bstack1lllll1lll_opy_.store()
        return [bstack1ll1l1111l1_opy_, bstack1ll1l111l11_opy_[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᜦ")]]
    @classmethod
    def bstack1ll1l11l111_opy_(cls, response=None):
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᜧ")] = bstack111l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᜨ")
        os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ᜩ")] = bstack111l1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧᜪ")
        os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᜫ")] = bstack111l1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᜬ")
        os.environ[bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᜭ")] = bstack111l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᜮ")
        os.environ[bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᜯ")] = bstack111l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᜰ")
        os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩᜱ")] = bstack111l1l_opy_ (u"ࠤࡱࡹࡱࡲࠢᜲ")
        cls.bstack1ll11llllll_opy_(response, bstack111l1l_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥᜳ"))
        return [None, None, None]
    @classmethod
    def bstack1ll11ll1lll_opy_(cls, response=None):
        os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅ᜴ࠩ")] = bstack111l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ᜵")
        os.environ[bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ᜶")] = bstack111l1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ᜷")
        os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᜸")] = bstack111l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ᜹")
        cls.bstack1ll11llllll_opy_(response, bstack111l1l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥ᜺"))
        return [None, None, None]
    @classmethod
    def bstack1ll1l111111_opy_(cls, bstack1ll1l111l1l_opy_, bstack1l1l1l1111_opy_):
        os.environ[bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᜻")] = bstack1ll1l111l1l_opy_
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ᜼")] = bstack1l1l1l1111_opy_
    @classmethod
    def bstack1ll11llllll_opy_(cls, response=None, product=bstack111l1l_opy_ (u"ࠨࠢ᜽")):
        if response == None:
            logger.error(product + bstack111l1l_opy_ (u"ࠢࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠤ᜾"))
        for error in response[bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ᜿")]:
            bstack1111ll1l1l_opy_ = error[bstack111l1l_opy_ (u"ࠩ࡮ࡩࡾ࠭ᝀ")]
            error_message = error[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᝁ")]
            if error_message:
                if bstack1111ll1l1l_opy_ == bstack111l1l_opy_ (u"ࠦࡊࡘࡒࡐࡔࡢࡅࡈࡉࡅࡔࡕࡢࡈࡊࡔࡉࡆࡆࠥᝂ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111l1l_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࠨᝃ") + product + bstack111l1l_opy_ (u"ࠨࠠࡧࡣ࡬ࡰࡪࡪࠠࡥࡷࡨࠤࡹࡵࠠࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦᝄ"))
    @classmethod
    def bstack1ll11l1ll11_opy_(cls):
        if cls.bstack1ll1ll1ll1l_opy_ is not None:
            return
        cls.bstack1ll1ll1ll1l_opy_ = bstack1ll1ll11lll_opy_(cls.bstack1ll1l1111ll_opy_)
        cls.bstack1ll1ll1ll1l_opy_.start()
    @classmethod
    def bstack11l11l1lll_opy_(cls):
        if cls.bstack1ll1ll1ll1l_opy_ is None:
            return
        cls.bstack1ll1ll1ll1l_opy_.shutdown()
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack1ll1l1111ll_opy_(cls, bstack11l1l1l1l1_opy_, bstack1ll11ll1l1l_opy_=bstack111l1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᝅ")):
        config = {
            bstack111l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᝆ"): cls.default_headers()
        }
        response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᝇ"), cls.request_url(bstack1ll11ll1l1l_opy_), bstack11l1l1l1l1_opy_, config)
        bstack111llll1l1_opy_ = response.json()
    @classmethod
    def bstack11l1l1ll11_opy_(cls, bstack11l1l1l1l1_opy_, bstack1ll11ll1l1l_opy_=bstack111l1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩᝈ")):
        if not bstack1ll11l11_opy_.bstack1ll11llll11_opy_(bstack11l1l1l1l1_opy_[bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᝉ")]):
            return
        bstack11l111l11_opy_ = bstack1ll11l11_opy_.bstack1ll11ll1l11_opy_(bstack11l1l1l1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᝊ")], bstack11l1l1l1l1_opy_.get(bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᝋ")))
        if bstack11l111l11_opy_ != None:
            if bstack11l1l1l1l1_opy_.get(bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩᝌ")) != None:
                bstack11l1l1l1l1_opy_[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᝍ")][bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧᝎ")] = bstack11l111l11_opy_
            else:
                bstack11l1l1l1l1_opy_[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨᝏ")] = bstack11l111l11_opy_
        if bstack1ll11ll1l1l_opy_ == bstack111l1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᝐ"):
            cls.bstack1ll11l1ll11_opy_()
            cls.bstack1ll1ll1ll1l_opy_.add(bstack11l1l1l1l1_opy_)
        elif bstack1ll11ll1l1l_opy_ == bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᝑ"):
            cls.bstack1ll1l1111ll_opy_([bstack11l1l1l1l1_opy_], bstack1ll11ll1l1l_opy_)
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack1lllllllll_opy_(cls, bstack11l1lll11l_opy_):
        bstack1ll11ll1ll1_opy_ = []
        for log in bstack11l1lll11l_opy_:
            bstack1ll11ll11l1_opy_ = {
                bstack111l1l_opy_ (u"࠭࡫ࡪࡰࡧࠫᝒ"): bstack111l1l_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᝓ"),
                bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ᝔"): log[bstack111l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ᝕")],
                bstack111l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭᝖"): log[bstack111l1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ᝗")],
                bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ᝘"): {},
                bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᝙"): log[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᝚")],
            }
            if bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᝛") in log:
                bstack1ll11ll11l1_opy_[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᝜")] = log[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᝝")]
            elif bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᝞") in log:
                bstack1ll11ll11l1_opy_[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᝟")] = log[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᝠ")]
            bstack1ll11ll1ll1_opy_.append(bstack1ll11ll11l1_opy_)
        cls.bstack11l1l1ll11_opy_({
            bstack111l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᝡ"): bstack111l1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᝢ"),
            bstack111l1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᝣ"): bstack1ll11ll1ll1_opy_
        })
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack1ll11lll1ll_opy_(cls, steps):
        bstack1ll11lllll1_opy_ = []
        for step in steps:
            bstack1ll11ll1111_opy_ = {
                bstack111l1l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᝤ"): bstack111l1l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᝥ"),
                bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᝦ"): step[bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᝧ")],
                bstack111l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᝨ"): step[bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᝩ")],
                bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᝪ"): step[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᝫ")],
                bstack111l1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᝬ"): step[bstack111l1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ᝭")]
            }
            if bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᝮ") in step:
                bstack1ll11ll1111_opy_[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᝯ")] = step[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᝰ")]
            elif bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᝱") in step:
                bstack1ll11ll1111_opy_[bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᝲ")] = step[bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᝳ")]
            bstack1ll11lllll1_opy_.append(bstack1ll11ll1111_opy_)
        cls.bstack11l1l1ll11_opy_({
            bstack111l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ᝴"): bstack111l1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ᝵"),
            bstack111l1l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ᝶"): bstack1ll11lllll1_opy_
        })
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack11llll11l1_opy_(cls, screenshot):
        cls.bstack11l1l1ll11_opy_({
            bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᝷"): bstack111l1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭᝸"),
            bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ᝹"): [{
                bstack111l1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ᝺"): bstack111l1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ᝻"),
                bstack111l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ᝼"): datetime.datetime.utcnow().isoformat() + bstack111l1l_opy_ (u"࡛ࠧࠩ᝽"),
                bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᝾"): screenshot[bstack111l1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ᝿")],
                bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪក"): screenshot[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫខ")]
            }]
        }, bstack1ll11ll1l1l_opy_=bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪគ"))
    @classmethod
    @bstack11l1l1ll1l_opy_(class_method=True)
    def bstack1llll1l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11l1l1ll11_opy_({
            bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪឃ"): bstack111l1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫង"),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪច"): {
                bstack111l1l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢឆ"): cls.current_test_uuid(),
                bstack111l1l_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤជ"): cls.bstack11ll11ll11_opy_(driver)
            }
        })
    @classmethod
    def bstack11ll1l11ll_opy_(cls, event: str, bstack11l1l1l1l1_opy_: bstack11l1llllll_opy_):
        bstack11l1l111l1_opy_ = {
            bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨឈ"): event,
            bstack11l1l1l1l1_opy_.bstack11l1lllll1_opy_(): bstack11l1l1l1l1_opy_.bstack11l1ll11l1_opy_(event)
        }
        cls.bstack11l1l1ll11_opy_(bstack11l1l111l1_opy_)
    @classmethod
    def on(cls):
        if (os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ញ"), None) is None or os.environ[bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧដ")] == bstack111l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧឋ")) and (os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ឌ"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧឍ")] == bstack111l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣណ")):
            return False
        return True
    @staticmethod
    def bstack1ll11lll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1ll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack111l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪត"): bstack111l1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨថ"),
            bstack111l1l_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩទ"): bstack111l1l_opy_ (u"ࠧࡵࡴࡸࡩࠬធ")
        }
        if os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩន"), None):
            headers[bstack111l1l_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩប")] = bstack111l1l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ផ").format(os.environ[bstack111l1l_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠧព")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack111l1l_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫភ").format(bstack1ll11l1lll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪម"), None)
    @staticmethod
    def bstack11ll11ll11_opy_(driver):
        return {
            bstack1111l11lll_opy_(): bstack11111ll11l_opy_(driver)
        }
    @staticmethod
    def bstack1ll1l11111l_opy_(exception_info, report):
        return [{bstack111l1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪយ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11l11111l1_opy_(typename):
        if bstack111l1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦរ") in typename:
            return bstack111l1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥល")
        return bstack111l1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦវ")