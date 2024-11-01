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
import re
from bstack_utils.bstack111l1111_opy_ import bstack1ll1llll111_opy_
def bstack1ll1llll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘌ")):
        return bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᘍ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘎ")):
        return bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᘏ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘐ")):
        return bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᘑ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᘒ")):
        return bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᘓ")
def bstack1ll1lll1lll_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᘔ"), fixture_name))
def bstack1ll1lll1l11_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᘕ"), fixture_name))
def bstack1ll1lll11l1_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᘖ"), fixture_name))
def bstack1ll1llll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᘗ")):
        return bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᘘ"), bstack111l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᘙ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᘚ")):
        return bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᘛ"), bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᘜ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᘝ")):
        return bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᘞ"), bstack111l1l_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᘟ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᘠ")):
        return bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᘡ"), bstack111l1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᘢ")
    return None, None
def bstack1ll1lllll11_opy_(hook_name):
    if hook_name in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᘣ"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᘤ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1ll1lllll1l_opy_(hook_name):
    if hook_name in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᘥ"), bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᘦ")]:
        return bstack111l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᘧ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᘨ"), bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᘩ")]:
        return bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᘪ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᘫ"), bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᘬ")]:
        return bstack111l1l_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᘭ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᘮ"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᘯ")]:
        return bstack111l1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᘰ")
    return hook_name
def bstack1ll1lll11ll_opy_(node, scenario):
    if hasattr(node, bstack111l1l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᘱ")):
        parts = node.nodeid.rsplit(bstack111l1l_opy_ (u"ࠧࡡࠢᘲ"))
        params = parts[-1]
        return bstack111l1l_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨᘳ").format(scenario.name, params)
    return scenario.name
def bstack1ll1lll111l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111l1l_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᘴ")):
            examples = list(node.callspec.params[bstack111l1l_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧᘵ")].values())
        return examples
    except:
        return []
def bstack1ll1llllll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1ll1lll1ll1_opy_(report):
    try:
        status = bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᘶ")
        if report.passed or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᘷ"))):
            status = bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᘸ")
        elif report.skipped:
            status = bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᘹ")
        bstack1ll1llll111_opy_(status)
    except:
        pass
def bstack1l1lll1lll_opy_(status):
    try:
        bstack1ll1llll1ll_opy_ = bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᘺ")
        if status == bstack111l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᘻ"):
            bstack1ll1llll1ll_opy_ = bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᘼ")
        elif status == bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᘽ"):
            bstack1ll1llll1ll_opy_ = bstack111l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᘾ")
        bstack1ll1llll111_opy_(bstack1ll1llll1ll_opy_)
    except:
        pass
def bstack1ll1lll1l1l_opy_(item=None, report=None, summary=None, extra=None):
    return