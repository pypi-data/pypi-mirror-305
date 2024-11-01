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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack111llll1ll_opy_ as bstack111ll1l11l_opy_
from bstack_utils.bstack1lllll1lll_opy_ import bstack1lllll1lll_opy_
from bstack_utils.helper import bstack1l1ll11l_opy_, bstack11ll11111l_opy_, bstack1lll1ll1_opy_, bstack111lll1ll1_opy_, bstack111lll111l_opy_, bstack1ll1llll1_opy_, get_host_info, bstack111ll1ll1l_opy_, bstack1ll1ll111_opy_, bstack11l1l1ll1l_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack11l1l1ll1l_opy_(class_method=False)
def _111llllll1_opy_(driver, bstack11l111l1ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111l1l_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧཝ"): caps.get(bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ཞ"), None),
        bstack111l1l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬཟ"): bstack11l111l1ll_opy_.get(bstack111l1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬའ"), None),
        bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩཡ"): caps.get(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩར"), None),
        bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧལ"): caps.get(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧཤ"), None)
    }
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫཥ") + str(error))
  return response
def on():
    if os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ས"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧཧ")] == bstack111l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣཨ"):
        return False
    return True
def bstack111ll1l1l1_opy_(config):
  return config.get(bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཀྵ"), False) or any([p.get(bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬཪ"), False) == True for p in config.get(bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩཫ"), [])])
def bstack11lll1l1ll_opy_(config, bstack1ll11ll1_opy_):
  try:
    if not bstack1lll1ll1_opy_(config):
      return False
    bstack111lllllll_opy_ = config.get(bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧཬ"), False)
    if int(bstack1ll11ll1_opy_) < len(config.get(bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ཭"), [])) and config[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ཮")][bstack1ll11ll1_opy_]:
      bstack111lll11l1_opy_ = config[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭཯")][bstack1ll11ll1_opy_].get(bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ཰"), None)
    else:
      bstack111lll11l1_opy_ = config.get(bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽཱࠬ"), None)
    if bstack111lll11l1_opy_ != None:
      bstack111lllllll_opy_ = bstack111lll11l1_opy_
    bstack111ll1l1ll_opy_ = os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗིࠫ")) is not None and len(os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘཱིࠬ"))) > 0 and os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍུ࡛࡙࠭")) != bstack111l1l_opy_ (u"ࠩࡱࡹࡱࡲཱུࠧ")
    return bstack111lllllll_opy_ and bstack111ll1l1ll_opy_
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪྲྀ") + str(error))
  return False
def bstack1lll1ll1ll_opy_(test_tags):
  bstack111lll1lll_opy_ = os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཷ"))
  if bstack111lll1lll_opy_ is None:
    return True
  bstack111lll1lll_opy_ = json.loads(bstack111lll1lll_opy_)
  try:
    include_tags = bstack111lll1lll_opy_[bstack111l1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪླྀ")] if bstack111l1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫཹ") in bstack111lll1lll_opy_ and isinstance(bstack111lll1lll_opy_[bstack111l1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩེࠬ")], list) else []
    exclude_tags = bstack111lll1lll_opy_[bstack111l1l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪཻ࠭")] if bstack111l1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ོࠧ") in bstack111lll1lll_opy_ and isinstance(bstack111lll1lll_opy_[bstack111l1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨཽ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦཾ") + str(error))
  return False
def bstack11l1111111_opy_(config, bstack111lllll11_opy_, bstack111ll1ll11_opy_, bstack111ll11lll_opy_):
  bstack111llll11l_opy_ = bstack111lll1ll1_opy_(config)
  bstack111llll111_opy_ = bstack111lll111l_opy_(config)
  if bstack111llll11l_opy_ is None or bstack111llll111_opy_ is None:
    logger.error(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭ཿ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒྀࠧ"), bstack111l1l_opy_ (u"ࠧࡼࡿཱྀࠪ")))
    data = {
        bstack111l1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ྂ"): config[bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧྃ")],
        bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ྄࠭"): config.get(bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ྅"), os.path.basename(os.getcwd())),
        bstack111l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨ྆"): bstack1l1ll11l_opy_(),
        bstack111l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ྇"): config.get(bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪྈ"), bstack111l1l_opy_ (u"ࠨࠩྉ")),
        bstack111l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩྊ"): {
            bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪྋ"): bstack111lllll11_opy_,
            bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧྌ"): bstack111ll1ll11_opy_,
            bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩྍ"): __version__,
            bstack111l1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨྎ"): bstack111l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧྏ"),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨྐ"): bstack111l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫྑ"),
            bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪྒ"): bstack111ll11lll_opy_
        },
        bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ྒྷ"): settings,
        bstack111l1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭ྔ"): bstack111ll1ll1l_opy_(),
        bstack111l1l_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭ྕ"): bstack1ll1llll1_opy_(),
        bstack111l1l_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩྖ"): get_host_info(),
        bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪྗ"): bstack1lll1ll1_opy_(config)
    }
    headers = {
        bstack111l1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ྘"): bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ྙ"),
    }
    config = {
        bstack111l1l_opy_ (u"ࠫࡦࡻࡴࡩࠩྚ"): (bstack111llll11l_opy_, bstack111llll111_opy_),
        bstack111l1l_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ྛ"): headers
    }
    response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"࠭ࡐࡐࡕࡗࠫྜ"), bstack111ll1l11l_opy_ + bstack111l1l_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧྜྷ"), data, config)
    bstack111llll1l1_opy_ = response.json()
    if bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩྞ")]:
      parsed = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪྟ"), bstack111l1l_opy_ (u"ࠪࡿࢂ࠭ྠ")))
      parsed[bstack111l1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬྡ")] = bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪྡྷ")][bstack111l1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧྣ")]
      os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨྤ")] = json.dumps(parsed)
      bstack1lllll1lll_opy_.bstack111ll1l111_opy_(bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ྥ")][bstack111l1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪྦ")])
      bstack1lllll1lll_opy_.bstack111ll11l11_opy_(bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨྦྷ")][bstack111l1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ྨ")])
      bstack1lllll1lll_opy_.store()
      return bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪྩ")][bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫྪ")], bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠧࡥࡣࡷࡥࠬྫ")][bstack111l1l_opy_ (u"ࠨ࡫ࡧࠫྫྷ")]
    else:
      logger.error(bstack111l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪྭ") + bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫྮ")])
      if bstack111llll1l1_opy_[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬྯ")] == bstack111l1l_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧྰ"):
        for bstack111ll11l1l_opy_ in bstack111llll1l1_opy_[bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ྱ")]:
          logger.error(bstack111ll11l1l_opy_[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨྲ")])
      return None, None
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤླ") +  str(error))
    return None, None
def bstack111ll1llll_opy_():
  if os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧྴ")) is None:
    return {
        bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪྵ"): bstack111l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪྶ"),
        bstack111l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ྷ"): bstack111l1l_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬྸ")
    }
  data = {bstack111l1l_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨྐྵ"): bstack1l1ll11l_opy_()}
  headers = {
      bstack111l1l_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨྺ"): bstack111l1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪྻ") + os.getenv(bstack111l1l_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣྼ")),
      bstack111l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ྽"): bstack111l1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ྾")
  }
  response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"࠭ࡐࡖࡖࠪ྿"), bstack111ll1l11l_opy_ + bstack111l1l_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩ࿀"), data, { bstack111l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ࿁"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111l1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥ࿂") + bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"ࠪ࡞ࠬ࿃"))
      return {bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ࿄"): bstack111l1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭࿅"), bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫࿆ࠧ"): bstack111l1l_opy_ (u"ࠧࠨ࿇")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦ࿈") + str(error))
    return {
        bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ࿉"): bstack111l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ࿊"),
        bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ࿋"): str(error)
    }
def bstack11lll11l1l_opy_(caps, options, desired_capabilities={}):
  try:
    bstack111lll1l11_opy_ = caps.get(bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭࿌"), {}).get(bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ࿍"), caps.get(bstack111l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿎"), bstack111l1l_opy_ (u"ࠨࠩ࿏")))
    if bstack111lll1l11_opy_:
      logger.warn(bstack111l1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ࿐"))
      return False
    if options:
      bstack111ll1111l_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack111ll1111l_opy_ = desired_capabilities
    else:
      bstack111ll1111l_opy_ = {}
    browser = caps.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ࿑"), bstack111l1l_opy_ (u"ࠫࠬ࿒")).lower() or bstack111ll1111l_opy_.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ࿓"), bstack111l1l_opy_ (u"࠭ࠧ࿔")).lower()
    if browser != bstack111l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ࿕"):
      logger.warn(bstack111l1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ࿖"))
      return False
    browser_version = caps.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ࿗")) or caps.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿘")) or bstack111ll1111l_opy_.get(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ࿙")) or bstack111ll1111l_opy_.get(bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭࿚"), {}).get(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ࿛")) or bstack111ll1111l_opy_.get(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ࿜"), {}).get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿝"))
    if browser_version and browser_version != bstack111l1l_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩ࿞") and int(browser_version.split(bstack111l1l_opy_ (u"ࠪ࠲ࠬ࿟"))[0]) <= 98:
      logger.warn(bstack111l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥ࠿࠸࠯ࠤ࿠"))
      return False
    if not options:
      bstack111ll11ll1_opy_ = caps.get(bstack111l1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ࿡")) or bstack111ll1111l_opy_.get(bstack111l1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ࿢"), {})
      if bstack111l1l_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ࿣") in bstack111ll11ll1_opy_.get(bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭࿤"), []):
        logger.warn(bstack111l1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ࿥"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧ࿦") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack111lllll1l_opy_ = config.get(bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ࿧"), {})
    bstack111lllll1l_opy_[bstack111l1l_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ࿨")] = os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ࿩"))
    bstack111lll11ll_opy_ = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ࿪"), bstack111l1l_opy_ (u"ࠨࡽࢀࠫ࿫"))).get(bstack111l1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ࿬"))
    caps[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ࿭")] = True
    if bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ࿮") in caps:
      caps[bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭࿯")][bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭࿰")] = bstack111lllll1l_opy_
      caps[bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ࿱")][bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ࿲")][bstack111l1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ࿳")] = bstack111lll11ll_opy_
    else:
      caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ࿴")] = bstack111lllll1l_opy_
      caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ࿵")][bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭࿶")] = bstack111lll11ll_opy_
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ࿷") +  str(error))
def bstack1l1ll1ll1_opy_(driver, bstack111ll111ll_opy_):
  try:
    setattr(driver, bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ࿸"), True)
    session = driver.session_id
    if session:
      bstack111ll111l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack111ll111l1_opy_ = False
      bstack111ll111l1_opy_ = url.scheme in [bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࠨ࿹"), bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ࿺")]
      if bstack111ll111l1_opy_:
        if bstack111ll111ll_opy_:
          logger.info(bstack111l1l_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥ࿻"))
      return bstack111ll111ll_opy_
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ࿼") + str(e))
    return False
def bstack1ll1111l_opy_(driver, name, path):
  try:
    bstack111lll1111_opy_ = {
        bstack111l1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬ࿽"): threading.current_thread().current_test_uuid,
        bstack111l1l_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ࿾"): os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ࿿"), bstack111l1l_opy_ (u"ࠨࠩက")),
        bstack111l1l_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ခ"): os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫဂ"), bstack111l1l_opy_ (u"ࠫࠬဃ"))
    }
    logger.debug(bstack111l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨင"))
    logger.debug(driver.execute_async_script(bstack1lllll1lll_opy_.perform_scan, {bstack111l1l_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨစ"): name}))
    logger.debug(driver.execute_async_script(bstack1lllll1lll_opy_.bstack111ll1lll1_opy_, bstack111lll1111_opy_))
    logger.info(bstack111l1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥဆ"))
  except Exception as bstack111lll1l1l_opy_:
    logger.error(bstack111l1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥဇ") + str(path) + bstack111l1l_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦဈ") + str(bstack111lll1l1l_opy_))