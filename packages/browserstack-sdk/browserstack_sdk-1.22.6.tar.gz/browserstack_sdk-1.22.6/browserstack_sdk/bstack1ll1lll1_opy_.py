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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1l11l1l1l_opy_ = {}
        bstack11lll1111l_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ෴"), bstack111l1l_opy_ (u"ࠪࠫ෵"))
        if not bstack11lll1111l_opy_:
            return bstack1l11l1l1l_opy_
        try:
            bstack11lll111l1_opy_ = json.loads(bstack11lll1111l_opy_)
            if bstack111l1l_opy_ (u"ࠦࡴࡹࠢ෶") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠧࡵࡳࠣ෷")] = bstack11lll111l1_opy_[bstack111l1l_opy_ (u"ࠨ࡯ࡴࠤ෸")]
            if bstack111l1l_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ෹") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ෺") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ෻")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ෼"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ෽")))
            if bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ෾") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ෿") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ฀")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤก"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢข")))
            if bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧฃ") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧค") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨฅ")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣฆ"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣง")))
            if bstack111l1l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣจ") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨฉ") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢช")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦซ"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤฌ")))
            if bstack111l1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣญ") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨฎ") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢฏ")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦฐ"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤฑ")))
            if bstack111l1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢฒ") in bstack11lll111l1_opy_ or bstack111l1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢณ") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣด")] = bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥต"), bstack11lll111l1_opy_.get(bstack111l1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥถ")))
            if bstack111l1l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦท") in bstack11lll111l1_opy_:
                bstack1l11l1l1l_opy_[bstack111l1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧธ")] = bstack11lll111l1_opy_[bstack111l1l_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨน")]
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦบ") +  str(error))
        return bstack1l11l1l1l_opy_