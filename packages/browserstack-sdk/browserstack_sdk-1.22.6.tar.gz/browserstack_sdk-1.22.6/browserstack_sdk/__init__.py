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
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1ll1lll1_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11lllll1ll_opy_ import bstack1l11ll1l11_opy_
import time
import requests
def bstack1l11l11l_opy_():
  global CONFIG
  headers = {
        bstack111l1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack11l11ll1l_opy_(CONFIG, bstack1l1111l1ll_opy_)
  try:
    response = requests.get(bstack1l1111l1ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l111llll1_opy_ = response.json()[bstack111l1l_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1ll1l11ll1_opy_.format(response.json()))
      return bstack1l111llll1_opy_
    else:
      logger.debug(bstack11l11l1l_opy_.format(bstack111l1l_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack11l11l1l_opy_.format(e))
def bstack1l1111l1l1_opy_(hub_url):
  global CONFIG
  url = bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack111l1l_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack111l1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack11l11ll1l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11ll111ll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111l1l1l_opy_.format(hub_url, e))
def bstack1ll1l111l_opy_():
  try:
    global bstack1l1ll11l11_opy_
    bstack1l111llll1_opy_ = bstack1l11l11l_opy_()
    bstack1ll11lll_opy_ = []
    results = []
    for bstack1lll1ll1l1_opy_ in bstack1l111llll1_opy_:
      bstack1ll11lll_opy_.append(bstack1ll111lll_opy_(target=bstack1l1111l1l1_opy_,args=(bstack1lll1ll1l1_opy_,)))
    for t in bstack1ll11lll_opy_:
      t.start()
    for t in bstack1ll11lll_opy_:
      results.append(t.join())
    bstack1ll11lll1_opy_ = {}
    for item in results:
      hub_url = item[bstack111l1l_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack111l1l_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1ll11lll1_opy_[hub_url] = latency
    bstack1lll1l1l_opy_ = min(bstack1ll11lll1_opy_, key= lambda x: bstack1ll11lll1_opy_[x])
    bstack1l1ll11l11_opy_ = bstack1lll1l1l_opy_
    logger.debug(bstack11lll11l11_opy_.format(bstack1lll1l1l_opy_))
  except Exception as e:
    logger.debug(bstack1llll111l_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1llll11lll_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack11ll11ll1_opy_, bstack1ll1ll111_opy_, bstack1ll11l111l_opy_, bstack1ll111l11_opy_, bstack1lll1ll1_opy_, \
  Notset, bstack11l11111l_opy_, \
  bstack11lllllll1_opy_, bstack1l111ll111_opy_, bstack1ll11lll1l_opy_, bstack1ll1llll1_opy_, bstack11llll1l_opy_, bstack1ll11l111_opy_, \
  bstack1lll1ll111_opy_, \
  bstack1l1lll1l_opy_, bstack11111l111_opy_, bstack1111l1111_opy_, bstack1lll11l1l_opy_, \
  bstack1lll1l111_opy_, bstack1111lllll_opy_, bstack11ll111l_opy_, bstack1l11111l1_opy_
from bstack_utils.bstack11llll11_opy_ import bstack1l1l1l111l_opy_
from bstack_utils.bstack1l111l1lll_opy_ import bstack11llll1ll1_opy_
from bstack_utils.bstack111l1111_opy_ import bstack1llll1llll_opy_, bstack11llll11l_opy_
from bstack_utils.bstack1l111111ll_opy_ import bstack1l1l1ll1l_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.bstack1lllll1lll_opy_ import bstack1lllll1lll_opy_
from bstack_utils.proxy import bstack1lll11l111_opy_, bstack11l11ll1l_opy_, bstack11lll1l11l_opy_, bstack11l1l1l1l_opy_
import bstack_utils.bstack1ll1ll1l11_opy_ as bstack1l1l1lll_opy_
from browserstack_sdk.bstack1l111l1l11_opy_ import *
from browserstack_sdk.bstack1lll11lll1_opy_ import *
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1l1lll1lll_opy_
from browserstack_sdk.bstack1l11l11ll_opy_ import *
import requests
from bstack_utils.constants import *
def bstack1llll1111_opy_():
    global bstack1l1ll11l11_opy_
    try:
        bstack11lll1ll_opy_ = bstack11111ll1l_opy_()
        bstack1lll111l11_opy_(bstack11lll1ll_opy_)
        hub_url = bstack11lll1ll_opy_.get(bstack111l1l_opy_ (u"ࠨࡵࡳ࡮ࠥࢀ"), bstack111l1l_opy_ (u"ࠢࠣࢁ"))
        if hub_url.endswith(bstack111l1l_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩࢂ")):
            hub_url = hub_url.rsplit(bstack111l1l_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪࢃ"), 1)[0]
        if hub_url.startswith(bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫࢄ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭ࢅ")):
            hub_url = hub_url[8:]
        bstack1l1ll11l11_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11111ll1l_opy_():
    global CONFIG
    bstack1l1l11l1ll_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢆ"), {}).get(bstack111l1l_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨࢇ"), bstack111l1l_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭࢈"))
    if not isinstance(bstack1l1l11l1ll_opy_, str):
        raise ValueError(bstack111l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧࢉ"))
    try:
        bstack11lll1ll_opy_ = bstack11lll1lll_opy_(bstack1l1l11l1ll_opy_)
        return bstack11lll1ll_opy_
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣࢊ").format(str(e)))
        return {}
def bstack11lll1lll_opy_(bstack1l1l11l1ll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࢋ")] or not CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧࢌ")]:
            raise ValueError(bstack111l1l_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢࢍ"))
        url = bstack1ll1l11l1_opy_ + bstack1l1l11l1ll_opy_
        auth = (CONFIG[bstack111l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࢎ")], CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ࢏")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l11l1ll1l_opy_ = json.loads(response.text)
            return bstack1l11l1ll1l_opy_
    except ValueError as ve:
        logger.error(bstack111l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ࢐").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ࢑").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1lll111l11_opy_(bstack1l1l1111_opy_):
    global CONFIG
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ࢒") not in CONFIG or str(CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ࢓")]).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࢔"):
        CONFIG[bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ࢕")] = False
    elif bstack111l1l_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ࢖") in bstack1l1l1111_opy_:
        bstack1lll1l1ll1_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢗ"), {})
        logger.debug(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ࢘"), bstack1lll1l1ll1_opy_)
        bstack1lll11111_opy_ = bstack1l1l1111_opy_.get(bstack111l1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷ࢙ࠧ"), [])
        bstack1ll1l11l1l_opy_ = bstack111l1l_opy_ (u"ࠦ࠱ࠨ࢚").join(bstack1lll11111_opy_)
        logger.debug(bstack111l1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵ࢛ࠥ"), bstack1ll1l11l1l_opy_)
        bstack1ll111111_opy_ = {
            bstack111l1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ࢜"): bstack111l1l_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨ࢝"),
            bstack111l1l_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧ࢞"): bstack111l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࢟"),
            bstack111l1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧࢠ"): bstack1ll1l11l1l_opy_
        }
        bstack1lll1l1ll1_opy_.update(bstack1ll111111_opy_)
        logger.debug(bstack111l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣࢡ"), bstack1lll1l1ll1_opy_)
        CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢢ")] = bstack1lll1l1ll1_opy_
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣࢣ"), CONFIG)
def bstack1111ll1ll_opy_():
    bstack11lll1ll_opy_ = bstack11111ll1l_opy_()
    if not bstack11lll1ll_opy_[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧࢤ")]:
      raise ValueError(bstack111l1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥࢥ"))
    return bstack11lll1ll_opy_[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩࢦ")] + bstack111l1l_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪࢧ")
def bstack11ll11lll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࢨ")], CONFIG[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࢩ")])
        url = bstack11llll111l_opy_
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥࢪ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack111l1l_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨࢫ"): bstack111l1l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦࢬ")})
            if response.status_code == 200:
                bstack1ll111lll1_opy_ = json.loads(response.text)
                bstack1l11l1l111_opy_ = bstack1ll111lll1_opy_.get(bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩࢭ"), [])
                if bstack1l11l1l111_opy_:
                    bstack11lll1ll1l_opy_ = bstack1l11l1l111_opy_[0]
                    bstack1l1l1l1111_opy_ = bstack11lll1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ࢮ"))
                    bstack1l11ll1ll_opy_ = bstack111ll111_opy_ + bstack1l1l1l1111_opy_
                    result.extend([bstack1l1l1l1111_opy_, bstack1l11ll1ll_opy_])
                    logger.info(bstack1l1l1l1l_opy_.format(bstack1l11ll1ll_opy_))
                    bstack1l1l111lll_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧࢯ")]
                    if bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢰ") in CONFIG:
                      bstack1l1l111lll_opy_ += bstack111l1l_opy_ (u"࠭ࠠࠨࢱ") + CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࢲ")]
                    if bstack1l1l111lll_opy_ != bstack11lll1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ࢳ")):
                      logger.debug(bstack1l11llll1l_opy_.format(bstack11lll1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧࢴ")), bstack1l1l111lll_opy_))
                    return result
                else:
                    logger.debug(bstack111l1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢࢵ"))
            else:
                logger.debug(bstack111l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢶ"))
        except Exception as e:
            logger.error(bstack111l1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧࢷ").format(str(e)))
    else:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢸ"))
    return [None, None]
import bstack_utils.bstack111llll1_opy_ as bstack1ll11l11_opy_
import bstack_utils.bstack1l1l1l1l1l_opy_ as bstack1l11lll111_opy_
bstack1l111lll11_opy_ = bstack111l1l_opy_ (u"ࠧࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠠࠡ࡫ࡩࠬࡵࡧࡧࡦࠢࡀࡁࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠠࡼ࡞ࡱࠤࠥࠦࡴࡳࡻࡾࡠࡳࠦࡣࡰࡰࡶࡸࠥ࡬ࡳࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࡡ࠭ࡦࡴ࡞ࠪ࠭ࡀࡢ࡮ࠡࠢࠣࠤࠥ࡬ࡳ࠯ࡣࡳࡴࡪࡴࡤࡇ࡫࡯ࡩࡘࡿ࡮ࡤࠪࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠬࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡳࡣ࡮ࡴࡤࡦࡺࠬࠤ࠰ࠦࠢ࠻ࠤࠣ࠯ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࠬࡦࡽࡡࡪࡶࠣࡲࡪࡽࡐࡢࡩࡨ࠶࠳࡫ࡶࡢ࡮ࡸࡥࡹ࡫ࠨࠣࠪࠬࠤࡂࡄࠠࡼࡿࠥ࠰ࠥࡢࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡨࡧࡷࡗࡪࡹࡳࡪࡱࡱࡈࡪࡺࡡࡪ࡮ࡶࠦࢂࡢࠧࠪࠫࠬ࡟ࠧ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠣ࡟ࠬࠤ࠰ࠦࠢ࠭࡞࡟ࡲࠧ࠯࡜࡯ࠢࠣࠤࠥࢃࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡽ࡝ࡰࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠧࢹ")
bstack11lll111_opy_ = bstack111l1l_opy_ (u"ࠨ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠࡠࡳࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬࡠࡳࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࡢ࡮ࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻ࡝ࡰ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࡡࡴࡴࡳࡻࠣࡿࡡࡴࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࡞ࡱࠤࠥࢃࠠࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࠣࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽ࡟ࡲࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࡠࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠦࡾࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪࡿࡣ࠰ࡡࡴࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࡢ࡮ࠡࠢࢀ࠭ࡡࡴࡽ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠧࢺ")
from ._version import __version__
bstack1l111l1ll_opy_ = None
CONFIG = {}
bstack11l11l111_opy_ = {}
bstack1llll1l111_opy_ = {}
bstack1lll111lll_opy_ = None
bstack1lll11l11l_opy_ = None
bstack111llll1l_opy_ = None
bstack1l1l1llll1_opy_ = -1
bstack11llll1111_opy_ = 0
bstack111ll1l1l_opy_ = bstack1l11ll1l1_opy_
bstack111l11l1l_opy_ = 1
bstack1lll11l1_opy_ = False
bstack11l111l1l_opy_ = False
bstack1l1111llll_opy_ = bstack111l1l_opy_ (u"ࠩࠪࢻ")
bstack1l1ll1l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࠫࢼ")
bstack1l111l11l_opy_ = False
bstack1l1l1ll11_opy_ = True
bstack1ll1l1l111_opy_ = bstack111l1l_opy_ (u"ࠫࠬࢽ")
bstack11ll11l1_opy_ = []
bstack1l1ll11l11_opy_ = bstack111l1l_opy_ (u"ࠬ࠭ࢾ")
bstack1lll1l1l11_opy_ = False
bstack1l1l1l111_opy_ = None
bstack111l11111_opy_ = None
bstack1l1ll111l_opy_ = None
bstack1l1l1l11ll_opy_ = -1
bstack1l11ll11l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨࢿ")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧࣀ"), bstack111l1l_opy_ (u"ࠨ࠰ࡵࡳࡧࡵࡴ࠮ࡴࡨࡴࡴࡸࡴ࠮ࡪࡨࡰࡵ࡫ࡲ࠯࡬ࡶࡳࡳ࠭ࣁ"))
bstack111l111l1_opy_ = 0
bstack1ll1111ll_opy_ = 0
bstack1l1ll1l1l_opy_ = []
bstack11l1111l_opy_ = []
bstack111111lll_opy_ = []
bstack1lllll111_opy_ = []
bstack1lll1lll1l_opy_ = bstack111l1l_opy_ (u"ࠩࠪࣂ")
bstack1lllll1ll1_opy_ = bstack111l1l_opy_ (u"ࠪࠫࣃ")
bstack1l1111ll11_opy_ = False
bstack1ll1111lll_opy_ = False
bstack1ll1l11lll_opy_ = {}
bstack1lll1llll_opy_ = None
bstack1ll11l1111_opy_ = None
bstack1l1ll1llll_opy_ = None
bstack1lll1l1l1l_opy_ = None
bstack11l11l1l1_opy_ = None
bstack11ll1ll11_opy_ = None
bstack1l1llllll_opy_ = None
bstack1lll1l1ll_opy_ = None
bstack1ll1ll11l_opy_ = None
bstack11llll1l11_opy_ = None
bstack1ll1lll1l_opy_ = None
bstack1lllll1l1l_opy_ = None
bstack1l1ll11ll1_opy_ = None
bstack1ll11l1l_opy_ = None
bstack1ll1l1ll11_opy_ = None
bstack11l1ll1ll_opy_ = None
bstack1l1l1lll11_opy_ = None
bstack11ll11ll_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1l111l11_opy_ = None
bstack111l1l1ll_opy_ = None
bstack111ll1l1_opy_ = None
bstack11l1lllll_opy_ = False
bstack1lllllll11_opy_ = bstack111l1l_opy_ (u"ࠦࠧࣄ")
logger = bstack1llll11lll_opy_.get_logger(__name__, bstack111ll1l1l_opy_)
bstack1l1ll111_opy_ = Config.bstack1lll11ll11_opy_()
percy = bstack1l1l1l1ll1_opy_()
bstack1ll11ll1ll_opy_ = bstack1l11ll1l11_opy_()
bstack1l1lllll_opy_ = bstack1l11l11ll_opy_()
def bstack1l111l111_opy_():
  global CONFIG
  global bstack1l1111ll11_opy_
  global bstack1l1ll111_opy_
  bstack1l11lll1ll_opy_ = bstack1ll1llll_opy_(CONFIG)
  if bstack1lll1ll1_opy_(CONFIG):
    if (bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࣅ") in bstack1l11lll1ll_opy_ and str(bstack1l11lll1ll_opy_[bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࣆ")]).lower() == bstack111l1l_opy_ (u"ࠧࡵࡴࡸࡩࠬࣇ")):
      bstack1l1111ll11_opy_ = True
    bstack1l1ll111_opy_.bstack11lll11l1_opy_(bstack1l11lll1ll_opy_.get(bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬࣈ"), False))
  else:
    bstack1l1111ll11_opy_ = True
    bstack1l1ll111_opy_.bstack11lll11l1_opy_(True)
def bstack11ll1l11_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1111ll1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1llll11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111l1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡦࡳࡳ࡬ࡩࡨࡨ࡬ࡰࡪࠨࣉ") == args[i].lower() or bstack111l1l_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡧ࡫ࡪࠦ࣊") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll1l1l111_opy_
      bstack1ll1l1l111_opy_ += bstack111l1l_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠡࠩ࣋") + path
      return path
  return None
bstack1l1111l11l_opy_ = re.compile(bstack111l1l_opy_ (u"ࡷࠨ࠮ࠫࡁ࡟ࠨࢀ࠮࠮ࠫࡁࠬࢁ࠳࠰࠿ࠣ࣌"))
def bstack11lll1lll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1111l11l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111l1l_opy_ (u"ࠨࠤࡼࠤ࣍") + group + bstack111l1l_opy_ (u"ࠢࡾࠤ࣎"), os.environ.get(group))
  return value
def bstack1l1l111111_opy_():
  bstack1l111ll1_opy_ = bstack1l1llll11_opy_()
  if bstack1l111ll1_opy_ and os.path.exists(os.path.abspath(bstack1l111ll1_opy_)):
    fileName = bstack1l111ll1_opy_
  if bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉ࣏ࠬ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࣐࠭")])) and not bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩ࣑ࠬ") in locals():
    fileName = os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ࣒")]
  if bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫࣓ࠧ") in locals():
    bstack1lll_opy_ = os.path.abspath(fileName)
  else:
    bstack1lll_opy_ = bstack111l1l_opy_ (u"࠭ࠧࣔ")
  bstack1lll11111l_opy_ = os.getcwd()
  bstack111111ll1_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪࣕ")
  bstack111lllll_opy_ = bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬࣖ")
  while (not os.path.exists(bstack1lll_opy_)) and bstack1lll11111l_opy_ != bstack111l1l_opy_ (u"ࠤࠥࣗ"):
    bstack1lll_opy_ = os.path.join(bstack1lll11111l_opy_, bstack111111ll1_opy_)
    if not os.path.exists(bstack1lll_opy_):
      bstack1lll_opy_ = os.path.join(bstack1lll11111l_opy_, bstack111lllll_opy_)
    if bstack1lll11111l_opy_ != os.path.dirname(bstack1lll11111l_opy_):
      bstack1lll11111l_opy_ = os.path.dirname(bstack1lll11111l_opy_)
    else:
      bstack1lll11111l_opy_ = bstack111l1l_opy_ (u"ࠥࠦࣘ")
  if not os.path.exists(bstack1lll_opy_):
    bstack111lll1l_opy_(
      bstack1l1l111l1_opy_.format(os.getcwd()))
  try:
    with open(bstack1lll_opy_, bstack111l1l_opy_ (u"ࠫࡷ࠭ࣙ")) as stream:
      yaml.add_implicit_resolver(bstack111l1l_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࣚ"), bstack1l1111l11l_opy_)
      yaml.add_constructor(bstack111l1l_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢࣛ"), bstack11lll1lll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1lll_opy_, bstack111l1l_opy_ (u"ࠧࡳࠩࣜ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack111lll1l_opy_(bstack111ll1lll_opy_.format(str(exc)))
def bstack1ll1ll1ll_opy_(config):
  bstack11lll1ll11_opy_ = bstack1111l11ll_opy_(config)
  for option in list(bstack11lll1ll11_opy_):
    if option.lower() in bstack11ll1lll_opy_ and option != bstack11ll1lll_opy_[option.lower()]:
      bstack11lll1ll11_opy_[bstack11ll1lll_opy_[option.lower()]] = bstack11lll1ll11_opy_[option]
      del bstack11lll1ll11_opy_[option]
  return config
def bstack1lll111l1l_opy_():
  global bstack1llll1l111_opy_
  for key, bstack1lll11llll_opy_ in bstack1lll1lll_opy_.items():
    if isinstance(bstack1lll11llll_opy_, list):
      for var in bstack1lll11llll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1llll1l111_opy_[key] = os.environ[var]
          break
    elif bstack1lll11llll_opy_ in os.environ and os.environ[bstack1lll11llll_opy_] and str(os.environ[bstack1lll11llll_opy_]).strip():
      bstack1llll1l111_opy_[key] = os.environ[bstack1lll11llll_opy_]
  if bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪࣝ") in os.environ:
    bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࣞ")] = {}
    bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣟ")][bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")] = os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ࣡")]
def bstack1lllll11l_opy_():
  global bstack11l11l111_opy_
  global bstack1ll1l1l111_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack111l1l_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣢").lower() == val.lower():
      bstack11l11l111_opy_[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࣣࠫ")] = {}
      bstack11l11l111_opy_[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣤ")][bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣥ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1l1l1111ll_opy_ in bstack111l1lll1_opy_.items():
    if isinstance(bstack1l1l1111ll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1l1l1111ll_opy_:
          if idx < len(sys.argv) and bstack111l1l_opy_ (u"ࠪ࠱࠲ࣦ࠭") + var.lower() == val.lower() and not key in bstack11l11l111_opy_:
            bstack11l11l111_opy_[key] = sys.argv[idx + 1]
            bstack1ll1l1l111_opy_ += bstack111l1l_opy_ (u"ࠫࠥ࠳࠭ࠨࣧ") + var + bstack111l1l_opy_ (u"ࠬࠦࠧࣨ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack111l1l_opy_ (u"࠭࠭࠮ࣩࠩ") + bstack1l1l1111ll_opy_.lower() == val.lower() and not key in bstack11l11l111_opy_:
          bstack11l11l111_opy_[key] = sys.argv[idx + 1]
          bstack1ll1l1l111_opy_ += bstack111l1l_opy_ (u"ࠧࠡ࠯࠰ࠫ࣪") + bstack1l1l1111ll_opy_ + bstack111l1l_opy_ (u"ࠨࠢࠪ࣫") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack111l111ll_opy_(config):
  bstack11ll1llll_opy_ = config.keys()
  for bstack1ll1lllll_opy_, bstack1l11111lll_opy_ in bstack1ll1l1l11_opy_.items():
    if bstack1l11111lll_opy_ in bstack11ll1llll_opy_:
      config[bstack1ll1lllll_opy_] = config[bstack1l11111lll_opy_]
      del config[bstack1l11111lll_opy_]
  for bstack1ll1lllll_opy_, bstack1l11111lll_opy_ in bstack1llll11111_opy_.items():
    if isinstance(bstack1l11111lll_opy_, list):
      for bstack11l111lll_opy_ in bstack1l11111lll_opy_:
        if bstack11l111lll_opy_ in bstack11ll1llll_opy_:
          config[bstack1ll1lllll_opy_] = config[bstack11l111lll_opy_]
          del config[bstack11l111lll_opy_]
          break
    elif bstack1l11111lll_opy_ in bstack11ll1llll_opy_:
      config[bstack1ll1lllll_opy_] = config[bstack1l11111lll_opy_]
      del config[bstack1l11111lll_opy_]
  for bstack11l111lll_opy_ in list(config):
    for bstack1l11llll_opy_ in bstack11lll111ll_opy_:
      if bstack11l111lll_opy_.lower() == bstack1l11llll_opy_.lower() and bstack11l111lll_opy_ != bstack1l11llll_opy_:
        config[bstack1l11llll_opy_] = config[bstack11l111lll_opy_]
        del config[bstack11l111lll_opy_]
  bstack1llllll1ll_opy_ = [{}]
  if not config.get(bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࣬")):
    config[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࣭࠭")] = [{}]
  bstack1llllll1ll_opy_ = config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹ࣮ࠧ")]
  for platform in bstack1llllll1ll_opy_:
    for bstack11l111lll_opy_ in list(platform):
      for bstack1l11llll_opy_ in bstack11lll111ll_opy_:
        if bstack11l111lll_opy_.lower() == bstack1l11llll_opy_.lower() and bstack11l111lll_opy_ != bstack1l11llll_opy_:
          platform[bstack1l11llll_opy_] = platform[bstack11l111lll_opy_]
          del platform[bstack11l111lll_opy_]
  for bstack1ll1lllll_opy_, bstack1l11111lll_opy_ in bstack1llll11111_opy_.items():
    for platform in bstack1llllll1ll_opy_:
      if isinstance(bstack1l11111lll_opy_, list):
        for bstack11l111lll_opy_ in bstack1l11111lll_opy_:
          if bstack11l111lll_opy_ in platform:
            platform[bstack1ll1lllll_opy_] = platform[bstack11l111lll_opy_]
            del platform[bstack11l111lll_opy_]
            break
      elif bstack1l11111lll_opy_ in platform:
        platform[bstack1ll1lllll_opy_] = platform[bstack1l11111lll_opy_]
        del platform[bstack1l11111lll_opy_]
  for bstack1l1ll1111l_opy_ in bstack1lllll111l_opy_:
    if bstack1l1ll1111l_opy_ in config:
      if not bstack1lllll111l_opy_[bstack1l1ll1111l_opy_] in config:
        config[bstack1lllll111l_opy_[bstack1l1ll1111l_opy_]] = {}
      config[bstack1lllll111l_opy_[bstack1l1ll1111l_opy_]].update(config[bstack1l1ll1111l_opy_])
      del config[bstack1l1ll1111l_opy_]
  for platform in bstack1llllll1ll_opy_:
    for bstack1l1ll1111l_opy_ in bstack1lllll111l_opy_:
      if bstack1l1ll1111l_opy_ in list(platform):
        if not bstack1lllll111l_opy_[bstack1l1ll1111l_opy_] in platform:
          platform[bstack1lllll111l_opy_[bstack1l1ll1111l_opy_]] = {}
        platform[bstack1lllll111l_opy_[bstack1l1ll1111l_opy_]].update(platform[bstack1l1ll1111l_opy_])
        del platform[bstack1l1ll1111l_opy_]
  config = bstack1ll1ll1ll_opy_(config)
  return config
def bstack1l1l11lll_opy_(config):
  global bstack1l1ll1l1l1_opy_
  bstack11ll1111l_opy_ = False
  if bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦ࣯ࠩ") in config and str(config[bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࣰࠪ")]).lower() != bstack111l1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪࣱ࠭"):
    if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࣲࠬ") not in config or str(config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ࣳ")]).lower() == bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩࣴ"):
      config[bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪࣵ")] = False
    else:
      bstack11lll1ll_opy_ = bstack11111ll1l_opy_()
      if bstack111l1l_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࣶࠪ") in bstack11lll1ll_opy_:
        if not bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࣷ") in config:
          config[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࣸ")] = {}
        config[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࣹࠬ")][bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࣺࠫ")] = bstack111l1l_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩࣻ")
        bstack11ll1111l_opy_ = True
        bstack1l1ll1l1l1_opy_ = config[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࣼ")].get(bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣽ"))
  if bstack1lll1ll1_opy_(config) and bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪࣾ") in config and str(config[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫࣿ")]).lower() != bstack111l1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧऀ") and not bstack11ll1111l_opy_:
    if not bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ँ") in config:
      config[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧं")] = {}
    if not config[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨः")].get(bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩऄ")) and not bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨअ") in config[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫआ")]:
      bstack1l1ll11l_opy_ = datetime.datetime.now()
      bstack1ll1111l1l_opy_ = bstack1l1ll11l_opy_.strftime(bstack111l1l_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬइ"))
      hostname = socket.gethostname()
      bstack1ll1lll1l1_opy_ = bstack111l1l_opy_ (u"ࠩࠪई").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111l1l_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬउ").format(bstack1ll1111l1l_opy_, hostname, bstack1ll1lll1l1_opy_)
      config[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऊ")][bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऋ")] = identifier
    bstack1l1ll1l1l1_opy_ = config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪऌ")].get(bstack111l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩऍ"))
  return config
def bstack1ll111l1l1_opy_():
  bstack1lllll1l1_opy_ =  bstack1ll1llll1_opy_()[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧऎ")]
  return bstack1lllll1l1_opy_ if bstack1lllll1l1_opy_ else -1
def bstack11l11l11l_opy_(bstack1lllll1l1_opy_):
  global CONFIG
  if not bstack111l1l_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫए") in CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬऐ")]:
    return
  CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ऑ")] = CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऒ")].replace(
    bstack111l1l_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨओ"),
    str(bstack1lllll1l1_opy_)
  )
def bstack1l111l1l1l_opy_():
  global CONFIG
  if not bstack111l1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭औ") in CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪक")]:
    return
  bstack1l1ll11l_opy_ = datetime.datetime.now()
  bstack1ll1111l1l_opy_ = bstack1l1ll11l_opy_.strftime(bstack111l1l_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧख"))
  CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬग")] = CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭घ")].replace(
    bstack111l1l_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫङ"),
    bstack1ll1111l1l_opy_
  )
def bstack111l11l1_opy_():
  global CONFIG
  if bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨच") in CONFIG and not bool(CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩछ")]):
    del CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪज")]
    return
  if not bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫझ") in CONFIG:
    CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬञ")] = bstack111l1l_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧट")
  if bstack111l1l_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫठ") in CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨड")]:
    bstack1l111l1l1l_opy_()
    os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫढ")] = CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪण")]
  if not bstack111l1l_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫत") in CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬथ")]:
    return
  bstack1lllll1l1_opy_ = bstack111l1l_opy_ (u"ࠫࠬद")
  bstack1l1l1l11l1_opy_ = bstack1ll111l1l1_opy_()
  if bstack1l1l1l11l1_opy_ != -1:
    bstack1lllll1l1_opy_ = bstack111l1l_opy_ (u"ࠬࡉࡉࠡࠩध") + str(bstack1l1l1l11l1_opy_)
  if bstack1lllll1l1_opy_ == bstack111l1l_opy_ (u"࠭ࠧन"):
    bstack1lll1lll1_opy_ = bstack1l11l11ll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪऩ")])
    if bstack1lll1lll1_opy_ != -1:
      bstack1lllll1l1_opy_ = str(bstack1lll1lll1_opy_)
  if bstack1lllll1l1_opy_:
    bstack11l11l11l_opy_(bstack1lllll1l1_opy_)
    os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬप")] = CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫफ")]
def bstack1l1ll1l11_opy_(bstack1l1l111ll_opy_, bstack1lllllll1_opy_, path):
  bstack11l11ll1_opy_ = {
    bstack111l1l_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧब"): bstack1lllllll1_opy_
  }
  if os.path.exists(path):
    bstack111lll11_opy_ = json.load(open(path, bstack111l1l_opy_ (u"ࠫࡷࡨࠧभ")))
  else:
    bstack111lll11_opy_ = {}
  bstack111lll11_opy_[bstack1l1l111ll_opy_] = bstack11l11ll1_opy_
  with open(path, bstack111l1l_opy_ (u"ࠧࡽࠫࠣम")) as outfile:
    json.dump(bstack111lll11_opy_, outfile)
def bstack1l11l11ll1_opy_(bstack1l1l111ll_opy_):
  bstack1l1l111ll_opy_ = str(bstack1l1l111ll_opy_)
  bstack111l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨय")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧर"))
  try:
    if not os.path.exists(bstack111l1l1l1_opy_):
      os.makedirs(bstack111l1l1l1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠨࢀࠪऱ")), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩल"), bstack111l1l_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬळ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111l1l_opy_ (u"ࠫࡼ࠭ऴ")):
        pass
      with open(file_path, bstack111l1l_opy_ (u"ࠧࡽࠫࠣव")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111l1l_opy_ (u"࠭ࡲࠨश")) as bstack1llll11l1l_opy_:
      bstack1l1l11ll1l_opy_ = json.load(bstack1llll11l1l_opy_)
    if bstack1l1l111ll_opy_ in bstack1l1l11ll1l_opy_:
      bstack11lll111l_opy_ = bstack1l1l11ll1l_opy_[bstack1l1l111ll_opy_][bstack111l1l_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫष")]
      bstack1l11l1ll_opy_ = int(bstack11lll111l_opy_) + 1
      bstack1l1ll1l11_opy_(bstack1l1l111ll_opy_, bstack1l11l1ll_opy_, file_path)
      return bstack1l11l1ll_opy_
    else:
      bstack1l1ll1l11_opy_(bstack1l1l111ll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1111l1_opy_.format(str(e)))
    return -1
def bstack11l1l1l11_opy_(config):
  if not config[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪस")] or not config[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬह")]:
    return True
  else:
    return False
def bstack1l1111lll_opy_(config, index=0):
  global bstack1l111l11l_opy_
  bstack111lll11l_opy_ = {}
  caps = bstack1l1l1lll1_opy_ + bstack1llll11ll1_opy_
  if bstack1l111l11l_opy_:
    caps += bstack1ll11111l_opy_
  for key in config:
    if key in caps + [bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ऺ")]:
      continue
    bstack111lll11l_opy_[key] = config[key]
  if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऻ") in config:
    for bstack1l111ll11_opy_ in config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ़")][index]:
      if bstack1l111ll11_opy_ in caps:
        continue
      bstack111lll11l_opy_[bstack1l111ll11_opy_] = config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩऽ")][index][bstack1l111ll11_opy_]
  bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦࠩा")] = socket.gethostname()
  if bstack111l1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩि") in bstack111lll11l_opy_:
    del (bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪी")])
  return bstack111lll11l_opy_
def bstack111lll1ll_opy_(config):
  global bstack1l111l11l_opy_
  bstack11l1l11l_opy_ = {}
  caps = bstack1llll11ll1_opy_
  if bstack1l111l11l_opy_:
    caps += bstack1ll11111l_opy_
  for key in caps:
    if key in config:
      bstack11l1l11l_opy_[key] = config[key]
  return bstack11l1l11l_opy_
def bstack111l1111l_opy_(bstack111lll11l_opy_, bstack11l1l11l_opy_):
  bstack111ll111l_opy_ = {}
  for key in bstack111lll11l_opy_.keys():
    if key in bstack1ll1l1l11_opy_:
      bstack111ll111l_opy_[bstack1ll1l1l11_opy_[key]] = bstack111lll11l_opy_[key]
    else:
      bstack111ll111l_opy_[key] = bstack111lll11l_opy_[key]
  for key in bstack11l1l11l_opy_:
    if key in bstack1ll1l1l11_opy_:
      bstack111ll111l_opy_[bstack1ll1l1l11_opy_[key]] = bstack11l1l11l_opy_[key]
    else:
      bstack111ll111l_opy_[key] = bstack11l1l11l_opy_[key]
  return bstack111ll111l_opy_
def bstack11l1ll1l1_opy_(config, index=0):
  global bstack1l111l11l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l111lllll_opy_ = bstack11ll11ll1_opy_(bstack111l11lll_opy_, config, logger)
  bstack11l1l11l_opy_ = bstack111lll1ll_opy_(config)
  bstack1l111ll1ll_opy_ = bstack1llll11ll1_opy_
  bstack1l111ll1ll_opy_ += bstack111lll1l1_opy_
  bstack11l1l11l_opy_ = update(bstack11l1l11l_opy_, bstack1l111lllll_opy_)
  if bstack1l111l11l_opy_:
    bstack1l111ll1ll_opy_ += bstack1ll11111l_opy_
  if bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ु") in config:
    if bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩू") in config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨृ")][index]:
      caps[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫॄ")] = config[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪॅ")][index][bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ॆ")]
    if bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪे") in config[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ै")][index]:
      caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬॉ")] = str(config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨॊ")][index][bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧो")])
    bstack1l1lll1l11_opy_ = bstack11ll11ll1_opy_(bstack111l11lll_opy_, config[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪौ")][index], logger)
    bstack1l111ll1ll_opy_ += list(bstack1l1lll1l11_opy_.keys())
    for bstack11l1l1l1_opy_ in bstack1l111ll1ll_opy_:
      if bstack11l1l1l1_opy_ in config[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ्ࠫ")][index]:
        if bstack11l1l1l1_opy_ == bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫॎ"):
          try:
            bstack1l1lll1l11_opy_[bstack11l1l1l1_opy_] = str(config[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ॏ")][index][bstack11l1l1l1_opy_] * 1.0)
          except:
            bstack1l1lll1l11_opy_[bstack11l1l1l1_opy_] = str(config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॐ")][index][bstack11l1l1l1_opy_])
        else:
          bstack1l1lll1l11_opy_[bstack11l1l1l1_opy_] = config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ॑")][index][bstack11l1l1l1_opy_]
        del (config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ॒ࠩ")][index][bstack11l1l1l1_opy_])
    bstack11l1l11l_opy_ = update(bstack11l1l11l_opy_, bstack1l1lll1l11_opy_)
  bstack111lll11l_opy_ = bstack1l1111lll_opy_(config, index)
  for bstack11l111lll_opy_ in bstack1llll11ll1_opy_ + list(bstack1l111lllll_opy_.keys()):
    if bstack11l111lll_opy_ in bstack111lll11l_opy_:
      bstack11l1l11l_opy_[bstack11l111lll_opy_] = bstack111lll11l_opy_[bstack11l111lll_opy_]
      del (bstack111lll11l_opy_[bstack11l111lll_opy_])
  if bstack11l11111l_opy_(config):
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ॓")] = True
    caps.update(bstack11l1l11l_opy_)
    caps[bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ॔")] = bstack111lll11l_opy_
  else:
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩॕ")] = False
    caps.update(bstack111l1111l_opy_(bstack111lll11l_opy_, bstack11l1l11l_opy_))
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨॖ") in caps:
      caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬॗ")] = caps[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪक़")]
      del (caps[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫख़")])
    if bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨग़") in caps:
      caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪज़")] = caps[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪड़")]
      del (caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫढ़")])
  return caps
def bstack1l1l11111_opy_():
  global bstack1l1ll11l11_opy_
  global CONFIG
  if bstack1111ll1l_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫफ़")):
    if bstack1l1ll11l11_opy_ != bstack111l1l_opy_ (u"ࠬ࠭य़"):
      return bstack111l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢॠ") + bstack1l1ll11l11_opy_ + bstack111l1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦॡ")
    return bstack1ll11l1l1l_opy_
  if bstack1l1ll11l11_opy_ != bstack111l1l_opy_ (u"ࠨࠩॢ"):
    return bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦॣ") + bstack1l1ll11l11_opy_ + bstack111l1l_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦ।")
  return bstack1llllll11_opy_
def bstack1l11ll111_opy_(options):
  return hasattr(options, bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬ॥"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l1l1ll1l1_opy_(options, bstack1llllllll_opy_):
  for bstack1111l11l_opy_ in bstack1llllllll_opy_:
    if bstack1111l11l_opy_ in [bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ०"), bstack111l1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ१")]:
      continue
    if bstack1111l11l_opy_ in options._experimental_options:
      options._experimental_options[bstack1111l11l_opy_] = update(options._experimental_options[bstack1111l11l_opy_],
                                                         bstack1llllllll_opy_[bstack1111l11l_opy_])
    else:
      options.add_experimental_option(bstack1111l11l_opy_, bstack1llllllll_opy_[bstack1111l11l_opy_])
  if bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ२") in bstack1llllllll_opy_:
    for arg in bstack1llllllll_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭३")]:
      options.add_argument(arg)
    del (bstack1llllllll_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ४")])
  if bstack111l1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ५") in bstack1llllllll_opy_:
    for ext in bstack1llllllll_opy_[bstack111l1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ६")]:
      options.add_extension(ext)
    del (bstack1llllllll_opy_[bstack111l1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ७")])
def bstack1lll111l_opy_(options, bstack1ll1llllll_opy_):
  if bstack111l1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ८") in bstack1ll1llllll_opy_:
    for bstack111ll11ll_opy_ in bstack1ll1llllll_opy_[bstack111l1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭९")]:
      if bstack111ll11ll_opy_ in options._preferences:
        options._preferences[bstack111ll11ll_opy_] = update(options._preferences[bstack111ll11ll_opy_], bstack1ll1llllll_opy_[bstack111l1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ॰")][bstack111ll11ll_opy_])
      else:
        options.set_preference(bstack111ll11ll_opy_, bstack1ll1llllll_opy_[bstack111l1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨॱ")][bstack111ll11ll_opy_])
  if bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨॲ") in bstack1ll1llllll_opy_:
    for arg in bstack1ll1llllll_opy_[bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩॳ")]:
      options.add_argument(arg)
def bstack111llllll_opy_(options, bstack1llll111ll_opy_):
  if bstack111l1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭ॴ") in bstack1llll111ll_opy_:
    options.use_webview(bool(bstack1llll111ll_opy_[bstack111l1l_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧॵ")]))
  bstack1l1l1ll1l1_opy_(options, bstack1llll111ll_opy_)
def bstack11lll11ll1_opy_(options, bstack1ll11l11l1_opy_):
  for bstack1l11111ll_opy_ in bstack1ll11l11l1_opy_:
    if bstack1l11111ll_opy_ in [bstack111l1l_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫॶ"), bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ॷ")]:
      continue
    options.set_capability(bstack1l11111ll_opy_, bstack1ll11l11l1_opy_[bstack1l11111ll_opy_])
  if bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧॸ") in bstack1ll11l11l1_opy_:
    for arg in bstack1ll11l11l1_opy_[bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨॹ")]:
      options.add_argument(arg)
  if bstack111l1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨॺ") in bstack1ll11l11l1_opy_:
    options.bstack1l11ll11ll_opy_(bool(bstack1ll11l11l1_opy_[bstack111l1l_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩॻ")]))
def bstack111ll1111_opy_(options, bstack1l1111l111_opy_):
  for bstack1l11lll1l1_opy_ in bstack1l1111l111_opy_:
    if bstack1l11lll1l1_opy_ in [bstack111l1l_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪॼ"), bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬॽ")]:
      continue
    options._options[bstack1l11lll1l1_opy_] = bstack1l1111l111_opy_[bstack1l11lll1l1_opy_]
  if bstack111l1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॾ") in bstack1l1111l111_opy_:
    for bstack1l1l1l1lll_opy_ in bstack1l1111l111_opy_[bstack111l1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ॿ")]:
      options.bstack1ll1l1l1l1_opy_(
        bstack1l1l1l1lll_opy_, bstack1l1111l111_opy_[bstack111l1l_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧঀ")][bstack1l1l1l1lll_opy_])
  if bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩঁ") in bstack1l1111l111_opy_:
    for arg in bstack1l1111l111_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡵࠪং")]:
      options.add_argument(arg)
def bstack1lll1l1111_opy_(options, caps):
  if not hasattr(options, bstack111l1l_opy_ (u"࠭ࡋࡆ࡛ࠪঃ")):
    return
  if options.KEY == bstack111l1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ঄") and options.KEY in caps:
    bstack1l1l1ll1l1_opy_(options, caps[bstack111l1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭অ")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧআ") and options.KEY in caps:
    bstack1lll111l_opy_(options, caps[bstack111l1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨই")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬঈ") and options.KEY in caps:
    bstack11lll11ll1_opy_(options, caps[bstack111l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭উ")])
  elif options.KEY == bstack111l1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧঊ") and options.KEY in caps:
    bstack111llllll_opy_(options, caps[bstack111l1l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨঋ")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧঌ") and options.KEY in caps:
    bstack111ll1111_opy_(options, caps[bstack111l1l_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ঍")])
def bstack1l1lll11l1_opy_(caps):
  global bstack1l111l11l_opy_
  if isinstance(os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ঎")), str):
    bstack1l111l11l_opy_ = eval(os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬএ")))
  if bstack1l111l11l_opy_:
    if bstack11ll1l11_opy_() < version.parse(bstack111l1l_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫঐ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111l1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭঑")
    if bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ঒") in caps:
      browser = caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ও")]
    elif bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪঔ") in caps:
      browser = caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫক")]
    browser = str(browser).lower()
    if browser == bstack111l1l_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫখ") or browser == bstack111l1l_opy_ (u"ࠬ࡯ࡰࡢࡦࠪগ"):
      browser = bstack111l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ঘ")
    if browser == bstack111l1l_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨঙ"):
      browser = bstack111l1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨচ")
    if browser not in [bstack111l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩছ"), bstack111l1l_opy_ (u"ࠪࡩࡩ࡭ࡥࠨজ"), bstack111l1l_opy_ (u"ࠫ࡮࡫ࠧঝ"), bstack111l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬঞ"), bstack111l1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧট")]:
      return None
    try:
      package = bstack111l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঠ").format(browser)
      name = bstack111l1l_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩড")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l11ll111_opy_(options):
        return None
      for bstack11l111lll_opy_ in caps.keys():
        options.set_capability(bstack11l111lll_opy_, caps[bstack11l111lll_opy_])
      bstack1lll1l1111_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lllll11_opy_(options, bstack1l1111111l_opy_):
  if not bstack1l11ll111_opy_(options):
    return
  for bstack11l111lll_opy_ in bstack1l1111111l_opy_.keys():
    if bstack11l111lll_opy_ in bstack111lll1l1_opy_:
      continue
    if bstack11l111lll_opy_ in options._caps and type(options._caps[bstack11l111lll_opy_]) in [dict, list]:
      options._caps[bstack11l111lll_opy_] = update(options._caps[bstack11l111lll_opy_], bstack1l1111111l_opy_[bstack11l111lll_opy_])
    else:
      options.set_capability(bstack11l111lll_opy_, bstack1l1111111l_opy_[bstack11l111lll_opy_])
  bstack1lll1l1111_opy_(options, bstack1l1111111l_opy_)
  if bstack111l1l_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨঢ") in options._caps:
    if options._caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨণ")] and options._caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩত")].lower() != bstack111l1l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭থ"):
      del options._caps[bstack111l1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬদ")]
def bstack1l1lll11ll_opy_(proxy_config):
  if bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫধ") in proxy_config:
    proxy_config[bstack111l1l_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪন")] = proxy_config[bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭঩")]
    del (proxy_config[bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧপ")])
  if bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧফ") in proxy_config and proxy_config[bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨব")].lower() != bstack111l1l_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭ভ"):
    proxy_config[bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪম")] = bstack111l1l_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨয")
  if bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧর") in proxy_config:
    proxy_config[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭঱")] = bstack111l1l_opy_ (u"ࠫࡵࡧࡣࠨল")
  return proxy_config
def bstack11111lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ঳") in config:
    return proxy
  config[bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ঴")] = bstack1l1lll11ll_opy_(config[bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭঵")])
  if proxy == None:
    proxy = Proxy(config[bstack111l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧশ")])
  return proxy
def bstack11l1l1ll1_opy_(self):
  global CONFIG
  global bstack1lllll1l1l_opy_
  try:
    proxy = bstack11lll1l11l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111l1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧষ")):
        proxies = bstack1lll11l111_opy_(proxy, bstack1l1l11111_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll111l1ll_opy_ = proxies.popitem()
          if bstack111l1l_opy_ (u"ࠥ࠾࠴࠵ࠢস") in bstack1ll111l1ll_opy_:
            return bstack1ll111l1ll_opy_
          else:
            return bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧহ") + bstack1ll111l1ll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤ঺").format(str(e)))
  return bstack1lllll1l1l_opy_(self)
def bstack1ll11ll11l_opy_():
  global CONFIG
  return bstack11l1l1l1l_opy_(CONFIG) and bstack1ll11l111_opy_() and bstack1111ll1l_opy_() >= version.parse(bstack1111l111l_opy_)
def bstack11lll1l1l1_opy_():
  global CONFIG
  return (bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ঻") in CONFIG or bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼ়ࠫ") in CONFIG) and bstack1lll1ll111_opy_()
def bstack1111l11ll_opy_(config):
  bstack11lll1ll11_opy_ = {}
  if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬঽ") in config:
    bstack11lll1ll11_opy_ = config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭া")]
  if bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩি") in config:
    bstack11lll1ll11_opy_ = config[bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪী")]
  proxy = bstack11lll1l11l_opy_(config)
  if proxy:
    if proxy.endswith(bstack111l1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪু")) and os.path.isfile(proxy):
      bstack11lll1ll11_opy_[bstack111l1l_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩূ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111l1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬৃ")):
        proxies = bstack11l11ll1l_opy_(config, bstack1l1l11111_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll111l1ll_opy_ = proxies.popitem()
          if bstack111l1l_opy_ (u"ࠣ࠼࠲࠳ࠧৄ") in bstack1ll111l1ll_opy_:
            parsed_url = urlparse(bstack1ll111l1ll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111l1l_opy_ (u"ࠤ࠽࠳࠴ࠨ৅") + bstack1ll111l1ll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11lll1ll11_opy_[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭৆")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11lll1ll11_opy_[bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧে")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11lll1ll11_opy_[bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨৈ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11lll1ll11_opy_[bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩ৉")] = str(parsed_url.password)
  return bstack11lll1ll11_opy_
def bstack1ll1llll_opy_(config):
  if bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ৊") in config:
    return config[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ো")]
  return {}
def bstack1l11l1l11l_opy_(caps):
  global bstack1l1ll1l1l1_opy_
  if bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪৌ") in caps:
    caps[bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶ্ࠫ")][bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪৎ")] = True
    if bstack1l1ll1l1l1_opy_:
      caps[bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭৏")][bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ৐")] = bstack1l1ll1l1l1_opy_
  else:
    caps[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ৑")] = True
    if bstack1l1ll1l1l1_opy_:
      caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ৒")] = bstack1l1ll1l1l1_opy_
def bstack1l11l111_opy_():
  global CONFIG
  if not bstack1lll1ll1_opy_(CONFIG):
    return
  if bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭৓") in CONFIG and bstack11ll111l_opy_(CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ৔")]):
    if (
      bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ৕") in CONFIG
      and bstack11ll111l_opy_(CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ৖")].get(bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪৗ")))
    ):
      logger.debug(bstack111l1l_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ৘"))
      return
    bstack11lll1ll11_opy_ = bstack1111l11ll_opy_(CONFIG)
    bstack1llll1lll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ৙")], bstack11lll1ll11_opy_)
def bstack1llll1lll1_opy_(key, bstack11lll1ll11_opy_):
  global bstack1l111l1ll_opy_
  logger.info(bstack1ll11l1lll_opy_)
  try:
    bstack1l111l1ll_opy_ = Local()
    bstack1lll1l111l_opy_ = {bstack111l1l_opy_ (u"ࠩ࡮ࡩࡾ࠭৚"): key}
    bstack1lll1l111l_opy_.update(bstack11lll1ll11_opy_)
    logger.debug(bstack11111111_opy_.format(str(bstack1lll1l111l_opy_)))
    bstack1l111l1ll_opy_.start(**bstack1lll1l111l_opy_)
    if bstack1l111l1ll_opy_.isRunning():
      logger.info(bstack111l1ll1l_opy_)
  except Exception as e:
    bstack111lll1l_opy_(bstack11ll111l1_opy_.format(str(e)))
def bstack1l1l1l1l11_opy_():
  global bstack1l111l1ll_opy_
  if bstack1l111l1ll_opy_.isRunning():
    logger.info(bstack1ll1ll1l_opy_)
    bstack1l111l1ll_opy_.stop()
  bstack1l111l1ll_opy_ = None
def bstack1lll1111_opy_(bstack1l11ll1l_opy_=[]):
  global CONFIG
  bstack1ll1ll1ll1_opy_ = []
  bstack1l1l11l11l_opy_ = [bstack111l1l_opy_ (u"ࠪࡳࡸ࠭৛"), bstack111l1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧড়"), bstack111l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩঢ়"), bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ৞"), bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬয়"), bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩৠ")]
  try:
    for err in bstack1l11ll1l_opy_:
      bstack1111111l_opy_ = {}
      for k in bstack1l1l11l11l_opy_:
        val = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬৡ")][int(err[bstack111l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩৢ")])].get(k)
        if val:
          bstack1111111l_opy_[k] = val
      if(err[bstack111l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪৣ")] != bstack111l1l_opy_ (u"ࠬ࠭৤")):
        bstack1111111l_opy_[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬ৥")] = {
          err[bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ০")]: err[bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ১")]
        }
        bstack1ll1ll1ll1_opy_.append(bstack1111111l_opy_)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫ২") + str(e))
  finally:
    return bstack1ll1ll1ll1_opy_
def bstack11lll1111_opy_(file_name):
  bstack11ll1ll1_opy_ = []
  try:
    bstack1111llll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1111llll_opy_):
      with open(bstack1111llll_opy_) as f:
        bstack1l1l11l1l_opy_ = json.load(f)
        bstack11ll1ll1_opy_ = bstack1l1l11l1l_opy_
      os.remove(bstack1111llll_opy_)
    return bstack11ll1ll1_opy_
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬ৩") + str(e))
    return bstack11ll1ll1_opy_
def bstack11ll1l1l_opy_():
  global bstack1lllllll11_opy_
  global bstack11ll11l1_opy_
  global bstack1l1ll1l1l_opy_
  global bstack11l1111l_opy_
  global bstack111111lll_opy_
  global bstack1lllll1ll1_opy_
  global CONFIG
  bstack11111llll_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬ৪"))
  if bstack11111llll_opy_ in [bstack111l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ৫"), bstack111l1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ৬")]:
    bstack1ll1l1111_opy_()
  percy.shutdown()
  if bstack1lllllll11_opy_:
    logger.warning(bstack1ll1111l1_opy_.format(str(bstack1lllllll11_opy_)))
  else:
    try:
      bstack111lll11_opy_ = bstack11lllllll1_opy_(bstack111l1l_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭৭"), logger)
      if bstack111lll11_opy_.get(bstack111l1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭৮")) and bstack111lll11_opy_.get(bstack111l1l_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ৯")).get(bstack111l1l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬৰ")):
        logger.warning(bstack1ll1111l1_opy_.format(str(bstack111lll11_opy_[bstack111l1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩৱ")][bstack111l1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ৲")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1ll111llll_opy_)
  global bstack1l111l1ll_opy_
  if bstack1l111l1ll_opy_:
    bstack1l1l1l1l11_opy_()
  try:
    for driver in bstack11ll11l1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1l111l11_opy_)
  if bstack1lllll1ll1_opy_ == bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ৳"):
    bstack111111lll_opy_ = bstack11lll1111_opy_(bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ৴"))
  if bstack1lllll1ll1_opy_ == bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ৵") and len(bstack11l1111l_opy_) == 0:
    bstack11l1111l_opy_ = bstack11lll1111_opy_(bstack111l1l_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ৶"))
    if len(bstack11l1111l_opy_) == 0:
      bstack11l1111l_opy_ = bstack11lll1111_opy_(bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ৷"))
  bstack111l1ll11_opy_ = bstack111l1l_opy_ (u"ࠫࠬ৸")
  if len(bstack1l1ll1l1l_opy_) > 0:
    bstack111l1ll11_opy_ = bstack1lll1111_opy_(bstack1l1ll1l1l_opy_)
  elif len(bstack11l1111l_opy_) > 0:
    bstack111l1ll11_opy_ = bstack1lll1111_opy_(bstack11l1111l_opy_)
  elif len(bstack111111lll_opy_) > 0:
    bstack111l1ll11_opy_ = bstack1lll1111_opy_(bstack111111lll_opy_)
  elif len(bstack1lllll111_opy_) > 0:
    bstack111l1ll11_opy_ = bstack1lll1111_opy_(bstack1lllll111_opy_)
  if bool(bstack111l1ll11_opy_):
    bstack1l111l11ll_opy_(bstack111l1ll11_opy_)
  else:
    bstack1l111l11ll_opy_()
  bstack1l111ll111_opy_(bstack11ll1l11l_opy_, logger)
  bstack1llll11lll_opy_.bstack1lllllllll_opy_(CONFIG)
  if len(bstack111111lll_opy_) > 0:
    sys.exit(len(bstack111111lll_opy_))
def bstack11ll11111_opy_(bstack1ll1l1lll1_opy_, frame):
  global bstack1l1ll111_opy_
  logger.error(bstack1l11l11l11_opy_)
  bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ৹"), bstack1ll1l1lll1_opy_)
  if hasattr(signal, bstack111l1l_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧ৺")):
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ৻"), signal.Signals(bstack1ll1l1lll1_opy_).name)
  else:
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨৼ"), bstack111l1l_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭৽"))
  bstack11111llll_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ৾"))
  if bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ৿"):
    bstack1l1l1ll1l_opy_.stop(bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ਀")))
  bstack11ll1l1l_opy_()
  sys.exit(1)
def bstack111lll1l_opy_(err):
  logger.critical(bstack111ll1l11_opy_.format(str(err)))
  bstack1l111l11ll_opy_(bstack111ll1l11_opy_.format(str(err)), True)
  atexit.unregister(bstack11ll1l1l_opy_)
  bstack1ll1l1111_opy_()
  sys.exit(1)
def bstack11llll111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l111l11ll_opy_(message, True)
  atexit.unregister(bstack11ll1l1l_opy_)
  bstack1ll1l1111_opy_()
  sys.exit(1)
def bstack1llll1l1l1_opy_():
  global CONFIG
  global bstack11l11l111_opy_
  global bstack1llll1l111_opy_
  global bstack1l1l1ll11_opy_
  CONFIG = bstack1l1l111111_opy_()
  load_dotenv(CONFIG.get(bstack111l1l_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧਁ")))
  bstack1lll111l1l_opy_()
  bstack1lllll11l_opy_()
  CONFIG = bstack111l111ll_opy_(CONFIG)
  update(CONFIG, bstack1llll1l111_opy_)
  update(CONFIG, bstack11l11l111_opy_)
  CONFIG = bstack1l1l11lll_opy_(CONFIG)
  bstack1l1l1ll11_opy_ = bstack1lll1ll1_opy_(CONFIG)
  os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪਂ")] = bstack1l1l1ll11_opy_.__str__()
  bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩਃ"), bstack1l1l1ll11_opy_)
  if (bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ਄") in CONFIG and bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ਅ") in bstack11l11l111_opy_) or (
          bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧਆ") in CONFIG and bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨਇ") not in bstack1llll1l111_opy_):
    if os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪਈ")):
      CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਉ")] = os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬਊ"))
    else:
      bstack111l11l1_opy_()
  elif (bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ਋") not in CONFIG and bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ਌") in CONFIG) or (
          bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ਍") in bstack1llll1l111_opy_ and bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ਎") not in bstack11l11l111_opy_):
    del (CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨਏ")])
  if bstack11l1l1l11_opy_(CONFIG):
    bstack111lll1l_opy_(bstack1llll1l1l_opy_)
  bstack1l1ll11l1l_opy_()
  bstack1l11l11111_opy_()
  if bstack1l111l11l_opy_:
    CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡲࡳࠫਐ")] = bstack111l1lll_opy_(CONFIG)
    logger.info(bstack11ll1l111_opy_.format(CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡳࡴࠬ਑")]))
  if not bstack1l1l1ll11_opy_:
    CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ਒")] = [{}]
def bstack11lllllll_opy_(config, bstack1l11ll11_opy_):
  global CONFIG
  global bstack1l111l11l_opy_
  CONFIG = config
  bstack1l111l11l_opy_ = bstack1l11ll11_opy_
def bstack1l11l11111_opy_():
  global CONFIG
  global bstack1l111l11l_opy_
  if bstack111l1l_opy_ (u"ࠪࡥࡵࡶࠧਓ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11llll111_opy_(e, bstack1lll11lll_opy_)
    bstack1l111l11l_opy_ = True
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪਔ"), True)
def bstack111l1lll_opy_(config):
  bstack11lllll1l_opy_ = bstack111l1l_opy_ (u"ࠬ࠭ਕ")
  app = config[bstack111l1l_opy_ (u"࠭ࡡࡱࡲࠪਖ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1ll1l1lll_opy_:
      if os.path.exists(app):
        bstack11lllll1l_opy_ = bstack1l11l1l1l1_opy_(config, app)
      elif bstack1l1l1lllll_opy_(app):
        bstack11lllll1l_opy_ = app
      else:
        bstack111lll1l_opy_(bstack11llllll_opy_.format(app))
    else:
      if bstack1l1l1lllll_opy_(app):
        bstack11lllll1l_opy_ = app
      elif os.path.exists(app):
        bstack11lllll1l_opy_ = bstack1l11l1l1l1_opy_(app)
      else:
        bstack111lll1l_opy_(bstack1ll1lll11l_opy_)
  else:
    if len(app) > 2:
      bstack111lll1l_opy_(bstack1l1lll1ll1_opy_)
    elif len(app) == 2:
      if bstack111l1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬਗ") in app and bstack111l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫਘ") in app:
        if os.path.exists(app[bstack111l1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧਙ")]):
          bstack11lllll1l_opy_ = bstack1l11l1l1l1_opy_(config, app[bstack111l1l_opy_ (u"ࠪࡴࡦࡺࡨࠨਚ")], app[bstack111l1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧਛ")])
        else:
          bstack111lll1l_opy_(bstack11llllll_opy_.format(app))
      else:
        bstack111lll1l_opy_(bstack1l1lll1ll1_opy_)
    else:
      for key in app:
        if key in bstack1l11ll1111_opy_:
          if key == bstack111l1l_opy_ (u"ࠬࡶࡡࡵࡪࠪਜ"):
            if os.path.exists(app[key]):
              bstack11lllll1l_opy_ = bstack1l11l1l1l1_opy_(config, app[key])
            else:
              bstack111lll1l_opy_(bstack11llllll_opy_.format(app))
          else:
            bstack11lllll1l_opy_ = app[key]
        else:
          bstack111lll1l_opy_(bstack1l111lll_opy_)
  return bstack11lllll1l_opy_
def bstack1l1l1lllll_opy_(bstack11lllll1l_opy_):
  import re
  bstack11lll11ll_opy_ = re.compile(bstack111l1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨਝ"))
  bstack1llll11ll_opy_ = re.compile(bstack111l1l_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯࠵࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦਞ"))
  if bstack111l1l_opy_ (u"ࠨࡤࡶ࠾࠴࠵ࠧਟ") in bstack11lllll1l_opy_ or re.fullmatch(bstack11lll11ll_opy_, bstack11lllll1l_opy_) or re.fullmatch(bstack1llll11ll_opy_, bstack11lllll1l_opy_):
    return True
  else:
    return False
def bstack1l11l1l1l1_opy_(config, path, bstack11l1ll1l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111l1l_opy_ (u"ࠩࡵࡦࠬਠ")).read()).hexdigest()
  bstack1l1ll11ll_opy_ = bstack1111l11l1_opy_(md5_hash)
  bstack11lllll1l_opy_ = None
  if bstack1l1ll11ll_opy_:
    logger.info(bstack1ll111ll1l_opy_.format(bstack1l1ll11ll_opy_, md5_hash))
    return bstack1l1ll11ll_opy_
  bstack11lllll111_opy_ = MultipartEncoder(
    fields={
      bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࠨਡ"): (os.path.basename(path), open(os.path.abspath(path), bstack111l1l_opy_ (u"ࠫࡷࡨࠧਢ")), bstack111l1l_opy_ (u"ࠬࡺࡥࡹࡶ࠲ࡴࡱࡧࡩ࡯ࠩਣ")),
      bstack111l1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩਤ"): bstack11l1ll1l_opy_
    }
  )
  response = requests.post(bstack1l1ll11lll_opy_, data=bstack11lllll111_opy_,
                           headers={bstack111l1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ਥ"): bstack11lllll111_opy_.content_type},
                           auth=(config[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪਦ")], config[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬਧ")]))
  try:
    res = json.loads(response.text)
    bstack11lllll1l_opy_ = res[bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡶࡴ࡯ࠫਨ")]
    logger.info(bstack1l1l1ll1ll_opy_.format(bstack11lllll1l_opy_))
    bstack1lll1ll1l_opy_(md5_hash, bstack11lllll1l_opy_)
  except ValueError as err:
    bstack111lll1l_opy_(bstack1l11lll1l_opy_.format(str(err)))
  return bstack11lllll1l_opy_
def bstack1l1ll11l1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack111l11l1l_opy_
  bstack1l11l1l1l_opy_ = 1
  bstack1lllll11ll_opy_ = 1
  if bstack111l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ਩") in CONFIG:
    bstack1lllll11ll_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬਪ")]
  else:
    bstack1lllll11ll_opy_ = bstack1llllll111_opy_(framework_name, args) or 1
  if bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਫ") in CONFIG:
    bstack1l11l1l1l_opy_ = len(CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਬ")])
  bstack111l11l1l_opy_ = int(bstack1lllll11ll_opy_) * int(bstack1l11l1l1l_opy_)
def bstack1llllll111_opy_(framework_name, args):
  if framework_name == bstack11l1l1111_opy_ and args and bstack111l1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ਭ") in args:
      bstack1l1ll11111_opy_ = args.index(bstack111l1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧਮ"))
      return int(args[bstack1l1ll11111_opy_ + 1]) or 1
  return 1
def bstack1111l11l1_opy_(md5_hash):
  bstack11l1lll11_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬਯ")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫਰ"), bstack111l1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭਱"))
  if os.path.exists(bstack11l1lll11_opy_):
    bstack11l1l11l1_opy_ = json.load(open(bstack11l1lll11_opy_, bstack111l1l_opy_ (u"࠭ࡲࡣࠩਲ")))
    if md5_hash in bstack11l1l11l1_opy_:
      bstack1l1l111l_opy_ = bstack11l1l11l1_opy_[md5_hash]
      bstack11lll11lll_opy_ = datetime.datetime.now()
      bstack1l11llll11_opy_ = datetime.datetime.strptime(bstack1l1l111l_opy_[bstack111l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪਲ਼")], bstack111l1l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ਴"))
      if (bstack11lll11lll_opy_ - bstack1l11llll11_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1l1l111l_opy_[bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧਵ")]):
        return None
      return bstack1l1l111l_opy_[bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ਸ਼")]
  else:
    return None
def bstack1lll1ll1l_opy_(md5_hash, bstack11lllll1l_opy_):
  bstack111l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠫࢃ࠭਷")), bstack111l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਸ"))
  if not os.path.exists(bstack111l1l1l1_opy_):
    os.makedirs(bstack111l1l1l1_opy_)
  bstack11l1lll11_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨਹ")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ਺"), bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ਻"))
  bstack11l1lll1_opy_ = {
    bstack111l1l_opy_ (u"ࠩ࡬ࡨ਼ࠬ"): bstack11lllll1l_opy_,
    bstack111l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭਽"): datetime.datetime.strftime(datetime.datetime.now(), bstack111l1l_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨਾ")),
    bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪਿ"): str(__version__)
  }
  if os.path.exists(bstack11l1lll11_opy_):
    bstack11l1l11l1_opy_ = json.load(open(bstack11l1lll11_opy_, bstack111l1l_opy_ (u"࠭ࡲࡣࠩੀ")))
  else:
    bstack11l1l11l1_opy_ = {}
  bstack11l1l11l1_opy_[md5_hash] = bstack11l1lll1_opy_
  with open(bstack11l1lll11_opy_, bstack111l1l_opy_ (u"ࠢࡸ࠭ࠥੁ")) as outfile:
    json.dump(bstack11l1l11l1_opy_, outfile)
def bstack1llll11l11_opy_(self):
  return
def bstack1l1ll1lll_opy_(self):
  return
def bstack1l1lll1l1_opy_(self):
  global bstack1l1ll11ll1_opy_
  bstack1l1ll11ll1_opy_(self)
def bstack1llll111l1_opy_():
  global bstack1l1ll111l_opy_
  bstack1l1ll111l_opy_ = True
def bstack1llllll1l_opy_(self):
  global bstack1l1111llll_opy_
  global bstack1lll111lll_opy_
  global bstack1ll11l1111_opy_
  try:
    if bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨੂ") in bstack1l1111llll_opy_ and self.session_id != None and bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭੃"), bstack111l1l_opy_ (u"ࠪࠫ੄")) != bstack111l1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ੅"):
      bstack1l1llll111_opy_ = bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ੆") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ੇ")
      if bstack1l1llll111_opy_ == bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧੈ"):
        bstack1lll1l111_opy_(logger)
      if self != None:
        bstack1llll1llll_opy_(self, bstack1l1llll111_opy_, bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫ੉").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠩࠪ੊")
    if bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪੋ") in bstack1l1111llll_opy_ and getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪੌ"), None):
      bstack1llll1ll1l_opy_.bstack1ll1ll11ll_opy_(self, bstack1ll1l11lll_opy_, logger, wait=True)
    if bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩ੍ࠬ") in bstack1l1111llll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1llll1llll_opy_(self, bstack111l1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ੎"))
      bstack1l11lll111_opy_.bstack1111l1ll_opy_(self)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣ੏") + str(e))
  bstack1ll11l1111_opy_(self)
  self.session_id = None
def bstack1l11ll1lll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11llllll1_opy_
    global bstack1l1111llll_opy_
    command_executor = kwargs.get(bstack111l1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫ੐"), bstack111l1l_opy_ (u"ࠩࠪੑ"))
    bstack11ll1lll1_opy_ = False
    if type(command_executor) == str and bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭੒") in command_executor:
      bstack11ll1lll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ੓") in str(getattr(command_executor, bstack111l1l_opy_ (u"ࠬࡥࡵࡳ࡮ࠪ੔"), bstack111l1l_opy_ (u"࠭ࠧ੕"))):
      bstack11ll1lll1_opy_ = True
    else:
      return bstack1lll1llll_opy_(self, *args, **kwargs)
    if bstack11ll1lll1_opy_:
      if kwargs.get(bstack111l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ੖")):
        kwargs[bstack111l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ੗")] = bstack11llllll1_opy_(kwargs[bstack111l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ੘")], bstack1l1111llll_opy_)
      elif kwargs.get(bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪਖ਼")):
        kwargs[bstack111l1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫਗ਼")] = bstack11llllll1_opy_(kwargs[bstack111l1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬਜ਼")], bstack1l1111llll_opy_)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨੜ").format(str(e)))
  return bstack1lll1llll_opy_(self, *args, **kwargs)
def bstack1ll1lllll1_opy_(self, command_executor=bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯࠲࠴࠺࠲࠵࠴࠰࠯࠳࠽࠸࠹࠺࠴ࠣ੝"), *args, **kwargs):
  bstack1111111l1_opy_ = bstack1l11ll1lll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1111lll1l_opy_.on():
    return bstack1111111l1_opy_
  try:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡲࡱࡲࡧ࡮ࡥࠢࡈࡼࡪࡩࡵࡵࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨࡤࡰࡸ࡫ࠠ࠮ࠢࡾࢁࠬਫ਼").format(str(command_executor)))
    logger.debug(bstack111l1l_opy_ (u"ࠩࡋࡹࡧࠦࡕࡓࡎࠣ࡭ࡸࠦ࠭ࠡࡽࢀࠫ੟").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭੠") in command_executor._url:
      bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ੡"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ੢") in command_executor):
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ੣"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1l1ll1l_opy_.bstack1llll1l1_opy_(self)
  return bstack1111111l1_opy_
def bstack1ll1l1l1_opy_(args):
  return bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨ੤") in str(args)
def bstack1ll11lll11_opy_(self, driver_command, *args, **kwargs):
  global bstack1l111l11_opy_
  global bstack11l1lllll_opy_
  bstack11l1111ll_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ੥"), None) and bstack1ll111l11_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ੦"), None)
  bstack1ll1ll1lll_opy_ = getattr(self, bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ੧"), None) != None and getattr(self, bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ੨"), None) == True
  if not bstack11l1lllll_opy_ and bstack1l1l1ll11_opy_ and bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ੩") in CONFIG and CONFIG[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭੪")] == True and bstack1lllll1lll_opy_.bstack11l1l111l_opy_(driver_command) and (bstack1ll1ll1lll_opy_ or bstack11l1111ll_opy_) and not bstack1ll1l1l1_opy_(args):
    try:
      bstack11l1lllll_opy_ = True
      logger.debug(bstack111l1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ੫").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭੬").format(str(err)))
    bstack11l1lllll_opy_ = False
  response = bstack1l111l11_opy_(self, driver_command, *args, **kwargs)
  if (bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ੭") in str(bstack1l1111llll_opy_).lower() or bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ੮") in str(bstack1l1111llll_opy_).lower()) and bstack1111lll1l_opy_.on():
    try:
      if driver_command == bstack111l1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ੯"):
        bstack1l1l1ll1l_opy_.bstack11llll11l1_opy_({
            bstack111l1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫੰ"): response[bstack111l1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬੱ")],
            bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧੲ"): bstack1l1l1ll1l_opy_.current_test_uuid() if bstack1l1l1ll1l_opy_.current_test_uuid() else bstack1111lll1l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack1l1llllll1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1lll111lll_opy_
  global bstack1l1l1llll1_opy_
  global bstack111llll1l_opy_
  global bstack1lll11l1_opy_
  global bstack11l111l1l_opy_
  global bstack1l1111llll_opy_
  global bstack1lll1llll_opy_
  global bstack11ll11l1_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1ll1l11lll_opy_
  CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪੳ")] = str(bstack1l1111llll_opy_) + str(__version__)
  command_executor = bstack1l1l11111_opy_()
  logger.debug(bstack1l1l111ll1_opy_.format(command_executor))
  proxy = bstack11111lll_opy_(CONFIG, proxy)
  bstack1ll11ll1_opy_ = 0 if bstack1l1l1llll1_opy_ < 0 else bstack1l1l1llll1_opy_
  try:
    if bstack1lll11l1_opy_ is True:
      bstack1ll11ll1_opy_ = int(multiprocessing.current_process().name)
    elif bstack11l111l1l_opy_ is True:
      bstack1ll11ll1_opy_ = int(threading.current_thread().name)
  except:
    bstack1ll11ll1_opy_ = 0
  bstack1l1111111l_opy_ = bstack11l1ll1l1_opy_(CONFIG, bstack1ll11ll1_opy_)
  logger.debug(bstack1111llll1_opy_.format(str(bstack1l1111111l_opy_)))
  if bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ੴ") in CONFIG and bstack11ll111l_opy_(CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧੵ")]):
    bstack1l11l1l11l_opy_(bstack1l1111111l_opy_)
  if bstack1l1l1lll_opy_.bstack11lll1l1ll_opy_(CONFIG, bstack1ll11ll1_opy_) and bstack1l1l1lll_opy_.bstack11lll11l1l_opy_(bstack1l1111111l_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    bstack1l1l1lll_opy_.set_capabilities(bstack1l1111111l_opy_, CONFIG)
  if desired_capabilities:
    bstack1l1lll111l_opy_ = bstack111l111ll_opy_(desired_capabilities)
    bstack1l1lll111l_opy_[bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ੶")] = bstack11l11111l_opy_(CONFIG)
    bstack1ll1l11111_opy_ = bstack11l1ll1l1_opy_(bstack1l1lll111l_opy_)
    if bstack1ll1l11111_opy_:
      bstack1l1111111l_opy_ = update(bstack1ll1l11111_opy_, bstack1l1111111l_opy_)
    desired_capabilities = None
  if options:
    bstack1lllll11_opy_(options, bstack1l1111111l_opy_)
  if not options:
    options = bstack1l1lll11l1_opy_(bstack1l1111111l_opy_)
  bstack1ll1l11lll_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੷"))[bstack1ll11ll1_opy_]
  if proxy and bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭੸")):
    options.proxy(proxy)
  if options and bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭੹")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1111ll1l_opy_() < version.parse(bstack111l1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ੺")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1111111l_opy_)
  logger.info(bstack1ll1llll1l_opy_)
  if bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ੻")):
    bstack1lll1llll_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ੼")):
    bstack1lll1llll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ੽")):
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
    bstack1l11lll11l_opy_ = bstack111l1l_opy_ (u"ࠬ࠭੾")
    if bstack1111ll1l_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ੿")):
      bstack1l11lll11l_opy_ = self.caps.get(bstack111l1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ઀"))
    else:
      bstack1l11lll11l_opy_ = self.capabilities.get(bstack111l1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣઁ"))
    if bstack1l11lll11l_opy_:
      bstack1111l1111_opy_(bstack1l11lll11l_opy_)
      if bstack1111ll1l_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩં")):
        self.command_executor._url = bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦઃ") + bstack1l1ll11l11_opy_ + bstack111l1l_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ઄")
      else:
        self.command_executor._url = bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢઅ") + bstack1l11lll11l_opy_ + bstack111l1l_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢઆ")
      logger.debug(bstack1ll1llll11_opy_.format(bstack1l11lll11l_opy_))
    else:
      logger.debug(bstack1l1ll1111_opy_.format(bstack111l1l_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣઇ")))
  except Exception as e:
    logger.debug(bstack1l1ll1111_opy_.format(e))
  if bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧઈ") in bstack1l1111llll_opy_:
    bstack11l1llll1_opy_(bstack1l1l1llll1_opy_, bstack1l1l1l11ll_opy_)
  bstack1lll111lll_opy_ = self.session_id
  if bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩઉ") in bstack1l1111llll_opy_ or bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪઊ") in bstack1l1111llll_opy_ or bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪઋ") in bstack1l1111llll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l1l1ll1l_opy_.bstack1llll1l1_opy_(self)
  bstack11ll11l1_opy_.append(self)
  if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઌ") in CONFIG and bstack111l1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫઍ") in CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ઎")][bstack1ll11ll1_opy_]:
    bstack111llll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫએ")][bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઐ")]
  logger.debug(bstack11111l1ll_opy_.format(bstack1lll111lll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111ll1ll_opy_
    def bstack1ll111111l_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll1l1l11_opy_
      if(bstack111l1l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧઑ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠫࢃ࠭઒")), bstack111l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬઓ"), bstack111l1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨઔ")), bstack111l1l_opy_ (u"ࠧࡸࠩક")) as fp:
          fp.write(bstack111l1l_opy_ (u"ࠣࠤખ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦગ")))):
          with open(args[1], bstack111l1l_opy_ (u"ࠪࡶࠬઘ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111l1l_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪઙ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l111lll11_opy_)
            if bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩચ") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪછ")]).lower() != bstack111l1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭જ"):
                bstack1llll11l_opy_ = bstack1111ll1ll_opy_()
                bstack11lll111_opy_ = bstack111l1l_opy_ (u"ࠨࠩࠪࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠ࠿ࠏࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬ࠿ࠏࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࠐࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࡰࡪࡺࠠࡤࡣࡳࡷࡀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࡴࡳࡻࠣࡿࢀࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࢀࠐࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࠩࡾࡧࡩࡶࡕࡳ࡮ࢀࠫࠥ࠱ࠠࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮࠲ࠊࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠊࠡࠢࢀࢁ࠮ࡁࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࢂࢃ࠻ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࠨࠩࠪઝ").format(bstack1llll11l_opy_=bstack1llll11l_opy_)
            lines.insert(1, bstack11lll111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦઞ")), bstack111l1l_opy_ (u"ࠪࡻࠬટ")) as bstack11l11l1ll_opy_:
              bstack11l11l1ll_opy_.writelines(lines)
        CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ઠ")] = str(bstack1l1111llll_opy_) + str(__version__)
        bstack1ll11ll1_opy_ = 0 if bstack1l1l1llll1_opy_ < 0 else bstack1l1l1llll1_opy_
        try:
          if bstack1lll11l1_opy_ is True:
            bstack1ll11ll1_opy_ = int(multiprocessing.current_process().name)
          elif bstack11l111l1l_opy_ is True:
            bstack1ll11ll1_opy_ = int(threading.current_thread().name)
        except:
          bstack1ll11ll1_opy_ = 0
        CONFIG[bstack111l1l_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧડ")] = False
        CONFIG[bstack111l1l_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧઢ")] = True
        bstack1l1111111l_opy_ = bstack11l1ll1l1_opy_(CONFIG, bstack1ll11ll1_opy_)
        logger.debug(bstack1111llll1_opy_.format(str(bstack1l1111111l_opy_)))
        if CONFIG.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫણ")):
          bstack1l11l1l11l_opy_(bstack1l1111111l_opy_)
        if bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫત") in CONFIG and bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧથ") in CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭દ")][bstack1ll11ll1_opy_]:
          bstack111llll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧધ")][bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪન")]
        args.append(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨ઩")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧપ"), bstack111l1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪફ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1111111l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦબ"))
      bstack1lll1l1l11_opy_ = True
      return bstack1ll1l1ll11_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1l11l111ll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1l1l1llll1_opy_
    global bstack111llll1l_opy_
    global bstack1lll11l1_opy_
    global bstack11l111l1l_opy_
    global bstack1l1111llll_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬભ")] = str(bstack1l1111llll_opy_) + str(__version__)
    bstack1ll11ll1_opy_ = 0 if bstack1l1l1llll1_opy_ < 0 else bstack1l1l1llll1_opy_
    try:
      if bstack1lll11l1_opy_ is True:
        bstack1ll11ll1_opy_ = int(multiprocessing.current_process().name)
      elif bstack11l111l1l_opy_ is True:
        bstack1ll11ll1_opy_ = int(threading.current_thread().name)
    except:
      bstack1ll11ll1_opy_ = 0
    CONFIG[bstack111l1l_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥમ")] = True
    bstack1l1111111l_opy_ = bstack11l1ll1l1_opy_(CONFIG, bstack1ll11ll1_opy_)
    logger.debug(bstack1111llll1_opy_.format(str(bstack1l1111111l_opy_)))
    if CONFIG.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩય")):
      bstack1l11l1l11l_opy_(bstack1l1111111l_opy_)
    if bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩર") in CONFIG and bstack111l1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ઱") in CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫલ")][bstack1ll11ll1_opy_]:
      bstack111llll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")][bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ઴")]
    import urllib
    import json
    if bstack111l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨવ") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩશ")]).lower() != bstack111l1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬષ"):
        bstack1l111ll1l_opy_ = bstack1111ll1ll_opy_()
        bstack1llll11l_opy_ = bstack1l111ll1l_opy_ + urllib.parse.quote(json.dumps(bstack1l1111111l_opy_))
    else:
        bstack1llll11l_opy_ = bstack111l1l_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩસ") + urllib.parse.quote(json.dumps(bstack1l1111111l_opy_))
    browser = self.connect(bstack1llll11l_opy_)
    return browser
except Exception as e:
    pass
def bstack1111l1lll_opy_():
    global bstack1lll1l1l11_opy_
    global bstack1l1111llll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11l1ll111_opy_
        if not bstack1l1l1ll11_opy_:
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
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1ll111111l_opy_
      bstack1lll1l1l11_opy_ = True
    except Exception as e:
      pass
def bstack1l11l1l1_opy_(context, bstack111111l1_opy_):
  try:
    context.page.evaluate(bstack111l1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤહ"), bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭઺")+ json.dumps(bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠥࢁࢂࠨ઻"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤ઼"), e)
def bstack111l11l11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111l1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨઽ"), bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫા") + json.dumps(message) + bstack111l1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪિ") + json.dumps(level) + bstack111l1l_opy_ (u"ࠨࡿࢀࠫી"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧુ"), e)
def bstack1l11l11lll_opy_(self, url):
  global bstack1ll11l1l_opy_
  try:
    bstack1111l111_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1ll1l11l_opy_.format(str(err)))
  try:
    bstack1ll11l1l_opy_(self, url)
  except Exception as e:
    try:
      bstack1llllll11l_opy_ = str(e)
      if any(err_msg in bstack1llllll11l_opy_ for err_msg in bstack1lll1l1l1_opy_):
        bstack1111l111_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1ll1l11l_opy_.format(str(err)))
    raise e
def bstack1ll11l11ll_opy_(self):
  global bstack111l11111_opy_
  bstack111l11111_opy_ = self
  return
def bstack1l11l1l11_opy_(self):
  global bstack1l1l1l111_opy_
  bstack1l1l1l111_opy_ = self
  return
def bstack1l11ll1ll1_opy_(test_name, bstack1l11l11l1l_opy_):
  global CONFIG
  if percy.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣૂ"):
    bstack1l11111111_opy_ = os.path.relpath(bstack1l11l11l1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l11111111_opy_)
    bstack11ll11l11_opy_ = suite_name + bstack111l1l_opy_ (u"ࠦ࠲ࠨૃ") + test_name
    threading.current_thread().percySessionName = bstack11ll11l11_opy_
def bstack11llllll1l_opy_(self, test, *args, **kwargs):
  global bstack1l1ll1llll_opy_
  test_name = None
  bstack1l11l11l1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l11l11l1l_opy_ = str(test.source)
  bstack1l11ll1ll1_opy_(test_name, bstack1l11l11l1l_opy_)
  bstack1l1ll1llll_opy_(self, test, *args, **kwargs)
def bstack1ll111l1l_opy_(driver, bstack11ll11l11_opy_):
  if not bstack1l1111ll11_opy_ and bstack11ll11l11_opy_:
      bstack1ll111ll_opy_ = {
          bstack111l1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬૄ"): bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧૅ"),
          bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ૆"): {
              bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ે"): bstack11ll11l11_opy_
          }
      }
      bstack111llll11_opy_ = bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧૈ").format(json.dumps(bstack1ll111ll_opy_))
      driver.execute_script(bstack111llll11_opy_)
  if bstack1lll11l11l_opy_:
      bstack1ll111ll11_opy_ = {
          bstack111l1l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪૉ"): bstack111l1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭૊"),
          bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨો"): {
              bstack111l1l_opy_ (u"࠭ࡤࡢࡶࡤࠫૌ"): bstack11ll11l11_opy_ + bstack111l1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤ્ࠢࠩ"),
              bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ૎"): bstack111l1l_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ૏")
          }
      }
      if bstack1lll11l11l_opy_.status == bstack111l1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨૐ"):
          bstack111111l1l_opy_ = bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ૑").format(json.dumps(bstack1ll111ll11_opy_))
          driver.execute_script(bstack111111l1l_opy_)
          bstack1llll1llll_opy_(driver, bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ૒"))
      elif bstack1lll11l11l_opy_.status == bstack111l1l_opy_ (u"࠭ࡆࡂࡋࡏࠫ૓"):
          reason = bstack111l1l_opy_ (u"ࠢࠣ૔")
          bstack11111111l_opy_ = bstack11ll11l11_opy_ + bstack111l1l_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠩ૕")
          if bstack1lll11l11l_opy_.message:
              reason = str(bstack1lll11l11l_opy_.message)
              bstack11111111l_opy_ = bstack11111111l_opy_ + bstack111l1l_opy_ (u"ࠩࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࠩ૖") + reason
          bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭૗")] = {
              bstack111l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ૘"): bstack111l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ૙"),
              bstack111l1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ૚"): bstack11111111l_opy_
          }
          bstack111111l1l_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ૛").format(json.dumps(bstack1ll111ll11_opy_))
          driver.execute_script(bstack111111l1l_opy_)
          bstack1llll1llll_opy_(driver, bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ૜"), reason)
          bstack1111lllll_opy_(reason, str(bstack1lll11l11l_opy_), str(bstack1l1l1llll1_opy_), logger)
def bstack1ll1ll1111_opy_(driver, test):
  if percy.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ૝") and percy.bstack1l111lll1_opy_() == bstack111l1l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ૞"):
      bstack11111l11l_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ૟"), None)
      bstack1ll1l111ll_opy_(driver, bstack11111l11l_opy_, test)
  if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩૠ"), None) and bstack1ll111l11_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬૡ"), None):
      logger.info(bstack111l1l_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢૢ"))
      bstack1l1l1lll_opy_.bstack1ll1111l_opy_(driver, name=test.name, path=test.source)
def bstack11111ll1_opy_(test, bstack11ll11l11_opy_):
    try:
      data = {}
      if test:
        data[bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ૣ")] = bstack11ll11l11_opy_
      if bstack1lll11l11l_opy_:
        if bstack1lll11l11l_opy_.status == bstack111l1l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ૤"):
          data[bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ૥")] = bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ૦")
        elif bstack1lll11l11l_opy_.status == bstack111l1l_opy_ (u"ࠬࡌࡁࡊࡎࠪ૧"):
          data[bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭૨")] = bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ૩")
          if bstack1lll11l11l_opy_.message:
            data[bstack111l1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ૪")] = str(bstack1lll11l11l_opy_.message)
      user = CONFIG[bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૫")]
      key = CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭૬")]
      url = bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩ૭").format(user, key, bstack1lll111lll_opy_)
      headers = {
        bstack111l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ૮"): bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ૯"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1111ll11_opy_.format(str(e)))
def bstack1l1lll1ll_opy_(test, bstack11ll11l11_opy_):
  global CONFIG
  global bstack1l1l1l111_opy_
  global bstack111l11111_opy_
  global bstack1lll111lll_opy_
  global bstack1lll11l11l_opy_
  global bstack111llll1l_opy_
  global bstack1lll1l1l1l_opy_
  global bstack11l11l1l1_opy_
  global bstack11ll1ll11_opy_
  global bstack111l1l1ll_opy_
  global bstack11ll11l1_opy_
  global bstack1ll1l11lll_opy_
  try:
    if not bstack1lll111lll_opy_:
      with open(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠧࡿࠩ૰")), bstack111l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૱"), bstack111l1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ૲"))) as f:
        bstack1111111ll_opy_ = json.loads(bstack111l1l_opy_ (u"ࠥࡿࠧ૳") + f.read().strip() + bstack111l1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭૴") + bstack111l1l_opy_ (u"ࠧࢃࠢ૵"))
        bstack1lll111lll_opy_ = bstack1111111ll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack11ll11l1_opy_:
    for driver in bstack11ll11l1_opy_:
      if bstack1lll111lll_opy_ == driver.session_id:
        if test:
          bstack1ll1ll1111_opy_(driver, test)
        bstack1ll111l1l_opy_(driver, bstack11ll11l11_opy_)
  elif bstack1lll111lll_opy_:
    bstack11111ll1_opy_(test, bstack11ll11l11_opy_)
  if bstack1l1l1l111_opy_:
    bstack11l11l1l1_opy_(bstack1l1l1l111_opy_)
  if bstack111l11111_opy_:
    bstack11ll1ll11_opy_(bstack111l11111_opy_)
  if bstack1l1ll111l_opy_:
    bstack111l1l1ll_opy_()
def bstack11l1ll11_opy_(self, test, *args, **kwargs):
  bstack11ll11l11_opy_ = None
  if test:
    bstack11ll11l11_opy_ = str(test.name)
  bstack1l1lll1ll_opy_(test, bstack11ll11l11_opy_)
  bstack1lll1l1l1l_opy_(self, test, *args, **kwargs)
def bstack1l11llllll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1llllll_opy_
  global CONFIG
  global bstack11ll11l1_opy_
  global bstack1lll111lll_opy_
  bstack1ll1l11l11_opy_ = None
  try:
    if bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ૶"), None):
      try:
        if not bstack1lll111lll_opy_:
          with open(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠧࡿࠩ૷")), bstack111l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૸"), bstack111l1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫૹ"))) as f:
            bstack1111111ll_opy_ = json.loads(bstack111l1l_opy_ (u"ࠥࡿࠧૺ") + f.read().strip() + bstack111l1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ૻ") + bstack111l1l_opy_ (u"ࠧࢃࠢૼ"))
            bstack1lll111lll_opy_ = bstack1111111ll_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack11ll11l1_opy_:
        for driver in bstack11ll11l1_opy_:
          if bstack1lll111lll_opy_ == driver.session_id:
            bstack1ll1l11l11_opy_ = driver
    bstack1l1lllllll_opy_ = bstack1l1l1lll_opy_.bstack1lll1ll1ll_opy_(test.tags)
    if bstack1ll1l11l11_opy_:
      threading.current_thread().isA11yTest = bstack1l1l1lll_opy_.bstack1l1ll1ll1_opy_(bstack1ll1l11l11_opy_, bstack1l1lllllll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1l1lllllll_opy_
  except:
    pass
  bstack1l1llllll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1lll11l11l_opy_
  bstack1lll11l11l_opy_ = self._test
def bstack1lll111ll1_opy_():
  global bstack1l11ll11l1_opy_
  try:
    if os.path.exists(bstack1l11ll11l1_opy_):
      os.remove(bstack1l11ll11l1_opy_)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ૽") + str(e))
def bstack1ll1l11ll_opy_():
  global bstack1l11ll11l1_opy_
  bstack111lll11_opy_ = {}
  try:
    if not os.path.isfile(bstack1l11ll11l1_opy_):
      with open(bstack1l11ll11l1_opy_, bstack111l1l_opy_ (u"ࠧࡸࠩ૾")):
        pass
      with open(bstack1l11ll11l1_opy_, bstack111l1l_opy_ (u"ࠣࡹ࠮ࠦ૿")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1l11ll11l1_opy_):
      bstack111lll11_opy_ = json.load(open(bstack1l11ll11l1_opy_, bstack111l1l_opy_ (u"ࠩࡵࡦࠬ଀")))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬଁ") + str(e))
  finally:
    return bstack111lll11_opy_
def bstack11l1llll1_opy_(platform_index, item_index):
  global bstack1l11ll11l1_opy_
  try:
    bstack111lll11_opy_ = bstack1ll1l11ll_opy_()
    bstack111lll11_opy_[item_index] = platform_index
    with open(bstack1l11ll11l1_opy_, bstack111l1l_opy_ (u"ࠦࡼ࠱ࠢଂ")) as outfile:
      json.dump(bstack111lll11_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪଃ") + str(e))
def bstack1l11l1lll1_opy_(bstack11111ll11_opy_):
  global CONFIG
  bstack11111lll1_opy_ = bstack111l1l_opy_ (u"࠭ࠧ଄")
  if not bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ") in CONFIG:
    logger.info(bstack111l1l_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬଆ"))
  try:
    platform = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][bstack11111ll11_opy_]
    if bstack111l1l_opy_ (u"ࠪࡳࡸ࠭ଈ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"ࠫࡴࡹࠧଉ")]) + bstack111l1l_opy_ (u"ࠬ࠲ࠠࠨଊ")
    if bstack111l1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩଋ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪଌ")]) + bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫ଍")
    if bstack111l1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭଎") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧଏ")]) + bstack111l1l_opy_ (u"ࠫ࠱ࠦࠧଐ")
    if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ଑") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ଒")]) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠪଓ")
    if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଔ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧକ")]) + bstack111l1l_opy_ (u"ࠪ࠰ࠥ࠭ଖ")
    if bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଗ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଘ")]) + bstack111l1l_opy_ (u"࠭ࠬࠡࠩଙ")
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧଚ") + str(e))
  finally:
    if bstack11111lll1_opy_[len(bstack11111lll1_opy_) - 2:] == bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫଛ"):
      bstack11111lll1_opy_ = bstack11111lll1_opy_[:-2]
    return bstack11111lll1_opy_
def bstack11l11111_opy_(path, bstack11111lll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1lll11_opy_ = ET.parse(path)
    bstack1l1llll1_opy_ = bstack1l1lll11_opy_.getroot()
    bstack111l1llll_opy_ = None
    for suite in bstack1l1llll1_opy_.iter(bstack111l1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨଜ")):
      if bstack111l1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪଝ") in suite.attrib:
        suite.attrib[bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩଞ")] += bstack111l1l_opy_ (u"ࠬࠦࠧଟ") + bstack11111lll1_opy_
        bstack111l1llll_opy_ = suite
    bstack1l111111l1_opy_ = None
    for robot in bstack1l1llll1_opy_.iter(bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬଠ")):
      bstack1l111111l1_opy_ = robot
    bstack11l1111l1_opy_ = len(bstack1l111111l1_opy_.findall(bstack111l1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ଡ")))
    if bstack11l1111l1_opy_ == 1:
      bstack1l111111l1_opy_.remove(bstack1l111111l1_opy_.findall(bstack111l1l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧଢ"))[0])
      bstack1l1ll11l1_opy_ = ET.Element(bstack111l1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨଣ"), attrib={bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨତ"): bstack111l1l_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫଥ"), bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨଦ"): bstack111l1l_opy_ (u"࠭ࡳ࠱ࠩଧ")})
      bstack1l111111l1_opy_.insert(1, bstack1l1ll11l1_opy_)
      bstack1lll1l11_opy_ = None
      for suite in bstack1l111111l1_opy_.iter(bstack111l1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ନ")):
        bstack1lll1l11_opy_ = suite
      bstack1lll1l11_opy_.append(bstack111l1llll_opy_)
      bstack1llll111_opy_ = None
      for status in bstack111l1llll_opy_.iter(bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ଩")):
        bstack1llll111_opy_ = status
      bstack1lll1l11_opy_.append(bstack1llll111_opy_)
    bstack1l1lll11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧପ") + str(e))
def bstack1l111111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11ll11ll_opy_
  global CONFIG
  if bstack111l1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢଫ") in options:
    del options[bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣବ")]
  bstack11l11ll1_opy_ = bstack1ll1l11ll_opy_()
  for bstack1l1111lll1_opy_ in bstack11l11ll1_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬଭ"), str(bstack1l1111lll1_opy_), bstack111l1l_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪମ"))
    bstack11l11111_opy_(path, bstack1l11l1lll1_opy_(bstack11l11ll1_opy_[bstack1l1111lll1_opy_]))
  bstack1lll111ll1_opy_()
  return bstack11ll11ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll1l1111l_opy_(self, ff_profile_dir):
  global bstack1lll1l1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll1l1ll_opy_(self, ff_profile_dir)
def bstack1l1lllll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1ll1l1l1_opy_
  bstack1ll11ll1l1_opy_ = []
  if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଯ") in CONFIG:
    bstack1ll11ll1l1_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫର")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111l1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥ଱")],
      pabot_args[bstack111l1l_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦଲ")],
      argfile,
      pabot_args.get(bstack111l1l_opy_ (u"ࠦ࡭࡯ࡶࡦࠤଳ")),
      pabot_args[bstack111l1l_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣ଴")],
      platform[0],
      bstack1l1ll1l1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111l1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨଵ")] or [(bstack111l1l_opy_ (u"ࠢࠣଶ"), None)]
    for platform in enumerate(bstack1ll11ll1l1_opy_)
  ]
def bstack1l111111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111ll11l_opy_=bstack111l1l_opy_ (u"ࠨࠩଷ")):
  global bstack11llll1l11_opy_
  self.platform_index = platform_index
  self.bstack1lllll1ll_opy_ = bstack1l111ll11l_opy_
  bstack11llll1l11_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11lll1l1l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll1lll1l_opy_
  global bstack1ll1l1l111_opy_
  bstack1ll11l1ll1_opy_ = copy.deepcopy(item)
  if not bstack111l1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫସ") in item.options:
    bstack1ll11l1ll1_opy_.options[bstack111l1l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬହ")] = []
  bstack1l11l1llll_opy_ = bstack1ll11l1ll1_opy_.options[bstack111l1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭଺")].copy()
  for v in bstack1ll11l1ll1_opy_.options[bstack111l1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ଻")]:
    if bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜଼ࠬ") in v:
      bstack1l11l1llll_opy_.remove(v)
    if bstack111l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧଽ") in v:
      bstack1l11l1llll_opy_.remove(v)
    if bstack111l1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬା") in v:
      bstack1l11l1llll_opy_.remove(v)
  bstack1l11l1llll_opy_.insert(0, bstack111l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫି").format(bstack1ll11l1ll1_opy_.platform_index))
  bstack1l11l1llll_opy_.insert(0, bstack111l1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪୀ").format(bstack1ll11l1ll1_opy_.bstack1lllll1ll_opy_))
  bstack1ll11l1ll1_opy_.options[bstack111l1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ୁ")] = bstack1l11l1llll_opy_
  if bstack1ll1l1l111_opy_:
    bstack1ll11l1ll1_opy_.options[bstack111l1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧୂ")].insert(0, bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩୃ").format(bstack1ll1l1l111_opy_))
  return bstack1ll1lll1l_opy_(caller_id, datasources, is_last, bstack1ll11l1ll1_opy_, outs_dir)
def bstack1llll1l11_opy_(command, item_index):
  if bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨୄ")):
    os.environ[bstack111l1l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ୅")] = json.dumps(CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ୆")][item_index % bstack11llll1111_opy_])
  global bstack1ll1l1l111_opy_
  if bstack1ll1l1l111_opy_:
    command[0] = command[0].replace(bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩେ"), bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨୈ") + str(
      item_index) + bstack111l1l_opy_ (u"ࠬࠦࠧ୉") + bstack1ll1l1l111_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ୊"),
                                    bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫୋ") + str(item_index), 1)
def bstack1ll1lll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll1ll11l_opy_
  bstack1llll1l11_opy_(command, item_index)
  return bstack1ll1ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1ll11l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll1ll11l_opy_
  bstack1llll1l11_opy_(command, item_index)
  return bstack1ll1ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l111l1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll1ll11l_opy_
  bstack1llll1l11_opy_(command, item_index)
  return bstack1ll1ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11111l1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack1lll1111ll_opy_
  bstack1111l1l1_opy_ = bstack1lll1111ll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack111l1l_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨୌ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111l1l_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ୍࠭")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1111l1l1_opy_
def bstack1l1l111l1l_opy_(runner, hook_name, context, element, bstack11llll1ll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1lllll_opy_.bstack1l1ll1ll1l_opy_(hook_name, element)
    bstack11llll1ll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1lllll_opy_.bstack1ll11lllll_opy_(element)
      if hook_name not in [bstack111l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧ୎"), bstack111l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ୏")] and args and hasattr(args[0], bstack111l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬ୐")):
        args[0].error_message = bstack111l1l_opy_ (u"࠭ࠧ୑")
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡬ࡦࡴࡤ࡭ࡧࠣ࡬ࡴࡵ࡫ࡴࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ୒").format(str(e)))
def bstack1ll1l111l1_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    if runner.hooks.get(bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧ୓")).__name__ != bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡤࡦࡨࡤࡹࡱࡺ࡟ࡩࡱࡲ࡯ࠧ୔"):
      bstack1l1l111l1l_opy_(runner, name, context, runner, bstack11llll1ll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1ll11ll111_opy_(bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ୕")) else context.browser
      runner.driver_initialised = bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣୖ")
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩ࠿ࠦࡻࡾࠩୗ").format(str(e)))
def bstack1l1l11l11_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    bstack1l1l111l1l_opy_(runner, name, context, context.feature, bstack11llll1ll_opy_, *args)
    try:
      if not bstack1l1111ll11_opy_:
        bstack1ll1l11l11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll11ll111_opy_(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ୘")) else context.browser
        if is_driver_active(bstack1ll1l11l11_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣ୙")
          bstack111111l1_opy_ = str(runner.feature.name)
          bstack1l11l1l1_opy_(context, bstack111111l1_opy_)
          bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭୚") + json.dumps(bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠩࢀࢁࠬ୛"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪଡ଼").format(str(e)))
def bstack11lllll1l1_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    if hasattr(context, bstack111l1l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ଢ଼")):
        bstack1l1lllll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack111l1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ୞")) else context.feature
    bstack1l1l111l1l_opy_(runner, name, context, target, bstack11llll1ll_opy_, *args)
def bstack11ll1ll1l_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1lllll_opy_.start_test(context)
    bstack1l1l111l1l_opy_(runner, name, context, context.scenario, bstack11llll1ll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l11lll111_opy_.bstack1lll11ll_opy_(context, *args)
    try:
      bstack1ll1l11l11_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬୟ"), context.browser)
      if is_driver_active(bstack1ll1l11l11_opy_):
        bstack1l1l1ll1l_opy_.bstack1llll1l1_opy_(bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ୠ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥୡ")
        if (not bstack1l1111ll11_opy_):
          scenario_name = args[0].name
          feature_name = bstack111111l1_opy_ = str(runner.feature.name)
          bstack111111l1_opy_ = feature_name + bstack111l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭ୢ") + scenario_name
          if runner.driver_initialised == bstack111l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧୣ"):
            bstack1l11l1l1_opy_(context, bstack111111l1_opy_)
            bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ୤") + json.dumps(bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠬࢃࡽࠨ୥"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ୦").format(str(e)))
def bstack1l1ll1l1ll_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    bstack1l1l111l1l_opy_(runner, name, context, args[0], bstack11llll1ll_opy_, *args)
    try:
      bstack1ll1l11l11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll11ll111_opy_(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭୧")) else context.browser
      if is_driver_active(bstack1ll1l11l11_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ୨")
        bstack1l1lllll_opy_.bstack11l111ll_opy_(args[0])
        if runner.driver_initialised == bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ୩"):
          feature_name = bstack111111l1_opy_ = str(runner.feature.name)
          bstack111111l1_opy_ = feature_name + bstack111l1l_opy_ (u"ࠪࠤ࠲ࠦࠧ୪") + context.scenario.name
          bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ୫") + json.dumps(bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠬࢃࡽࠨ୬"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪ୭").format(str(e)))
def bstack1lllll11l1_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
  bstack1l1lllll_opy_.bstack1l1ll1l1_opy_(args[0])
  try:
    bstack1111l1ll1_opy_ = args[0].status.name
    bstack1ll1l11l11_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭୮") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll1l11l11_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack111l1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ୯")
        feature_name = bstack111111l1_opy_ = str(runner.feature.name)
        bstack111111l1_opy_ = feature_name + bstack111l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭୰") + context.scenario.name
        bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨୱ") + json.dumps(bstack111111l1_opy_) + bstack111l1l_opy_ (u"ࠫࢂࢃࠧ୲"))
    if str(bstack1111l1ll1_opy_).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ୳"):
      bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"࠭ࠧ୴")
      bstack1l11111l11_opy_ = bstack111l1l_opy_ (u"ࠧࠨ୵")
      bstack1l1l1l11_opy_ = bstack111l1l_opy_ (u"ࠨࠩ୶")
      try:
        import traceback
        bstack1llll1lll_opy_ = runner.exception.__class__.__name__
        bstack1ll111l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l11111l11_opy_ = bstack111l1l_opy_ (u"ࠩࠣࠫ୷").join(bstack1ll111l1_opy_)
        bstack1l1l1l11_opy_ = bstack1ll111l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
      bstack1llll1lll_opy_ += bstack1l1l1l11_opy_
      bstack111l11l11_opy_(context, json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ୸") + str(bstack1l11111l11_opy_)),
                          bstack111l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ୹"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ୺"):
        bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ୻"), None), bstack111l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ୼"), bstack1llll1lll_opy_)
        bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭୽") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ୾") + str(bstack1l11111l11_opy_)) + bstack111l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ୿"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ஀"):
        bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ஁"), bstack111l1l_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥஂ") + str(bstack1llll1lll_opy_))
    else:
      bstack111l11l11_opy_(context, bstack111l1l_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣஃ"), bstack111l1l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ஄"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢஅ"):
        bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨஆ"), None), bstack111l1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦஇ"))
      bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪஈ") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥஉ")) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ஊ"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ஋"):
        bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ஌"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ஍").format(str(e)))
  bstack1l1l111l1l_opy_(runner, name, context, args[0], bstack11llll1ll_opy_, *args)
def bstack1l11ll1l1l_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
  bstack1l1lllll_opy_.end_test(args[0])
  try:
    bstack1l1111ll1l_opy_ = args[0].status.name
    bstack1ll1l11l11_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪஎ"), context.browser)
    bstack1l11lll111_opy_.bstack1111l1ll_opy_(bstack1ll1l11l11_opy_)
    if str(bstack1l1111ll1l_opy_).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬஏ"):
      bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"࠭ࠧஐ")
      bstack1l11111l11_opy_ = bstack111l1l_opy_ (u"ࠧࠨ஑")
      bstack1l1l1l11_opy_ = bstack111l1l_opy_ (u"ࠨࠩஒ")
      try:
        import traceback
        bstack1llll1lll_opy_ = runner.exception.__class__.__name__
        bstack1ll111l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l11111l11_opy_ = bstack111l1l_opy_ (u"ࠩࠣࠫஓ").join(bstack1ll111l1_opy_)
        bstack1l1l1l11_opy_ = bstack1ll111l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
      bstack1llll1lll_opy_ += bstack1l1l1l11_opy_
      bstack111l11l11_opy_(context, json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤஔ") + str(bstack1l11111l11_opy_)),
                          bstack111l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥக"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ஖") or runner.driver_initialised == bstack111l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭஗"):
        bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"ࠧࡱࡣࡪࡩࠬ஘"), None), bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣங"), bstack1llll1lll_opy_)
        bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧச") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ஛") + str(bstack1l11111l11_opy_)) + bstack111l1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫஜ"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ஝") or runner.driver_initialised == bstack111l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ஞ"):
        bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧட"), bstack111l1l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ஠") + str(bstack1llll1lll_opy_))
    else:
      bstack111l11l11_opy_(context, bstack111l1l_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥ஡"), bstack111l1l_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ஢"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨண") or runner.driver_initialised == bstack111l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬத"):
        bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ஥"), None), bstack111l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ஦"))
      bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭஧") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨந")) + bstack111l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩன"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨப") or runner.driver_initialised == bstack111l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ஫"):
        bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ஬"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ஭").format(str(e)))
  bstack1l1l111l1l_opy_(runner, name, context, context.scenario, bstack11llll1ll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1ll1l11l_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    target = context.scenario if hasattr(context, bstack111l1l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪம")) else context.feature
    bstack1l1l111l1l_opy_(runner, name, context, target, bstack11llll1ll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1111111_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    try:
      bstack1ll1l11l11_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨய"), context.browser)
      if context.failed is True:
        bstack1lllll1l11_opy_ = []
        bstack1ll111l111_opy_ = []
        bstack1111l1l11_opy_ = []
        bstack11lll1ll1_opy_ = bstack111l1l_opy_ (u"ࠪࠫர")
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1lllll1l11_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack1ll111l1_opy_ = traceback.format_tb(exc_tb)
            bstack1llll1l1ll_opy_ = bstack111l1l_opy_ (u"ࠫࠥ࠭ற").join(bstack1ll111l1_opy_)
            bstack1ll111l111_opy_.append(bstack1llll1l1ll_opy_)
            bstack1111l1l11_opy_.append(bstack1ll111l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
        bstack1llll1lll_opy_ = bstack111l1l_opy_ (u"ࠬ࠭ல")
        for i in range(len(bstack1lllll1l11_opy_)):
          bstack1llll1lll_opy_ += bstack1lllll1l11_opy_[i] + bstack1111l1l11_opy_[i] + bstack111l1l_opy_ (u"࠭࡜࡯ࠩள")
        bstack11lll1ll1_opy_ = bstack111l1l_opy_ (u"ࠧࠡࠩழ").join(bstack1ll111l111_opy_)
        if runner.driver_initialised in [bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤவ"), bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨஶ")]:
          bstack111l11l11_opy_(context, bstack11lll1ll1_opy_, bstack111l1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤஷ"))
          bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"ࠫࡵࡧࡧࡦࠩஸ"), None), bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧஹ"), bstack1llll1lll_opy_)
          bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ஺") + json.dumps(bstack11lll1ll1_opy_) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ஻"))
          bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ஼"), bstack111l1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢ஽") + str(bstack1llll1lll_opy_))
          bstack1ll11111_opy_ = bstack1lll11l1l_opy_(bstack11lll1ll1_opy_, runner.feature.name, logger)
          if (bstack1ll11111_opy_ != None):
            bstack1lllll111_opy_.append(bstack1ll11111_opy_)
      else:
        if runner.driver_initialised in [bstack111l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦா"), bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣி")]:
          bstack111l11l11_opy_(context, bstack111l1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣீ") + str(runner.feature.name) + bstack111l1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣு"), bstack111l1l_opy_ (u"ࠢࡪࡰࡩࡳࠧூ"))
          bstack11llll11l_opy_(getattr(context, bstack111l1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭௃"), None), bstack111l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ௄"))
          bstack1ll1l11l11_opy_.execute_script(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ௅") + json.dumps(bstack111l1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢெ") + str(runner.feature.name) + bstack111l1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢே")) + bstack111l1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬை"))
          bstack1llll1llll_opy_(bstack1ll1l11l11_opy_, bstack111l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ௉"))
          bstack1ll11111_opy_ = bstack1lll11l1l_opy_(bstack11lll1ll1_opy_, runner.feature.name, logger)
          if (bstack1ll11111_opy_ != None):
            bstack1lllll111_opy_.append(bstack1ll11111_opy_)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪொ").format(str(e)))
    bstack1l1l111l1l_opy_(runner, name, context, context.feature, bstack11llll1ll_opy_, *args)
def bstack11lll1l11_opy_(runner, name, context, bstack11llll1ll_opy_, *args):
    bstack1l1l111l1l_opy_(runner, name, context, runner, bstack11llll1ll_opy_, *args)
def bstack11l1l1ll_opy_(self, name, context, *args):
  if bstack1l1l1ll11_opy_:
    platform_index = int(threading.current_thread()._name) % bstack11llll1111_opy_
    bstack11l111111_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬோ")][platform_index]
    os.environ[bstack111l1l_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫௌ")] = json.dumps(bstack11l111111_opy_)
  global bstack11llll1ll_opy_
  if not hasattr(self, bstack111l1l_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥ்ࠩ")):
    self.driver_initialised = None
  bstack1ll1l1ll1l_opy_ = {
      bstack111l1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩ௎"): bstack1ll1l111l1_opy_,
      bstack111l1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ௏"): bstack1l1l11l11_opy_,
      bstack111l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫௐ"): bstack11lllll1l1_opy_,
      bstack111l1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ௑"): bstack11ll1ll1l_opy_,
      bstack111l1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧ௒"): bstack1l1ll1l1ll_opy_,
      bstack111l1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧ௓"): bstack1lllll11l1_opy_,
      bstack111l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ௔"): bstack1l11ll1l1l_opy_,
      bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨ௕"): bstack1ll1l11l_opy_,
      bstack111l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭௖"): bstack1l1111111_opy_,
      bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪௗ"): bstack11lll1l11_opy_
  }
  handler = bstack1ll1l1ll1l_opy_.get(name, bstack11llll1ll_opy_)
  handler(self, name, context, bstack11llll1ll_opy_, *args)
  if name in [bstack111l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨ௘"), bstack111l1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ௙"), bstack111l1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭௚")]:
    try:
      bstack1ll1l11l11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll11ll111_opy_(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ௛")) else context.browser
      bstack1lll111ll_opy_ = (
        (name == bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨ௜") and self.driver_initialised == bstack111l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ௝")) or
        (name == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ௞") and self.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ௟")) or
        (name == bstack111l1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ௠") and self.driver_initialised in [bstack111l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ௡"), bstack111l1l_opy_ (u"ࠦ࡮ࡴࡳࡵࡧࡳࠦ௢")]) or
        (name == bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩ௣") and self.driver_initialised == bstack111l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ௤"))
      )
      if bstack1lll111ll_opy_:
        self.driver_initialised = None
        bstack1ll1l11l11_opy_.quit()
    except Exception:
      pass
def bstack11llll1l1l_opy_(config, startdir):
  return bstack111l1l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧ௥").format(bstack111l1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ௦"))
notset = Notset()
def bstack11llll1lll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11l1ll1ll_opy_
  if str(name).lower() == bstack111l1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ௧"):
    return bstack111l1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ௨")
  else:
    return bstack11l1ll1ll_opy_(self, name, default, skip)
def bstack111111111_opy_(item, when):
  global bstack1l1l1lll11_opy_
  try:
    bstack1l1l1lll11_opy_(item, when)
  except Exception as e:
    pass
def bstack11l111l1_opy_():
  return
def bstack111l1l11l_opy_(type, name, status, reason, bstack11ll1l1ll_opy_, bstack1lll1l11l_opy_):
  bstack1ll111ll_opy_ = {
    bstack111l1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ௩"): type,
    bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ௪"): {}
  }
  if type == bstack111l1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ௫"):
    bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ௬")][bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ௭")] = bstack11ll1l1ll_opy_
    bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ௮")][bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨ௯")] = json.dumps(str(bstack1lll1l11l_opy_))
  if type == bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ௰"):
    bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ௱")][bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ௲")] = name
  if type == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ௳"):
    bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ௴")][bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ௵")] = status
    if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ௶"):
      bstack1ll111ll_opy_[bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ௷")][bstack111l1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ௸")] = json.dumps(str(reason))
  bstack111llll11_opy_ = bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ௹").format(json.dumps(bstack1ll111ll_opy_))
  return bstack111llll11_opy_
def bstack1l1lll1111_opy_(driver_command, response):
    if driver_command == bstack111l1l_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ௺"):
        bstack1l1l1ll1l_opy_.bstack11llll11l1_opy_({
            bstack111l1l_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ௻"): response[bstack111l1l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ௼")],
            bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ௽"): bstack1l1l1ll1l_opy_.current_test_uuid()
        })
def bstack1l111lll1l_opy_(item, call, rep):
  global bstack1l1l1ll1_opy_
  global bstack11ll11l1_opy_
  global bstack1l1111ll11_opy_
  name = bstack111l1l_opy_ (u"ࠫࠬ௾")
  try:
    if rep.when == bstack111l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ௿"):
      bstack1lll111lll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l1111ll11_opy_:
          name = str(rep.nodeid)
          bstack1ll11llll_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఀ"), name, bstack111l1l_opy_ (u"ࠧࠨఁ"), bstack111l1l_opy_ (u"ࠨࠩం"), bstack111l1l_opy_ (u"ࠩࠪః"), bstack111l1l_opy_ (u"ࠪࠫఄ"))
          threading.current_thread().bstack1l1111l11_opy_ = name
          for driver in bstack11ll11l1_opy_:
            if bstack1lll111lll_opy_ == driver.session_id:
              driver.execute_script(bstack1ll11llll_opy_)
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫఅ").format(str(e)))
      try:
        bstack1l1lll1lll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ఆ"):
          status = bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ఇ") if rep.outcome.lower() == bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧఈ") else bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨఉ")
          reason = bstack111l1l_opy_ (u"ࠩࠪఊ")
          if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪఋ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111l1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩఌ") if status == bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ఍") else bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬఎ")
          data = name + bstack111l1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩఏ") if status == bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨఐ") else name + bstack111l1l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ఑") + reason
          bstack111l1l111_opy_ = bstack111l1l11l_opy_(bstack111l1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬఒ"), bstack111l1l_opy_ (u"ࠫࠬఓ"), bstack111l1l_opy_ (u"ࠬ࠭ఔ"), bstack111l1l_opy_ (u"࠭ࠧక"), level, data)
          for driver in bstack11ll11l1_opy_:
            if bstack1lll111lll_opy_ == driver.session_id:
              driver.execute_script(bstack111l1l111_opy_)
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫఖ").format(str(e)))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬగ").format(str(e)))
  bstack1l1l1ll1_opy_(item, call, rep)
def bstack1ll1l111ll_opy_(driver, bstack11l111ll1_opy_, test=None):
  global bstack1l1l1llll1_opy_
  if test != None:
    bstack1l11llll1_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧఘ"), None)
    bstack1l1l11lll1_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨఙ"), None)
    PercySDK.screenshot(driver, bstack11l111ll1_opy_, bstack1l11llll1_opy_=bstack1l11llll1_opy_, bstack1l1l11lll1_opy_=bstack1l1l11lll1_opy_, bstack1ll1lll1ll_opy_=bstack1l1l1llll1_opy_)
  else:
    PercySDK.screenshot(driver, bstack11l111ll1_opy_)
def bstack111lllll1_opy_(driver):
  if bstack1ll11ll1ll_opy_.bstack111111l11_opy_() is True or bstack1ll11ll1ll_opy_.capturing() is True:
    return
  bstack1ll11ll1ll_opy_.bstack1ll1lll111_opy_()
  while not bstack1ll11ll1ll_opy_.bstack111111l11_opy_():
    bstack11ll1111_opy_ = bstack1ll11ll1ll_opy_.bstack1l111l1l1_opy_()
    bstack1ll1l111ll_opy_(driver, bstack11ll1111_opy_)
  bstack1ll11ll1ll_opy_.bstack1111ll1l1_opy_()
def bstack1l1l11ll11_opy_(sequence, driver_command, response = None, bstack1l111ll1l1_opy_ = None, args = None):
    try:
      if sequence != bstack111l1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫచ"):
        return
      if percy.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦఛ"):
        return
      bstack11ll1111_opy_ = bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩజ"), None)
      for command in bstack111ll1ll1_opy_:
        if command == driver_command:
          for driver in bstack11ll11l1_opy_:
            bstack111lllll1_opy_(driver)
      bstack1ll1111111_opy_ = percy.bstack1l111lll1_opy_()
      if driver_command in bstack1l11l1111l_opy_[bstack1ll1111111_opy_]:
        bstack1ll11ll1ll_opy_.bstack1l1l11ll1_opy_(bstack11ll1111_opy_, driver_command)
    except Exception as e:
      pass
def bstack1ll111l11l_opy_(framework_name):
  if bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫఝ")):
      return
  bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬఞ"), True)
  global bstack1l1111llll_opy_
  global bstack1lll1l1l11_opy_
  global bstack1ll1111lll_opy_
  bstack1l1111llll_opy_ = framework_name
  logger.info(bstack1111ll111_opy_.format(bstack1l1111llll_opy_.split(bstack111l1l_opy_ (u"ࠩ࠰ࠫట"))[0]))
  bstack1l111l111_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l1l1ll11_opy_:
      Service.start = bstack1llll11l11_opy_
      Service.stop = bstack1l1ll1lll_opy_
      webdriver.Remote.get = bstack1l11l11lll_opy_
      WebDriver.close = bstack1l1lll1l1_opy_
      WebDriver.quit = bstack1llllll1l_opy_
      webdriver.Remote.__init__ = bstack1l1llllll1_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1l1l1ll11_opy_:
        webdriver.Remote.__init__ = bstack1ll1lllll1_opy_
    WebDriver.execute = bstack1ll11lll11_opy_
    bstack1lll1l1l11_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l1l1ll11_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1llll111l1_opy_
  except Exception as e:
    pass
  bstack1111l1lll_opy_()
  if not bstack1lll1l1l11_opy_:
    bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧఠ"), bstack11llllllll_opy_)
  if bstack1ll11ll11l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack11l1l1ll1_opy_
    except Exception as e:
      logger.error(bstack1l11l1ll1_opy_.format(str(e)))
  if bstack11lll1l1l1_opy_():
    bstack1l1lll1l_opy_(CONFIG, logger)
  if (bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪడ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠧࡺࡲࡶࡧࠥఢ"):
          bstack11llll1ll1_opy_(bstack1l1l11ll11_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll1l1111l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l11l1l11_opy_
      except Exception as e:
        logger.warn(bstack1l11l1l1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll11l11ll_opy_
      except Exception as e:
        logger.debug(bstack1ll1l1ll_opy_ + str(e))
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1l1ll_opy_)
    Output.start_test = bstack11llllll1l_opy_
    Output.end_test = bstack11l1ll11_opy_
    TestStatus.__init__ = bstack1l11llllll_opy_
    QueueItem.__init__ = bstack1l111111l_opy_
    pabot._create_items = bstack1l1lllll1_opy_
    try:
      from pabot import __version__ as bstack1l111l1l_opy_
      if version.parse(bstack1l111l1l_opy_) >= version.parse(bstack111l1l_opy_ (u"࠭࠲࠯࠳࠸࠲࠵࠭ణ")):
        pabot._run = bstack1l111l1ll1_opy_
      elif version.parse(bstack1l111l1l_opy_) >= version.parse(bstack111l1l_opy_ (u"ࠧ࠳࠰࠴࠷࠳࠶ࠧత")):
        pabot._run = bstack1ll11l11l_opy_
      else:
        pabot._run = bstack1ll1lll11_opy_
    except Exception as e:
      pabot._run = bstack1ll1lll11_opy_
    pabot._create_command_for_execution = bstack11lll1l1l_opy_
    pabot._report_results = bstack1l111111_opy_
  if bstack111l1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨథ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1lll_opy_)
    Runner.run_hook = bstack11l1l1ll_opy_
    Step.run = bstack11111l1l1_opy_
  if bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩద") in str(framework_name).lower():
    if not bstack1l1l1ll11_opy_:
      return
    try:
      if percy.bstack11lll1l111_opy_() == bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣధ"):
          bstack11llll1ll1_opy_(bstack1l1l11ll11_opy_)
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
def bstack111ll1ll_opy_():
  global CONFIG
  if bstack111l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫన") in CONFIG and int(CONFIG[bstack111l1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ఩")]) > 1:
    logger.warn(bstack111ll11l_opy_)
def bstack1ll11l1l11_opy_(arg, bstack1ll11llll1_opy_, bstack11ll1ll1_opy_=None):
  global CONFIG
  global bstack1l1ll11l11_opy_
  global bstack1l111l11l_opy_
  global bstack1l1l1ll11_opy_
  global bstack1l1ll111_opy_
  bstack11111llll_opy_ = bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ప")
  if bstack1ll11llll1_opy_ and isinstance(bstack1ll11llll1_opy_, str):
    bstack1ll11llll1_opy_ = eval(bstack1ll11llll1_opy_)
  CONFIG = bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧఫ")]
  bstack1l1ll11l11_opy_ = bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩబ")]
  bstack1l111l11l_opy_ = bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫభ")]
  bstack1l1l1ll11_opy_ = bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭మ")]
  bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬయ"), bstack1l1l1ll11_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧర")] = bstack11111llll_opy_
  os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬఱ")] = json.dumps(CONFIG)
  os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧల")] = bstack1l1ll11l11_opy_
  os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩళ")] = str(bstack1l111l11l_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨఴ")] = str(True)
  if bstack1ll11lll1l_opy_(arg, [bstack111l1l_opy_ (u"ࠪ࠱ࡳ࠭వ"), bstack111l1l_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬశ")]) != -1:
    os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ష")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll1ll1l1l_opy_)
    return
  bstack1l1lllll1l_opy_()
  global bstack111l11l1l_opy_
  global bstack1l1l1llll1_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1ll1l1l111_opy_
  global bstack11l1111l_opy_
  global bstack1ll1111lll_opy_
  global bstack1lll11l1_opy_
  arg.append(bstack111l1l_opy_ (u"ࠨ࠭ࡘࠤస"))
  arg.append(bstack111l1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥహ"))
  arg.append(bstack111l1l_opy_ (u"ࠣ࠯࡚ࠦ఺"))
  arg.append(bstack111l1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡗ࡬ࡪࠦࡨࡰࡱ࡮࡭ࡲࡶ࡬ࠣ఻"))
  global bstack1lll1llll_opy_
  global bstack1ll11l1111_opy_
  global bstack1l111l11_opy_
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
    bstack1l111l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11l1l1l1l_opy_(CONFIG) and bstack1ll11l111_opy_():
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
    logger.debug(bstack111l1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶ఼ࠫ"))
  bstack1l1ll1l1l1_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨఽ"), {}).get(bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧా"))
  bstack1lll11l1_opy_ = True
  bstack1ll111l11l_opy_(bstack1l1l1ll11l_opy_)
  os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧి")] = CONFIG[bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩీ")]
  os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫు")] = CONFIG[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬూ")]
  os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ృ")] = bstack1l1l1ll11_opy_.__str__()
  from _pytest.config import main as bstack1lll1llll1_opy_
  bstack1l1llll1l1_opy_ = []
  try:
    bstack1l111llll_opy_ = bstack1lll1llll1_opy_(arg)
    if bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨౄ") in multiprocessing.current_process().__dict__.keys():
      for bstack1lllll1111_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1llll1l1_opy_.append(bstack1lllll1111_opy_)
    try:
      bstack1l11ll111l_opy_ = (bstack1l1llll1l1_opy_, int(bstack1l111llll_opy_))
      bstack11ll1ll1_opy_.append(bstack1l11ll111l_opy_)
    except:
      bstack11ll1ll1_opy_.append((bstack1l1llll1l1_opy_, bstack1l111llll_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l1llll1l1_opy_.append({bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ౅"): bstack111l1l_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨె") + os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧే")), bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧై"): traceback.format_exc(), bstack111l1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ౉"): int(os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪొ")))})
    bstack11ll1ll1_opy_.append((bstack1l1llll1l1_opy_, 1))
def bstack1l1llll1l_opy_(arg):
  global bstack1ll1111ll_opy_
  bstack1ll111l11l_opy_(bstack1l1lll11l_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬో")] = str(bstack1l111l11l_opy_)
  from behave.__main__ import main as bstack111lll111_opy_
  status_code = bstack111lll111_opy_(arg)
  if status_code != 0:
    bstack1ll1111ll_opy_ = status_code
def bstack11l11ll11_opy_():
  logger.info(bstack1l1l11ll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫౌ"), help=bstack111l1l_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭్ࠧ"))
  parser.add_argument(bstack111l1l_opy_ (u"ࠧ࠮ࡷࠪ౎"), bstack111l1l_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ౏"), help=bstack111l1l_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨ౐"))
  parser.add_argument(bstack111l1l_opy_ (u"ࠪ࠱ࡰ࠭౑"), bstack111l1l_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪ౒"), help=bstack111l1l_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭౓"))
  parser.add_argument(bstack111l1l_opy_ (u"࠭࠭ࡧࠩ౔"), bstack111l1l_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ౕࠬ"), help=bstack111l1l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱౖࠧ"))
  bstack1l111l1111_opy_ = parser.parse_args()
  try:
    bstack1l1llll1ll_opy_ = bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭౗")
    if bstack1l111l1111_opy_.framework and bstack1l111l1111_opy_.framework not in (bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪౘ"), bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬౙ")):
      bstack1l1llll1ll_opy_ = bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫౚ")
    bstack11l11llll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1llll1ll_opy_)
    bstack1llll1ll11_opy_ = open(bstack11l11llll_opy_, bstack111l1l_opy_ (u"࠭ࡲࠨ౛"))
    bstack1llll1111l_opy_ = bstack1llll1ll11_opy_.read()
    bstack1llll1ll11_opy_.close()
    if bstack1l111l1111_opy_.username:
      bstack1llll1111l_opy_ = bstack1llll1111l_opy_.replace(bstack111l1l_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ౜"), bstack1l111l1111_opy_.username)
    if bstack1l111l1111_opy_.key:
      bstack1llll1111l_opy_ = bstack1llll1111l_opy_.replace(bstack111l1l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪౝ"), bstack1l111l1111_opy_.key)
    if bstack1l111l1111_opy_.framework:
      bstack1llll1111l_opy_ = bstack1llll1111l_opy_.replace(bstack111l1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ౞"), bstack1l111l1111_opy_.framework)
    file_name = bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭౟")
    file_path = os.path.abspath(file_name)
    bstack11l1l11ll_opy_ = open(file_path, bstack111l1l_opy_ (u"ࠫࡼ࠭ౠ"))
    bstack11l1l11ll_opy_.write(bstack1llll1111l_opy_)
    bstack11l1l11ll_opy_.close()
    logger.info(bstack1ll1ll1l1_opy_)
    try:
      os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧౡ")] = bstack1l111l1111_opy_.framework if bstack1l111l1111_opy_.framework != None else bstack111l1l_opy_ (u"ࠨࠢౢ")
      config = yaml.safe_load(bstack1llll1111l_opy_)
      config[bstack111l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧౣ")] = bstack111l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧ౤")
      bstack1l1111ll1_opy_(bstack1l1l1lll1l_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1l1l1l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11l1llll_opy_.format(str(e)))
def bstack1l1111ll1_opy_(bstack11l1ll11l_opy_, config, bstack1llll1ll_opy_={}):
  global bstack1l1l1ll11_opy_
  global bstack1lllll1ll1_opy_
  global bstack1l1ll111_opy_
  if not config:
    return
  bstack11111l1l_opy_ = bstack1lll1l1lll_opy_ if not bstack1l1l1ll11_opy_ else (
    bstack1l1l11l1_opy_ if bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠭౥") in config else bstack1lll1111l1_opy_)
  bstack1l1l1111l1_opy_ = False
  bstack11l11lll1_opy_ = False
  if bstack1l1l1ll11_opy_ is True:
      if bstack111l1l_opy_ (u"ࠪࡥࡵࡶࠧ౦") in config:
          bstack1l1l1111l1_opy_ = True
      else:
          bstack11l11lll1_opy_ = True
  bstack11l111l11_opy_ = bstack1ll11l11_opy_.bstack1lll1lll11_opy_(config, bstack1lllll1ll1_opy_)
  data = {
    bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭౧"): config[bstack111l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ౨")],
    bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ౩"): config[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ౪")],
    bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ౫"): bstack11l1ll11l_opy_,
    bstack111l1l_opy_ (u"ࠩࡧࡩࡹ࡫ࡣࡵࡧࡧࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭౬"): os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ౭"), bstack1lllll1ll1_opy_),
    bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭౮"): bstack1lll1lll1l_opy_,
    bstack111l1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲࠧ౯"): bstack11111l111_opy_(),
    bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ౰"): {
      bstack111l1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ౱"): str(config[bstack111l1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ౲")]) if bstack111l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ౳") in config else bstack111l1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ౴"),
      bstack111l1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࡜ࡥࡳࡵ࡬ࡳࡳ࠭౵"): sys.version,
      bstack111l1l_opy_ (u"ࠬࡸࡥࡧࡧࡵࡶࡪࡸࠧ౶"): bstack11lllll1_opy_(os.getenv(bstack111l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠣ౷"), bstack111l1l_opy_ (u"ࠢࠣ౸"))),
      bstack111l1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ౹"): bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ౺"),
      bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫ౻"): bstack11111l1l_opy_,
      bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ౼"): bstack11l111l11_opy_,
      bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠫ౽"): os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ౾")],
      bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ౿"): bstack1l1l1l111l_opy_(os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪಀ"), bstack1lllll1ll1_opy_)),
      bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬಁ"): config[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ಂ")] if config[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧಃ")] else bstack111l1l_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ಄"),
      bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨಅ"): str(config[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩಆ")]) if bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪಇ") in config else bstack111l1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥಈ"),
      bstack111l1l_opy_ (u"ࠪࡳࡸ࠭ಉ"): sys.platform,
      bstack111l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ಊ"): socket.gethostname(),
      bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧಋ"): bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨಌ"))
    }
  }
  if not bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ಍")) is None:
    data[bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫಎ")][bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬಏ")] = {
      bstack111l1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪಐ"): bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ಑"),
      bstack111l1l_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬಒ"): bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ಓ")),
      bstack111l1l_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭ಔ"): bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫಕ"))
    }
  if bstack11l1ll11l_opy_ == bstack1l1111ll_opy_:
    data[bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬಖ")][bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨಗ")] = bstack1l11111l1_opy_(config)
    data[bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧಘ")][bstack111l1l_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪಙ")] = percy.bstack111l1l11_opy_
    data[bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩಚ")][bstack111l1l_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ࠭ಛ")] = percy.bstack1ll1111l11_opy_
  update(data[bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫಜ")], bstack1llll1ll_opy_)
  try:
    response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧಝ"), bstack1ll11l111l_opy_(bstack1l11lllll_opy_), data, {
      bstack111l1l_opy_ (u"ࠪࡥࡺࡺࡨࠨಞ"): (config[bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ಟ")], config[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨಠ")])
    })
    if response:
      logger.debug(bstack1l11ll11l_opy_.format(bstack11l1ll11l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l1ll1l111_opy_.format(str(e)))
def bstack11lllll1_opy_(framework):
  return bstack111l1l_opy_ (u"ࠨࡻࡾ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥಡ").format(str(framework), __version__) if framework else bstack111l1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣಢ").format(
    __version__)
def bstack1l1lllll1l_opy_():
  global CONFIG
  global bstack111ll1l1l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1llll1l1l1_opy_()
    logger.debug(bstack1l1l1l1ll_opy_.format(str(CONFIG)))
    bstack111ll1l1l_opy_ = bstack1llll11lll_opy_.bstack1l11111l_opy_(CONFIG, bstack111ll1l1l_opy_)
    bstack1l111l111_opy_()
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧಣ") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l1l11l111_opy_
  atexit.register(bstack11ll1l1l_opy_)
  signal.signal(signal.SIGINT, bstack11ll11111_opy_)
  signal.signal(signal.SIGTERM, bstack11ll11111_opy_)
def bstack1l1l11l111_opy_(exctype, value, traceback):
  global bstack11ll11l1_opy_
  try:
    for driver in bstack11ll11l1_opy_:
      bstack1llll1llll_opy_(driver, bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩತ"), bstack111l1l_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨಥ") + str(value))
  except Exception:
    pass
  bstack1l111l11ll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l111l11ll_opy_(message=bstack111l1l_opy_ (u"ࠫࠬದ"), bstack11ll1l1l1_opy_ = False):
  global CONFIG
  bstack111l1ll1_opy_ = bstack111l1l_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠧಧ") if bstack11ll1l1l1_opy_ else bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬನ")
  try:
    if message:
      bstack1llll1ll_opy_ = {
        bstack111l1ll1_opy_ : str(message)
      }
      bstack1l1111ll1_opy_(bstack1l1111ll_opy_, CONFIG, bstack1llll1ll_opy_)
    else:
      bstack1l1111ll1_opy_(bstack1l1111ll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11lll1llll_opy_.format(str(e)))
def bstack1lll111l1_opy_(bstack1ll1ll111l_opy_, size):
  bstack11llll11ll_opy_ = []
  while len(bstack1ll1ll111l_opy_) > size:
    bstack1111lll11_opy_ = bstack1ll1ll111l_opy_[:size]
    bstack11llll11ll_opy_.append(bstack1111lll11_opy_)
    bstack1ll1ll111l_opy_ = bstack1ll1ll111l_opy_[size:]
  bstack11llll11ll_opy_.append(bstack1ll1ll111l_opy_)
  return bstack11llll11ll_opy_
def bstack1l11l111l_opy_(args):
  if bstack111l1l_opy_ (u"ࠧ࠮࡯ࠪ಩") in args and bstack111l1l_opy_ (u"ࠨࡲࡧࡦࠬಪ") in args:
    return True
  return False
def run_on_browserstack(bstack1l11l111l1_opy_=None, bstack11ll1ll1_opy_=None, bstack111l11ll_opy_=False):
  global CONFIG
  global bstack1l1ll11l11_opy_
  global bstack1l111l11l_opy_
  global bstack1lllll1ll1_opy_
  global bstack1l1ll111_opy_
  bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠩࠪಫ")
  bstack1l111ll111_opy_(bstack11ll1l11l_opy_, logger)
  if bstack1l11l111l1_opy_ and isinstance(bstack1l11l111l1_opy_, str):
    bstack1l11l111l1_opy_ = eval(bstack1l11l111l1_opy_)
  if bstack1l11l111l1_opy_:
    CONFIG = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪಬ")]
    bstack1l1ll11l11_opy_ = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬಭ")]
    bstack1l111l11l_opy_ = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧಮ")]
    bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨಯ"), bstack1l111l11l_opy_)
    bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧರ")
  bstack1l1ll111_opy_.bstack1l1l1111l_opy_(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪಱ"), uuid4().__str__())
  logger.debug(bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࡁࠬಲ") + bstack1l1ll111_opy_.get_property(bstack111l1l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬಳ")))
  if not bstack111l11ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll1ll1l1l_opy_)
      return
    if sys.argv[1] == bstack111l1l_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧ಴") or sys.argv[1] == bstack111l1l_opy_ (u"ࠬ࠳ࡶࠨವ"):
      logger.info(bstack111l1l_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭ಶ").format(__version__))
      return
    if sys.argv[1] == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ಷ"):
      bstack11l11ll11_opy_()
      return
  args = sys.argv
  bstack1l1lllll1l_opy_()
  global bstack111l11l1l_opy_
  global bstack11llll1111_opy_
  global bstack1lll11l1_opy_
  global bstack11l111l1l_opy_
  global bstack1l1l1llll1_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1ll1l1l111_opy_
  global bstack1l1ll1l1l_opy_
  global bstack11l1111l_opy_
  global bstack1ll1111lll_opy_
  global bstack111l111l1_opy_
  bstack11llll1111_opy_ = len(CONFIG.get(bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಸ"), []))
  if not bstack11111llll_opy_:
    if args[1] == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩಹ") or args[1] == bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ಺"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ಻")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ಼ࠫ"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಽ")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ಾ"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧಿ")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪೀ"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫು")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫೂ"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬೃ")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ೄ"):
      bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ೅")
      args = args[2:]
    else:
      if not bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫೆ") in CONFIG or str(CONFIG[bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬೇ")]).lower() in [bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪೈ"), bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ೉")]:
        bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬೊ")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩೋ")]).lower() == bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ೌ"):
        bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ್ࠧ")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ೎")]).lower() == bstack111l1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ೏"):
        bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ೐")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ೑")]).lower() == bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭೒"):
        bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ೓")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ೔")]).lower() == bstack111l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩೕ"):
        bstack11111llll_opy_ = bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪೖ")
        args = args[1:]
      else:
        os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭೗")] = bstack11111llll_opy_
        bstack111lll1l_opy_(bstack1lll1ll11l_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭೘")] = bstack11111llll_opy_
  bstack1lllll1ll1_opy_ = bstack11111llll_opy_
  global bstack1ll1l1ll11_opy_
  global bstack111ll1l1_opy_
  if bstack1l11l111l1_opy_:
    try:
      os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ೙")] = bstack11111llll_opy_
      bstack1l1111ll1_opy_(bstack1ll11111l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1lll1ll11_opy_.format(str(e)))
  global bstack1lll1llll_opy_
  global bstack1ll11l1111_opy_
  global bstack1l1ll1llll_opy_
  global bstack1lll1l1l1l_opy_
  global bstack11ll1ll11_opy_
  global bstack11l11l1l1_opy_
  global bstack1l1llllll_opy_
  global bstack1lll1l1ll_opy_
  global bstack1ll1ll11l_opy_
  global bstack11llll1l11_opy_
  global bstack1ll1lll1l_opy_
  global bstack1l1ll11ll1_opy_
  global bstack11llll1ll_opy_
  global bstack1lll1111ll_opy_
  global bstack1ll11l1l_opy_
  global bstack1lllll1l1l_opy_
  global bstack11l1ll1ll_opy_
  global bstack1l1l1lll11_opy_
  global bstack11ll11ll_opy_
  global bstack1l1l1ll1_opy_
  global bstack1l111l11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lll1llll_opy_ = webdriver.Remote.__init__
    bstack1ll11l1111_opy_ = WebDriver.quit
    bstack1l1ll11ll1_opy_ = WebDriver.close
    bstack1ll11l1l_opy_ = WebDriver.get
    bstack1l111l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll1l1ll11_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1l1l1ll111_opy_
    bstack111ll1l1_opy_ = bstack1l1l1ll111_opy_()
  except Exception as e:
    pass
  try:
    global bstack111l1l1ll_opy_
    from QWeb.keywords import browser
    bstack111l1l1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11l1l1l1l_opy_(CONFIG) and bstack1ll11l111_opy_():
    if bstack1111ll1l_opy_() < version.parse(bstack1111l111l_opy_):
      logger.error(bstack1lll1lllll_opy_.format(bstack1111ll1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lllll1l1l_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l11l1ll1_opy_.format(str(e)))
  if not CONFIG.get(bstack111l1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ೚"), False) and not bstack1l11l111l1_opy_:
    logger.info(bstack1l1lll111_opy_)
  if bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೛") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭೜")]).lower() != bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೝ"):
    bstack1llll1111_opy_()
  elif bstack11111llll_opy_ != bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫೞ") or (bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ೟") and not bstack1l11l111l1_opy_):
    bstack1ll1l111l_opy_()
  if (bstack11111llll_opy_ in [bstack111l1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬೠ"), bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ೡ"), bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩೢ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll1l1111l_opy_
        bstack11l11l1l1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l11l1l1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11ll1ll11_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll1l1ll_opy_ + str(e))
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1l1ll_opy_)
    if bstack11111llll_opy_ != bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪೣ"):
      bstack1lll111ll1_opy_()
    bstack1l1ll1llll_opy_ = Output.start_test
    bstack1lll1l1l1l_opy_ = Output.end_test
    bstack1l1llllll_opy_ = TestStatus.__init__
    bstack1ll1ll11l_opy_ = pabot._run
    bstack11llll1l11_opy_ = QueueItem.__init__
    bstack1ll1lll1l_opy_ = pabot._create_command_for_execution
    bstack11ll11ll_opy_ = pabot._report_results
  if bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ೤"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1lll_opy_)
    bstack11llll1ll_opy_ = Runner.run_hook
    bstack1lll1111ll_opy_ = Step.run
  if bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ೥"):
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
      logger.debug(bstack111l1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭೦"))
  try:
    framework_name = bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ೧") if bstack11111llll_opy_ in [bstack111l1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭೨"), bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ೩"), bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ೪")] else bstack1lll11ll1_opy_(bstack11111llll_opy_)
    bstack1111lll1_opy_ = {
      bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫ೫"): bstack111l1l_opy_ (u"ࠫࢀ࠶ࡽ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪ೬").format(framework_name) if bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ೭") and bstack11llll1l_opy_() else framework_name,
      bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ೮"): bstack1l1l1l111l_opy_(framework_name),
      bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ೯"): __version__,
      bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ೰"): bstack11111llll_opy_
    }
    if bstack11111llll_opy_ in bstack1ll1l1ll1_opy_:
      if bstack1l1l1ll11_opy_ and bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩೱ") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪೲ")] == True:
        if bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫೳ") in CONFIG:
          os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭೴")] = os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ೵"), json.dumps(CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ೶")]))
          CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ೷")].pop(bstack111l1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ೸"), None)
          CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ೹")].pop(bstack111l1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ೺"), None)
        bstack1111lll1_opy_[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ೻")] = {
          bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೼"): bstack111l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ೽"),
          bstack111l1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ೾"): str(bstack1111ll1l_opy_())
        }
    if bstack11111llll_opy_ not in [bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ೿")]:
      bstack11l1l111_opy_ = bstack1l1l1ll1l_opy_.launch(CONFIG, bstack1111lll1_opy_)
  except Exception as e:
    logger.debug(bstack1l11l1ll11_opy_.format(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡉࡷࡥࠫഀ"), str(e)))
  if bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫഁ"):
    bstack1lll11l1_opy_ = True
    if bstack1l11l111l1_opy_ and bstack111l11ll_opy_:
      bstack1l1ll1l1l1_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩം"), {}).get(bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨഃ"))
      bstack1ll111l11l_opy_(bstack1l11lll11_opy_)
    elif bstack1l11l111l1_opy_:
      bstack1l1ll1l1l1_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫഄ"), {}).get(bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪഅ"))
      global bstack11ll11l1_opy_
      try:
        if bstack1l11l111l_opy_(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬആ")]) and multiprocessing.current_process().name == bstack111l1l_opy_ (u"ࠪ࠴ࠬഇ"):
          bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧഈ")].remove(bstack111l1l_opy_ (u"ࠬ࠳࡭ࠨഉ"))
          bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩഊ")].remove(bstack111l1l_opy_ (u"ࠧࡱࡦࡥࠫഋ"))
          bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫഌ")] = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ഍")][0]
          with open(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭എ")], bstack111l1l_opy_ (u"ࠫࡷ࠭ഏ")) as f:
            bstack1l11lllll1_opy_ = f.read()
          bstack1l111l111l_opy_ = bstack111l1l_opy_ (u"ࠧࠨࠢࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡪ࡫ࠡ࡫ࡰࡴࡴࡸࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨ࠿ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࠩࡽࢀ࠭ࡀࠦࡦࡳࡱࡰࠤࡵࡪࡢࠡ࡫ࡰࡴࡴࡸࡴࠡࡒࡧࡦࡀࠦ࡯ࡨࡡࡧࡦࠥࡃࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࡴࡨࡥࡰࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨࡪ࡬ࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠫࡷࡪࡲࡦ࠭ࠢࡤࡶ࡬࠲ࠠࡵࡧࡰࡴࡴࡸࡡࡳࡻࠣࡁࠥ࠶ࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡴࡼ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡧࡲࡨࠢࡀࠤࡸࡺࡲࠩ࡫ࡱࡸ࠭ࡧࡲࡨࠫ࠮࠵࠵࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫ࡸࡤࡧࡳࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡣࡶࠤࡪࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡶࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡳ࡬ࡥࡤࡣࠪࡶࡩࡱ࡬ࠬࡢࡴࡪ࠰ࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࠦ࠽ࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࡴࡨࡥࡰࠦ࠽ࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥࠬ࠮࠴ࡳࡦࡶࡢࡸࡷࡧࡣࡦࠪࠬࡠࡳࠨࠢࠣഐ").format(str(bstack1l11l111l1_opy_))
          bstack1llllll1l1_opy_ = bstack1l111l111l_opy_ + bstack1l11lllll1_opy_
          bstack1l1l1l11l_opy_ = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ഑")] + bstack111l1l_opy_ (u"ࠧࡠࡤࡶࡸࡦࡩ࡫ࡠࡶࡨࡱࡵ࠴ࡰࡺࠩഒ")
          with open(bstack1l1l1l11l_opy_, bstack111l1l_opy_ (u"ࠨࡹࠪഓ")):
            pass
          with open(bstack1l1l1l11l_opy_, bstack111l1l_opy_ (u"ࠤࡺ࠯ࠧഔ")) as f:
            f.write(bstack1llllll1l1_opy_)
          import subprocess
          bstack1llll11l1_opy_ = subprocess.run([bstack111l1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥക"), bstack1l1l1l11l_opy_])
          if os.path.exists(bstack1l1l1l11l_opy_):
            os.unlink(bstack1l1l1l11l_opy_)
          os._exit(bstack1llll11l1_opy_.returncode)
        else:
          if bstack1l11l111l_opy_(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧഖ")]):
            bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨഗ")].remove(bstack111l1l_opy_ (u"࠭࠭࡮ࠩഘ"))
            bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪങ")].remove(bstack111l1l_opy_ (u"ࠨࡲࡧࡦࠬച"))
            bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬഛ")] = bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ജ")][0]
          bstack1ll111l11l_opy_(bstack1l11lll11_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧഝ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111l1l_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧഞ")] = bstack111l1l_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨട")
          mod_globals[bstack111l1l_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩഠ")] = os.path.abspath(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫഡ")])
          exec(open(bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬഢ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111l1l_opy_ (u"ࠪࡇࡦࡻࡧࡩࡶࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠪണ").format(str(e)))
          for driver in bstack11ll11l1_opy_:
            bstack11ll1ll1_opy_.append({
              bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩത"): bstack1l11l111l1_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨഥ")],
              bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬദ"): str(e),
              bstack111l1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ധ"): multiprocessing.current_process().name
            })
            bstack1llll1llll_opy_(driver, bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨന"), bstack111l1l_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧഩ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11ll11l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l111l11l_opy_, CONFIG, logger)
      bstack1l11l111_opy_()
      bstack111ll1ll_opy_()
      bstack1ll11llll1_opy_ = {
        bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭പ"): args[0],
        bstack111l1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫഫ"): CONFIG,
        bstack111l1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭ബ"): bstack1l1ll11l11_opy_,
        bstack111l1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨഭ"): bstack1l111l11l_opy_
      }
      percy.bstack1111l1l1l_opy_()
      if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪമ") in CONFIG:
        bstack1ll11l1ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lll1l11l1_opy_ = manager.list()
        if bstack1l11l111l_opy_(args):
          for index, platform in enumerate(CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫയ")]):
            if index == 0:
              bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬര")] = args
            bstack1ll11l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1ll11llll1_opy_, bstack1lll1l11l1_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭റ")]):
            bstack1ll11l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1ll11llll1_opy_, bstack1lll1l11l1_opy_)))
        for t in bstack1ll11l1ll_opy_:
          t.start()
        for t in bstack1ll11l1ll_opy_:
          t.join()
        bstack1l1ll1l1l_opy_ = list(bstack1lll1l11l1_opy_)
      else:
        if bstack1l11l111l_opy_(args):
          bstack1ll11llll1_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧല")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1ll11llll1_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll111l11l_opy_(bstack1l11lll11_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111l1l_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧള")] = bstack111l1l_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨഴ")
          mod_globals[bstack111l1l_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩവ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧശ") or bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨഷ"):
    percy.init(bstack1l111l11l_opy_, CONFIG, logger)
    percy.bstack1111l1l1l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1l1ll_opy_)
    bstack1l11l111_opy_()
    bstack1ll111l11l_opy_(bstack11l1l1111_opy_)
    if bstack1l1l1ll11_opy_:
      bstack1l1ll11l1l_opy_(bstack11l1l1111_opy_, args)
      if bstack111l1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨസ") in args:
        i = args.index(bstack111l1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩഹ"))
        args.pop(i)
        args.pop(i)
      if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨഺ") not in CONFIG:
        CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ഻ࠩ")] = [{}]
        bstack11llll1111_opy_ = 1
      if bstack111l11l1l_opy_ == 0:
        bstack111l11l1l_opy_ = 1
      args.insert(0, str(bstack111l11l1l_opy_))
      args.insert(0, str(bstack111l1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷ഼ࠬ")))
    if bstack1l1l1ll1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l1ll1ll11_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l1l11llll_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack111l1l_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣഽ"),
        ).parse_args(bstack1l1ll1ll11_opy_)
        bstack11lll11l_opy_ = args.index(bstack1l1ll1ll11_opy_[0]) if len(bstack1l1ll1ll11_opy_) > 0 else len(args)
        args.insert(bstack11lll11l_opy_, str(bstack111l1l_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭ാ")))
        args.insert(bstack11lll11l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧി"))))
        if bstack11ll111l_opy_(os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩീ"))) and str(os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩു"), bstack111l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫൂ"))) != bstack111l1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬൃ"):
          for bstack1l11111l1l_opy_ in bstack1l1l11llll_opy_:
            args.remove(bstack1l11111l1l_opy_)
          bstack111l11ll1_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬൄ")).split(bstack111l1l_opy_ (u"ࠩ࠯ࠫ൅"))
          for bstack1ll1l1llll_opy_ in bstack111l11ll1_opy_:
            args.append(bstack1ll1l1llll_opy_)
      except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡷࡸࡦࡩࡨࡪࡰࡪࠤࡱ࡯ࡳࡵࡧࡱࡩࡷࠦࡦࡰࡴࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࠨെ").format(e))
    pabot.main(args)
  elif bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬേ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1l1ll_opy_)
    for a in args:
      if bstack111l1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫൈ") in a:
        bstack1l1l1llll1_opy_ = int(a.split(bstack111l1l_opy_ (u"࠭࠺ࠨ൉"))[1])
      if bstack111l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫൊ") in a:
        bstack1l1ll1l1l1_opy_ = str(a.split(bstack111l1l_opy_ (u"ࠨ࠼ࠪോ"))[1])
      if bstack111l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩൌ") in a:
        bstack1ll1l1l111_opy_ = str(a.split(bstack111l1l_opy_ (u"ࠪ࠾്ࠬ"))[1])
    bstack1lll1l11ll_opy_ = None
    if bstack111l1l_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪൎ") in args:
      i = args.index(bstack111l1l_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ൏"))
      args.pop(i)
      bstack1lll1l11ll_opy_ = args.pop(i)
    if bstack1lll1l11ll_opy_ is not None:
      global bstack1l1l1l11ll_opy_
      bstack1l1l1l11ll_opy_ = bstack1lll1l11ll_opy_
    bstack1ll111l11l_opy_(bstack11l1l1111_opy_)
    run_cli(args)
    if bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ൐") in multiprocessing.current_process().__dict__.keys():
      for bstack1lllll1111_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11ll1ll1_opy_.append(bstack1lllll1111_opy_)
  elif bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ൑"):
    percy.init(bstack1l111l11l_opy_, CONFIG, logger)
    percy.bstack1111l1l1l_opy_()
    bstack1l1l11l1l1_opy_ = bstack1llll1ll1l_opy_(args, logger, CONFIG, bstack1l1l1ll11_opy_)
    bstack1l1l11l1l1_opy_.bstack1l1ll111ll_opy_()
    bstack1l11l111_opy_()
    bstack11l111l1l_opy_ = True
    bstack1ll1111lll_opy_ = bstack1l1l11l1l1_opy_.bstack1l1111l1l_opy_()
    bstack1l1l11l1l1_opy_.bstack1ll11llll1_opy_(bstack1l1111ll11_opy_)
    bstack11llll1l1_opy_ = bstack1l1l11l1l1_opy_.bstack1ll1ll11l1_opy_(bstack1ll11l1l11_opy_, {
      bstack111l1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ൒"): bstack1l1ll11l11_opy_,
      bstack111l1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ൓"): bstack1l111l11l_opy_,
      bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ൔ"): bstack1l1l1ll11_opy_
    })
    try:
      bstack1l1llll1l1_opy_, bstack1lll11l11_opy_ = map(list, zip(*bstack11llll1l1_opy_))
      bstack11l1111l_opy_ = bstack1l1llll1l1_opy_[0]
      for status_code in bstack1lll11l11_opy_:
        if status_code != 0:
          bstack111l111l1_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥ࡫ࡲࡳࡱࡵࡷࠥࡧ࡮ࡥࠢࡶࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠮ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠿ࠦࡻࡾࠤൕ").format(str(e)))
  elif bstack11111llll_opy_ == bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬൖ"):
    try:
      from behave.__main__ import main as bstack111lll111_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11llll111_opy_(e, bstack1l11l1lll_opy_)
    bstack1l11l111_opy_()
    bstack11l111l1l_opy_ = True
    bstack11l1lll1l_opy_ = 1
    if bstack111l1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ൗ") in CONFIG:
      bstack11l1lll1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ൘")]
    if bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൙") in CONFIG:
      bstack1ll1ll11_opy_ = int(bstack11l1lll1l_opy_) * int(len(CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൚")]))
    else:
      bstack1ll1ll11_opy_ = int(bstack11l1lll1l_opy_)
    config = Configuration(args)
    bstack1l1ll1lll1_opy_ = config.paths
    if len(bstack1l1ll1lll1_opy_) == 0:
      import glob
      pattern = bstack111l1l_opy_ (u"ࠪ࠮࠯࠵ࠪ࠯ࡨࡨࡥࡹࡻࡲࡦࠩ൛")
      bstack1ll111ll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1ll111ll1_opy_)
      config = Configuration(args)
      bstack1l1ll1lll1_opy_ = config.paths
    bstack1lll11ll1l_opy_ = [os.path.normpath(item) for item in bstack1l1ll1lll1_opy_]
    bstack1l11111ll1_opy_ = [os.path.normpath(item) for item in args]
    bstack1l11l1111_opy_ = [item for item in bstack1l11111ll1_opy_ if item not in bstack1lll11ll1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack111l1l_opy_ (u"ࠫࡼ࡯࡮ࡥࡱࡺࡷࠬ൜"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lll11ll1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l111l11l1_opy_)))
                    for bstack1l111l11l1_opy_ in bstack1lll11ll1l_opy_]
    bstack1ll1111ll1_opy_ = []
    for spec in bstack1lll11ll1l_opy_:
      bstack1l1l1l1l1_opy_ = []
      bstack1l1l1l1l1_opy_ += bstack1l11l1111_opy_
      bstack1l1l1l1l1_opy_.append(spec)
      bstack1ll1111ll1_opy_.append(bstack1l1l1l1l1_opy_)
    execution_items = []
    for bstack1l1l1l1l1_opy_ in bstack1ll1111ll1_opy_:
      if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൝") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൞")]):
          item = {}
          item[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࠫൟ")] = bstack111l1l_opy_ (u"ࠨࠢࠪൠ").join(bstack1l1l1l1l1_opy_)
          item[bstack111l1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨൡ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࠧൢ")] = bstack111l1l_opy_ (u"ࠫࠥ࠭ൣ").join(bstack1l1l1l1l1_opy_)
        item[bstack111l1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ൤")] = 0
        execution_items.append(item)
    bstack11ll11l1l_opy_ = bstack1lll111l1_opy_(execution_items, bstack1ll1ll11_opy_)
    for execution_item in bstack11ll11l1l_opy_:
      bstack1ll11l1ll_opy_ = []
      for item in execution_item:
        bstack1ll11l1ll_opy_.append(bstack1ll111lll_opy_(name=str(item[bstack111l1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ൥")]),
                                             target=bstack1l1llll1l_opy_,
                                             args=(item[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࠫ൦")],)))
      for t in bstack1ll11l1ll_opy_:
        t.start()
      for t in bstack1ll11l1ll_opy_:
        t.join()
  else:
    bstack111lll1l_opy_(bstack1lll1ll11l_opy_)
  if not bstack1l11l111l1_opy_:
    bstack1ll1l1111_opy_()
  bstack1llll11lll_opy_.bstack1l1lllll11_opy_()
def browserstack_initialize(bstack11llllll11_opy_=None):
  run_on_browserstack(bstack11llllll11_opy_, None, True)
def bstack1ll1l1111_opy_():
  global CONFIG
  global bstack1lllll1ll1_opy_
  global bstack111l111l1_opy_
  global bstack1ll1111ll_opy_
  global bstack1l1ll111_opy_
  bstack1l1l1ll1l_opy_.stop()
  bstack1111lll1l_opy_.bstack1llll1l11l_opy_()
  if bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ൧") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭൨")]).lower() != bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ൩"):
    bstack1llllllll1_opy_, bstack1l11ll1ll_opy_ = bstack11ll11lll_opy_()
  else:
    bstack1llllllll1_opy_, bstack1l11ll1ll_opy_ = get_build_link()
  if bstack1llllllll1_opy_ is not None and bstack1ll111l1l1_opy_() != -1:
    sessions = bstack1l1l1llll_opy_(bstack1llllllll1_opy_)
    bstack11l11lll_opy_(sessions, bstack1l11ll1ll_opy_)
  if bstack1lllll1ll1_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ൪") and bstack111l111l1_opy_ != 0:
    sys.exit(bstack111l111l1_opy_)
  if bstack1lllll1ll1_opy_ == bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ൫") and bstack1ll1111ll_opy_ != 0:
    sys.exit(bstack1ll1111ll_opy_)
def bstack1lll11ll1_opy_(bstack1ll1l111_opy_):
  if bstack1ll1l111_opy_:
    return bstack1ll1l111_opy_.capitalize()
  else:
    return bstack111l1l_opy_ (u"࠭ࠧ൬")
def bstack1ll11ll11_opy_(bstack11lllll11l_opy_):
  if bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ൭") in bstack11lllll11l_opy_ and bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭൮")] != bstack111l1l_opy_ (u"ࠩࠪ൯"):
    return bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ൰")]
  else:
    bstack11ll11l11_opy_ = bstack111l1l_opy_ (u"ࠦࠧ൱")
    if bstack111l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ൲") in bstack11lllll11l_opy_ and bstack11lllll11l_opy_[bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭൳")] != None:
      bstack11ll11l11_opy_ += bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ൴")] + bstack111l1l_opy_ (u"ࠣ࠮ࠣࠦ൵")
      if bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠩࡲࡷࠬ൶")] == bstack111l1l_opy_ (u"ࠥ࡭ࡴࡹࠢ൷"):
        bstack11ll11l11_opy_ += bstack111l1l_opy_ (u"ࠦ࡮ࡕࡓࠡࠤ൸")
      bstack11ll11l11_opy_ += (bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ൹")] or bstack111l1l_opy_ (u"࠭ࠧൺ"))
      return bstack11ll11l11_opy_
    else:
      bstack11ll11l11_opy_ += bstack1lll11ll1_opy_(bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨൻ")]) + bstack111l1l_opy_ (u"ࠣࠢࠥർ") + (
              bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫൽ")] or bstack111l1l_opy_ (u"ࠪࠫൾ")) + bstack111l1l_opy_ (u"ࠦ࠱ࠦࠢൿ")
      if bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠬࡵࡳࠨ඀")] == bstack111l1l_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢඁ"):
        bstack11ll11l11_opy_ += bstack111l1l_opy_ (u"ࠢࡘ࡫ࡱࠤࠧං")
      bstack11ll11l11_opy_ += bstack11lllll11l_opy_[bstack111l1l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬඃ")] or bstack111l1l_opy_ (u"ࠩࠪ඄")
      return bstack11ll11l11_opy_
def bstack1llll1ll1_opy_(bstack1l11l11l1_opy_):
  if bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠥࡨࡴࡴࡥࠣඅ"):
    return bstack111l1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧආ")
  elif bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧඇ"):
    return bstack111l1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩඈ")
  elif bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢඉ"):
    return bstack111l1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨඊ")
  elif bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣඋ"):
    return bstack111l1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬඌ")
  elif bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧඍ"):
    return bstack111l1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪඎ")
  elif bstack1l11l11l1_opy_ == bstack111l1l_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢඏ"):
    return bstack111l1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨඐ")
  else:
    return bstack111l1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬඑ") + bstack1lll11ll1_opy_(
      bstack1l11l11l1_opy_) + bstack111l1l_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨඒ")
def bstack1111ll11l_opy_(session):
  return bstack111l1l_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪඓ").format(
    session[bstack111l1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨඔ")], bstack1ll11ll11_opy_(session), bstack1llll1ll1_opy_(session[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫඕ")]),
    bstack1llll1ll1_opy_(session[bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ඖ")]),
    bstack1lll11ll1_opy_(session[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ඗")] or session[bstack111l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ඘")] or bstack111l1l_opy_ (u"ࠩࠪ඙")) + bstack111l1l_opy_ (u"ࠥࠤࠧක") + (session[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ඛ")] or bstack111l1l_opy_ (u"ࠬ࠭ග")),
    session[bstack111l1l_opy_ (u"࠭࡯ࡴࠩඝ")] + bstack111l1l_opy_ (u"ࠢࠡࠤඞ") + session[bstack111l1l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬඟ")], session[bstack111l1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫච")] or bstack111l1l_opy_ (u"ࠪࠫඡ"),
    session[bstack111l1l_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨජ")] if session[bstack111l1l_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩඣ")] else bstack111l1l_opy_ (u"࠭ࠧඤ"))
def bstack11l11lll_opy_(sessions, bstack1l11ll1ll_opy_):
  try:
    bstack1lll1111l_opy_ = bstack111l1l_opy_ (u"ࠢࠣඥ")
    if not os.path.exists(bstack111l111l_opy_):
      os.mkdir(bstack111l111l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1l_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭ඦ")), bstack111l1l_opy_ (u"ࠩࡵࠫට")) as f:
      bstack1lll1111l_opy_ = f.read()
    bstack1lll1111l_opy_ = bstack1lll1111l_opy_.replace(bstack111l1l_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧඨ"), str(len(sessions)))
    bstack1lll1111l_opy_ = bstack1lll1111l_opy_.replace(bstack111l1l_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫඩ"), bstack1l11ll1ll_opy_)
    bstack1lll1111l_opy_ = bstack1lll1111l_opy_.replace(bstack111l1l_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭ඪ"),
                                              sessions[0].get(bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪණ")) if sessions[0] else bstack111l1l_opy_ (u"ࠧࠨඬ"))
    with open(os.path.join(bstack111l111l_opy_, bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬත")), bstack111l1l_opy_ (u"ࠩࡺࠫථ")) as stream:
      stream.write(bstack1lll1111l_opy_.split(bstack111l1l_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧද"))[0])
      for session in sessions:
        stream.write(bstack1111ll11l_opy_(session))
      stream.write(bstack1lll1111l_opy_.split(bstack111l1l_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨධ"))[1])
    logger.info(bstack111l1l_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨන").format(bstack111l111l_opy_));
  except Exception as e:
    logger.debug(bstack11l1l1lll_opy_.format(str(e)))
def bstack1l1l1llll_opy_(bstack1llllllll1_opy_):
  global CONFIG
  try:
    host = bstack111l1l_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩ඲") if bstack111l1l_opy_ (u"ࠧࡢࡲࡳࠫඳ") in CONFIG else bstack111l1l_opy_ (u"ࠨࡣࡳ࡭ࠬප")
    user = CONFIG[bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫඵ")]
    key = CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭බ")]
    bstack11111l11_opy_ = bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪභ") if bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩම") in CONFIG else bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨඹ")
    url = bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬය").format(user, key, host, bstack11111l11_opy_,
                                                                                bstack1llllllll1_opy_)
    headers = {
      bstack111l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧර"): bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ඼"),
    }
    proxies = bstack11l11ll1l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨල")], response.json()))
  except Exception as e:
    logger.debug(bstack11lllll11_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack1lll1lll1l_opy_
  try:
    if bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ඾") in CONFIG:
      host = bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨ඿") if bstack111l1l_opy_ (u"࠭ࡡࡱࡲࠪව") in CONFIG else bstack111l1l_opy_ (u"ࠧࡢࡲ࡬ࠫශ")
      user = CONFIG[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪෂ")]
      key = CONFIG[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬස")]
      bstack11111l11_opy_ = bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩහ") if bstack111l1l_opy_ (u"ࠫࡦࡶࡰࠨළ") in CONFIG else bstack111l1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧෆ")
      url = bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭෇").format(user, key, host, bstack11111l11_opy_)
      headers = {
        bstack111l1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭෈"): bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ෉"),
      }
      if bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ්ࠫ") in CONFIG:
        params = {bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ෋"): CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ෌")], bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ෍"): CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ෎")]}
      else:
        params = {bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬා"): CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫැ")]}
      proxies = bstack11l11ll1l_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1lll111111_opy_ = response.json()[0][bstack111l1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬෑ")]
        if bstack1lll111111_opy_:
          bstack1l11ll1ll_opy_ = bstack1lll111111_opy_[bstack111l1l_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧි")].split(bstack111l1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪී"))[0] + bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ු") + bstack1lll111111_opy_[
            bstack111l1l_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ෕")]
          logger.info(bstack1l1l1l1l_opy_.format(bstack1l11ll1ll_opy_))
          bstack1lll1lll1l_opy_ = bstack1lll111111_opy_[bstack111l1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪූ")]
          bstack1l1l111lll_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ෗")]
          if bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫෘ") in CONFIG:
            bstack1l1l111lll_opy_ += bstack111l1l_opy_ (u"ࠪࠤࠬෙ") + CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ේ")]
          if bstack1l1l111lll_opy_ != bstack1lll111111_opy_[bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪෛ")]:
            logger.debug(bstack1l11llll1l_opy_.format(bstack1lll111111_opy_[bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫො")], bstack1l1l111lll_opy_))
          return [bstack1lll111111_opy_[bstack111l1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪෝ")], bstack1l11ll1ll_opy_]
    else:
      logger.warn(bstack1l11lll1_opy_)
  except Exception as e:
    logger.debug(bstack1ll11111ll_opy_.format(str(e)))
  return [None, None]
def bstack1111l111_opy_(url, bstack1lll11l1ll_opy_=False):
  global CONFIG
  global bstack1lllllll11_opy_
  if not bstack1lllllll11_opy_:
    hostname = bstack111ll11l1_opy_(url)
    is_private = bstack1l1ll1ll_opy_(hostname)
    if (bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬෞ") in CONFIG and not bstack11ll111l_opy_(CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ෟ")])) and (is_private or bstack1lll11l1ll_opy_):
      bstack1lllllll11_opy_ = hostname
def bstack111ll11l1_opy_(url):
  return urlparse(url).hostname
def bstack1l1ll1ll_opy_(hostname):
  for bstack1ll1l1l1ll_opy_ in bstack1l1llll11l_opy_:
    regex = re.compile(bstack1ll1l1l1ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1ll11ll111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1l1llll1_opy_
  bstack1l1l11111l_opy_ = not (bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ෠"), None) and bstack1ll111l11_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ෡"), None))
  bstack1ll11ll1l_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ෢"), None) != True
  if not bstack1l1l1lll_opy_.bstack11lll1l1ll_opy_(CONFIG, bstack1l1l1llll1_opy_) or (bstack1ll11ll1l_opy_ and bstack1l1l11111l_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤ෣"))
    return {}
  try:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫ෤"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1lllll1lll_opy_.bstack111111ll_opy_)
    return results
  except Exception:
    logger.error(bstack111l1l_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥ෥"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1l1llll1_opy_
  bstack1l1l11111l_opy_ = not (bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭෦"), None) and bstack1ll111l11_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ෧"), None))
  bstack1ll11ll1l_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ෨"), None) != True
  if not bstack1l1l1lll_opy_.bstack11lll1l1ll_opy_(CONFIG, bstack1l1l1llll1_opy_) or (bstack1ll11ll1l_opy_ and bstack1l1l11111l_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤ෩"))
    return {}
  try:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫ෪"))
    logger.debug(perform_scan(driver))
    bstack1l1ll111l1_opy_ = driver.execute_async_script(bstack1lllll1lll_opy_.bstack11l11l11_opy_)
    return bstack1l1ll111l1_opy_
  except Exception:
    logger.error(bstack111l1l_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣ෫"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1l1llll1_opy_
  bstack1l1l11111l_opy_ = not (bstack1ll111l11_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ෬"), None) and bstack1ll111l11_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ෭"), None))
  bstack1ll11ll1l_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ෮"), None) != True
  if not bstack1l1l1lll_opy_.bstack11lll1l1ll_opy_(CONFIG, bstack1l1l1llll1_opy_) or (bstack1ll11ll1l_opy_ and bstack1l1l11111l_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨ෯"))
    return {}
  try:
    bstack11lll1l1_opy_ = driver.execute_async_script(bstack1lllll1lll_opy_.perform_scan, {bstack111l1l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ෰"): kwargs.get(bstack111l1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧ෱"), None) or bstack111l1l_opy_ (u"ࠧࠨෲ")})
    return bstack11lll1l1_opy_
  except Exception:
    logger.error(bstack111l1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢෳ"))
    return {}