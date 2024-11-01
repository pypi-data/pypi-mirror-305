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
class bstack11llll1ll1_opy_:
    def __init__(self, handler):
        self._1ll1ll111ll_opy_ = None
        self.handler = handler
        self._1ll1ll11l11_opy_ = self.bstack1ll1ll1111l_opy_()
        self.patch()
    def patch(self):
        self._1ll1ll111ll_opy_ = self._1ll1ll11l11_opy_.execute
        self._1ll1ll11l11_opy_.execute = self.bstack1ll1ll111l1_opy_()
    def bstack1ll1ll111l1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࠦᘿ"), driver_command, None, this, args)
            response = self._1ll1ll111ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack111l1l_opy_ (u"ࠧࡧࡦࡵࡧࡵࠦᙀ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1ll1ll11l11_opy_.execute = self._1ll1ll111ll_opy_
    @staticmethod
    def bstack1ll1ll1111l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver