# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Sulfuras(5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Sulfuras(5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # tests whether normal items's quality degrades correcly after sellin day
    def test_twice_quality_degrades(self):
        items = [NormalItem(1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() # quality 10->9
        gilded_rose.update_quality() # quality 9->7
        normal_item = items[0]
        self.assertEqual(normal_item.quality, 7)

    # tests whether backstage pass's quality is correctly updated before sellin
    def test_backstage_pass_quality_before_sellin(self):
        items = [BackstagePass(1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)

    # tests whether backstage pass's quality is correctly updated after sellin
    def test_backstage_pass_quality_after_sellin(self):
        items = [BackstagePass(1, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    # tests giled_rose sell function
    def test_gilded_rose_sell_item(self):
        items = [NormalItem("A", 1, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.sell(NormalItem, 1)
        self.assertEqual(len(items), 0)


if __name__ == '__main__':
    unittest.main()
