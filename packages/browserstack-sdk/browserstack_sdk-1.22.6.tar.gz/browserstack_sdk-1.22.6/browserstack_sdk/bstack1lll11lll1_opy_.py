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
class bstack1ll111lll_opy_(threading.Thread):
    def run(self):
        self.exc = None
        try:
            self.ret = self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exc = e
    def join(self, timeout=None):
        super(bstack1ll111lll_opy_, self).join(timeout)
        if self.exc:
            raise self.exc
        return self.ret