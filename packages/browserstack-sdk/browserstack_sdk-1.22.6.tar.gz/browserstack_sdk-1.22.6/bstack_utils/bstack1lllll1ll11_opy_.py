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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack1111111111_opy_
from browserstack_sdk.bstack1l111l1l11_opy_ import bstack1llll1ll1l_opy_
def _1lllll1111l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1lllll11l11_opy_:
    def __init__(self, handler):
        self._1llll1llll1_opy_ = {}
        self._1llll1lll1l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llll1ll1l_opy_.version()
        if bstack1111111111_opy_(pytest_version, bstack111l1l_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣᓘ")) >= 0:
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᓙ")] = Module._register_setup_function_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᓚ")] = Module._register_setup_module_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᓛ")] = Class._register_setup_class_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᓜ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᓝ"))
            Module._register_setup_module_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᓞ"))
            Class._register_setup_class_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᓟ"))
            Class._register_setup_method_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᓠ"))
        else:
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᓡ")] = Module._inject_setup_function_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᓢ")] = Module._inject_setup_module_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᓣ")] = Class._inject_setup_class_fixture
            self._1llll1llll1_opy_[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᓤ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᓥ"))
            Module._inject_setup_module_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᓦ"))
            Class._inject_setup_class_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᓧ"))
            Class._inject_setup_method_fixture = self.bstack1lllll111ll_opy_(bstack111l1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᓨ"))
    def bstack1lllll11lll_opy_(self, bstack1lllll1l111_opy_, hook_type):
        bstack1lllll11ll1_opy_ = id(bstack1lllll1l111_opy_.__class__)
        if (bstack1lllll11ll1_opy_, hook_type) in self._1llll1lll1l_opy_:
            return
        meth = getattr(bstack1lllll1l111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1llll1lll1l_opy_[(bstack1lllll11ll1_opy_, hook_type)] = meth
            setattr(bstack1lllll1l111_opy_, hook_type, self.bstack1lllll1l11l_opy_(hook_type, bstack1lllll11ll1_opy_))
    def bstack1lllll11l1l_opy_(self, instance, bstack1lllll111l1_opy_):
        if bstack1lllll111l1_opy_ == bstack111l1l_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᓩ"):
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢᓪ"))
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦᓫ"))
        if bstack1lllll111l1_opy_ == bstack111l1l_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤᓬ"):
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣᓭ"))
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧᓮ"))
        if bstack1lllll111l1_opy_ == bstack111l1l_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦᓯ"):
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥᓰ"))
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢᓱ"))
        if bstack1lllll111l1_opy_ == bstack111l1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᓲ"):
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢᓳ"))
            self.bstack1lllll11lll_opy_(instance.obj, bstack111l1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦᓴ"))
    @staticmethod
    def bstack1lllll1ll1l_opy_(hook_type, func, args):
        if hook_type in [bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᓵ"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᓶ")]:
            _1lllll1111l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1lllll1l11l_opy_(self, hook_type, bstack1lllll11ll1_opy_):
        def bstack1lllll1l1ll_opy_(arg=None):
            self.handler(hook_type, bstack111l1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬᓷ"))
            result = None
            try:
                bstack1llll1lllll_opy_ = self._1llll1lll1l_opy_[(bstack1lllll11ll1_opy_, hook_type)]
                self.bstack1lllll1ll1l_opy_(hook_type, bstack1llll1lllll_opy_, (arg,))
                result = Result(result=bstack111l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᓸ"))
            except Exception as e:
                result = Result(result=bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᓹ"), exception=e)
                self.handler(hook_type, bstack111l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᓺ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111l1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨᓻ"), result)
        def bstack1lllll1l1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack111l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᓼ"))
            result = None
            exception = None
            try:
                self.bstack1lllll1ll1l_opy_(hook_type, self._1llll1lll1l_opy_[hook_type], (this, arg))
                result = Result(result=bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᓽ"))
            except Exception as e:
                result = Result(result=bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᓾ"), exception=e)
                self.handler(hook_type, bstack111l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᓿ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᔀ"), result)
        if hook_type in [bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᔁ"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᔂ")]:
            return bstack1lllll1l1l1_opy_
        return bstack1lllll1l1ll_opy_
    def bstack1lllll111ll_opy_(self, bstack1lllll111l1_opy_):
        def bstack1lllll11111_opy_(this, *args, **kwargs):
            self.bstack1lllll11l1l_opy_(this, bstack1lllll111l1_opy_)
            self._1llll1llll1_opy_[bstack1lllll111l1_opy_](this, *args, **kwargs)
        return bstack1lllll11111_opy_