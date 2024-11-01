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
import atexit
import datetime
import inspect
import logging
import os
import signal
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11l1ll1l1_opy_, bstack111l111ll_opy_, update, bstack1l1lll11l1_opy_,
                                       bstack11llll1l1l_opy_, bstack11l111l1_opy_, bstack1llll11l11_opy_, bstack1l1ll1lll_opy_,
                                       bstack1l1lll1l1_opy_, bstack1lllll11_opy_, bstack11llll111_opy_, bstack11lllllll_opy_,
                                       bstack11111lll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll1l1l1_opy_)
from browserstack_sdk.bstack1l111l1l11_opy_ import bstack1llll1ll1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1llll11lll_opy_
from bstack_utils.capture import bstack11ll1lll11_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1l11ll1l1_opy_, bstack1111l111l_opy_, bstack1lll1l1l1_opy_, \
    bstack1l1l1ll11l_opy_
from bstack_utils.helper import bstack1ll111l11_opy_, bstack1llllll1l11_opy_, bstack11ll11111l_opy_, bstack1ll11l111_opy_, bstack1lllllll1l1_opy_, bstack1l1ll11l_opy_, \
    bstack1lllllll111_opy_, \
    bstack1111l111l1_opy_, bstack1111ll1l_opy_, bstack1l1l11111_opy_, bstack1111ll11l1_opy_, bstack11llll1l_opy_, Notset, \
    bstack11l11111l_opy_, bstack1111l11l1l_opy_, bstack1111ll1lll_opy_, Result, bstack11111l1l11_opy_, bstack111l11111l_opy_, bstack11l1l1ll1l_opy_, \
    bstack1111l1111_opy_, bstack1lll1l111_opy_, bstack11ll111l_opy_, bstack111111l1ll_opy_
from bstack_utils.bstack1lllll1ll11_opy_ import bstack1lllll11l11_opy_
from bstack_utils.messages import bstack1l1ll1111_opy_, bstack1ll1llll11_opy_, bstack1ll1llll1l_opy_, bstack1l1l111ll1_opy_, bstack1lllllll1l_opy_, \
    bstack1l11l1ll1_opy_, bstack1lll1lllll_opy_, bstack1111llll1_opy_, bstack1l1ll1l11l_opy_, bstack11111l1ll_opy_, \
    bstack11llllllll_opy_, bstack1111ll111_opy_
from bstack_utils.proxy import bstack11lll1l11l_opy_, bstack1lll11l111_opy_
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1ll1lll1l1l_opy_, bstack1ll1lllll11_opy_, bstack1ll1lllll1l_opy_, bstack1ll1lll1l11_opy_, \
    bstack1ll1lll11l1_opy_, bstack1ll1lll11ll_opy_, bstack1ll1llllll1_opy_, bstack1l1lll1lll_opy_, bstack1ll1lll1ll1_opy_
from bstack_utils.bstack1l111l1lll_opy_ import bstack11llll1ll1_opy_
from bstack_utils.bstack111l1111_opy_ import bstack111l1l11l_opy_, bstack1111l111_opy_, bstack1l11l1l11l_opy_, \
    bstack1llll1llll_opy_, bstack11llll11l_opy_
from bstack_utils.bstack11ll11l1l1_opy_ import bstack11ll11l111_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from bstack_utils.bstack1l111111ll_opy_ import bstack1l1l1ll1l_opy_
from bstack_utils.bstack1lllll1lll_opy_ import bstack1lllll1lll_opy_
from browserstack_sdk.__init__ import bstack1111ll1ll_opy_
bstack1lll1llll_opy_ = None
bstack1ll11l1111_opy_ = None
bstack1l1llllll_opy_ = None
bstack1lll1l1ll_opy_ = None
bstack11llll1l11_opy_ = None
bstack1ll1lll1l_opy_ = None
bstack1lllll1l1l_opy_ = None
bstack1l1ll11ll1_opy_ = None
bstack1ll11l1l_opy_ = None
bstack1ll1l1ll11_opy_ = None
bstack11l1ll1ll_opy_ = None
bstack1l1l1lll11_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1l1111llll_opy_ = bstack111l1l_opy_ (u"ࠨࠩ៼")
CONFIG = {}
bstack1l111l11l_opy_ = False
bstack1l1ll11l11_opy_ = bstack111l1l_opy_ (u"ࠩࠪ៽")
bstack1l1ll1l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࠫ៾")
bstack1lll11l1_opy_ = False
bstack11ll11l1_opy_ = []
bstack111ll1l1l_opy_ = bstack1l11ll1l1_opy_
bstack1ll111l1ll1_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ៿")
bstack1ll1l11lll_opy_ = {}
bstack11l1lllll_opy_ = False
logger = bstack1llll11lll_opy_.get_logger(__name__, bstack111ll1l1l_opy_)
store = {
    bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᠀"): []
}
bstack1ll1111l1ll_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11l1l1111l_opy_ = {}
current_test_uuid = None
def bstack1l11l1l1_opy_(page, bstack111111l1_opy_):
    try:
        page.evaluate(bstack111l1l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ᠁"),
                      bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫ᠂") + json.dumps(
                          bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠣࡿࢀࠦ᠃"))
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢ᠄"), e)
def bstack111l11l11_opy_(page, message, level):
    try:
        page.evaluate(bstack111l1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ᠅"), bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ᠆") + json.dumps(
            message) + bstack111l1l_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ᠇") + json.dumps(level) + bstack111l1l_opy_ (u"࠭ࡽࡾࠩ᠈"))
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿࠥ᠉"), e)
def pytest_configure(config):
    bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
    config.args = bstack1111lll1l_opy_.bstack1ll111lll11_opy_(config.args)
    bstack1l1ll111_opy_.bstack11lll11l1_opy_(bstack11ll111l_opy_(config.getoption(bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ᠊"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1ll1111l111_opy_ = item.config.getoption(bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᠋"))
    plugins = item.config.getoption(bstack111l1l_opy_ (u"ࠥࡴࡱࡻࡧࡪࡰࡶࠦ᠌"))
    report = outcome.get_result()
    bstack1ll1111ll1l_opy_(item, call, report)
    if bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤ᠍") not in plugins or bstack11llll1l_opy_():
        return
    summary = []
    driver = getattr(item, bstack111l1l_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨ᠎"), None)
    page = getattr(item, bstack111l1l_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧ᠏"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1l1lllllll1_opy_(item, report, summary, bstack1ll1111l111_opy_)
    if (page is not None):
        bstack1ll11111l11_opy_(item, report, summary, bstack1ll1111l111_opy_)
def bstack1l1lllllll1_opy_(item, report, summary, bstack1ll1111l111_opy_):
    if report.when == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭᠐") and report.skipped:
        bstack1ll1lll1ll1_opy_(report)
    if report.when in [bstack111l1l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ᠑"), bstack111l1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦ᠒")]:
        return
    if not bstack1lllllll1l1_opy_():
        return
    try:
        if (str(bstack1ll1111l111_opy_).lower() != bstack111l1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ᠓")):
            item._driver.execute_script(
                bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ᠔") + json.dumps(
                    report.nodeid) + bstack111l1l_opy_ (u"ࠬࢃࡽࠨ᠕"))
        os.environ[bstack111l1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ᠖")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack111l1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢ᠗").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ᠘")))
    bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"ࠤࠥ᠙")
    bstack1ll1lll1ll1_opy_(report)
    if not passed:
        try:
            bstack1llll1lll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111l1l_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ᠚").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1llll1lll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ᠛")))
        bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"ࠧࠨ᠜")
        if not passed:
            try:
                bstack1llll1lll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ᠝").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1llll1lll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ᠞")
                    + json.dumps(bstack111l1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤ᠟"))
                    + bstack111l1l_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᠠ")
                )
            else:
                item._driver.execute_script(
                    bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᠡ")
                    + json.dumps(str(bstack1llll1lll_opy_))
                    + bstack111l1l_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᠢ")
                )
        except Exception as e:
            summary.append(bstack111l1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥᠣ").format(e))
def bstack1ll111l111l_opy_(test_name, error_message):
    try:
        bstack1ll1111l11l_opy_ = []
        bstack1ll11ll1_opy_ = os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᠤ"), bstack111l1l_opy_ (u"ࠧ࠱ࠩᠥ"))
        bstack1ll11111_opy_ = {bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᠦ"): test_name, bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᠧ"): error_message, bstack111l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᠨ"): bstack1ll11ll1_opy_}
        bstack1l1lllll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᠩ"))
        if os.path.exists(bstack1l1lllll1ll_opy_):
            with open(bstack1l1lllll1ll_opy_) as f:
                bstack1ll1111l11l_opy_ = json.load(f)
        bstack1ll1111l11l_opy_.append(bstack1ll11111_opy_)
        with open(bstack1l1lllll1ll_opy_, bstack111l1l_opy_ (u"ࠬࡽࠧᠪ")) as f:
            json.dump(bstack1ll1111l11l_opy_, f)
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫᠫ") + str(e))
def bstack1ll11111l11_opy_(item, report, summary, bstack1ll1111l111_opy_):
    if report.when in [bstack111l1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᠬ"), bstack111l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᠭ")]:
        return
    if (str(bstack1ll1111l111_opy_).lower() != bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᠮ")):
        bstack1l11l1l1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᠯ")))
    bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"ࠦࠧᠰ")
    bstack1ll1lll1ll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1llll1lll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᠱ").format(e)
                )
        try:
            if passed:
                bstack11llll11l_opy_(getattr(item, bstack111l1l_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᠲ"), None), bstack111l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᠳ"))
            else:
                error_message = bstack111l1l_opy_ (u"ࠨࠩᠴ")
                if bstack1llll1lll_opy_:
                    bstack111l11l11_opy_(item._page, str(bstack1llll1lll_opy_), bstack111l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣᠵ"))
                    bstack11llll11l_opy_(getattr(item, bstack111l1l_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᠶ"), None), bstack111l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᠷ"), str(bstack1llll1lll_opy_))
                    error_message = str(bstack1llll1lll_opy_)
                else:
                    bstack11llll11l_opy_(getattr(item, bstack111l1l_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᠸ"), None), bstack111l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᠹ"))
                bstack1ll111l111l_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack111l1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦᠺ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111l1l_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᠻ"), default=bstack111l1l_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣᠼ"), help=bstack111l1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤᠽ"))
    parser.addoption(bstack111l1l_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᠾ"), default=bstack111l1l_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᠿ"), help=bstack111l1l_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧᡀ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111l1l_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤᡁ"), action=bstack111l1l_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢᡂ"), default=bstack111l1l_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤᡃ"),
                         help=bstack111l1l_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤᡄ"))
def bstack11ll1l111l_opy_(log):
    if not (log[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᡅ")] and log[bstack111l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᡆ")].strip()):
        return
    active = bstack11ll1lll1l_opy_()
    log = {
        bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᡇ"): log[bstack111l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᡈ")],
        bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᡉ"): bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"ࠩ࡝ࠫᡊ"),
        bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᡋ"): log[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᡌ")],
    }
    if active:
        if active[bstack111l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪᡍ")] == bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᡎ"):
            log[bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᡏ")] = active[bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᡐ")]
        elif active[bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᡑ")] == bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࠨᡒ"):
            log[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᡓ")] = active[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᡔ")]
    bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_([log])
def bstack11ll1lll1l_opy_():
    if len(store[bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᡕ")]) > 0 and store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᡖ")][-1]:
        return {
            bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᡗ"): bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᡘ"),
            bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᡙ"): store[bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᡚ")][-1]
        }
    if store.get(bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᡛ"), None):
        return {
            bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫᡜ"): bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࠬᡝ"),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᡞ"): store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᡟ")]
        }
    return None
bstack11ll1l1lll_opy_ = bstack11ll1lll11_opy_(bstack11ll1l111l_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        item._1ll11111111_opy_ = True
        bstack1l1lllllll_opy_ = bstack1l1l1lll_opy_.bstack1lll1ll1ll_opy_(bstack1111l111l1_opy_(item.own_markers))
        item._a11y_test_case = bstack1l1lllllll_opy_
        if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᡠ"), None):
            driver = getattr(item, bstack111l1l_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᡡ"), None)
            item._a11y_started = bstack1l1l1lll_opy_.bstack1l1ll1ll1_opy_(driver, bstack1l1lllllll_opy_)
        if not bstack1l1l1ll1l_opy_.on() or bstack1ll111l1ll1_opy_ != bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᡢ"):
            return
        global current_test_uuid, bstack11ll1l1lll_opy_
        bstack11ll1l1lll_opy_.start()
        bstack11l1l1lll1_opy_ = {
            bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᡣ"): uuid4().__str__(),
            bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᡤ"): bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"ࠨ࡜ࠪᡥ")
        }
        current_test_uuid = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᡦ")]
        store[bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᡧ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩᡨ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11l1l1111l_opy_[item.nodeid] = {**_11l1l1111l_opy_[item.nodeid], **bstack11l1l1lll1_opy_}
        bstack1ll1111lll1_opy_(item, _11l1l1111l_opy_[item.nodeid], bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᡩ"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨᡪ"), str(err))
def pytest_runtest_setup(item):
    global bstack1ll1111l1ll_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1111ll11l1_opy_():
        atexit.register(bstack11ll1l1l_opy_)
        if not bstack1ll1111l1ll_opy_:
            try:
                bstack1ll1111ll11_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111111l1ll_opy_():
                    bstack1ll1111ll11_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1ll1111ll11_opy_:
                    signal.signal(s, bstack1ll1111llll_opy_)
                bstack1ll1111l1ll_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack111l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣᡫ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1ll1lll1l1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᡬ")
    try:
        if not bstack1l1l1ll1l_opy_.on():
            return
        bstack11ll1l1lll_opy_.start()
        uuid = uuid4().__str__()
        bstack11l1l1lll1_opy_ = {
            bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᡭ"): uuid,
            bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᡮ"): bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"ࠫ࡟࠭ᡯ"),
            bstack111l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪᡰ"): bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᡱ"),
            bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᡲ"): bstack111l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᡳ"),
            bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᡴ"): bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᡵ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᡶ")] = item
        store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᡷ")] = [uuid]
        if not _11l1l1111l_opy_.get(item.nodeid, None):
            _11l1l1111l_opy_[item.nodeid] = {bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᡸ"): [], bstack111l1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ᡹"): []}
        _11l1l1111l_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᡺")].append(bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᡻")])
        _11l1l1111l_opy_[item.nodeid + bstack111l1l_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪ᡼")] = bstack11l1l1lll1_opy_
        bstack1ll111111ll_opy_(item, bstack11l1l1lll1_opy_, bstack111l1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ᡽"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ᡾"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1ll1l11lll_opy_
        bstack1ll11ll1_opy_ = 0
        if bstack1lll11l1_opy_ is True:
            bstack1ll11ll1_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭᡿")))
        if bstack1l1l1l1ll1_opy_.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᢀ"):
            if bstack1l1l1l1ll1_opy_.bstack1l111lll1_opy_() == bstack111l1l_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᢁ"):
                bstack1ll111l11l1_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᢂ"), None)
                bstack11111l11l_opy_ = bstack1ll111l11l1_opy_ + bstack111l1l_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᢃ")
                driver = getattr(item, bstack111l1l_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᢄ"), None)
                bstack1l11llll1_opy_ = getattr(item, bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᢅ"), None)
                bstack1l1l11lll1_opy_ = getattr(item, bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᢆ"), None)
                PercySDK.screenshot(driver, bstack11111l11l_opy_, bstack1l11llll1_opy_=bstack1l11llll1_opy_, bstack1l1l11lll1_opy_=bstack1l1l11lll1_opy_, bstack1ll1lll1ll_opy_=bstack1ll11ll1_opy_)
        if getattr(item, bstack111l1l_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧᢇ"), False):
            bstack1llll1ll1l_opy_.bstack1ll1ll11ll_opy_(getattr(item, bstack111l1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᢈ"), None), bstack1ll1l11lll_opy_, logger, item)
        if not bstack1l1l1ll1l_opy_.on():
            return
        bstack11l1l1lll1_opy_ = {
            bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᢉ"): uuid4().__str__(),
            bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᢊ"): bstack11ll11111l_opy_().isoformat() + bstack111l1l_opy_ (u"ࠫ࡟࠭ᢋ"),
            bstack111l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪᢌ"): bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᢍ"),
            bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᢎ"): bstack111l1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᢏ"),
            bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᢐ"): bstack111l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᢑ")
        }
        _11l1l1111l_opy_[item.nodeid + bstack111l1l_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧᢒ")] = bstack11l1l1lll1_opy_
        bstack1ll111111ll_opy_(item, bstack11l1l1lll1_opy_, bstack111l1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᢓ"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬᢔ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l1l1ll1l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1ll1lll1l11_opy_(fixturedef.argname):
        store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᢕ")] = request.node
    elif bstack1ll1lll11l1_opy_(fixturedef.argname):
        store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭ᢖ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᢗ"): fixturedef.argname,
            bstack111l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᢘ"): bstack1lllllll111_opy_(outcome),
            bstack111l1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᢙ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᢚ")]
        if not _11l1l1111l_opy_.get(current_test_item.nodeid, None):
            _11l1l1111l_opy_[current_test_item.nodeid] = {bstack111l1l_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᢛ"): []}
        _11l1l1111l_opy_[current_test_item.nodeid][bstack111l1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᢜ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫᢝ"), str(err))
if bstack11llll1l_opy_() and bstack1l1l1ll1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11l1l1111l_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᢞ")].bstack11l111ll_opy_(id(step))
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨᢟ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11l1l1111l_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᢠ")].bstack11ll1ll111_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᢡ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11ll11l1l1_opy_: bstack11ll11l111_opy_ = _11l1l1111l_opy_[request.node.nodeid][bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᢢ")]
            bstack11ll11l1l1_opy_.bstack11ll1ll111_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᢣ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1ll111l1ll1_opy_
        try:
            if not bstack1l1l1ll1l_opy_.on() or bstack1ll111l1ll1_opy_ != bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᢤ"):
                return
            global bstack11ll1l1lll_opy_
            bstack11ll1l1lll_opy_.start()
            driver = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨᢥ"), None)
            if not _11l1l1111l_opy_.get(request.node.nodeid, None):
                _11l1l1111l_opy_[request.node.nodeid] = {}
            bstack11ll11l1l1_opy_ = bstack11ll11l111_opy_.bstack1ll1l1ll1l1_opy_(
                scenario, feature, request.node,
                name=bstack1ll1lll11ll_opy_(request.node, scenario),
                bstack11ll1ll11l_opy_=bstack1l1ll11l_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111l1l_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᢦ"),
                tags=bstack1ll1llllll1_opy_(feature, scenario),
                bstack11ll111lll_opy_=bstack1l1l1ll1l_opy_.bstack11ll11ll11_opy_(driver) if driver and driver.session_id else {}
            )
            _11l1l1111l_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᢧ")] = bstack11ll11l1l1_opy_
            bstack1ll111ll111_opy_(bstack11ll11l1l1_opy_.uuid)
            bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᢨ"), bstack11ll11l1l1_opy_)
        except Exception as err:
            print(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨᢩ"), str(err))
def bstack1ll111l1l1l_opy_(bstack11ll1l1ll1_opy_):
    if bstack11ll1l1ll1_opy_ in store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᢪ")]:
        store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ᢫")].remove(bstack11ll1l1ll1_opy_)
def bstack1ll111ll111_opy_(bstack11ll1l1l11_opy_):
    store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᢬")] = bstack11ll1l1l11_opy_
    threading.current_thread().current_test_uuid = bstack11ll1l1l11_opy_
@bstack1l1l1ll1l_opy_.bstack1ll11lll111_opy_
def bstack1ll1111ll1l_opy_(item, call, report):
    global bstack1ll111l1ll1_opy_
    bstack11lll11lll_opy_ = bstack1l1ll11l_opy_()
    if hasattr(report, bstack111l1l_opy_ (u"ࠪࡷࡹࡵࡰࠨ᢭")):
        bstack11lll11lll_opy_ = bstack11111l1l11_opy_(report.stop)
    elif hasattr(report, bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪ᢮")):
        bstack11lll11lll_opy_ = bstack11111l1l11_opy_(report.start)
    try:
        if getattr(report, bstack111l1l_opy_ (u"ࠬࡽࡨࡦࡰࠪ᢯"), bstack111l1l_opy_ (u"࠭ࠧᢰ")) == bstack111l1l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᢱ"):
            bstack11ll1l1lll_opy_.reset()
        if getattr(report, bstack111l1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᢲ"), bstack111l1l_opy_ (u"ࠩࠪᢳ")) == bstack111l1l_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᢴ"):
            if bstack1ll111l1ll1_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᢵ"):
                _11l1l1111l_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᢶ")] = bstack11lll11lll_opy_
                bstack1ll1111lll1_opy_(item, _11l1l1111l_opy_[item.nodeid], bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᢷ"), report, call)
                store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᢸ")] = None
            elif bstack1ll111l1ll1_opy_ == bstack111l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᢹ"):
                bstack11ll11l1l1_opy_ = _11l1l1111l_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᢺ")]
                bstack11ll11l1l1_opy_.set(hooks=_11l1l1111l_opy_[item.nodeid].get(bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᢻ"), []))
                exception, bstack11ll11lll1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11ll11lll1_opy_ = [call.excinfo.exconly(), getattr(report, bstack111l1l_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪᢼ"), bstack111l1l_opy_ (u"ࠬ࠭ᢽ"))]
                bstack11ll11l1l1_opy_.stop(time=bstack11lll11lll_opy_, result=Result(result=getattr(report, bstack111l1l_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᢾ"), bstack111l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᢿ")), exception=exception, bstack11ll11lll1_opy_=bstack11ll11lll1_opy_))
                bstack1l1l1ll1l_opy_.bstack11ll1l11ll_opy_(bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᣀ"), _11l1l1111l_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᣁ")])
        elif getattr(report, bstack111l1l_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᣂ"), bstack111l1l_opy_ (u"ࠫࠬᣃ")) in [bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᣄ"), bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᣅ")]:
            bstack11ll1ll1ll_opy_ = item.nodeid + bstack111l1l_opy_ (u"ࠧ࠮ࠩᣆ") + getattr(report, bstack111l1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᣇ"), bstack111l1l_opy_ (u"ࠩࠪᣈ"))
            if getattr(report, bstack111l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᣉ"), False):
                hook_type = bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᣊ") if getattr(report, bstack111l1l_opy_ (u"ࠬࡽࡨࡦࡰࠪᣋ"), bstack111l1l_opy_ (u"࠭ࠧᣌ")) == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᣍ") else bstack111l1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᣎ")
                _11l1l1111l_opy_[bstack11ll1ll1ll_opy_] = {
                    bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᣏ"): uuid4().__str__(),
                    bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᣐ"): bstack11lll11lll_opy_,
                    bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᣑ"): hook_type
                }
            _11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᣒ")] = bstack11lll11lll_opy_
            bstack1ll111l1l1l_opy_(_11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᣓ")])
            bstack1ll111111ll_opy_(item, _11l1l1111l_opy_[bstack11ll1ll1ll_opy_], bstack111l1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᣔ"), report, call)
            if getattr(report, bstack111l1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᣕ"), bstack111l1l_opy_ (u"ࠩࠪᣖ")) == bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᣗ"):
                if getattr(report, bstack111l1l_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᣘ"), bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᣙ")) == bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᣚ"):
                    bstack11l1l1lll1_opy_ = {
                        bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᣛ"): uuid4().__str__(),
                        bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᣜ"): bstack1l1ll11l_opy_(),
                        bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᣝ"): bstack1l1ll11l_opy_()
                    }
                    _11l1l1111l_opy_[item.nodeid] = {**_11l1l1111l_opy_[item.nodeid], **bstack11l1l1lll1_opy_}
                    bstack1ll1111lll1_opy_(item, _11l1l1111l_opy_[item.nodeid], bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᣞ"))
                    bstack1ll1111lll1_opy_(item, _11l1l1111l_opy_[item.nodeid], bstack111l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᣟ"), report, call)
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡼࡿࠪᣠ"), str(err))
def bstack1ll111l1lll_opy_(test, bstack11l1l1lll1_opy_, result=None, call=None, bstack11l1ll11l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11ll11l1l1_opy_ = {
        bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᣡ"): bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᣢ")],
        bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᣣ"): bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࠧᣤ"),
        bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᣥ"): test.name,
        bstack111l1l_opy_ (u"ࠫࡧࡵࡤࡺࠩᣦ"): {
            bstack111l1l_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᣧ"): bstack111l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᣨ"),
            bstack111l1l_opy_ (u"ࠧࡤࡱࡧࡩࠬᣩ"): inspect.getsource(test.obj)
        },
        bstack111l1l_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᣪ"): test.name,
        bstack111l1l_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨᣫ"): test.name,
        bstack111l1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪᣬ"): bstack1111lll1l_opy_.bstack11l1l1l111_opy_(test),
        bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧᣭ"): file_path,
        bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧᣮ"): file_path,
        bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᣯ"): bstack111l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᣰ"),
        bstack111l1l_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᣱ"): file_path,
        bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᣲ"): bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᣳ")],
        bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᣴ"): bstack111l1l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᣵ"),
        bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩ᣶"): {
            bstack111l1l_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫ᣷"): test.nodeid
        },
        bstack111l1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭᣸"): bstack1111l111l1_opy_(test.own_markers)
    }
    if bstack11l1ll11l_opy_ in [bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ᣹"), bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ᣺")]:
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡴࡢࠩ᣻")] = {
            bstack111l1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ᣼"): bstack11l1l1lll1_opy_.get(bstack111l1l_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ᣽"), [])
        }
    if bstack11l1ll11l_opy_ == bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ᣾"):
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᣿")] = bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᤀ")
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᤁ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᤂ")]
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᤃ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᤄ")]
    if result:
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᤅ")] = result.outcome
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᤆ")] = result.duration * 1000
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᤇ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᤈ")]
        if result.failed:
            bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᤉ")] = bstack1l1l1ll1l_opy_.bstack11l11111l1_opy_(call.excinfo.typename)
            bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᤊ")] = bstack1l1l1ll1l_opy_.bstack1ll1l11111l_opy_(call.excinfo, result)
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᤋ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᤌ")]
    if outcome:
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᤍ")] = bstack1lllllll111_opy_(outcome)
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᤎ")] = 0
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᤏ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᤐ")]
        if bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᤑ")] == bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᤒ"):
            bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ᤓ")] = bstack111l1l_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩᤔ")  # bstack1ll11111ll1_opy_
            bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᤕ")] = [{bstack111l1l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᤖ"): [bstack111l1l_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨᤗ")]}]
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᤘ")] = bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᤙ")]
    return bstack11ll11l1l1_opy_
def bstack1ll111l11ll_opy_(test, bstack11l1ll1lll_opy_, bstack11l1ll11l_opy_, result, call, outcome, bstack1l1llllll1l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᤚ")]
    hook_name = bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᤛ")]
    hook_data = {
        bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᤜ"): bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᤝ")],
        bstack111l1l_opy_ (u"ࠫࡹࡿࡰࡦࠩᤞ"): bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ᤟"),
        bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᤠ"): bstack111l1l_opy_ (u"ࠧࡼࡿࠪᤡ").format(bstack1ll1lllll11_opy_(hook_name)),
        bstack111l1l_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᤢ"): {
            bstack111l1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᤣ"): bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᤤ"),
            bstack111l1l_opy_ (u"ࠫࡨࡵࡤࡦࠩᤥ"): None
        },
        bstack111l1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫᤦ"): test.name,
        bstack111l1l_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ᤧ"): bstack1111lll1l_opy_.bstack11l1l1l111_opy_(test, hook_name),
        bstack111l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᤨ"): file_path,
        bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᤩ"): file_path,
        bstack111l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᤪ"): bstack111l1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᤫ"),
        bstack111l1l_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩ᤬"): file_path,
        bstack111l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ᤭"): bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ᤮")],
        bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ᤯"): bstack111l1l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪᤰ") if bstack1ll111l1ll1_opy_ == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᤱ") else bstack111l1l_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᤲ"),
        bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᤳ"): hook_type
    }
    bstack1ll1l11lll1_opy_ = bstack11l1ll111l_opy_(_11l1l1111l_opy_.get(test.nodeid, None))
    if bstack1ll1l11lll1_opy_:
        hook_data[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪᤴ")] = bstack1ll1l11lll1_opy_
    if result:
        hook_data[bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᤵ")] = result.outcome
        hook_data[bstack111l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᤶ")] = result.duration * 1000
        hook_data[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᤷ")] = bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᤸ")]
        if result.failed:
            hook_data[bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦ᤹ࠩ")] = bstack1l1l1ll1l_opy_.bstack11l11111l1_opy_(call.excinfo.typename)
            hook_data[bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ᤺")] = bstack1l1l1ll1l_opy_.bstack1ll1l11111l_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸ᤻ࠬ")] = bstack1lllllll111_opy_(outcome)
        hook_data[bstack111l1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ᤼")] = 100
        hook_data[bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᤽")] = bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᤾")]
        if hook_data[bstack111l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᤿")] == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᥀"):
            hook_data[bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ᥁")] = bstack111l1l_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭᥂")  # bstack1ll11111ll1_opy_
            hook_data[bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ᥃")] = [{bstack111l1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ᥄"): [bstack111l1l_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬ᥅")]}]
    if bstack1l1llllll1l_opy_:
        hook_data[bstack111l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᥆")] = bstack1l1llllll1l_opy_.result
        hook_data[bstack111l1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ᥇")] = bstack1111l11l1l_opy_(bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ᥈")], bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᥉")])
        hook_data[bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᥊")] = bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᥋")]
        if hook_data[bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ᥌")] == bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᥍"):
            hook_data[bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ᥎")] = bstack1l1l1ll1l_opy_.bstack11l11111l1_opy_(bstack1l1llllll1l_opy_.exception_type)
            hook_data[bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ᥏")] = [{bstack111l1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᥐ"): bstack1111ll1lll_opy_(bstack1l1llllll1l_opy_.exception)}]
    return hook_data
def bstack1ll1111lll1_opy_(test, bstack11l1l1lll1_opy_, bstack11l1ll11l_opy_, result=None, call=None, outcome=None):
    bstack11ll11l1l1_opy_ = bstack1ll111l1lll_opy_(test, bstack11l1l1lll1_opy_, result, call, bstack11l1ll11l_opy_, outcome)
    driver = getattr(test, bstack111l1l_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᥑ"), None)
    if bstack11l1ll11l_opy_ == bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᥒ") and driver:
        bstack11ll11l1l1_opy_[bstack111l1l_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᥓ")] = bstack1l1l1ll1l_opy_.bstack11ll11ll11_opy_(driver)
    if bstack11l1ll11l_opy_ == bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᥔ"):
        bstack11l1ll11l_opy_ = bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᥕ")
    bstack11l1l111l1_opy_ = {
        bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᥖ"): bstack11l1ll11l_opy_,
        bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᥗ"): bstack11ll11l1l1_opy_
    }
    bstack1l1l1ll1l_opy_.bstack11l1l1ll11_opy_(bstack11l1l111l1_opy_)
def bstack1ll111111ll_opy_(test, bstack11l1l1lll1_opy_, bstack11l1ll11l_opy_, result=None, call=None, outcome=None, bstack1l1llllll1l_opy_=None):
    hook_data = bstack1ll111l11ll_opy_(test, bstack11l1l1lll1_opy_, bstack11l1ll11l_opy_, result, call, outcome, bstack1l1llllll1l_opy_)
    bstack11l1l111l1_opy_ = {
        bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᥘ"): bstack11l1ll11l_opy_,
        bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩᥙ"): hook_data
    }
    bstack1l1l1ll1l_opy_.bstack11l1l1ll11_opy_(bstack11l1l111l1_opy_)
def bstack11l1ll111l_opy_(bstack11l1l1lll1_opy_):
    if not bstack11l1l1lll1_opy_:
        return None
    if bstack11l1l1lll1_opy_.get(bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᥚ"), None):
        return getattr(bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᥛ")], bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᥜ"), None)
    return bstack11l1l1lll1_opy_.get(bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩᥝ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l1l1ll1l_opy_.on():
            return
        places = [bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᥞ"), bstack111l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᥟ"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᥠ")]
        bstack11l1lll11l_opy_ = []
        for bstack1ll11111l1l_opy_ in places:
            records = caplog.get_records(bstack1ll11111l1l_opy_)
            bstack1ll111l1l11_opy_ = bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᥡ") if bstack1ll11111l1l_opy_ == bstack111l1l_opy_ (u"ࠩࡦࡥࡱࡲࠧᥢ") else bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᥣ")
            bstack1ll111ll11l_opy_ = request.node.nodeid + (bstack111l1l_opy_ (u"ࠫࠬᥤ") if bstack1ll11111l1l_opy_ == bstack111l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᥥ") else bstack111l1l_opy_ (u"࠭࠭ࠨᥦ") + bstack1ll11111l1l_opy_)
            bstack11ll1l1l11_opy_ = bstack11l1ll111l_opy_(_11l1l1111l_opy_.get(bstack1ll111ll11l_opy_, None))
            if not bstack11ll1l1l11_opy_:
                continue
            for record in records:
                if bstack111l11111l_opy_(record.message):
                    continue
                bstack11l1lll11l_opy_.append({
                    bstack111l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᥧ"): bstack1llllll1l11_opy_(record.created).isoformat() + bstack111l1l_opy_ (u"ࠨ࡜ࠪᥨ"),
                    bstack111l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᥩ"): record.levelname,
                    bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᥪ"): record.message,
                    bstack1ll111l1l11_opy_: bstack11ll1l1l11_opy_
                })
        if len(bstack11l1lll11l_opy_) > 0:
            bstack1l1l1ll1l_opy_.bstack1lllllllll_opy_(bstack11l1lll11l_opy_)
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨᥫ"), str(err))
def bstack1l1lll1111_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1lllll_opy_
    bstack11l1111ll_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩᥬ"), None) and bstack1ll111l11_opy_(
            threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᥭ"), None)
    bstack1ll1ll1lll_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ᥮"), None) != None and getattr(driver, bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ᥯"), None) == True
    if sequence == bstack111l1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᥰ") and driver != None:
      if not bstack11l1lllll_opy_ and bstack1lllllll1l1_opy_() and bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᥱ") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᥲ")] == True and bstack1lllll1lll_opy_.bstack11l1l111l_opy_(driver_command) and (bstack1ll1ll1lll_opy_ or bstack11l1111ll_opy_) and not bstack1ll1l1l1_opy_(args):
        try:
          bstack11l1lllll_opy_ = True
          logger.debug(bstack111l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧᥳ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack111l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫᥴ").format(str(err)))
        bstack11l1lllll_opy_ = False
    if sequence == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭᥵"):
        if driver_command == bstack111l1l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ᥶"):
            bstack1l1l1ll1l_opy_.bstack11llll11l1_opy_({
                bstack111l1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ᥷"): response[bstack111l1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ᥸")],
                bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᥹"): store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᥺")]
            })
def bstack11ll1l1l_opy_():
    global bstack11ll11l1_opy_
    bstack1llll11lll_opy_.bstack1l1lllll11_opy_()
    logging.shutdown()
    bstack1l1l1ll1l_opy_.bstack11l11l1lll_opy_()
    for driver in bstack11ll11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1111llll_opy_(*args):
    global bstack11ll11l1_opy_
    bstack1l1l1ll1l_opy_.bstack11l11l1lll_opy_()
    for driver in bstack11ll11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1lllll1_opy_(self, *args, **kwargs):
    bstack1111111l1_opy_ = bstack1lll1llll_opy_(self, *args, **kwargs)
    bstack1l1l1ll1l_opy_.bstack1llll1l1_opy_(self)
    return bstack1111111l1_opy_
def bstack1ll111l11l_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
    if bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ᥻")):
        return
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ᥼"), True)
    global bstack1l1111llll_opy_
    global bstack1lll1l1l11_opy_
    bstack1l1111llll_opy_ = framework_name
    logger.info(bstack1111ll111_opy_.format(bstack1l1111llll_opy_.split(bstack111l1l_opy_ (u"ࠨ࠯ࠪ᥽"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lllllll1l1_opy_():
            Service.start = bstack1llll11l11_opy_
            Service.stop = bstack1l1ll1lll_opy_
            webdriver.Remote.__init__ = bstack1l1llllll1_opy_
            webdriver.Remote.get = bstack1l11l11lll_opy_
            if not isinstance(os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ᥾")), str):
                return
            WebDriver.close = bstack1l1lll1l1_opy_
            WebDriver.quit = bstack1llllll1l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack1lllllll1l1_opy_() and bstack1l1l1ll1l_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1lllll1_opy_
        bstack1lll1l1l11_opy_ = True
    except Exception as e:
        pass
    bstack1111l1lll_opy_()
    if os.environ.get(bstack111l1l_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨ᥿")):
        bstack1lll1l1l11_opy_ = eval(os.environ.get(bstack111l1l_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᦀ")))
    if not bstack1lll1l1l11_opy_:
        bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢᦁ"), bstack11llllllll_opy_)
    if bstack1ll11ll11l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack11l1l1ll1_opy_
        except Exception as e:
            logger.error(bstack1l11l1ll1_opy_.format(str(e)))
    if bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᦂ") in str(framework_name).lower():
        if not bstack1lllllll1l1_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11llll1l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11l111l1_opy_
            Config.getoption = bstack11llll1lll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l111lll1l_opy_
        except Exception as e:
            pass
def bstack1llllll1l_opy_(self):
    global bstack1l1111llll_opy_
    global bstack1lll111lll_opy_
    global bstack1ll11l1111_opy_
    try:
        if bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᦃ") in bstack1l1111llll_opy_ and self.session_id != None and bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᦄ"), bstack111l1l_opy_ (u"ࠩࠪᦅ")) != bstack111l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᦆ"):
            bstack1l1llll111_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᦇ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᦈ")
            bstack1lll1l111_opy_(logger, True)
            if self != None:
                bstack1llll1llll_opy_(self, bstack1l1llll111_opy_, bstack111l1l_opy_ (u"࠭ࠬࠡࠩᦉ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᦊ"), None)
        if item is not None and bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᦋ"), None):
            bstack1llll1ll1l_opy_.bstack1ll1ll11ll_opy_(self, bstack1ll1l11lll_opy_, logger, item)
        threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠩࠪᦌ")
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦᦍ") + str(e))
    bstack1ll11l1111_opy_(self)
    self.session_id = None
def bstack1l1llllll1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1lll111lll_opy_
    global bstack111llll1l_opy_
    global bstack1lll11l1_opy_
    global bstack1l1111llll_opy_
    global bstack1lll1llll_opy_
    global bstack11ll11l1_opy_
    global bstack1l1ll11l11_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack1ll1l11lll_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᦎ")] = str(bstack1l1111llll_opy_) + str(__version__)
    command_executor = bstack1l1l11111_opy_(bstack1l1ll11l11_opy_, CONFIG)
    logger.debug(bstack1l1l111ll1_opy_.format(command_executor))
    proxy = bstack11111lll_opy_(CONFIG, proxy)
    bstack1ll11ll1_opy_ = 0
    try:
        if bstack1lll11l1_opy_ is True:
            bstack1ll11ll1_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᦏ")))
    except:
        bstack1ll11ll1_opy_ = 0
    bstack1l1111111l_opy_ = bstack11l1ll1l1_opy_(CONFIG, bstack1ll11ll1_opy_)
    logger.debug(bstack1111llll1_opy_.format(str(bstack1l1111111l_opy_)))
    bstack1ll1l11lll_opy_ = CONFIG.get(bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᦐ"))[bstack1ll11ll1_opy_]
    if bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᦑ") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᦒ")]:
        bstack1l11l1l11l_opy_(bstack1l1111111l_opy_, bstack1l1ll1l1l1_opy_)
    if bstack1l1l1lll_opy_.bstack11lll1l1ll_opy_(CONFIG, bstack1ll11ll1_opy_) and bstack1l1l1lll_opy_.bstack11lll11l1l_opy_(bstack1l1111111l_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        bstack1l1l1lll_opy_.set_capabilities(bstack1l1111111l_opy_, CONFIG)
    if desired_capabilities:
        bstack1l1lll111l_opy_ = bstack111l111ll_opy_(desired_capabilities)
        bstack1l1lll111l_opy_[bstack111l1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᦓ")] = bstack11l11111l_opy_(CONFIG)
        bstack1ll1l11111_opy_ = bstack11l1ll1l1_opy_(bstack1l1lll111l_opy_)
        if bstack1ll1l11111_opy_:
            bstack1l1111111l_opy_ = update(bstack1ll1l11111_opy_, bstack1l1111111l_opy_)
        desired_capabilities = None
    if options:
        bstack1lllll11_opy_(options, bstack1l1111111l_opy_)
    if not options:
        options = bstack1l1lll11l1_opy_(bstack1l1111111l_opy_)
    if proxy and bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪᦔ")):
        options.proxy(proxy)
    if options and bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᦕ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1111ll1l_opy_() < version.parse(bstack111l1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᦖ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l1111111l_opy_)
    logger.info(bstack1ll1llll1l_opy_)
    if bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ᦗ")):
        bstack1lll1llll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᦘ")):
        bstack1lll1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨᦙ")):
        bstack1lll1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1lll1llll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l11lll11l_opy_ = bstack111l1l_opy_ (u"ࠩࠪᦚ")
        if bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫᦛ")):
            bstack1l11lll11l_opy_ = self.caps.get(bstack111l1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦᦜ"))
        else:
            bstack1l11lll11l_opy_ = self.capabilities.get(bstack111l1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧᦝ"))
        if bstack1l11lll11l_opy_:
            bstack1111l1111_opy_(bstack1l11lll11l_opy_)
            if bstack1111ll1l_opy_() <= version.parse(bstack111l1l_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᦞ")):
                self.command_executor._url = bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᦟ") + bstack1l1ll11l11_opy_ + bstack111l1l_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᦠ")
            else:
                self.command_executor._url = bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᦡ") + bstack1l11lll11l_opy_ + bstack111l1l_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᦢ")
            logger.debug(bstack1ll1llll11_opy_.format(bstack1l11lll11l_opy_))
        else:
            logger.debug(bstack1l1ll1111_opy_.format(bstack111l1l_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᦣ")))
    except Exception as e:
        logger.debug(bstack1l1ll1111_opy_.format(e))
    bstack1lll111lll_opy_ = self.session_id
    if bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᦤ") in bstack1l1111llll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᦥ"), None)
        if item:
            bstack1ll111l1111_opy_ = getattr(item, bstack111l1l_opy_ (u"ࠧࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࡣࡸࡺࡡࡳࡶࡨࡨࠬᦦ"), False)
            if not getattr(item, bstack111l1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᦧ"), None) and bstack1ll111l1111_opy_:
                setattr(store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᦨ")], bstack111l1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᦩ"), self)
        bstack1l1l1ll1l_opy_.bstack1llll1l1_opy_(self)
    bstack11ll11l1_opy_.append(self)
    if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᦪ") in CONFIG and bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᦫ") in CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᦬")][bstack1ll11ll1_opy_]:
        bstack111llll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᦭")][bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭᦮")]
    logger.debug(bstack11111l1ll_opy_.format(bstack1lll111lll_opy_))
def bstack1l11l11lll_opy_(self, url):
    global bstack1ll11l1l_opy_
    global CONFIG
    try:
        bstack1111l111_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l1ll1l11l_opy_.format(str(err)))
    try:
        bstack1ll11l1l_opy_(self, url)
    except Exception as e:
        try:
            bstack1llllll11l_opy_ = str(e)
            if any(err_msg in bstack1llllll11l_opy_ for err_msg in bstack1lll1l1l1_opy_):
                bstack1111l111_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l1ll1l11l_opy_.format(str(err)))
        raise e
def bstack111111111_opy_(item, when):
    global bstack1l1l1lll11_opy_
    try:
        bstack1l1l1lll11_opy_(item, when)
    except Exception as e:
        pass
def bstack1l111lll1l_opy_(item, call, rep):
    global bstack1l1l1ll1_opy_
    global bstack11ll11l1_opy_
    name = bstack111l1l_opy_ (u"ࠩࠪ᦯")
    try:
        if rep.when == bstack111l1l_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᦰ"):
            bstack1lll111lll_opy_ = threading.current_thread().bstackSessionId
            bstack1ll1111l111_opy_ = item.config.getoption(bstack111l1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᦱ"))
            try:
                if (str(bstack1ll1111l111_opy_).lower() != bstack111l1l_opy_ (u"ࠬࡺࡲࡶࡧࠪᦲ")):
                    name = str(rep.nodeid)
                    bstack1ll11llll_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᦳ"), name, bstack111l1l_opy_ (u"ࠧࠨᦴ"), bstack111l1l_opy_ (u"ࠨࠩᦵ"), bstack111l1l_opy_ (u"ࠩࠪᦶ"), bstack111l1l_opy_ (u"ࠪࠫᦷ"))
                    os.environ[bstack111l1l_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᦸ")] = name
                    for driver in bstack11ll11l1_opy_:
                        if bstack1lll111lll_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll11llll_opy_)
            except Exception as e:
                logger.debug(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬᦹ").format(str(e)))
            try:
                bstack1l1lll1lll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᦺ"):
                    status = bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᦻ") if rep.outcome.lower() == bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᦼ") else bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᦽ")
                    reason = bstack111l1l_opy_ (u"ࠪࠫᦾ")
                    if status == bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᦿ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111l1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪᧀ") if status == bstack111l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᧁ") else bstack111l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᧂ")
                    data = name + bstack111l1l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪᧃ") if status == bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᧄ") else name + bstack111l1l_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭ᧅ") + reason
                    bstack111l1l111_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᧆ"), bstack111l1l_opy_ (u"ࠬ࠭ᧇ"), bstack111l1l_opy_ (u"࠭ࠧᧈ"), bstack111l1l_opy_ (u"ࠧࠨᧉ"), level, data)
                    for driver in bstack11ll11l1_opy_:
                        if bstack1lll111lll_opy_ == driver.session_id:
                            driver.execute_script(bstack111l1l111_opy_)
            except Exception as e:
                logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ᧊").format(str(e)))
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭᧋").format(str(e)))
    bstack1l1l1ll1_opy_(item, call, rep)
notset = Notset()
def bstack11llll1lll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l1ll1ll_opy_
    if str(name).lower() == bstack111l1l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪ᧌"):
        return bstack111l1l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ᧍")
    else:
        return bstack11l1ll1ll_opy_(self, name, default, skip)
def bstack11l1l1ll1_opy_(self):
    global CONFIG
    global bstack1lllll1l1l_opy_
    try:
        proxy = bstack11lll1l11l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111l1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ᧎")):
                proxies = bstack1lll11l111_opy_(proxy, bstack1l1l11111_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll111l1ll_opy_ = proxies.popitem()
                    if bstack111l1l_opy_ (u"ࠨ࠺࠰࠱ࠥ᧏") in bstack1ll111l1ll_opy_:
                        return bstack1ll111l1ll_opy_
                    else:
                        return bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ᧐") + bstack1ll111l1ll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧ᧑").format(str(e)))
    return bstack1lllll1l1l_opy_(self)
def bstack1ll11ll11l_opy_():
    return (bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᧒") in CONFIG or bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᧓") in CONFIG) and bstack1ll11l111_opy_() and bstack1111ll1l_opy_() >= version.parse(
        bstack1111l111l_opy_)
def bstack1l11l111ll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack111llll1l_opy_
    global bstack1lll11l1_opy_
    global bstack1l1111llll_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭᧔")] = str(bstack1l1111llll_opy_) + str(__version__)
    bstack1ll11ll1_opy_ = 0
    try:
        if bstack1lll11l1_opy_ is True:
            bstack1ll11ll1_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ᧕")))
    except:
        bstack1ll11ll1_opy_ = 0
    CONFIG[bstack111l1l_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ᧖")] = True
    bstack1l1111111l_opy_ = bstack11l1ll1l1_opy_(CONFIG, bstack1ll11ll1_opy_)
    logger.debug(bstack1111llll1_opy_.format(str(bstack1l1111111l_opy_)))
    if CONFIG.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᧗")):
        bstack1l11l1l11l_opy_(bstack1l1111111l_opy_, bstack1l1ll1l1l1_opy_)
    if bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᧘") in CONFIG and bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᧙") in CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᧚")][bstack1ll11ll1_opy_]:
        bstack111llll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᧛")][bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᧜")]
    import urllib
    import json
    if bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ᧝") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ᧞")]).lower() != bstack111l1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ᧟"):
        bstack1l111ll1l_opy_ = bstack1111ll1ll_opy_()
        bstack1llll11l_opy_ = bstack1l111ll1l_opy_ + urllib.parse.quote(json.dumps(bstack1l1111111l_opy_))
    else:
        bstack1llll11l_opy_ = bstack111l1l_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ᧠") + urllib.parse.quote(json.dumps(bstack1l1111111l_opy_))
    browser = self.connect(bstack1llll11l_opy_)
    return browser
def bstack1111l1lll_opy_():
    global bstack1lll1l1l11_opy_
    global bstack1l1111llll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11l1ll111_opy_
        if not bstack1lllllll1l1_opy_():
            global bstack111ll1l1_opy_
            if not bstack111ll1l1_opy_:
                from bstack_utils.helper import bstack1l1l1ll111_opy_, bstack1ll11l1l1_opy_
                bstack111ll1l1_opy_ = bstack1l1l1ll111_opy_()
                bstack1ll11l1l1_opy_(bstack1l1111llll_opy_)
            BrowserType.connect = bstack11l1ll111_opy_
            return
        BrowserType.launch = bstack1l11l111ll_opy_
        bstack1lll1l1l11_opy_ = True
    except Exception as e:
        pass
def bstack1ll1111111l_opy_():
    global CONFIG
    global bstack1l111l11l_opy_
    global bstack1l1ll11l11_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack1lll11l1_opy_
    global bstack111ll1l1l_opy_
    CONFIG = json.loads(os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩ᧡")))
    bstack1l111l11l_opy_ = eval(os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ᧢")))
    bstack1l1ll11l11_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ᧣"))
    bstack11lllllll_opy_(CONFIG, bstack1l111l11l_opy_)
    bstack111ll1l1l_opy_ = bstack1llll11lll_opy_.bstack1l11111l_opy_(CONFIG, bstack111ll1l1l_opy_)
    global bstack1lll1llll_opy_
    global bstack1ll11l1111_opy_
    global bstack1l1llllll_opy_
    global bstack1lll1l1ll_opy_
    global bstack11llll1l11_opy_
    global bstack1ll1lll1l_opy_
    global bstack1l1ll11ll1_opy_
    global bstack1ll11l1l_opy_
    global bstack1lllll1l1l_opy_
    global bstack11l1ll1ll_opy_
    global bstack1l1l1lll11_opy_
    global bstack1l1l1ll1_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1lll1llll_opy_ = webdriver.Remote.__init__
        bstack1ll11l1111_opy_ = WebDriver.quit
        bstack1l1ll11ll1_opy_ = WebDriver.close
        bstack1ll11l1l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᧤") in CONFIG or bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᧥") in CONFIG) and bstack1ll11l111_opy_():
        if bstack1111ll1l_opy_() < version.parse(bstack1111l111l_opy_):
            logger.error(bstack1lll1lllll_opy_.format(bstack1111ll1l_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1lllll1l1l_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1l11l1ll1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11l1ll1ll_opy_ = Config.getoption
        from _pytest import runner
        bstack1l1l1lll11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1lllllll1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l1l1ll1_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ᧦"))
    bstack1l1ll1l1l1_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᧧"), {}).get(bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᧨"))
    bstack1lll11l1_opy_ = True
    bstack1ll111l11l_opy_(bstack1l1l1ll11l_opy_)
if (bstack1111ll11l1_opy_()):
    bstack1ll1111111l_opy_()
@bstack11l1l1ll1l_opy_(class_method=False)
def bstack1ll11111lll_opy_(hook_name, event, bstack1l1llllllll_opy_=None):
    if hook_name not in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ᧩"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᧪"), bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᧫"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᧬"), bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭᧭"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ᧮"), bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩ᧯"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᧰")]:
        return
    node = store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ᧱")]
    if hook_name in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᧲"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᧳")]:
        node = store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ᧴")]
    elif hook_name in [bstack111l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ᧵"), bstack111l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ᧶")]:
        node = store[bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ᧷")]
    if event == bstack111l1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ᧸"):
        hook_type = bstack1ll1lllll1l_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11l1ll1lll_opy_ = {
            bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ᧹"): uuid,
            bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ᧺"): bstack1l1ll11l_opy_(),
            bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭᧻"): bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ᧼"),
            bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭᧽"): hook_type,
            bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ᧾"): hook_name
        }
        store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᧿")].append(uuid)
        bstack1ll111111l1_opy_ = node.nodeid
        if hook_type == bstack111l1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᨀ"):
            if not _11l1l1111l_opy_.get(bstack1ll111111l1_opy_, None):
                _11l1l1111l_opy_[bstack1ll111111l1_opy_] = {bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᨁ"): []}
            _11l1l1111l_opy_[bstack1ll111111l1_opy_][bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᨂ")].append(bstack11l1ll1lll_opy_[bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᨃ")])
        _11l1l1111l_opy_[bstack1ll111111l1_opy_ + bstack111l1l_opy_ (u"ࠪ࠱ࠬᨄ") + hook_name] = bstack11l1ll1lll_opy_
        bstack1ll111111ll_opy_(node, bstack11l1ll1lll_opy_, bstack111l1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᨅ"))
    elif event == bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᨆ"):
        bstack11ll1ll1ll_opy_ = node.nodeid + bstack111l1l_opy_ (u"࠭࠭ࠨᨇ") + hook_name
        _11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᨈ")] = bstack1l1ll11l_opy_()
        bstack1ll111l1l1l_opy_(_11l1l1111l_opy_[bstack11ll1ll1ll_opy_][bstack111l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᨉ")])
        bstack1ll111111ll_opy_(node, _11l1l1111l_opy_[bstack11ll1ll1ll_opy_], bstack111l1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᨊ"), bstack1l1llllll1l_opy_=bstack1l1llllllll_opy_)
def bstack1ll1111l1l1_opy_():
    global bstack1ll111l1ll1_opy_
    if bstack11llll1l_opy_():
        bstack1ll111l1ll1_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᨋ")
    else:
        bstack1ll111l1ll1_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᨌ")
@bstack1l1l1ll1l_opy_.bstack1ll11lll111_opy_
def bstack1l1llllll11_opy_():
    bstack1ll1111l1l1_opy_()
    if bstack1ll11l111_opy_():
        bstack11llll1ll1_opy_(bstack1l1lll1111_opy_)
    try:
        bstack1lllll11l11_opy_(bstack1ll11111lll_opy_)
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨᨍ").format(e))
bstack1l1llllll11_opy_()