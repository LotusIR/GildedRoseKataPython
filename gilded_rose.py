# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality, conjured=False):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.degrade_rate = 1
        if conjured:
            self.degrade_rate = 2

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class NormalItem(Item):
    def __init__(self, sell_in, quality, conjured=False):
        super().__init__("Item", sell_in, quality, conjured)

    def update_quality(self):
        if self.quality > 0:
            self.quality -= self.degrade_rate
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= self.degrade_rate

class AgedBrie(Item):
    def __init__(self, sell_in, quality, conjured=False):
        super().__init__("Aged Brie", sell_in, quality, conjured)

    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1

class Sulfuras(Item):
    def __init__(self, sell_in, quality, conjured=False):
        super().__init__("Sulfuras", sell_in, quality, conjured)

    def update_quality(self):
        pass

class BackstagePass(Item):
    def __init__(self, sell_in, quality, conjured=False):
        super().__init__("Backstage pass", sell_in, quality, conjured)
        
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality += 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
    
    def sell(self, itemType: type, amount: int):
        for item in self.items:
            if isinstance(item, itemType):
                self.items.remove(item)
                amount -= 1
            if amount == 0:
                break
    
    def get_items(self)->list[str]:
        return [item.name for item in self.items]
