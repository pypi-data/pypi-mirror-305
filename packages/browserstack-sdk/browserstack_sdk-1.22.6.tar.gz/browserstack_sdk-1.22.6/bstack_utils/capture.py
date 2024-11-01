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
import builtins
import logging
class bstack11ll1lll11_opy_:
    def __init__(self, handler):
        self._111l1ll11l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111l1l1l1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack111l1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪဧ"), bstack111l1l_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬဨ"), bstack111l1l_opy_ (u"ࠧࡸࡣࡵࡲ࡮ࡴࡧࠨဩ"), bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧဪ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111l1ll111_opy_
        self._111l1ll1l1_opy_()
    def _111l1ll111_opy_(self, *args, **kwargs):
        self._111l1ll11l_opy_(*args, **kwargs)
        message = bstack111l1l_opy_ (u"ࠩࠣࠫါ").join(map(str, args)) + bstack111l1l_opy_ (u"ࠪࡠࡳ࠭ာ")
        self._log_message(bstack111l1l_opy_ (u"ࠫࡎࡔࡆࡐࠩိ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫီ"): level, bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧု"): msg})
    def _111l1ll1l1_opy_(self):
        for level, bstack111l1l1lll_opy_ in self._111l1l1l1l_opy_.items():
            setattr(logging, level, self._111l1l1ll1_opy_(level, bstack111l1l1lll_opy_))
    def _111l1l1ll1_opy_(self, level, bstack111l1l1lll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111l1l1lll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111l1ll11l_opy_
        for level, bstack111l1l1lll_opy_ in self._111l1l1l1l_opy_.items():
            setattr(logging, level, bstack111l1l1lll_opy_)