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
import json
class bstack111l1lllll_opy_(object):
  bstack111l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬဉ")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫည"))
  bstack111l1llll1_opy_ = os.path.join(bstack111l1l1l1_opy_, bstack111l1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹ࠮࡫ࡵࡲࡲࠬဋ"))
  bstack111l1lll11_opy_ = None
  perform_scan = None
  bstack111111ll_opy_ = None
  bstack11l11l11_opy_ = None
  bstack111ll1lll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack111l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡥࡳࡩࡥࠨဌ")):
      cls.instance = super(bstack111l1lllll_opy_, cls).__new__(cls)
      cls.instance.bstack111l1ll1ll_opy_()
    return cls.instance
  def bstack111l1ll1ll_opy_(self):
    try:
      with open(self.bstack111l1llll1_opy_, bstack111l1l_opy_ (u"ࠧࡳࠩဍ")) as bstack1llll11l1l_opy_:
        bstack111ll11111_opy_ = bstack1llll11l1l_opy_.read()
        data = json.loads(bstack111ll11111_opy_)
        if bstack111l1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪဎ") in data:
          self.bstack111ll11l11_opy_(data[bstack111l1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫဏ")])
        if bstack111l1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫတ") in data:
          self.bstack111ll1l111_opy_(data[bstack111l1l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬထ")])
    except:
      pass
  def bstack111ll1l111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࠪဒ")]
      self.bstack111111ll_opy_ = scripts[bstack111l1l_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪဓ")]
      self.bstack11l11l11_opy_ = scripts[bstack111l1l_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫန")]
      self.bstack111ll1lll1_opy_ = scripts[bstack111l1l_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ပ")]
  def bstack111ll11l11_opy_(self, bstack111l1lll11_opy_):
    if bstack111l1lll11_opy_ != None and len(bstack111l1lll11_opy_) != 0:
      self.bstack111l1lll11_opy_ = bstack111l1lll11_opy_
  def store(self):
    try:
      with open(self.bstack111l1llll1_opy_, bstack111l1l_opy_ (u"ࠩࡺࠫဖ")) as file:
        json.dump({
          bstack111l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࠧဗ"): self.bstack111l1lll11_opy_,
          bstack111l1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࡷࠧဘ"): {
            bstack111l1l_opy_ (u"ࠧࡹࡣࡢࡰࠥမ"): self.perform_scan,
            bstack111l1l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥယ"): self.bstack111111ll_opy_,
            bstack111l1l_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦရ"): self.bstack11l11l11_opy_,
            bstack111l1l_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨလ"): self.bstack111ll1lll1_opy_
          }
        }, file)
    except:
      pass
  def bstack11l1l111l_opy_(self, bstack111l1lll1l_opy_):
    try:
      return any(command.get(bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧဝ")) == bstack111l1lll1l_opy_ for command in self.bstack111l1lll11_opy_)
    except:
      return False
bstack1lllll1lll_opy_ = bstack111l1lllll_opy_()