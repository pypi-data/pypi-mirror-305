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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from browserstack_sdk.bstack1lll11lll1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lllllll1l_opy_
class bstack1llll1ll1l_opy_:
    def __init__(self, args, logger, bstack11l111ll1l_opy_, bstack11l111l111_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l111ll1l_opy_ = bstack11l111ll1l_opy_
        self.bstack11l111l111_opy_ = bstack11l111l111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lll11ll1l_opy_ = []
        self.bstack11l11l1111_opy_ = None
        self.bstack1ll1111ll1_opy_ = []
        self.bstack11l11l111l_opy_ = self.bstack1l1111l1l_opy_()
        self.bstack11l1lll1l_opy_ = -1
    def bstack1ll11llll1_opy_(self, bstack11l111l11l_opy_):
        self.parse_args()
        self.bstack11l111l1l1_opy_()
        self.bstack11l1111l1l_opy_(bstack11l111l11l_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11l11l1l1l_opy_():
        import importlib
        if getattr(importlib, bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱࡨࡤࡲ࡯ࡢࡦࡨࡶࠬ༴"), False):
            bstack11l1111lll_opy_ = importlib.find_loader(bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡵࡨࡰࡪࡴࡩࡶ࡯༵ࠪ"))
        else:
            bstack11l1111lll_opy_ = importlib.util.find_spec(bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ༶"))
    def bstack11l111llll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11l1lll1l_opy_ = -1
        if self.bstack11l111l111_opy_ and bstack111l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯༷ࠪ") in self.bstack11l111ll1l_opy_:
            self.bstack11l1lll1l_opy_ = int(self.bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ༸")])
        try:
            bstack11l11l11l1_opy_ = [bstack111l1l_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸ༹ࠧ"), bstack111l1l_opy_ (u"࠭࠭࠮ࡲ࡯ࡹ࡬࡯࡮ࡴࠩ༺"), bstack111l1l_opy_ (u"ࠧ࠮ࡲࠪ༻")]
            if self.bstack11l1lll1l_opy_ >= 0:
                bstack11l11l11l1_opy_.extend([bstack111l1l_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ༼"), bstack111l1l_opy_ (u"ࠩ࠰ࡲࠬ༽")])
            for arg in bstack11l11l11l1_opy_:
                self.bstack11l111llll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11l111l1l1_opy_(self):
        bstack11l11l1111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11l11l1111_opy_ = bstack11l11l1111_opy_
        return bstack11l11l1111_opy_
    def bstack1l1ll111ll_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11l11l1l1l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1lllllll1l_opy_)
    def bstack11l1111l1l_opy_(self, bstack11l111l11l_opy_):
        bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
        if bstack11l111l11l_opy_:
            self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ༾"))
            self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"࡙ࠫࡸࡵࡦࠩ༿"))
        if bstack1l1ll111_opy_.bstack11l11l1l11_opy_():
            self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫཀ"))
            self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"࠭ࡔࡳࡷࡨࠫཁ"))
        self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠧ࠮ࡲࠪག"))
        self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳ࠭གྷ"))
        self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫང"))
        self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪཅ"))
        if self.bstack11l1lll1l_opy_ > 1:
            self.bstack11l11l1111_opy_.append(bstack111l1l_opy_ (u"ࠫ࠲ࡴࠧཆ"))
            self.bstack11l11l1111_opy_.append(str(self.bstack11l1lll1l_opy_))
    def bstack11l11l11ll_opy_(self):
        bstack1ll1111ll1_opy_ = []
        for spec in self.bstack1lll11ll1l_opy_:
            bstack1l1l1l1l1_opy_ = [spec]
            bstack1l1l1l1l1_opy_ += self.bstack11l11l1111_opy_
            bstack1ll1111ll1_opy_.append(bstack1l1l1l1l1_opy_)
        self.bstack1ll1111ll1_opy_ = bstack1ll1111ll1_opy_
        return bstack1ll1111ll1_opy_
    def bstack1l1111l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11l11l111l_opy_ = True
            return True
        except Exception as e:
            self.bstack11l11l111l_opy_ = False
        return self.bstack11l11l111l_opy_
    def bstack1ll1ll11l1_opy_(self, bstack11l111lll1_opy_, bstack1ll11llll1_opy_):
        bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬཇ")] = self.bstack11l111ll1l_opy_
        multiprocessing.set_start_method(bstack111l1l_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ཈"))
        bstack1ll11l1ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lll1l11l1_opy_ = manager.list()
        if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪཉ") in self.bstack11l111ll1l_opy_:
            for index, platform in enumerate(self.bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫཊ")]):
                bstack1ll11l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11l111lll1_opy_,
                                                            args=(self.bstack11l11l1111_opy_, bstack1ll11llll1_opy_, bstack1lll1l11l1_opy_)))
            bstack11l111ll11_opy_ = len(self.bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬཋ")])
        else:
            bstack1ll11l1ll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11l111lll1_opy_,
                                                        args=(self.bstack11l11l1111_opy_, bstack1ll11llll1_opy_, bstack1lll1l11l1_opy_)))
            bstack11l111ll11_opy_ = 1
        i = 0
        for t in bstack1ll11l1ll_opy_:
            os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪཌ")] = str(i)
            if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧཌྷ") in self.bstack11l111ll1l_opy_:
                os.environ[bstack111l1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ཎ")] = json.dumps(self.bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩཏ")][i % bstack11l111ll11_opy_])
            i += 1
            t.start()
        for t in bstack1ll11l1ll_opy_:
            t.join()
        return list(bstack1lll1l11l1_opy_)
    @staticmethod
    def bstack1ll1ll11ll_opy_(driver, bstack11l111l1ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫཐ"), None)
        if item and getattr(item, bstack111l1l_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪད"), None) and not getattr(item, bstack111l1l_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫདྷ"), False):
            logger.info(
                bstack111l1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤན"))
            bstack11l1111ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l1l1lll_opy_.bstack1ll1111l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)