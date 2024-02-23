from enum import Enum
from typing import Optional

class ItemStatus(Enum):
  ON_SALE = "ON_SALE"
  SOLD_OUT ="SOLD_OUT"

class Item:
  def __init__(
    self,
    id: int,
    name: str,
    price: int,
    description: Optional[str],
    status: ItemStatus
  ):
    self.id = id
    self.name = name
    self.price = price
    self.description = description
    self.status = status

items = [
  Item(1, "PC", 100000, "備品です", ItemStatus.ON_SALE),
  Item(2, "スマートフォン", 50000, None, ItemStatus.ON_SALE),
  Item(3, "Python本", 1000, "使用感あり", ItemStatus.SOLD_OUT)
]

def find_all():
  return items