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
from collections import deque
from bstack_utils.constants import *
class bstack1l11ll1l11_opy_:
    def __init__(self):
        self._1lll111l1l1_opy_ = deque()
        self._1lll111l11l_opy_ = {}
        self._1lll111l1ll_opy_ = False
    def bstack1lll11l11ll_opy_(self, test_name, bstack1lll111lll1_opy_):
        bstack1lll111ll1l_opy_ = self._1lll111l11l_opy_.get(test_name, {})
        return bstack1lll111ll1l_opy_.get(bstack1lll111lll1_opy_, 0)
    def bstack1lll111ll11_opy_(self, test_name, bstack1lll111lll1_opy_):
        bstack1lll111l111_opy_ = self.bstack1lll11l11ll_opy_(test_name, bstack1lll111lll1_opy_)
        self.bstack1lll11l111l_opy_(test_name, bstack1lll111lll1_opy_)
        return bstack1lll111l111_opy_
    def bstack1lll11l111l_opy_(self, test_name, bstack1lll111lll1_opy_):
        if test_name not in self._1lll111l11l_opy_:
            self._1lll111l11l_opy_[test_name] = {}
        bstack1lll111ll1l_opy_ = self._1lll111l11l_opy_[test_name]
        bstack1lll111l111_opy_ = bstack1lll111ll1l_opy_.get(bstack1lll111lll1_opy_, 0)
        bstack1lll111ll1l_opy_[bstack1lll111lll1_opy_] = bstack1lll111l111_opy_ + 1
    def bstack1l1l11ll1_opy_(self, bstack1lll11l11l1_opy_, bstack1lll1111lll_opy_):
        bstack1lll11l1l11_opy_ = self.bstack1lll111ll11_opy_(bstack1lll11l11l1_opy_, bstack1lll1111lll_opy_)
        bstack1lll111llll_opy_ = bstack111l111l11_opy_[bstack1lll1111lll_opy_]
        bstack1lll11l1111_opy_ = bstack111l1l_opy_ (u"ࠧࢁࡽ࠮ࡽࢀ࠱ࢀࢃࠢᗥ").format(bstack1lll11l11l1_opy_, bstack1lll111llll_opy_, bstack1lll11l1l11_opy_)
        self._1lll111l1l1_opy_.append(bstack1lll11l1111_opy_)
    def bstack111111l11_opy_(self):
        return len(self._1lll111l1l1_opy_) == 0
    def bstack1l111l1l1_opy_(self):
        bstack1lll1111ll1_opy_ = self._1lll111l1l1_opy_.popleft()
        return bstack1lll1111ll1_opy_
    def capturing(self):
        return self._1lll111l1ll_opy_
    def bstack1ll1lll111_opy_(self):
        self._1lll111l1ll_opy_ = True
    def bstack1111ll1l1_opy_(self):
        self._1lll111l1ll_opy_ = False