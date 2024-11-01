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
from browserstack_sdk.bstack1l111l1l11_opy_ import bstack1llll1ll1l_opy_
from browserstack_sdk.bstack11l1l11l11_opy_ import RobotHandler
def bstack1l1l1l111l_opy_(framework):
    if framework.lower() == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩཙ"):
        return bstack1llll1ll1l_opy_.version()
    elif framework.lower() == bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩཚ"):
        return RobotHandler.version()
    elif framework.lower() == bstack111l1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫཛ"):
        import behave
        return behave.__version__
    else:
        return bstack111l1l_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳ࠭ཛྷ")