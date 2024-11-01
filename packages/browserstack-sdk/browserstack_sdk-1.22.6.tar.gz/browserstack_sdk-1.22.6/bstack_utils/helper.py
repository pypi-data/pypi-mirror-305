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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack111l1111ll_opy_, bstack1l1llll11l_opy_, bstack1ll11l1l1l_opy_, bstack1llllll11_opy_,
                                    bstack111l1l111l_opy_, bstack111l111l1l_opy_, bstack111l1l1111_opy_, bstack111l1l11l1_opy_)
from bstack_utils.messages import bstack1l1111l1_opy_, bstack1l11l1ll1_opy_
from bstack_utils.proxy import bstack11l11ll1l_opy_, bstack11lll1l11l_opy_
bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
logger = logging.getLogger(__name__)
def bstack111lll1ll1_opy_(config):
    return config[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪጐ")]
def bstack111lll111l_opy_(config):
    return config[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ጑")]
def bstack1lll1ll111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111111llll_opy_(obj):
    values = []
    bstack1111l11111_opy_ = re.compile(bstack111l1l_opy_ (u"ࡵࠦࡣࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࡟ࡨ࠰ࠪࠢጒ"), re.I)
    for key in obj.keys():
        if bstack1111l11111_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111111l1l_opy_(config):
    tags = []
    tags.extend(bstack111111llll_opy_(os.environ))
    tags.extend(bstack111111llll_opy_(config))
    return tags
def bstack1111l111l1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1llllll11l1_opy_(bstack1111l1ll1l_opy_):
    if not bstack1111l1ll1l_opy_:
        return bstack111l1l_opy_ (u"ࠫࠬጓ")
    return bstack111l1l_opy_ (u"ࠧࢁࡽࠡࠪࡾࢁ࠮ࠨጔ").format(bstack1111l1ll1l_opy_.name, bstack1111l1ll1l_opy_.email)
def bstack111ll1ll1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111l11l11_opy_ = repo.common_dir
        info = {
            bstack111l1l_opy_ (u"ࠨࡳࡩࡣࠥጕ"): repo.head.commit.hexsha,
            bstack111l1l_opy_ (u"ࠢࡴࡪࡲࡶࡹࡥࡳࡩࡣࠥ጖"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111l1l_opy_ (u"ࠣࡤࡵࡥࡳࡩࡨࠣ጗"): repo.active_branch.name,
            bstack111l1l_opy_ (u"ࠤࡷࡥ࡬ࠨጘ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࠨጙ"): bstack1llllll11l1_opy_(repo.head.commit.committer),
            bstack111l1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸ࡟ࡥࡣࡷࡩࠧጚ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111l1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࠧጛ"): bstack1llllll11l1_opy_(repo.head.commit.author),
            bstack111l1l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡥࡤࡢࡶࡨࠦጜ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111l1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣጝ"): repo.head.commit.message,
            bstack111l1l_opy_ (u"ࠣࡴࡲࡳࡹࠨጞ"): repo.git.rev_parse(bstack111l1l_opy_ (u"ࠤ࠰࠱ࡸ࡮࡯ࡸ࠯ࡷࡳࡵࡲࡥࡷࡧ࡯ࠦጟ")),
            bstack111l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡰࡰࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦጠ"): bstack1111l11l11_opy_,
            bstack111l1l_opy_ (u"ࠦࡼࡵࡲ࡬ࡶࡵࡩࡪࡥࡧࡪࡶࡢࡨ࡮ࡸࠢጡ"): subprocess.check_output([bstack111l1l_opy_ (u"ࠧ࡭ࡩࡵࠤጢ"), bstack111l1l_opy_ (u"ࠨࡲࡦࡸ࠰ࡴࡦࡸࡳࡦࠤጣ"), bstack111l1l_opy_ (u"ࠢ࠮࠯ࡪ࡭ࡹ࠳ࡣࡰ࡯ࡰࡳࡳ࠳ࡤࡪࡴࠥጤ")]).strip().decode(
                bstack111l1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧጥ")),
            bstack111l1l_opy_ (u"ࠤ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦጦ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡶࡣࡸ࡯࡮ࡤࡧࡢࡰࡦࡹࡴࡠࡶࡤ࡫ࠧጧ"): repo.git.rev_list(
                bstack111l1l_opy_ (u"ࠦࢀࢃ࠮࠯ࡽࢀࠦጨ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lll1ll_opy_ = []
        for remote in remotes:
            bstack1lllllll1ll_opy_ = {
                bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥጩ"): remote.name,
                bstack111l1l_opy_ (u"ࠨࡵࡳ࡮ࠥጪ"): remote.url,
            }
            bstack1111lll1ll_opy_.append(bstack1lllllll1ll_opy_)
        bstack1llllll1lll_opy_ = {
            bstack111l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧጫ"): bstack111l1l_opy_ (u"ࠣࡩ࡬ࡸࠧጬ"),
            **info,
            bstack111l1l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡵࠥጭ"): bstack1111lll1ll_opy_
        }
        bstack1llllll1lll_opy_ = bstack1111l1lll1_opy_(bstack1llllll1lll_opy_)
        return bstack1llllll1lll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨጮ").format(err))
        return {}
def bstack1111l1lll1_opy_(bstack1llllll1lll_opy_):
    bstack111111l11l_opy_ = bstack1111ll1111_opy_(bstack1llllll1lll_opy_)
    if bstack111111l11l_opy_ and bstack111111l11l_opy_ > bstack111l1l111l_opy_:
        bstack11111lll11_opy_ = bstack111111l11l_opy_ - bstack111l1l111l_opy_
        bstack1111lll111_opy_ = bstack11111ll1ll_opy_(bstack1llllll1lll_opy_[bstack111l1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧጯ")], bstack11111lll11_opy_)
        bstack1llllll1lll_opy_[bstack111l1l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨጰ")] = bstack1111lll111_opy_
        logger.info(bstack111l1l_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣጱ")
                    .format(bstack1111ll1111_opy_(bstack1llllll1lll_opy_) / 1024))
    return bstack1llllll1lll_opy_
def bstack1111ll1111_opy_(bstack11l11ll1_opy_):
    try:
        if bstack11l11ll1_opy_:
            bstack11111111l1_opy_ = json.dumps(bstack11l11ll1_opy_)
            bstack11111l1l1l_opy_ = sys.getsizeof(bstack11111111l1_opy_)
            return bstack11111l1l1l_opy_
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢጲ").format(e))
    return -1
def bstack11111ll1ll_opy_(field, bstack1lllll1lll1_opy_):
    try:
        bstack1111111ll1_opy_ = len(bytes(bstack111l111l1l_opy_, bstack111l1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧጳ")))
        bstack1llllll1ll1_opy_ = bytes(field, bstack111l1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨጴ"))
        bstack1111lllll1_opy_ = len(bstack1llllll1ll1_opy_)
        bstack1111ll1l11_opy_ = ceil(bstack1111lllll1_opy_ - bstack1lllll1lll1_opy_ - bstack1111111ll1_opy_)
        if bstack1111ll1l11_opy_ > 0:
            bstack111111l1l1_opy_ = bstack1llllll1ll1_opy_[:bstack1111ll1l11_opy_].decode(bstack111l1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩጵ"), errors=bstack111l1l_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫጶ")) + bstack111l111l1l_opy_
            return bstack111111l1l1_opy_
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥጷ").format(e))
    return field
def bstack1ll1llll1_opy_():
    env = os.environ
    if (bstack111l1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦጸ") in env and len(env[bstack111l1l_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧጹ")]) > 0) or (
            bstack111l1l_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢጺ") in env and len(env[bstack111l1l_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣጻ")]) > 0):
        return {
            bstack111l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣጼ"): bstack111l1l_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧጽ"),
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣጾ"): env.get(bstack111l1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤጿ")),
            bstack111l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤፀ"): env.get(bstack111l1l_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥፁ")),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣፂ"): env.get(bstack111l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤፃ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠦࡈࡏࠢፄ")) == bstack111l1l_opy_ (u"ࠧࡺࡲࡶࡧࠥፅ") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣፆ"))):
        return {
            bstack111l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧፇ"): bstack111l1l_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥፈ"),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧፉ"): env.get(bstack111l1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨፊ")),
            bstack111l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨፋ"): env.get(bstack111l1l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤፌ")),
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧፍ"): env.get(bstack111l1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥፎ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠣࡅࡌࠦፏ")) == bstack111l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢፐ") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥፑ"))):
        return {
            bstack111l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤፒ"): bstack111l1l_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣፓ"),
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤፔ"): env.get(bstack111l1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢፕ")),
            bstack111l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥፖ"): env.get(bstack111l1l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦፗ")),
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤፘ"): env.get(bstack111l1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥፙ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠧࡉࡉࠣፚ")) == bstack111l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ፛") and env.get(bstack111l1l_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣ፜")) == bstack111l1l_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥ፝"):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ፞"): bstack111l1l_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧ፟"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ፠"): None,
            bstack111l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ፡"): None,
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ።"): None
        }
    if env.get(bstack111l1l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥ፣")) and env.get(bstack111l1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦ፤")):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ፥"): bstack111l1l_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨ፦"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ፧"): env.get(bstack111l1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥ፨")),
            bstack111l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ፩"): None,
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ፪"): env.get(bstack111l1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ፫"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠤࡆࡍࠧ፬")) == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣ፭") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥ፮"))):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ፯"): bstack111l1l_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧ፰"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ፱"): env.get(bstack111l1l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦ፲")),
            bstack111l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ፳"): None,
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ፴"): env.get(bstack111l1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ፵"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠧࡉࡉࠣ፶")) == bstack111l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ፷") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥ፸"))):
        return {
            bstack111l1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ፹"): bstack111l1l_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧ፺"),
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ፻"): env.get(bstack111l1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥ፼")),
            bstack111l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ፽"): env.get(bstack111l1l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ፾")),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ፿"): env.get(bstack111l1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᎀ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠤࡆࡍࠧᎁ")) == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᎂ") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᎃ"))):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᎄ"): bstack111l1l_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᎅ"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᎆ"): env.get(bstack111l1l_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᎇ")),
            bstack111l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᎈ"): env.get(bstack111l1l_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᎉ")),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᎊ"): env.get(bstack111l1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣᎋ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠨࡃࡊࠤᎌ")) == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᎍ") and bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦᎎ"))):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎏ"): bstack111l1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨ᎐"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᎑"): env.get(bstack111l1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᎒")),
            bstack111l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᎓"): env.get(bstack111l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤ᎔")) or env.get(bstack111l1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦ᎕")),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᎖"): env.get(bstack111l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᎗"))
        }
    if bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨ᎘"))):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᎙"): bstack111l1l_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨ᎚"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᎛"): bstack111l1l_opy_ (u"ࠣࡽࢀࡿࢂࠨ᎜").format(env.get(bstack111l1l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬ᎝")), env.get(bstack111l1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪ᎞"))),
            bstack111l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᎟"): env.get(bstack111l1l_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦᎠ")),
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᎡ"): env.get(bstack111l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᎢ"))
        }
    if bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥᎣ"))):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎤ"): bstack111l1l_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧᎥ"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᎦ"): bstack111l1l_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦᎧ").format(env.get(bstack111l1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬᎨ")), env.get(bstack111l1l_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨᎩ")), env.get(bstack111l1l_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩᎪ")), env.get(bstack111l1l_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭Ꭻ"))),
            bstack111l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᎬ"): env.get(bstack111l1l_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᎭ")),
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᎮ"): env.get(bstack111l1l_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᎯ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣᎰ")) and env.get(bstack111l1l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥᎱ")):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎲ"): bstack111l1l_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧᎳ"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᎴ"): bstack111l1l_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣᎵ").format(env.get(bstack111l1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩᎶ")), env.get(bstack111l1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬᎷ")), env.get(bstack111l1l_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨᎸ"))),
            bstack111l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᎹ"): env.get(bstack111l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᎺ")),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᎻ"): env.get(bstack111l1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᎼ"))
        }
    if any([env.get(bstack111l1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᎽ")), env.get(bstack111l1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᎾ")), env.get(bstack111l1l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᎿ"))]):
        return {
            bstack111l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᏀ"): bstack111l1l_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥᏁ"),
            bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᏂ"): env.get(bstack111l1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᏃ")),
            bstack111l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᏄ"): env.get(bstack111l1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᏅ")),
            bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᏆ"): env.get(bstack111l1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᏇ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣᏈ")):
        return {
            bstack111l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏉ"): bstack111l1l_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧᏊ"),
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᏋ"): env.get(bstack111l1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤᏌ")),
            bstack111l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᏍ"): env.get(bstack111l1l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣᏎ")),
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᏏ"): env.get(bstack111l1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᏐ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨᏑ")) or env.get(bstack111l1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᏒ")):
        return {
            bstack111l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏓ"): bstack111l1l_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤᏔ"),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᏕ"): env.get(bstack111l1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᏖ")),
            bstack111l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᏗ"): bstack111l1l_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧᏘ") if env.get(bstack111l1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᏙ")) else None,
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᏚ"): env.get(bstack111l1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᏛ"))
        }
    if any([env.get(bstack111l1l_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᏜ")), env.get(bstack111l1l_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᏝ")), env.get(bstack111l1l_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᏞ"))]):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏟ"): bstack111l1l_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧᏠ"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᏡ"): None,
            bstack111l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᏢ"): env.get(bstack111l1l_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨᏣ")),
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᏤ"): env.get(bstack111l1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᏥ"))
        }
    if env.get(bstack111l1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣᏦ")):
        return {
            bstack111l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᏧ"): bstack111l1l_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥᏨ"),
            bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᏩ"): env.get(bstack111l1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᏪ")),
            bstack111l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᏫ"): bstack111l1l_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧᏬ").format(env.get(bstack111l1l_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨᏭ"))) if env.get(bstack111l1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤᏮ")) else None,
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᏯ"): env.get(bstack111l1l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᏰ"))
        }
    if bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥᏱ"))):
        return {
            bstack111l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᏲ"): bstack111l1l_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧᏳ"),
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᏴ"): env.get(bstack111l1l_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥᏵ")),
            bstack111l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᏶"): env.get(bstack111l1l_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦ᏷")),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᏸ"): env.get(bstack111l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᏹ"))
        }
    if bstack11ll111l_opy_(env.get(bstack111l1l_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧᏺ"))):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏻ"): bstack111l1l_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢᏼ"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᏽ"): bstack111l1l_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤ᏾").format(env.get(bstack111l1l_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭᏿")), env.get(bstack111l1l_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧ᐀")), env.get(bstack111l1l_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᐁ"))),
            bstack111l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᐂ"): env.get(bstack111l1l_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣᐃ")),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᐄ"): env.get(bstack111l1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᐅ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠤࡆࡍࠧᐆ")) == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᐇ") and env.get(bstack111l1l_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦᐈ")) == bstack111l1l_opy_ (u"ࠧ࠷ࠢᐉ"):
        return {
            bstack111l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐊ"): bstack111l1l_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢᐋ"),
            bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᐌ"): bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧᐍ").format(env.get(bstack111l1l_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧᐎ"))),
            bstack111l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᐏ"): None,
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᐐ"): None,
        }
    if env.get(bstack111l1l_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤᐑ")):
        return {
            bstack111l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐒ"): bstack111l1l_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥᐓ"),
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᐔ"): None,
            bstack111l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᐕ"): env.get(bstack111l1l_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᐖ")),
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᐗ"): env.get(bstack111l1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᐘ"))
        }
    if any([env.get(bstack111l1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᐙ")), env.get(bstack111l1l_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᐚ")), env.get(bstack111l1l_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᐛ")), env.get(bstack111l1l_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᐜ"))]):
        return {
            bstack111l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐝ"): bstack111l1l_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᐞ"),
            bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᐟ"): None,
            bstack111l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᐠ"): env.get(bstack111l1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᐡ")) or None,
            bstack111l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᐢ"): env.get(bstack111l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᐣ"), 0)
        }
    if env.get(bstack111l1l_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᐤ")):
        return {
            bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᐥ"): bstack111l1l_opy_ (u"ࠨࡇࡰࡅࡇࠦᐦ"),
            bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᐧ"): None,
            bstack111l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᐨ"): env.get(bstack111l1l_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᐩ")),
            bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᐪ"): env.get(bstack111l1l_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᐫ"))
        }
    if env.get(bstack111l1l_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᐬ")):
        return {
            bstack111l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐭ"): bstack111l1l_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᐮ"),
            bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᐯ"): env.get(bstack111l1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᐰ")),
            bstack111l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᐱ"): env.get(bstack111l1l_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᐲ")),
            bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᐳ"): env.get(bstack111l1l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᐴ"))
        }
    return {bstack111l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᐵ"): None}
def get_host_info():
    return {
        bstack111l1l_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᐶ"): platform.node(),
        bstack111l1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᐷ"): platform.system(),
        bstack111l1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᐸ"): platform.machine(),
        bstack111l1l_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᐹ"): platform.version(),
        bstack111l1l_opy_ (u"ࠧࡧࡲࡤࡪࠥᐺ"): platform.architecture()[0]
    }
def bstack1ll11l111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111l11lll_opy_():
    if bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᐻ")):
        return bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᐼ")
    return bstack111l1l_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᐽ")
def bstack11111ll11l_opy_(driver):
    info = {
        bstack111l1l_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᐾ"): driver.capabilities,
        bstack111l1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᐿ"): driver.session_id,
        bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᑀ"): driver.capabilities.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᑁ"), None),
        bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᑂ"): driver.capabilities.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᑃ"), None),
        bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᑄ"): driver.capabilities.get(bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᑅ"), None),
    }
    if bstack1111l11lll_opy_() == bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᑆ"):
        info[bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᑇ")] = bstack111l1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᑈ") if bstack1l11ll11_opy_() else bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᑉ")
    return info
def bstack1l11ll11_opy_():
    if bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᑊ")):
        return True
    if bstack11ll111l_opy_(os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᑋ"), None)):
        return True
    return False
def bstack1ll1ll111_opy_(bstack1111l1ll11_opy_, url, data, config):
    headers = config.get(bstack111l1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᑌ"), None)
    proxies = bstack11l11ll1l_opy_(config, url)
    auth = config.get(bstack111l1l_opy_ (u"ࠪࡥࡺࡺࡨࠨᑍ"), None)
    response = requests.request(
            bstack1111l1ll11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1lll111l1_opy_(bstack1ll1ll111l_opy_, size):
    bstack11llll11ll_opy_ = []
    while len(bstack1ll1ll111l_opy_) > size:
        bstack1111lll11_opy_ = bstack1ll1ll111l_opy_[:size]
        bstack11llll11ll_opy_.append(bstack1111lll11_opy_)
        bstack1ll1ll111l_opy_ = bstack1ll1ll111l_opy_[size:]
    bstack11llll11ll_opy_.append(bstack1ll1ll111l_opy_)
    return bstack11llll11ll_opy_
def bstack1111l1llll_opy_(message, bstack111111ll1l_opy_=False):
    os.write(1, bytes(message, bstack111l1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᑎ")))
    os.write(1, bytes(bstack111l1l_opy_ (u"ࠬࡢ࡮ࠨᑏ"), bstack111l1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᑐ")))
    if bstack111111ll1l_opy_:
        with open(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᑑ") + os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᑒ")] + bstack111l1l_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᑓ"), bstack111l1l_opy_ (u"ࠪࡥࠬᑔ")) as f:
            f.write(message + bstack111l1l_opy_ (u"ࠫࡡࡴࠧᑕ"))
def bstack1lllllll1l1_opy_():
    return os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᑖ")].lower() == bstack111l1l_opy_ (u"࠭ࡴࡳࡷࡨࠫᑗ")
def bstack1ll11l111l_opy_(bstack1111llll1l_opy_):
    return bstack111l1l_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ᑘ").format(bstack111l1111ll_opy_, bstack1111llll1l_opy_)
def bstack1l1ll11l_opy_():
    return bstack11ll11111l_opy_().replace(tzinfo=None).isoformat() + bstack111l1l_opy_ (u"ࠨ࡜ࠪᑙ")
def bstack1111l11l1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111l1l_opy_ (u"ࠩ࡝ࠫᑚ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111l1l_opy_ (u"ࠪ࡞ࠬᑛ")))).total_seconds() * 1000
def bstack11111l1l11_opy_(timestamp):
    return bstack1llllll1l11_opy_(timestamp).isoformat() + bstack111l1l_opy_ (u"ࠫ࡟࠭ᑜ")
def bstack1llllll111l_opy_(bstack111111ll11_opy_):
    date_format = bstack111l1l_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᑝ")
    bstack111l1111l1_opy_ = datetime.datetime.strptime(bstack111111ll11_opy_, date_format)
    return bstack111l1111l1_opy_.isoformat() + bstack111l1l_opy_ (u"࡚࠭ࠨᑞ")
def bstack1lllllll111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᑟ")
    else:
        return bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᑠ")
def bstack11ll111l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᑡ")
def bstack1llllllllll_opy_(val):
    return val.__str__().lower() == bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᑢ")
def bstack11l1l1ll1l_opy_(bstack1111ll1l1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111ll1l1l_opy_ as e:
                print(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᑣ").format(func.__name__, bstack1111ll1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11111l11l1_opy_(bstack11111ll1l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11111ll1l1_opy_(cls, *args, **kwargs)
            except bstack1111ll1l1l_opy_ as e:
                print(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᑤ").format(bstack11111ll1l1_opy_.__name__, bstack1111ll1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11111l11l1_opy_
    else:
        return decorator
def bstack1lll1ll1_opy_(bstack11l111ll1l_opy_):
    if bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᑥ") in bstack11l111ll1l_opy_ and bstack1llllllllll_opy_(bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᑦ")]):
        return False
    if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᑧ") in bstack11l111ll1l_opy_ and bstack1llllllllll_opy_(bstack11l111ll1l_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᑨ")]):
        return False
    return True
def bstack11llll1l_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1l1l11111_opy_(hub_url, CONFIG):
    if bstack1111ll1l_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪᑩ")):
        if hub_url != bstack111l1l_opy_ (u"ࠫࠬᑪ"):
            return bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᑫ") + hub_url + bstack111l1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥᑬ")
        return bstack1ll11l1l1l_opy_
    if hub_url != bstack111l1l_opy_ (u"ࠧࠨᑭ"):
        return bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᑮ") + hub_url + bstack111l1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᑯ")
    return bstack1llllll11_opy_
def bstack1111ll11l1_opy_():
    return isinstance(os.getenv(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩᑰ")), str)
def bstack111ll11l1_opy_(url):
    return urlparse(url).hostname
def bstack1l1ll1ll_opy_(hostname):
    for bstack1ll1l1l1ll_opy_ in bstack1l1llll11l_opy_:
        regex = re.compile(bstack1ll1l1l1ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1111l1l1l1_opy_(bstack11111lllll_opy_, file_name, logger):
    bstack111l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠫࢃ࠭ᑱ")), bstack11111lllll_opy_)
    try:
        if not os.path.exists(bstack111l1l1l1_opy_):
            os.makedirs(bstack111l1l1l1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠬࢄࠧᑲ")), bstack11111lllll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111l1l_opy_ (u"࠭ࡷࠨᑳ")):
                pass
            with open(file_path, bstack111l1l_opy_ (u"ࠢࡸ࠭ࠥᑴ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l1111l1_opy_.format(str(e)))
def bstack1111111lll_opy_(file_name, key, value, logger):
    file_path = bstack1111l1l1l1_opy_(bstack111l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᑵ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111lll11_opy_ = json.load(open(file_path, bstack111l1l_opy_ (u"ࠩࡵࡦࠬᑶ")))
        else:
            bstack111lll11_opy_ = {}
        bstack111lll11_opy_[key] = value
        with open(file_path, bstack111l1l_opy_ (u"ࠥࡻ࠰ࠨᑷ")) as outfile:
            json.dump(bstack111lll11_opy_, outfile)
def bstack11lllllll1_opy_(file_name, logger):
    file_path = bstack1111l1l1l1_opy_(bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᑸ"), file_name, logger)
    bstack111lll11_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111l1l_opy_ (u"ࠬࡸࠧᑹ")) as bstack1llll11l1l_opy_:
            bstack111lll11_opy_ = json.load(bstack1llll11l1l_opy_)
    return bstack111lll11_opy_
def bstack1l111ll111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᑺ") + file_path + bstack111l1l_opy_ (u"ࠧࠡࠩᑻ") + str(e))
def bstack1111ll1l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111l1l_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᑼ")
def bstack11l11111l_opy_(config):
    if bstack111l1l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᑽ") in config:
        del (config[bstack111l1l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᑾ")])
        return False
    if bstack1111ll1l_opy_() < version.parse(bstack111l1l_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᑿ")):
        return False
    if bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᒀ")):
        return True
    if bstack111l1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᒁ") in config and config[bstack111l1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᒂ")] is False:
        return False
    else:
        return True
def bstack1ll11lll1l_opy_(args_list, bstack1lllllll11l_opy_):
    index = -1
    for value in bstack1lllllll11l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11ll11lll1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11ll11lll1_opy_ = bstack11ll11lll1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᒃ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᒄ"), exception=exception)
    def bstack11l11111l1_opy_(self):
        if self.result != bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᒅ"):
            return None
        if isinstance(self.exception_type, str) and bstack111l1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᒆ") in self.exception_type:
            return bstack111l1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᒇ")
        return bstack111l1l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᒈ")
    def bstack1111ll1ll1_opy_(self):
        if self.result != bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒉ"):
            return None
        if self.bstack11ll11lll1_opy_:
            return self.bstack11ll11lll1_opy_
        return bstack1111ll1lll_opy_(self.exception)
def bstack1111ll1lll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l11111l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll111l11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1lll1l_opy_(config, logger):
    try:
        import playwright
        bstack1111llll11_opy_ = playwright.__file__
        bstack1111ll11ll_opy_ = os.path.split(bstack1111llll11_opy_)
        bstack1111111l11_opy_ = bstack1111ll11ll_opy_[0] + bstack111l1l_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫᒊ")
        os.environ[bstack111l1l_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ࠬᒋ")] = bstack11lll1l11l_opy_(config)
        with open(bstack1111111l11_opy_, bstack111l1l_opy_ (u"ࠪࡶࠬᒌ")) as f:
            bstack1l11lllll1_opy_ = f.read()
            bstack1111ll111l_opy_ = bstack111l1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪᒍ")
            bstack1111l1111l_opy_ = bstack1l11lllll1_opy_.find(bstack1111ll111l_opy_)
            if bstack1111l1111l_opy_ == -1:
              process = subprocess.Popen(bstack111l1l_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤᒎ"), shell=True, cwd=bstack1111ll11ll_opy_[0])
              process.wait()
              bstack1lllll1llll_opy_ = bstack111l1l_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭ᒏ")
              bstack1llllll11ll_opy_ = bstack111l1l_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦᒐ")
              bstack11111l1ll1_opy_ = bstack1l11lllll1_opy_.replace(bstack1lllll1llll_opy_, bstack1llllll11ll_opy_)
              with open(bstack1111111l11_opy_, bstack111l1l_opy_ (u"ࠨࡹࠪᒑ")) as f:
                f.write(bstack11111l1ll1_opy_)
    except Exception as e:
        logger.error(bstack1l11l1ll1_opy_.format(str(e)))
def bstack11111l111_opy_():
  try:
    bstack111111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᒒ"))
    bstack11111lll1l_opy_ = []
    if os.path.exists(bstack111111111l_opy_):
      with open(bstack111111111l_opy_) as f:
        bstack11111lll1l_opy_ = json.load(f)
      os.remove(bstack111111111l_opy_)
    return bstack11111lll1l_opy_
  except:
    pass
  return []
def bstack1111l1111_opy_(bstack1l11lll11l_opy_):
  try:
    bstack11111lll1l_opy_ = []
    bstack111111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᒓ"))
    if os.path.exists(bstack111111111l_opy_):
      with open(bstack111111111l_opy_) as f:
        bstack11111lll1l_opy_ = json.load(f)
    bstack11111lll1l_opy_.append(bstack1l11lll11l_opy_)
    with open(bstack111111111l_opy_, bstack111l1l_opy_ (u"ࠫࡼ࠭ᒔ")) as f:
        json.dump(bstack11111lll1l_opy_, f)
  except:
    pass
def bstack1lll1l111_opy_(logger, bstack11111ll111_opy_ = False):
  try:
    test_name = os.environ.get(bstack111l1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᒕ"), bstack111l1l_opy_ (u"࠭ࠧᒖ"))
    if test_name == bstack111l1l_opy_ (u"ࠧࠨᒗ"):
        test_name = threading.current_thread().__dict__.get(bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧᒘ"), bstack111l1l_opy_ (u"ࠩࠪᒙ"))
    bstack1111llllll_opy_ = bstack111l1l_opy_ (u"ࠪ࠰ࠥ࠭ᒚ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11111ll111_opy_:
        bstack1ll11ll1_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᒛ"), bstack111l1l_opy_ (u"ࠬ࠶ࠧᒜ"))
        bstack1ll11111_opy_ = {bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᒝ"): test_name, bstack111l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᒞ"): bstack1111llllll_opy_, bstack111l1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᒟ"): bstack1ll11ll1_opy_}
        bstack1llllllll1l_opy_ = []
        bstack11111l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᒠ"))
        if os.path.exists(bstack11111l1lll_opy_):
            with open(bstack11111l1lll_opy_) as f:
                bstack1llllllll1l_opy_ = json.load(f)
        bstack1llllllll1l_opy_.append(bstack1ll11111_opy_)
        with open(bstack11111l1lll_opy_, bstack111l1l_opy_ (u"ࠪࡻࠬᒡ")) as f:
            json.dump(bstack1llllllll1l_opy_, f)
    else:
        bstack1ll11111_opy_ = {bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᒢ"): test_name, bstack111l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᒣ"): bstack1111llllll_opy_, bstack111l1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᒤ"): str(multiprocessing.current_process().name)}
        if bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᒥ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1ll11111_opy_)
  except Exception as e:
      logger.warn(bstack111l1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᒦ").format(e))
def bstack1111lllll_opy_(error_message, test_name, index, logger):
  try:
    bstack11111llll1_opy_ = []
    bstack1ll11111_opy_ = {bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᒧ"): test_name, bstack111l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᒨ"): error_message, bstack111l1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᒩ"): index}
    bstack1111l1l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᒪ"))
    if os.path.exists(bstack1111l1l11l_opy_):
        with open(bstack1111l1l11l_opy_) as f:
            bstack11111llll1_opy_ = json.load(f)
    bstack11111llll1_opy_.append(bstack1ll11111_opy_)
    with open(bstack1111l1l11l_opy_, bstack111l1l_opy_ (u"࠭ࡷࠨᒫ")) as f:
        json.dump(bstack11111llll1_opy_, f)
  except Exception as e:
    logger.warn(bstack111l1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᒬ").format(e))
def bstack1lll11l1l_opy_(bstack11lll1ll1_opy_, name, logger):
  try:
    bstack1ll11111_opy_ = {bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᒭ"): name, bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᒮ"): bstack11lll1ll1_opy_, bstack111l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᒯ"): str(threading.current_thread()._name)}
    return bstack1ll11111_opy_
  except Exception as e:
    logger.warn(bstack111l1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡢࡦࡪࡤࡺࡪࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᒰ").format(e))
  return
def bstack111111l1ll_opy_():
    return platform.system() == bstack111l1l_opy_ (u"ࠬ࡝ࡩ࡯ࡦࡲࡻࡸ࠭ᒱ")
def bstack11ll11ll1_opy_(bstack1llllll1l1l_opy_, config, logger):
    bstack1llllll1111_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1llllll1l1l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡱࡺࡥࡳࠢࡦࡳࡳ࡬ࡩࡨࠢ࡮ࡩࡾࡹࠠࡣࡻࠣࡶࡪ࡭ࡥࡹࠢࡰࡥࡹࡩࡨ࠻ࠢࡾࢁࠧᒲ").format(e))
    return bstack1llllll1111_opy_
def bstack1111111111_opy_(bstack11111l111l_opy_, bstack1llllllll11_opy_):
    bstack1111l111ll_opy_ = version.parse(bstack11111l111l_opy_)
    bstack11111111ll_opy_ = version.parse(bstack1llllllll11_opy_)
    if bstack1111l111ll_opy_ > bstack11111111ll_opy_:
        return 1
    elif bstack1111l111ll_opy_ < bstack11111111ll_opy_:
        return -1
    else:
        return 0
def bstack11ll11111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1llllll1l11_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll1l1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11llllll1_opy_(options, framework):
    if options is None:
        return
    if getattr(options, bstack111l1l_opy_ (u"ࠧࡨࡧࡷࠫᒳ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack111lll11l_opy_ = caps.get(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒴ"))
    bstack111111lll1_opy_ = True
    if bstack1llllllllll_opy_(caps.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩ࡜࠹ࡃࠨᒵ"))) or bstack1llllllllll_opy_(caps.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪᒶ"))):
        bstack111111lll1_opy_ = False
    if bstack11l11111l_opy_({bstack111l1l_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦᒷ"): bstack111111lll1_opy_}):
        bstack111lll11l_opy_ = bstack111lll11l_opy_ or {}
        bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᒸ")] = bstack1111lll1l1_opy_(framework)
        bstack111lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᒹ")] = bstack1lllllll1l1_opy_()
        if getattr(options, bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨᒺ"), None):
            options.set_capability(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒻ"), bstack111lll11l_opy_)
        else:
            options[bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᒼ")] = bstack111lll11l_opy_
    else:
        if getattr(options, bstack111l1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫᒽ"), None):
            options.set_capability(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᒾ"), bstack1111lll1l1_opy_(framework))
            options.set_capability(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᒿ"), bstack1lllllll1l1_opy_())
        else:
            options[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᓀ")] = bstack1111lll1l1_opy_(framework)
            options[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᓁ")] = bstack1lllllll1l1_opy_()
    return options
def bstack11111l1111_opy_(bstack1111l1l111_opy_, framework):
    if bstack1111l1l111_opy_ and len(bstack1111l1l111_opy_.split(bstack111l1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᓂ"))) > 1:
        ws_url = bstack1111l1l111_opy_.split(bstack111l1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᓃ"))[0]
        if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᓄ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1lllllllll1_opy_ = json.loads(urllib.parse.unquote(bstack1111l1l111_opy_.split(bstack111l1l_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᓅ"))[1]))
            bstack1lllllllll1_opy_ = bstack1lllllllll1_opy_ or {}
            bstack1lllllllll1_opy_[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᓆ")] = str(framework) + str(__version__)
            bstack1lllllllll1_opy_[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᓇ")] = bstack1lllllll1l1_opy_()
            bstack1111l1l111_opy_ = bstack1111l1l111_opy_.split(bstack111l1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᓈ"))[0] + bstack111l1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᓉ") + urllib.parse.quote(json.dumps(bstack1lllllllll1_opy_))
    return bstack1111l1l111_opy_
def bstack1l1l1ll111_opy_():
    global bstack111ll1l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111ll1l1_opy_ = BrowserType.connect
    return bstack111ll1l1_opy_
def bstack1ll11l1l1_opy_(framework_name):
    global bstack1l1111llll_opy_
    bstack1l1111llll_opy_ = framework_name
    return framework_name
def bstack11l1ll111_opy_(self, *args, **kwargs):
    global bstack111ll1l1_opy_
    try:
        global bstack1l1111llll_opy_
        if bstack111l1l_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᓊ") in kwargs:
            kwargs[bstack111l1l_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᓋ")] = bstack11111l1111_opy_(
                kwargs.get(bstack111l1l_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᓌ"), None),
                bstack1l1111llll_opy_
            )
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧᓍ").format(str(e)))
    return bstack111ll1l1_opy_(self, *args, **kwargs)
def bstack111l111111_opy_(bstack1111lll11l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l11ll1l_opy_(bstack1111lll11l_opy_, bstack111l1l_opy_ (u"ࠨࠢᓎ"))
        if proxies and proxies.get(bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᓏ")):
            parsed_url = urlparse(proxies.get(bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᓐ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬᓑ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᓒ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧᓓ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨᓔ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l11111l1_opy_(bstack1111lll11l_opy_):
    bstack111111l111_opy_ = {
        bstack111l1l11l1_opy_[bstack1111l1l1ll_opy_]: bstack1111lll11l_opy_[bstack1111l1l1ll_opy_]
        for bstack1111l1l1ll_opy_ in bstack1111lll11l_opy_
        if bstack1111l1l1ll_opy_ in bstack111l1l11l1_opy_
    }
    bstack111111l111_opy_[bstack111l1l_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᓕ")] = bstack111l111111_opy_(bstack1111lll11l_opy_, bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢᓖ")))
    bstack11111l11ll_opy_ = [element.lower() for element in bstack111l1l1111_opy_]
    bstack1111l11ll1_opy_(bstack111111l111_opy_, bstack11111l11ll_opy_)
    return bstack111111l111_opy_
def bstack1111l11ll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack111l1l_opy_ (u"ࠣࠬ࠭࠮࠯ࠨᓗ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l11ll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l11ll1_opy_(item, keys)