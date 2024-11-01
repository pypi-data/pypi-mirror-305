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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1ll11l111l_opy_, bstack1ll1ll111_opy_
class bstack1l1l1l1ll1_opy_:
  working_dir = os.getcwd()
  bstack1l11ll11_opy_ = False
  config = {}
  binary_path = bstack111l1l_opy_ (u"ࠩࠪᕲ")
  bstack1llll111ll1_opy_ = bstack111l1l_opy_ (u"ࠪࠫᕳ")
  bstack1ll11ll1ll_opy_ = False
  bstack1lll1ll11l1_opy_ = None
  bstack1lll1lll1l1_opy_ = {}
  bstack1lll1ll1ll1_opy_ = 300
  bstack1lll1l1lll1_opy_ = False
  logger = None
  bstack1lll11lll1l_opy_ = False
  bstack111l1l11_opy_ = False
  bstack1ll1111l11_opy_ = None
  bstack1lll11llll1_opy_ = bstack111l1l_opy_ (u"ࠫࠬᕴ")
  bstack1lll11ll1ll_opy_ = {
    bstack111l1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᕵ") : 1,
    bstack111l1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧᕶ") : 2,
    bstack111l1l_opy_ (u"ࠧࡦࡦࡪࡩࠬᕷ") : 3,
    bstack111l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᕸ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lll1l11111_opy_(self):
    bstack1lll1lll111_opy_ = bstack111l1l_opy_ (u"ࠩࠪᕹ")
    bstack1lll1l11l1l_opy_ = sys.platform
    bstack1lll1l1l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᕺ")
    if re.match(bstack111l1l_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦᕻ"), bstack1lll1l11l1l_opy_) != None:
      bstack1lll1lll111_opy_ = bstack111l11l111_opy_ + bstack111l1l_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨᕼ")
      self.bstack1lll11llll1_opy_ = bstack111l1l_opy_ (u"࠭࡭ࡢࡥࠪᕽ")
    elif re.match(bstack111l1l_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧᕾ"), bstack1lll1l11l1l_opy_) != None:
      bstack1lll1lll111_opy_ = bstack111l11l111_opy_ + bstack111l1l_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤᕿ")
      bstack1lll1l1l1l1_opy_ = bstack111l1l_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧᖀ")
      self.bstack1lll11llll1_opy_ = bstack111l1l_opy_ (u"ࠪࡻ࡮ࡴࠧᖁ")
    else:
      bstack1lll1lll111_opy_ = bstack111l11l111_opy_ + bstack111l1l_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢᖂ")
      self.bstack1lll11llll1_opy_ = bstack111l1l_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫᖃ")
    return bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_
  def bstack1lll1lllll1_opy_(self):
    try:
      bstack1llll111l11_opy_ = [os.path.join(expanduser(bstack111l1l_opy_ (u"ࠨࡾࠣᖄ")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᖅ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llll111l11_opy_:
        if(self.bstack1lll1ll1l11_opy_(path)):
          return path
      raise bstack111l1l_opy_ (u"ࠣࡗࡱࡥࡱࡨࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᖆ")
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦᖇ").format(e))
  def bstack1lll1ll1l11_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lll1l11ll1_opy_(self, bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_):
    try:
      bstack1lll1lll1ll_opy_ = self.bstack1lll1lllll1_opy_()
      bstack1llll111lll_opy_ = os.path.join(bstack1lll1lll1ll_opy_, bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ᖈ"))
      bstack1lll11ll11l_opy_ = os.path.join(bstack1lll1lll1ll_opy_, bstack1lll1l1l1l1_opy_)
      if os.path.exists(bstack1lll11ll11l_opy_):
        self.logger.info(bstack111l1l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᖉ").format(bstack1lll11ll11l_opy_))
        return bstack1lll11ll11l_opy_
      if os.path.exists(bstack1llll111lll_opy_):
        self.logger.info(bstack111l1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥᖊ").format(bstack1llll111lll_opy_))
        return self.bstack1lll1l1llll_opy_(bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_)
      self.logger.info(bstack111l1l_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦᖋ").format(bstack1lll1lll111_opy_))
      response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠧࡈࡇࡗࠫᖌ"), bstack1lll1lll111_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1llll111lll_opy_, bstack111l1l_opy_ (u"ࠨࡹࡥࠫᖍ")) as file:
          file.write(response.content)
        self.logger.info(bstack111l1l_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢᖎ").format(bstack1llll111lll_opy_))
        return self.bstack1lll1l1llll_opy_(bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_)
      else:
        raise(bstack111l1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨᖏ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᖐ").format(e))
  def bstack1llll11l111_opy_(self, bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_):
    try:
      retry = 2
      bstack1lll11ll11l_opy_ = None
      bstack1lll11l1lll_opy_ = False
      while retry > 0:
        bstack1lll11ll11l_opy_ = self.bstack1lll1l11ll1_opy_(bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_)
        bstack1lll11l1lll_opy_ = self.bstack1lll1l1ll1l_opy_(bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_, bstack1lll11ll11l_opy_)
        if bstack1lll11l1lll_opy_:
          break
        retry -= 1
      return bstack1lll11ll11l_opy_, bstack1lll11l1lll_opy_
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᖑ").format(e))
    return bstack1lll11ll11l_opy_, False
  def bstack1lll1l1ll1l_opy_(self, bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_, bstack1lll11ll11l_opy_, bstack1llll111111_opy_ = 0):
    if bstack1llll111111_opy_ > 1:
      return False
    if bstack1lll11ll11l_opy_ == None or os.path.exists(bstack1lll11ll11l_opy_) == False:
      self.logger.warn(bstack111l1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᖒ"))
      return False
    bstack1lll1l11lll_opy_ = bstack111l1l_opy_ (u"ࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࡟࠳ࡨࡲࡩࠡ࡞ࡧ࠲ࡡࡪࠫ࠯࡞ࡧ࠯ࠧᖓ")
    command = bstack111l1l_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᖔ").format(bstack1lll11ll11l_opy_)
    bstack1lll1ll11ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lll1l11lll_opy_, bstack1lll1ll11ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack111l1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᖕ"))
      return False
  def bstack1lll1l1llll_opy_(self, bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_):
    try:
      working_dir = os.path.dirname(bstack1llll111lll_opy_)
      shutil.unpack_archive(bstack1llll111lll_opy_, working_dir)
      bstack1lll11ll11l_opy_ = os.path.join(working_dir, bstack1lll1l1l1l1_opy_)
      os.chmod(bstack1lll11ll11l_opy_, 0o755)
      return bstack1lll11ll11l_opy_
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᖖ"))
  def bstack1lll1l1ll11_opy_(self):
    try:
      bstack1lll1ll111l_opy_ = self.config.get(bstack111l1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᖗ"))
      bstack1lll1l1ll11_opy_ = bstack1lll1ll111l_opy_ or (bstack1lll1ll111l_opy_ is None and self.bstack1l11ll11_opy_)
      if not bstack1lll1l1ll11_opy_ or self.config.get(bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᖘ"), None) not in bstack111l11ll1l_opy_:
        return False
      self.bstack1ll11ll1ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᖙ").format(e))
  def bstack1llll11l11l_opy_(self):
    try:
      bstack1llll11l11l_opy_ = self.bstack1lll1l1l11l_opy_
      return bstack1llll11l11l_opy_
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺࠢࡦࡥࡵࡺࡵࡳࡧࠣࡱࡴࡪࡥ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᖚ").format(e))
  def init(self, bstack1l11ll11_opy_, config, logger):
    self.bstack1l11ll11_opy_ = bstack1l11ll11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lll1l1ll11_opy_():
      return
    self.bstack1lll1lll1l1_opy_ = config.get(bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᖛ"), {})
    self.bstack1lll1l1l11l_opy_ = config.get(bstack111l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᖜ"))
    try:
      bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_ = self.bstack1lll1l11111_opy_()
      bstack1lll11ll11l_opy_, bstack1lll11l1lll_opy_ = self.bstack1llll11l111_opy_(bstack1lll1lll111_opy_, bstack1lll1l1l1l1_opy_)
      if bstack1lll11l1lll_opy_:
        self.binary_path = bstack1lll11ll11l_opy_
        thread = Thread(target=self.bstack1lll1ll1lll_opy_)
        thread.start()
      else:
        self.bstack1lll11lll1l_opy_ = True
        self.logger.error(bstack111l1l_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡨࡲࡹࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡒࡨࡶࡨࡿࠢᖝ").format(bstack1lll11ll11l_opy_))
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᖞ").format(e))
  def bstack1llll11111l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111l1l_opy_ (u"ࠬࡲ࡯ࡨࠩᖟ"), bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࡲ࡯ࡨࠩᖠ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111l1l_opy_ (u"ࠢࡑࡷࡶ࡬࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࡷࠥࡧࡴࠡࡽࢀࠦᖡ").format(logfile))
      self.bstack1llll111ll1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࠤࡵࡧࡴࡩ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᖢ").format(e))
  def bstack1lll1ll1lll_opy_(self):
    bstack1lll1l1l111_opy_ = self.bstack1lll1ll1l1l_opy_()
    if bstack1lll1l1l111_opy_ == None:
      self.bstack1lll11lll1l_opy_ = True
      self.logger.error(bstack111l1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠧᖣ"))
      return False
    command_args = [bstack111l1l_opy_ (u"ࠥࡥࡵࡶ࠺ࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠦᖤ") if self.bstack1l11ll11_opy_ else bstack111l1l_opy_ (u"ࠫࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠨᖥ")]
    bstack1lll1l1111l_opy_ = self.bstack1lll11lllll_opy_()
    if bstack1lll1l1111l_opy_ != None:
      command_args.append(bstack111l1l_opy_ (u"ࠧ࠳ࡣࠡࡽࢀࠦᖦ").format(bstack1lll1l1111l_opy_))
    env = os.environ.copy()
    env[bstack111l1l_opy_ (u"ࠨࡐࡆࡔࡆ࡝ࡤ࡚ࡏࡌࡇࡑࠦᖧ")] = bstack1lll1l1l111_opy_
    env[bstack111l1l_opy_ (u"ࠢࡕࡊࡢࡆ࡚ࡏࡌࡅࡡࡘ࡙ࡎࡊࠢᖨ")] = os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᖩ"), bstack111l1l_opy_ (u"ࠩࠪᖪ"))
    bstack1lll1l1l1ll_opy_ = [self.binary_path]
    self.bstack1llll11111l_opy_()
    self.bstack1lll1ll11l1_opy_ = self.bstack1lll11ll1l1_opy_(bstack1lll1l1l1ll_opy_ + command_args, env)
    self.logger.debug(bstack111l1l_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦᖫ"))
    bstack1llll111111_opy_ = 0
    while self.bstack1lll1ll11l1_opy_.poll() == None:
      bstack1lll1ll1111_opy_ = self.bstack1lll1l111ll_opy_()
      if bstack1lll1ll1111_opy_:
        self.logger.debug(bstack111l1l_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢᖬ"))
        self.bstack1lll1l1lll1_opy_ = True
        return True
      bstack1llll111111_opy_ += 1
      self.logger.debug(bstack111l1l_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣᖭ").format(bstack1llll111111_opy_))
      time.sleep(2)
    self.logger.error(bstack111l1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦᖮ").format(bstack1llll111111_opy_))
    self.bstack1lll11lll1l_opy_ = True
    return False
  def bstack1lll1l111ll_opy_(self, bstack1llll111111_opy_ = 0):
    if bstack1llll111111_opy_ > 10:
      return False
    try:
      bstack1lll1llll11_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧᖯ"), bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩᖰ"))
      bstack1lll1llllll_opy_ = bstack1lll1llll11_opy_ + bstack111l11lll1_opy_
      response = requests.get(bstack1lll1llllll_opy_)
      data = response.json()
      self.bstack1ll1111l11_opy_ = data.get(bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨᖱ"), {}).get(bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ᖲ"), None)
      return True
    except:
      self.logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥࡽࡨࡪ࡮ࡨࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡪࡨࡥࡱࡺࡨࠡࡥ࡫ࡩࡨࡱࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤᖳ"))
      return False
  def bstack1lll1ll1l1l_opy_(self):
    bstack1lll11lll11_opy_ = bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩᖴ") if self.bstack1l11ll11_opy_ else bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᖵ")
    bstack1lll1l11l11_opy_ = bstack111l1l_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥᖶ") if self.config.get(bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᖷ")) is None else True
    bstack1111llll1l_opy_ = bstack111l1l_opy_ (u"ࠤࡤࡴ࡮࠵ࡡࡱࡲࡢࡴࡪࡸࡣࡺ࠱ࡪࡩࡹࡥࡰࡳࡱ࡭ࡩࡨࡺ࡟ࡵࡱ࡮ࡩࡳࡅ࡮ࡢ࡯ࡨࡁࢀࢃࠦࡵࡻࡳࡩࡂࢁࡽࠧࡲࡨࡶࡨࡿ࠽ࡼࡿࠥᖸ").format(self.config[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᖹ")], bstack1lll11lll11_opy_, bstack1lll1l11l11_opy_)
    if self.bstack1lll1l1l11l_opy_:
      bstack1111llll1l_opy_ += bstack111l1l_opy_ (u"ࠦࠫࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࡀࡿࢂࠨᖺ").format(self.bstack1lll1l1l11l_opy_)
    uri = bstack1ll11l111l_opy_(bstack1111llll1l_opy_)
    try:
      response = bstack1ll1ll111_opy_(bstack111l1l_opy_ (u"ࠬࡍࡅࡕࠩᖻ"), uri, {}, {bstack111l1l_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᖼ"): (self.config[bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᖽ")], self.config[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᖾ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1ll11ll1ll_opy_ = data.get(bstack111l1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪᖿ"))
        self.bstack1lll1l1l11l_opy_ = data.get(bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥࠨᗀ"))
        os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᗁ")] = str(self.bstack1ll11ll1ll_opy_)
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᗂ")] = str(self.bstack1lll1l1l11l_opy_)
        if bstack1lll1l11l11_opy_ == bstack111l1l_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤᗃ") and str(self.bstack1ll11ll1ll_opy_).lower() == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᗄ"):
          self.bstack111l1l11_opy_ = True
        if bstack111l1l_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢᗅ") in data:
          return data[bstack111l1l_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣᗆ")]
        else:
          raise bstack111l1l_opy_ (u"ࠪࡘࡴࡱࡥ࡯ࠢࡑࡳࡹࠦࡆࡰࡷࡱࡨࠥ࠳ࠠࡼࡿࠪᗇ").format(data)
      else:
        raise bstack111l1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡰࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡴࡶࡤࡸࡺࡹࠠ࠮ࠢࡾࢁ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡄࡲࡨࡾࠦ࠭ࠡࡽࢀࠦᗈ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡶࡲࡰ࡬ࡨࡧࡹࠨᗉ").format(e))
  def bstack1lll11lllll_opy_(self):
    bstack1lll11l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠨࡰࡦࡴࡦࡽࡈࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠤᗊ"))
    try:
      if bstack111l1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨᗋ") not in self.bstack1lll1lll1l1_opy_:
        self.bstack1lll1lll1l1_opy_[bstack111l1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᗌ")] = 2
      with open(bstack1lll11l1l1l_opy_, bstack111l1l_opy_ (u"ࠩࡺࠫᗍ")) as fp:
        json.dump(self.bstack1lll1lll1l1_opy_, fp)
      return bstack1lll11l1l1l_opy_
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡣࡳࡧࡤࡸࡪࠦࡰࡦࡴࡦࡽࠥࡩ࡯࡯ࡨ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᗎ").format(e))
  def bstack1lll11ll1l1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lll11llll1_opy_ == bstack111l1l_opy_ (u"ࠫࡼ࡯࡮ࠨᗏ"):
        bstack1lll1llll1l_opy_ = [bstack111l1l_opy_ (u"ࠬࡩ࡭ࡥ࠰ࡨࡼࡪ࠭ᗐ"), bstack111l1l_opy_ (u"࠭࠯ࡤࠩᗑ")]
        cmd = bstack1lll1llll1l_opy_ + cmd
      cmd = bstack111l1l_opy_ (u"ࠧࠡࠩᗒ").join(cmd)
      self.logger.debug(bstack111l1l_opy_ (u"ࠣࡔࡸࡲࡳ࡯࡮ࡨࠢࡾࢁࠧᗓ").format(cmd))
      with open(self.bstack1llll111ll1_opy_, bstack111l1l_opy_ (u"ࠤࡤࠦᗔ")) as bstack1lll11l1ll1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lll11l1ll1_opy_, text=True, stderr=bstack1lll11l1ll1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lll11lll1l_opy_ = True
      self.logger.error(bstack111l1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠤࡼ࡯ࡴࡩࠢࡦࡱࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧᗕ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lll1l1lll1_opy_:
        self.logger.info(bstack111l1l_opy_ (u"ࠦࡘࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡐࡦࡴࡦࡽࠧᗖ"))
        cmd = [self.binary_path, bstack111l1l_opy_ (u"ࠧ࡫ࡸࡦࡥ࠽ࡷࡹࡵࡰࠣᗗ")]
        self.bstack1lll11ll1l1_opy_(cmd)
        self.bstack1lll1l1lll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡴࡶࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᗘ").format(cmd, e))
  def bstack1111l1l1l_opy_(self):
    if not self.bstack1ll11ll1ll_opy_:
      return
    try:
      bstack1lll1l111l1_opy_ = 0
      while not self.bstack1lll1l1lll1_opy_ and bstack1lll1l111l1_opy_ < self.bstack1lll1ll1ll1_opy_:
        if self.bstack1lll11lll1l_opy_:
          self.logger.info(bstack111l1l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥ࡬ࡡࡪ࡮ࡨࡨࠧᗙ"))
          return
        time.sleep(1)
        bstack1lll1l111l1_opy_ += 1
      os.environ[bstack111l1l_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡃࡇࡖࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓࠧᗚ")] = str(self.bstack1llll111l1l_opy_())
      self.logger.info(bstack111l1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠥᗛ"))
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᗜ").format(e))
  def bstack1llll111l1l_opy_(self):
    if self.bstack1l11ll11_opy_:
      return
    try:
      bstack1llll1111l1_opy_ = [platform[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᗝ")].lower() for platform in self.config.get(bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᗞ"), [])]
      bstack1llll1111ll_opy_ = sys.maxsize
      bstack1lll11ll111_opy_ = bstack111l1l_opy_ (u"࠭ࠧᗟ")
      for browser in bstack1llll1111l1_opy_:
        if browser in self.bstack1lll11ll1ll_opy_:
          bstack1lll1lll11l_opy_ = self.bstack1lll11ll1ll_opy_[browser]
        if bstack1lll1lll11l_opy_ < bstack1llll1111ll_opy_:
          bstack1llll1111ll_opy_ = bstack1lll1lll11l_opy_
          bstack1lll11ll111_opy_ = browser
      return bstack1lll11ll111_opy_
    except Exception as e:
      self.logger.error(bstack111l1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡤࡨࡷࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᗠ").format(e))
  @classmethod
  def bstack11lll1l111_opy_(self):
    return os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᗡ"), bstack111l1l_opy_ (u"ࠩࡉࡥࡱࡹࡥࠨᗢ")).lower()
  @classmethod
  def bstack1l111lll1_opy_(self):
    return os.getenv(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᗣ"), bstack111l1l_opy_ (u"ࠫࠬᗤ"))