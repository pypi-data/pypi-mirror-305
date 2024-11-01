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
from uuid import uuid4
from bstack_utils.helper import bstack1l1ll11l_opy_, bstack1111l11l1l_opy_
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1ll1lll111l_opy_
class bstack11l1llllll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11ll1ll11l_opy_=None, framework=None, tags=[], scope=[], bstack1ll1l11l1ll_opy_=None, bstack1ll1l1ll111_opy_=True, bstack1ll1l11ll11_opy_=None, bstack11l1ll11l_opy_=None, result=None, duration=None, bstack11l1ll1111_opy_=None, meta={}):
        self.bstack11l1ll1111_opy_ = bstack11l1ll1111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1ll1l1ll111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11ll1ll11l_opy_ = bstack11ll1ll11l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1ll1l11l1ll_opy_ = bstack1ll1l11l1ll_opy_
        self.bstack1ll1l11ll11_opy_ = bstack1ll1l11ll11_opy_
        self.bstack11l1ll11l_opy_ = bstack11l1ll11l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack11l11lllll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1l1111_opy_(self, meta):
        self.meta = meta
    def bstack11ll1l11l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack1ll1l1ll11l_opy_(self):
        bstack1ll1l1l1ll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬᙵ"): bstack1ll1l1l1ll1_opy_,
            bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬᙶ"): bstack1ll1l1l1ll1_opy_,
            bstack111l1l_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᙷ"): bstack1ll1l1l1ll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111l1l_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷ࠾ࠥࠨᙸ") + key)
            setattr(self, key, val)
    def bstack1ll1l1lll11_opy_(self):
        return {
            bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᙹ"): self.name,
            bstack111l1l_opy_ (u"ࠧࡣࡱࡧࡽࠬᙺ"): {
                bstack111l1l_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᙻ"): bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᙼ"),
                bstack111l1l_opy_ (u"ࠪࡧࡴࡪࡥࠨᙽ"): self.code
            },
            bstack111l1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᙾ"): self.scope,
            bstack111l1l_opy_ (u"ࠬࡺࡡࡨࡵࠪᙿ"): self.tags,
            bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ "): self.framework,
            bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᚁ"): self.bstack11ll1ll11l_opy_
        }
    def bstack1ll1l1l1l1l_opy_(self):
        return {
         bstack111l1l_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ᚂ"): self.meta
        }
    def bstack1ll1l1l11ll_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬᚃ"): {
                bstack111l1l_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧᚄ"): self.bstack1ll1l11l1ll_opy_
            }
        }
    def bstack1ll1l11llll_opy_(self, bstack1ll1l1l11l1_opy_, details):
        step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧᚅ")] == bstack1ll1l1l11l1_opy_, self.meta[bstack111l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᚆ")]), None)
        step.update(details)
    def bstack11l111ll_opy_(self, bstack1ll1l1l11l1_opy_):
        step = next(filter(lambda st: st[bstack111l1l_opy_ (u"࠭ࡩࡥࠩᚇ")] == bstack1ll1l1l11l1_opy_, self.meta[bstack111l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᚈ")]), None)
        step.update({
            bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᚉ"): bstack1l1ll11l_opy_()
        })
    def bstack11ll1ll111_opy_(self, bstack1ll1l1l11l1_opy_, result, duration=None):
        bstack1ll1l11ll11_opy_ = bstack1l1ll11l_opy_()
        if bstack1ll1l1l11l1_opy_ is not None and self.meta.get(bstack111l1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᚊ")):
            step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ᚋ")] == bstack1ll1l1l11l1_opy_, self.meta[bstack111l1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᚌ")]), None)
            step.update({
                bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᚍ"): bstack1ll1l11ll11_opy_,
                bstack111l1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᚎ"): duration if duration else bstack1111l11l1l_opy_(step[bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᚏ")], bstack1ll1l11ll11_opy_),
                bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᚐ"): result.result,
                bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᚑ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1ll1l1l1lll_opy_):
        if self.meta.get(bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᚒ")):
            self.meta[bstack111l1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᚓ")].append(bstack1ll1l1l1lll_opy_)
        else:
            self.meta[bstack111l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᚔ")] = [ bstack1ll1l1l1lll_opy_ ]
    def bstack1ll1l11ll1l_opy_(self):
        return {
            bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᚕ"): self.bstack11l11lllll_opy_(),
            **self.bstack1ll1l1lll11_opy_(),
            **self.bstack1ll1l1ll11l_opy_(),
            **self.bstack1ll1l1l1l1l_opy_()
        }
    def bstack1ll1l1l111l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᚖ"): self.bstack1ll1l11ll11_opy_,
            bstack111l1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᚗ"): self.duration,
            bstack111l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᚘ"): self.result.result
        }
        if data[bstack111l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᚙ")] == bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᚚ"):
            data[bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ᚛")] = self.result.bstack11l11111l1_opy_()
            data[bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ᚜")] = [{bstack111l1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ᚝"): self.result.bstack1111ll1ll1_opy_()}]
        return data
    def bstack1ll1l1ll1ll_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭᚞"): self.bstack11l11lllll_opy_(),
            **self.bstack1ll1l1lll11_opy_(),
            **self.bstack1ll1l1ll11l_opy_(),
            **self.bstack1ll1l1l111l_opy_(),
            **self.bstack1ll1l1l1l1l_opy_()
        }
    def bstack11l1ll11l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111l1l_opy_ (u"ࠩࡖࡸࡦࡸࡴࡦࡦࠪ᚟") in event:
            return self.bstack1ll1l11ll1l_opy_()
        elif bstack111l1l_opy_ (u"ࠪࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᚠ") in event:
            return self.bstack1ll1l1ll1ll_opy_()
    def bstack11l1lllll1_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l11ll11_opy_ = time if time else bstack1l1ll11l_opy_()
        self.duration = duration if duration else bstack1111l11l1l_opy_(self.bstack11ll1ll11l_opy_, self.bstack1ll1l11ll11_opy_)
        if result:
            self.result = result
class bstack11ll11l111_opy_(bstack11l1llllll_opy_):
    def __init__(self, hooks=[], bstack11ll111lll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11ll111lll_opy_ = bstack11ll111lll_opy_
        super().__init__(*args, **kwargs, bstack11l1ll11l_opy_=bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᚡ"))
    @classmethod
    def bstack1ll1l1ll1l1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨᚢ"): id(step),
                bstack111l1l_opy_ (u"࠭ࡴࡦࡺࡷࠫᚣ"): step.name,
                bstack111l1l_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨᚤ"): step.keyword,
            })
        return bstack11ll11l111_opy_(
            **kwargs,
            meta={
                bstack111l1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩᚥ"): {
                    bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᚦ"): feature.name,
                    bstack111l1l_opy_ (u"ࠪࡴࡦࡺࡨࠨᚧ"): feature.filename,
                    bstack111l1l_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᚨ"): feature.description
                },
                bstack111l1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧᚩ"): {
                    bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᚪ"): scenario.name
                },
                bstack111l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᚫ"): steps,
                bstack111l1l_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪᚬ"): bstack1ll1lll111l_opy_(test)
            }
        )
    def bstack1ll1l11l1l1_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᚭ"): self.hooks
        }
    def bstack1ll1l1l1l11_opy_(self):
        if self.bstack11ll111lll_opy_:
            return {
                bstack111l1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩᚮ"): self.bstack11ll111lll_opy_
            }
        return {}
    def bstack1ll1l1ll1ll_opy_(self):
        return {
            **super().bstack1ll1l1ll1ll_opy_(),
            **self.bstack1ll1l11l1l1_opy_()
        }
    def bstack1ll1l11ll1l_opy_(self):
        return {
            **super().bstack1ll1l11ll1l_opy_(),
            **self.bstack1ll1l1l1l11_opy_()
        }
    def bstack11l1lllll1_opy_(self):
        return bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᚯ")
class bstack11ll11llll_opy_(bstack11l1llllll_opy_):
    def __init__(self, hook_type, *args,bstack11ll111lll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1ll1l11lll1_opy_ = None
        self.bstack11ll111lll_opy_ = bstack11ll111lll_opy_
        super().__init__(*args, **kwargs, bstack11l1ll11l_opy_=bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᚰ"))
    def bstack11ll111111_opy_(self):
        return self.hook_type
    def bstack1ll1l1l1111_opy_(self):
        return {
            bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᚱ"): self.hook_type
        }
    def bstack1ll1l1ll1ll_opy_(self):
        return {
            **super().bstack1ll1l1ll1ll_opy_(),
            **self.bstack1ll1l1l1111_opy_()
        }
    def bstack1ll1l11ll1l_opy_(self):
        return {
            **super().bstack1ll1l11ll1l_opy_(),
            bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬᚲ"): self.bstack1ll1l11lll1_opy_,
            **self.bstack1ll1l1l1111_opy_()
        }
    def bstack11l1lllll1_opy_(self):
        return bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪᚳ")
    def bstack11ll11l11l_opy_(self, bstack1ll1l11lll1_opy_):
        self.bstack1ll1l11lll1_opy_ = bstack1ll1l11lll1_opy_