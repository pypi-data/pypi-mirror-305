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
import os
import logging
from uuid import uuid4
from bstack_utils.bstack11ll11l1l1_opy_ import bstack11ll11llll_opy_, bstack11ll11l111_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.helper import bstack1ll111l11_opy_, bstack1l1ll11l_opy_, Result
from bstack_utils.bstack1l111111ll_opy_ import bstack1l1l1ll1l_opy_
from bstack_utils.capture import bstack11ll1lll11_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack1l11l11ll_opy_:
    def __init__(self):
        self.bstack11ll1l1lll_opy_ = bstack11ll1lll11_opy_(self.bstack11ll1l111l_opy_)
        self.tests = {}
    @staticmethod
    def bstack11ll1l111l_opy_(log):
        if not (log[bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧป")] and log[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨผ")].strip()):
            return
        active = bstack1111lll1l_opy_.bstack11ll1lll1l_opy_()
        log = {
            bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧฝ"): log[bstack111l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨพ")],
            bstack111l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ฟ"): bstack1l1ll11l_opy_(),
            bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬภ"): log[bstack111l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ม")],
        }
        if active:
            if active[bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫย")] == bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬร"):
                log[bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨฤ")] = active[bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩล")]
            elif active[bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨฦ")] == bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࠩว"):
                log[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬศ")] = active[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ษ")]
        bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_([log])
    def start_test(self, attrs):
        bstack11ll1l1l11_opy_ = uuid4().__str__()
        self.tests[bstack11ll1l1l11_opy_] = {}
        self.bstack11ll1l1lll_opy_.start()
        driver = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ส"), None)
        bstack11ll11l1l1_opy_ = bstack11ll11l111_opy_(
            name=attrs.scenario.name,
            uuid=bstack11ll1l1l11_opy_,
            bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
            file_path=attrs.feature.filename,
            result=bstack111l1l_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤห"),
            framework=bstack111l1l_opy_ (u"ࠩࡅࡩ࡭ࡧࡶࡦࠩฬ"),
            scope=[attrs.feature.name],
            bstack11ll111lll_opy_=bstack1l1l1ll1l_opy_.bstack11ll11ll11_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[bstack11ll1l1l11_opy_][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭อ")] = bstack11ll11l1l1_opy_
        threading.current_thread().current_test_uuid = bstack11ll1l1l11_opy_
        bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬฮ"), bstack11ll11l1l1_opy_)
    def end_test(self, attrs):
        bstack11ll1ll1l1_opy_ = {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥฯ"): attrs.feature.name,
            bstack111l1l_opy_ (u"ࠨࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦะ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack11ll11l1l1_opy_ = self.tests[current_test_uuid][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪั")]
        meta = {
            bstack111l1l_opy_ (u"ࠣࡨࡨࡥࡹࡻࡲࡦࠤา"): bstack11ll1ll1l1_opy_,
            bstack111l1l_opy_ (u"ࠤࡶࡸࡪࡶࡳࠣำ"): bstack11ll11l1l1_opy_.meta.get(bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩิ"), []),
            bstack111l1l_opy_ (u"ࠦࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨี"): {
                bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥึ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack11ll11l1l1_opy_.bstack11ll1l1111_opy_(meta)
        bstack11ll11l1l1_opy_.bstack11ll1l11l1_opy_(bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫื"), []))
        bstack11ll1lllll_opy_, exception = self._11lll11111_opy_(attrs)
        bstack11ll11ll1l_opy_ = Result(result=attrs.status.name, exception=exception, bstack11ll11lll1_opy_=[bstack11ll1lllll_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣุࠪ")].stop(time=bstack1l1ll11l_opy_(), duration=int(attrs.duration)*1000, result=bstack11ll11ll1l_opy_)
        bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦูࠪ"), self.tests[threading.current_thread().current_test_uuid][bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥฺࠬ")])
    def bstack11l111ll_opy_(self, attrs):
        bstack11ll1l1l1l_opy_ = {
            bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭฻"): uuid4().__str__(),
            bstack111l1l_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬ฼"): attrs.keyword,
            bstack111l1l_opy_ (u"ࠬࡹࡴࡦࡲࡢࡥࡷ࡭ࡵ࡮ࡧࡱࡸࠬ฽"): [],
            bstack111l1l_opy_ (u"࠭ࡴࡦࡺࡷࠫ฾"): attrs.name,
            bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ฿"): bstack1l1ll11l_opy_(),
            bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨเ"): bstack111l1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪแ"),
            bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨโ"): bstack111l1l_opy_ (u"ࠫࠬใ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨไ")].add_step(bstack11ll1l1l1l_opy_)
        threading.current_thread().current_step_uuid = bstack11ll1l1l1l_opy_[bstack111l1l_opy_ (u"࠭ࡩࡥࠩๅ")]
    def bstack1l1ll1l1_opy_(self, attrs):
        current_test_id = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫๆ"), None)
        current_step_uuid = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡸࡪࡶ࡟ࡶࡷ࡬ࡨࠬ็"), None)
        bstack11ll1lllll_opy_, exception = self._11lll11111_opy_(attrs)
        bstack11ll11ll1l_opy_ = Result(result=attrs.status.name, exception=exception, bstack11ll11lll1_opy_=[bstack11ll1lllll_opy_])
        self.tests[current_test_id][bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥ่ࠬ")].bstack11ll1ll111_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack11ll11ll1l_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack1l1ll1ll1l_opy_(self, name, attrs):
        try:
            bstack11ll1l1ll1_opy_ = uuid4().__str__()
            self.tests[bstack11ll1l1ll1_opy_] = {}
            self.bstack11ll1l1lll_opy_.start()
            scopes = []
            driver = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳ้ࠩ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴ๊ࠩ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11ll1l1ll1_opy_)
            if name in [bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ๋"), bstack111l1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤ์")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack111l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣํ"), bstack111l1l_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠣ๎")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack111l1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪ๏")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack11ll11llll_opy_(
                name=name,
                uuid=bstack11ll1l1ll1_opy_,
                bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
                file_path=file_path,
                framework=bstack111l1l_opy_ (u"ࠥࡆࡪ࡮ࡡࡷࡧࠥ๐"),
                bstack11ll111lll_opy_=bstack1l1l1ll1l_opy_.bstack11ll11ll11_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack111l1l_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧ๑"),
                hook_type=name
            )
            self.tests[bstack11ll1l1ll1_opy_][bstack111l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡦࡺࡡࠣ๒")] = hook_data
            current_test_id = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠥ๓"), None)
            if current_test_id:
                hook_data.bstack11ll11l11l_opy_(current_test_id)
            if name == bstack111l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ๔"):
                threading.current_thread().before_all_hook_uuid = bstack11ll1l1ll1_opy_
            threading.current_thread().current_hook_uuid = bstack11ll1l1ll1_opy_
            bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠣࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠤ๕"), hook_data)
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣ࡭ࡳࠦࡳࡵࡣࡵࡸࠥ࡮࡯ࡰ࡭ࠣࡩࡻ࡫࡮ࡵࡵ࠯ࠤ࡭ࡵ࡯࡬ࠢࡱࡥࡲ࡫࠺ࠡࠧࡶ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠫࡳࠣ๖"), name, e)
    def bstack1ll11lllll_opy_(self, attrs):
        bstack11ll1ll1ll_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ๗"), None)
        hook_data = self.tests[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ๘")]
        status = bstack111l1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ๙")
        exception = None
        bstack11ll1lllll_opy_ = None
        if hook_data.name == bstack111l1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤ๚"):
            self.bstack11ll1l1lll_opy_.reset()
            bstack11ll11l1ll_opy_ = self.tests[bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ๛"), None)][bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ๜")].result.result
            if bstack11ll11l1ll_opy_ == bstack111l1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ๝"):
                if attrs.hook_failures == 1:
                    status = bstack111l1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ๞")
                elif attrs.hook_failures == 2:
                    status = bstack111l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ๟")
            elif attrs.bstack11ll1llll1_opy_:
                status = bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ๠")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack111l1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪ๡") and attrs.hook_failures == 1:
                status = bstack111l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ๢")
            elif hasattr(attrs, bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨ๣")) and attrs.error_message:
                status = bstack111l1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ๤")
            bstack11ll1lllll_opy_, exception = self._11lll11111_opy_(attrs)
        bstack11ll11ll1l_opy_ = Result(result=status, exception=exception, bstack11ll11lll1_opy_=[bstack11ll1lllll_opy_])
        hook_data.stop(time=bstack1l1ll11l_opy_(), duration=0, result=bstack11ll11ll1l_opy_)
        bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ๥"), self.tests[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ๦")])
        threading.current_thread().current_hook_uuid = None
    def _11lll11111_opy_(self, attrs):
        try:
            import traceback
            bstack1ll111l1_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11ll1lllll_opy_ = bstack1ll111l1_opy_[-1] if bstack1ll111l1_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡵࡷࡳࡲࠦࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࠤ๧"))
            bstack11ll1lllll_opy_ = None
            exception = None
        return bstack11ll1lllll_opy_, exception