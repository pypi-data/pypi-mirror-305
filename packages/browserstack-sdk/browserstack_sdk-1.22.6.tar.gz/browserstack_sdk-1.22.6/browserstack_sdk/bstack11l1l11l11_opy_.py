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
class RobotHandler():
    def __init__(self, args, logger, bstack11l111ll1l_opy_, bstack11l111l111_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l111ll1l_opy_ = bstack11l111ll1l_opy_
        self.bstack11l111l111_opy_ = bstack11l111l111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11l1l1l111_opy_(bstack11l1111l11_opy_):
        bstack11l111111l_opy_ = []
        if bstack11l1111l11_opy_:
            tokens = str(os.path.basename(bstack11l1111l11_opy_)).split(bstack111l1l_opy_ (u"ࠦࡤࠨཔ"))
            camelcase_name = bstack111l1l_opy_ (u"ࠧࠦࠢཕ").join(t.title() for t in tokens)
            suite_name, bstack11l11111ll_opy_ = os.path.splitext(camelcase_name)
            bstack11l111111l_opy_.append(suite_name)
        return bstack11l111111l_opy_
    @staticmethod
    def bstack11l11111l1_opy_(typename):
        if bstack111l1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤབ") in typename:
            return bstack111l1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣབྷ")
        return bstack111l1l_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤམ")