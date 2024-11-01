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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack111l11l1ll_opy_, bstack111l1l1111_opy_
import tempfile
import json
bstack1llll1ll111_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬᔃ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack111l1l_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩᔄ"),
      datefmt=bstack111l1l_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧᔅ"),
      stream=sys.stdout
    )
  return logger
def bstack1llll1l1l11_opy_():
  global bstack1llll1ll111_opy_
  if os.path.exists(bstack1llll1ll111_opy_):
    os.remove(bstack1llll1ll111_opy_)
def bstack1l1lllll11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l11111l_opy_(config, log_level):
  bstack1llll1l1lll_opy_ = log_level
  if bstack111l1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᔆ") in config and config[bstack111l1l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᔇ")] in bstack111l11l1ll_opy_:
    bstack1llll1l1lll_opy_ = bstack111l11l1ll_opy_[config[bstack111l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᔈ")]]
  if config.get(bstack111l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᔉ"), False):
    logging.getLogger().setLevel(bstack1llll1l1lll_opy_)
    return bstack1llll1l1lll_opy_
  global bstack1llll1ll111_opy_
  bstack1l1lllll11_opy_()
  bstack1llll1l1l1l_opy_ = logging.Formatter(
    fmt=bstack111l1l_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨᔊ"),
    datefmt=bstack111l1l_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ᔋ")
  )
  bstack1llll1ll1l1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1llll1ll111_opy_)
  file_handler.setFormatter(bstack1llll1l1l1l_opy_)
  bstack1llll1ll1l1_opy_.setFormatter(bstack1llll1l1l1l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1llll1ll1l1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack111l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧᔌ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1llll1ll1l1_opy_.setLevel(bstack1llll1l1lll_opy_)
  logging.getLogger().addHandler(bstack1llll1ll1l1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1llll1l1lll_opy_
def bstack1llll1lll11_opy_(config):
  try:
    bstack1llll1l11ll_opy_ = set(bstack111l1l1111_opy_)
    bstack1llll1l11l1_opy_ = bstack111l1l_opy_ (u"࠭ࠧᔍ")
    with open(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪᔎ")) as bstack1llll1l111l_opy_:
      bstack1llll1ll1ll_opy_ = bstack1llll1l111l_opy_.read()
      bstack1llll1l11l1_opy_ = re.sub(bstack111l1l_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩᔏ"), bstack111l1l_opy_ (u"ࠩࠪᔐ"), bstack1llll1ll1ll_opy_, flags=re.M)
      bstack1llll1l11l1_opy_ = re.sub(
        bstack111l1l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭ᔑ") + bstack111l1l_opy_ (u"ࠫࢁ࠭ᔒ").join(bstack1llll1l11ll_opy_) + bstack111l1l_opy_ (u"ࠬ࠯࠮ࠫࠦࠪᔓ"),
        bstack111l1l_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨᔔ"),
        bstack1llll1l11l1_opy_, flags=re.M | re.I
      )
    def bstack1llll1l1ll1_opy_(dic):
      bstack1llll1l1111_opy_ = {}
      for key, value in dic.items():
        if key in bstack1llll1l11ll_opy_:
          bstack1llll1l1111_opy_[key] = bstack111l1l_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫᔕ")
        else:
          if isinstance(value, dict):
            bstack1llll1l1111_opy_[key] = bstack1llll1l1ll1_opy_(value)
          else:
            bstack1llll1l1111_opy_[key] = value
      return bstack1llll1l1111_opy_
    bstack1llll1l1111_opy_ = bstack1llll1l1ll1_opy_(config)
    return {
      bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫᔖ"): bstack1llll1l11l1_opy_,
      bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᔗ"): json.dumps(bstack1llll1l1111_opy_)
    }
  except Exception as e:
    return {}
def bstack1lllllllll_opy_(config):
  global bstack1llll1ll111_opy_
  try:
    if config.get(bstack111l1l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬᔘ"), False):
      return
    uuid = os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᔙ"))
    if not uuid or uuid == bstack111l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᔚ"):
      return
    bstack1llll1ll11l_opy_ = [bstack111l1l_opy_ (u"࠭ࡲࡦࡳࡸ࡭ࡷ࡫࡭ࡦࡰࡷࡷ࠳ࡺࡸࡵࠩᔛ"), bstack111l1l_opy_ (u"ࠧࡑ࡫ࡳࡪ࡮ࡲࡥࠨᔜ"), bstack111l1l_opy_ (u"ࠨࡲࡼࡴࡷࡵࡪࡦࡥࡷ࠲ࡹࡵ࡭࡭ࠩᔝ"), bstack1llll1ll111_opy_]
    bstack1l1lllll11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯࡯ࡳ࡬ࡹ࠭ࠨᔞ") + uuid + bstack111l1l_opy_ (u"ࠪ࠲ࡹࡧࡲ࠯ࡩࡽࠫᔟ"))
    with tarfile.open(output_file, bstack111l1l_opy_ (u"ࠦࡼࡀࡧࡻࠤᔠ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1llll1ll11l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1llll1lll11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1llll11llll_opy_ = data.encode()
        tarinfo.size = len(bstack1llll11llll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1llll11llll_opy_))
    bstack11lllll111_opy_ = MultipartEncoder(
      fields= {
        bstack111l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪᔡ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack111l1l_opy_ (u"࠭ࡲࡣࠩᔢ")), bstack111l1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡨࡼ࡬ࡴࠬᔣ")),
        bstack111l1l_opy_ (u"ࠨࡥ࡯࡭ࡪࡴࡴࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᔤ"): uuid
      }
    )
    response = requests.post(
      bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡹࡵࡲ࡯ࡢࡦ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦᔥ"),
      data=bstack11lllll111_opy_,
      headers={bstack111l1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᔦ"): bstack11lllll111_opy_.content_type},
      auth=(config[bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᔧ")], config[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᔨ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬᔩ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack111l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭ᔪ") + str(e))
  finally:
    try:
      bstack1llll1l1l11_opy_()
    except:
      pass