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
import datetime
import threading
from bstack_utils.helper import bstack111ll1ll1l_opy_, bstack1ll1llll1_opy_, get_host_info, bstack1111111l1l_opy_, \
 bstack1lll1ll1_opy_, bstack1ll111l11_opy_, bstack11l1l1ll1l_opy_, bstack1111l1llll_opy_, bstack1l1ll11l_opy_
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.percy import bstack1l1l1l1ll1_opy_
from bstack_utils.config import Config
bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l1l1l1ll1_opy_()
@bstack11l1l1ll1l_opy_(class_method=False)
def bstack1ll11l1l1ll_opy_(bs_config, bstack1111lll1_opy_):
  try:
    data = {
        bstack111l1l_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫឝ"): bstack111l1l_opy_ (u"ࠬࡰࡳࡰࡰࠪឞ"),
        bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬស"): bs_config.get(bstack111l1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬហ"), bstack111l1l_opy_ (u"ࠨࠩឡ")),
        bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧអ"): bs_config.get(bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ឣ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧឤ"): bs_config.get(bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧឥ")),
        bstack111l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫឦ"): bs_config.get(bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪឧ"), bstack111l1l_opy_ (u"ࠨࠩឨ")),
        bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ឩ"): bstack1l1ll11l_opy_(),
        bstack111l1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨឪ"): bstack1111111l1l_opy_(bs_config),
        bstack111l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧឫ"): get_host_info(),
        bstack111l1l_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭ឬ"): bstack1ll1llll1_opy_(),
        bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ឭ"): os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ឮ")),
        bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭ឯ"): os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧឰ"), False),
        bstack111l1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬឱ"): bstack111ll1ll1l_opy_(),
        bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫឲ"): bstack1ll11l11lll_opy_(),
        bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩឳ"): bstack1ll11l1l1l1_opy_(bstack1111lll1_opy_),
        bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ឴"): bstack1lll1lll11_opy_(bs_config, bstack1111lll1_opy_.get(bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨ឵"), bstack111l1l_opy_ (u"ࠨࠩា"))),
        bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫិ"): bstack1lll1ll1_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡣࡼࡰࡴࡧࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦី").format(str(error)))
    return None
def bstack1ll11l1l1l1_opy_(framework):
  return {
    bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫឹ"): framework.get(bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ឺ"), bstack111l1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ុ")),
    bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪូ"): framework.get(bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬួ")),
    bstack111l1l_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ើ"): framework.get(bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨឿ")),
    bstack111l1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ៀ"): bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬេ"),
    bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ែ"): framework.get(bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧៃ"))
  }
def bstack1lll1lll11_opy_(bs_config, framework):
  bstack1l1l1111l1_opy_ = False
  bstack11l11lll1_opy_ = False
  bstack1ll11l11ll1_opy_ = False
  if bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬោ") in bs_config:
    bstack1ll11l11ll1_opy_ = True
  elif bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠭ៅ") in bs_config:
    bstack1l1l1111l1_opy_ = True
  else:
    bstack11l11lll1_opy_ = True
  bstack11l111l11_opy_ = {
    bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪំ"): bstack1111lll1l_opy_.bstack1ll11l11111_opy_(bs_config, framework),
    bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫះ"): bstack1l1l1lll_opy_.bstack111ll1l1l1_opy_(bs_config),
    bstack111l1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫៈ"): bs_config.get(bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ៉"), False),
    bstack111l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ៊"): bstack11l11lll1_opy_,
    bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ់"): bstack1l1l1111l1_opy_
  }
  return bstack11l111l11_opy_
@bstack11l1l1ll1l_opy_(class_method=False)
def bstack1ll11l11lll_opy_():
  try:
    bstack1ll11l111ll_opy_ = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ៌"), bstack111l1l_opy_ (u"ࠪࡿࢂ࠭៍")))
    return {
        bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭៎"): bstack1ll11l111ll_opy_
    }
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ៏").format(str(error)))
    return {}
def bstack1ll11lll11l_opy_(array, bstack1ll11l111l1_opy_, bstack1ll11l1111l_opy_):
  result = {}
  for o in array:
    key = o[bstack1ll11l111l1_opy_]
    result[key] = o[bstack1ll11l1111l_opy_]
  return result
def bstack1ll11llll11_opy_(bstack11l1ll11l_opy_=bstack111l1l_opy_ (u"࠭ࠧ័")):
  bstack1ll11l11l11_opy_ = bstack1l1l1lll_opy_.on()
  bstack1ll11l1l111_opy_ = bstack1111lll1l_opy_.on()
  bstack1ll11l11l1l_opy_ = percy.bstack11lll1l111_opy_()
  if bstack1ll11l11l1l_opy_ and not bstack1ll11l1l111_opy_ and not bstack1ll11l11l11_opy_:
    return bstack11l1ll11l_opy_ not in [bstack111l1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ៑"), bstack111l1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨ្ࠬ")]
  elif bstack1ll11l11l11_opy_ and not bstack1ll11l1l111_opy_:
    return bstack11l1ll11l_opy_ not in [bstack111l1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ៓"), bstack111l1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ។"), bstack111l1l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ៕")]
  return bstack1ll11l11l11_opy_ or bstack1ll11l1l111_opy_ or bstack1ll11l11l1l_opy_
@bstack11l1l1ll1l_opy_(class_method=False)
def bstack1ll11ll1l11_opy_(bstack11l1ll11l_opy_, test=None):
  bstack1ll11l1l11l_opy_ = bstack1l1l1lll_opy_.on()
  if not bstack1ll11l1l11l_opy_ or bstack11l1ll11l_opy_ not in [bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ៖")] or test == None:
    return None
  return {
    bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ៗ"): bstack1ll11l1l11l_opy_ and bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭៘"), None) == True and bstack1l1l1lll_opy_.bstack1lll1ll1ll_opy_(test[bstack111l1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭៙")])
  }