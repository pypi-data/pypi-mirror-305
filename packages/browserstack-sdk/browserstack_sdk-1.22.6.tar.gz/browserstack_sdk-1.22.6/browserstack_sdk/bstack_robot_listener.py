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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11l1l11l11_opy_ import RobotHandler
from bstack_utils.capture import bstack11ll1lll11_opy_
from bstack_utils.bstack11ll11l1l1_opy_ import bstack11l1llllll_opy_, bstack11ll11llll_opy_, bstack11ll11l111_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.bstack1l111111ll_opy_ import bstack1l1l1ll1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1ll111l11_opy_, bstack1l1ll11l_opy_, Result, \
    bstack11l1l1ll1l_opy_, bstack11ll11111l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ๨"): [],
        bstack111l1l_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭๩"): [],
        bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ๪"): []
    }
    bstack11l1ll11ll_opy_ = []
    bstack11ll111l11_opy_ = []
    @staticmethod
    def bstack11ll1l111l_opy_(log):
        if not (log[bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ๫")] and log[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ๬")].strip()):
            return
        active = bstack1111lll1l_opy_.bstack11ll1lll1l_opy_()
        log = {
            bstack111l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ๭"): log[bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ๮")],
            bstack111l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ๯"): bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"࡛ࠧࠩ๰"),
            bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ๱"): log[bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ๲")],
        }
        if active:
            if active[bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨ๳")] == bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ๴"):
                log[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ๵")] = active[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭๶")]
            elif active[bstack111l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬ๷")] == bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭๸"):
                log[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๹")] = active[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ๺")]
        bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._11l11ll1l1_opy_ = None
        self._11l1lll111_opy_ = None
        self._11l1l1111l_opy_ = OrderedDict()
        self.bstack11ll1l1lll_opy_ = bstack11ll1lll11_opy_(self.bstack11ll1l111l_opy_)
    @bstack11l1l1ll1l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11l1lll1ll_opy_()
        if not self._11l1l1111l_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧ๻")), None):
            self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨ๼"))] = {}
        bstack11l11ll111_opy_ = bstack11ll11l111_opy_(
                bstack11l1ll1111_opy_=attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩ๽")),
                name=name,
                bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
                file_path=os.path.relpath(attrs[bstack111l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ๾")], start=os.getcwd()) if attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ๿")) != bstack111l1l_opy_ (u"ࠩࠪ຀") else bstack111l1l_opy_ (u"ࠪࠫກ"),
                framework=bstack111l1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪຂ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨ຃"), None)
        self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩຄ"))][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ຅")] = bstack11l11ll111_opy_
    @bstack11l1l1ll1l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11l1l11ll1_opy_()
        self._11l11lll11_opy_(messages)
        for bstack11ll1111l1_opy_ in self.bstack11l1ll11ll_opy_:
            bstack11ll1111l1_opy_[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪຆ")][bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨງ")].extend(self.store[bstack111l1l_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴࠩຈ")])
            bstack1l1l1ll1l_opy_.bstack11l1l1ll11_opy_(bstack11ll1111l1_opy_)
        self.bstack11l1ll11ll_opy_ = []
        self.store[bstack111l1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪຉ")] = []
    @bstack11l1l1ll1l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11ll1l1lll_opy_.start()
        if not self._11l1l1111l_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨຊ")), None):
            self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩ຋"))] = {}
        driver = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ຌ"), None)
        bstack11ll11l1l1_opy_ = bstack11ll11l111_opy_(
            bstack11l1ll1111_opy_=attrs.get(bstack111l1l_opy_ (u"ࠨ࡫ࡧࠫຍ")),
            name=name,
            bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
            file_path=os.path.relpath(attrs[bstack111l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩຎ")], start=os.getcwd()),
            scope=RobotHandler.bstack11l1l1l111_opy_(attrs.get(bstack111l1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪຏ"), None)),
            framework=bstack111l1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪຐ"),
            tags=attrs[bstack111l1l_opy_ (u"ࠬࡺࡡࡨࡵࠪຑ")],
            hooks=self.store[bstack111l1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬຒ")],
            bstack11ll111lll_opy_=bstack1l1l1ll1l_opy_.bstack11ll11ll11_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack111l1l_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤຓ").format(bstack111l1l_opy_ (u"ࠣࠢࠥດ").join(attrs[bstack111l1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧຕ")]), name) if attrs[bstack111l1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨຖ")] else name
        )
        self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧທ"))][bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨຘ")] = bstack11ll11l1l1_opy_
        threading.current_thread().current_test_uuid = bstack11ll11l1l1_opy_.bstack11l11lllll_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩນ"), None)
        self.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨບ"), bstack11ll11l1l1_opy_)
    @bstack11l1l1ll1l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11ll1l1lll_opy_.reset()
        bstack11l1l1l1ll_opy_ = bstack11l11lll1l_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨປ")), bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪຜ"))
        self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ຝ"))][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧພ")].stop(time=bstack1l1ll11l_opy_(), duration=int(attrs.get(bstack111l1l_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪຟ"), bstack111l1l_opy_ (u"࠭࠰ࠨຠ"))), result=Result(result=bstack11l1l1l1ll_opy_, exception=attrs.get(bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨມ")), bstack11ll11lll1_opy_=[attrs.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩຢ"))]))
        self.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫຣ"), self._11l1l1111l_opy_[attrs.get(bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭຤"))][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧລ")], True)
        self.store[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩ຦")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11l1l1ll1l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11l1lll1ll_opy_()
        current_test_id = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨວ"), None)
        bstack11l1l11111_opy_ = current_test_id if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩຨ"), None) else bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫຩ"), None)
        if attrs.get(bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧສ"), bstack111l1l_opy_ (u"ࠪࠫຫ")).lower() in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪຬ"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧອ")]:
            hook_type = bstack11l1l1llll_opy_(attrs.get(bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫຮ")), bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫຯ"), None))
            hook_name = bstack111l1l_opy_ (u"ࠨࡽࢀࠫະ").format(attrs.get(bstack111l1l_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩັ"), bstack111l1l_opy_ (u"ࠪࠫາ")))
            if hook_type in [bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨຳ"), bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨິ")]:
                hook_name = bstack111l1l_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧີ").format(bstack11l1llll1l_opy_.get(hook_type), attrs.get(bstack111l1l_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧຶ"), bstack111l1l_opy_ (u"ࠨࠩື")))
            bstack11l1ll1lll_opy_ = bstack11ll11llll_opy_(
                bstack11l1ll1111_opy_=bstack11l1l11111_opy_ + bstack111l1l_opy_ (u"ࠩ࠰ຸࠫ") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨູ"), bstack111l1l_opy_ (u"຺ࠫࠬ")).lower(),
                name=hook_name,
                bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
                file_path=os.path.relpath(attrs.get(bstack111l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬົ")), start=os.getcwd()),
                framework=bstack111l1l_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬຼ"),
                tags=attrs[bstack111l1l_opy_ (u"ࠧࡵࡣࡪࡷࠬຽ")],
                scope=RobotHandler.bstack11l1l1l111_opy_(attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ຾"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11l1ll1lll_opy_.bstack11l11lllll_opy_()
            threading.current_thread().current_hook_id = bstack11l1l11111_opy_ + bstack111l1l_opy_ (u"ࠩ࠰ࠫ຿") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨເ"), bstack111l1l_opy_ (u"ࠫࠬແ")).lower()
            self.store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩໂ")] = [bstack11l1ll1lll_opy_.bstack11l11lllll_opy_()]
            if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪໃ"), None):
                self.store[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫໄ")].append(bstack11l1ll1lll_opy_.bstack11l11lllll_opy_())
            else:
                self.store[bstack111l1l_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧ໅")].append(bstack11l1ll1lll_opy_.bstack11l11lllll_opy_())
            if bstack11l1l11111_opy_:
                self._11l1l1111l_opy_[bstack11l1l11111_opy_ + bstack111l1l_opy_ (u"ࠩ࠰ࠫໆ") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨ໇"), bstack111l1l_opy_ (u"່ࠫࠬ")).lower()] = { bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ້"): bstack11l1ll1lll_opy_ }
            bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪ໊ࠧ"), bstack11l1ll1lll_opy_)
        else:
            bstack11ll1l1l1l_opy_ = {
                bstack111l1l_opy_ (u"ࠧࡪࡦ໋ࠪ"): uuid4().__str__(),
                bstack111l1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭໌"): bstack111l1l_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨໍ").format(attrs.get(bstack111l1l_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ໎")), attrs.get(bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ໏"), bstack111l1l_opy_ (u"ࠬ࠭໐"))) if attrs.get(bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ໑"), []) else attrs.get(bstack111l1l_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧ໒")),
                bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨ໓"): attrs.get(bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ໔"), []),
                bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ໕"): bstack1l1ll11l_opy_(),
                bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ໖"): bstack111l1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭໗"),
                bstack111l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ໘"): attrs.get(bstack111l1l_opy_ (u"ࠧࡥࡱࡦࠫ໙"), bstack111l1l_opy_ (u"ࠨࠩ໚"))
            }
            if attrs.get(bstack111l1l_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪ໛"), bstack111l1l_opy_ (u"ࠪࠫໜ")) != bstack111l1l_opy_ (u"ࠫࠬໝ"):
                bstack11ll1l1l1l_opy_[bstack111l1l_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ໞ")] = attrs.get(bstack111l1l_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࠧໟ"))
            if not self.bstack11ll111l11_opy_:
                self._11l1l1111l_opy_[self._11l1l11l1l_opy_()][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ໠")].add_step(bstack11ll1l1l1l_opy_)
                threading.current_thread().current_step_uuid = bstack11ll1l1l1l_opy_[bstack111l1l_opy_ (u"ࠨ࡫ࡧࠫ໡")]
            self.bstack11ll111l11_opy_.append(bstack11ll1l1l1l_opy_)
    @bstack11l1l1ll1l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11l1l11ll1_opy_()
        self._11l11lll11_opy_(messages)
        current_test_id = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫ໢"), None)
        bstack11l1l11111_opy_ = current_test_id if current_test_id else bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭໣"), None)
        bstack11l11ll11l_opy_ = bstack11l11lll1l_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ໤")), bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭໥"))
        bstack11l1l111ll_opy_ = attrs.get(bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ໦"))
        if bstack11l11ll11l_opy_ != bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ໧") and not attrs.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ໨")) and self._11l11ll1l1_opy_:
            bstack11l1l111ll_opy_ = self._11l11ll1l1_opy_
        bstack11ll11ll1l_opy_ = Result(result=bstack11l11ll11l_opy_, exception=bstack11l1l111ll_opy_, bstack11ll11lll1_opy_=[bstack11l1l111ll_opy_])
        if attrs.get(bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ໩"), bstack111l1l_opy_ (u"ࠪࠫ໪")).lower() in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ໫"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ໬")]:
            bstack11l1l11111_opy_ = current_test_id if current_test_id else bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩ໭"), None)
            if bstack11l1l11111_opy_:
                bstack11ll1ll1ll_opy_ = bstack11l1l11111_opy_ + bstack111l1l_opy_ (u"ࠢ࠮ࠤ໮") + attrs.get(bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭໯"), bstack111l1l_opy_ (u"ࠩࠪ໰")).lower()
                self._11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭໱")].stop(time=bstack1l1ll11l_opy_(), duration=int(attrs.get(bstack111l1l_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩ໲"), bstack111l1l_opy_ (u"ࠬ࠶ࠧ໳"))), result=bstack11ll11ll1l_opy_)
                bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ໴"), self._11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ໵")])
        else:
            bstack11l1l11111_opy_ = current_test_id if current_test_id else bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪ໶"), None)
            if bstack11l1l11111_opy_ and len(self.bstack11ll111l11_opy_) == 1:
                current_step_uuid = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭໷"), None)
                self._11l1l1111l_opy_[bstack11l1l11111_opy_][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭໸")].bstack11ll1ll111_opy_(current_step_uuid, duration=int(attrs.get(bstack111l1l_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩ໹"), bstack111l1l_opy_ (u"ࠬ࠶ࠧ໺"))), result=bstack11ll11ll1l_opy_)
            else:
                self.bstack11l1l11lll_opy_(attrs)
            self.bstack11ll111l11_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack111l1l_opy_ (u"࠭ࡨࡵ࡯࡯ࠫ໻"), bstack111l1l_opy_ (u"ࠧ࡯ࡱࠪ໼")) == bstack111l1l_opy_ (u"ࠨࡻࡨࡷࠬ໽"):
                return
            self.messages.push(message)
            bstack11l1lll11l_opy_ = []
            if bstack1111lll1l_opy_.bstack11ll1lll1l_opy_():
                bstack11l1lll11l_opy_.append({
                    bstack111l1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ໾"): bstack1l1ll11l_opy_(),
                    bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ໿"): message.get(bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬༀ")),
                    bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ༁"): message.get(bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ༂")),
                    **bstack1111lll1l_opy_.bstack11ll1lll1l_opy_()
                })
                if len(bstack11l1lll11l_opy_) > 0:
                    bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_(bstack11l1lll11l_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1l1l1ll1l_opy_.bstack11l11l1lll_opy_()
    def bstack11l1l11lll_opy_(self, bstack11ll111ll1_opy_):
        if not bstack1111lll1l_opy_.bstack11ll1lll1l_opy_():
            return
        kwname = bstack111l1l_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭༃").format(bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨ༄")), bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ༅"), bstack111l1l_opy_ (u"ࠪࠫ༆"))) if bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ༇"), []) else bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬ༈"))
        error_message = bstack111l1l_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧ༉").format(kwname, bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ༊")), str(bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ་"))))
        bstack11l11ll1ll_opy_ = bstack111l1l_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣ༌").format(kwname, bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ།")))
        bstack11l1lll1l1_opy_ = error_message if bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༎")) else bstack11l11ll1ll_opy_
        bstack11l11l1ll1_opy_ = {
            bstack111l1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ༏"): self.bstack11ll111l11_opy_[-1].get(bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ༐"), bstack1l1ll11l_opy_()),
            bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ༑"): bstack11l1lll1l1_opy_,
            bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ༒"): bstack111l1l_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨ༓") if bstack11ll111ll1_opy_.get(bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ༔")) == bstack111l1l_opy_ (u"ࠫࡋࡇࡉࡍࠩ༕") else bstack111l1l_opy_ (u"ࠬࡏࡎࡇࡑࠪ༖"),
            **bstack1111lll1l_opy_.bstack11ll1lll1l_opy_()
        }
        bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_([bstack11l11l1ll1_opy_])
    def _11l1l11l1l_opy_(self):
        for bstack11l1ll1111_opy_ in reversed(self._11l1l1111l_opy_):
            bstack11l1llll11_opy_ = bstack11l1ll1111_opy_
            data = self._11l1l1111l_opy_[bstack11l1ll1111_opy_][bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ༗")]
            if isinstance(data, bstack11ll11llll_opy_):
                if not bstack111l1l_opy_ (u"ࠧࡆࡃࡆࡌ༘ࠬ") in data.bstack11ll111111_opy_():
                    return bstack11l1llll11_opy_
            else:
                return bstack11l1llll11_opy_
    def _11l11lll11_opy_(self, messages):
        try:
            bstack11ll1111ll_opy_ = BuiltIn().get_variable_value(bstack111l1l_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃ༙ࠢ")) in (bstack11l1ll1l11_opy_.DEBUG, bstack11l1ll1l11_opy_.TRACE)
            for message, bstack11ll111l1l_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ༚"))
                level = message.get(bstack111l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ༛"))
                if level == bstack11l1ll1l11_opy_.FAIL:
                    self._11l11ll1l1_opy_ = name or self._11l11ll1l1_opy_
                    self._11l1lll111_opy_ = bstack11ll111l1l_opy_.get(bstack111l1l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧ༜")) if bstack11ll1111ll_opy_ and bstack11ll111l1l_opy_ else self._11l1lll111_opy_
        except:
            pass
    @classmethod
    def bstack11ll1l11ll_opy_(self, event: str, bstack11l1l1l1l1_opy_: bstack11l1llllll_opy_, bstack11l11llll1_opy_=False):
        if event == bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ༝"):
            bstack11l1l1l1l1_opy_.set(hooks=self.store[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ༞")])
        if event == bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ༟"):
            event = bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ༠")
        if bstack11l11llll1_opy_:
            bstack11l1l111l1_opy_ = {
                bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭༡"): event,
                bstack11l1l1l1l1_opy_.bstack11l1lllll1_opy_(): bstack11l1l1l1l1_opy_.bstack11l1ll11l1_opy_(event)
            }
            self.bstack11l1ll11ll_opy_.append(bstack11l1l111l1_opy_)
        else:
            bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(event, bstack11l1l1l1l1_opy_)
class Messages:
    def __init__(self):
        self._11l1ll1l1l_opy_ = []
    def bstack11l1lll1ll_opy_(self):
        self._11l1ll1l1l_opy_.append([])
    def bstack11l1l11ll1_opy_(self):
        return self._11l1ll1l1l_opy_.pop() if self._11l1ll1l1l_opy_ else list()
    def push(self, message):
        self._11l1ll1l1l_opy_[-1].append(message) if self._11l1ll1l1l_opy_ else self._11l1ll1l1l_opy_.append([message])
class bstack11l1ll1l11_opy_:
    FAIL = bstack111l1l_opy_ (u"ࠪࡊࡆࡏࡌࠨ༢")
    ERROR = bstack111l1l_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪ༣")
    WARNING = bstack111l1l_opy_ (u"ࠬ࡝ࡁࡓࡐࠪ༤")
    bstack11l1ll1ll1_opy_ = bstack111l1l_opy_ (u"࠭ࡉࡏࡈࡒࠫ༥")
    DEBUG = bstack111l1l_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭༦")
    TRACE = bstack111l1l_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧ༧")
    bstack11l1l1l11l_opy_ = [FAIL, ERROR]
def bstack11l1ll111l_opy_(bstack11l1l1lll1_opy_):
    if not bstack11l1l1lll1_opy_:
        return None
    if bstack11l1l1lll1_opy_.get(bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ༨"), None):
        return getattr(bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭༩")], bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ༪"), None)
    return bstack11l1l1lll1_opy_.get(bstack111l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ༫"), None)
def bstack11l1l1llll_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༬"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ༭")]:
        return
    if hook_type.lower() == bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ༮"):
        if current_test_uuid is None:
            return bstack111l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭༯")
        else:
            return bstack111l1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨ༰")
    elif hook_type.lower() == bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭༱"):
        if current_test_uuid is None:
            return bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ༲")
        else:
            return bstack111l1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ༳")