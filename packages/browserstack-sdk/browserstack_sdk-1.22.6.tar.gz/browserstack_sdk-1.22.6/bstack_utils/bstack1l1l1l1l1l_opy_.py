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
import threading
import logging
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from bstack_utils.helper import bstack1ll111l11_opy_
logger = logging.getLogger(__name__)
def bstack1ll11ll111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1lll11ll_opy_(context, *args):
    tags = getattr(args[0], bstack111l1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨသ"), [])
    bstack1l1lllllll_opy_ = bstack1l1l1lll_opy_.bstack1lll1ll1ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l1lllllll_opy_
    try:
      bstack1ll1l11l11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll11ll111_opy_(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪဟ")) else context.browser
      if bstack1ll1l11l11_opy_ and bstack1ll1l11l11_opy_.session_id and bstack1l1lllllll_opy_ and bstack1ll111l11_opy_(
              threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫဠ"), None):
          threading.current_thread().isA11yTest = bstack1l1l1lll_opy_.bstack1l1ll1ll1_opy_(bstack1ll1l11l11_opy_, bstack1l1lllllll_opy_)
    except Exception as e:
       logger.debug(bstack111l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡣ࠴࠵ࡾࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭အ").format(str(e)))
def bstack1111l1ll_opy_(bstack1ll1l11l11_opy_):
    if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫဢ"), None) and bstack1ll111l11_opy_(
      threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧဣ"), None) and not bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࠬဤ"), False):
      threading.current_thread().a11y_stop = True
      bstack1l1l1lll_opy_.bstack1ll1111l_opy_(bstack1ll1l11l11_opy_, name=bstack111l1l_opy_ (u"ࠥࠦဥ"), path=bstack111l1l_opy_ (u"ࠦࠧဦ"))