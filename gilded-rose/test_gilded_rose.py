# -*- coding: utf-8 -*-

from gilded_rose import GildedRose
from item import Item


def get_gilded_items(test_cases):
    items = [test_case[0] for test_case in test_cases]
    print('1: {}'.format(items))
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    print('2: {}'.format(items))
    return items


def validate(items, test_cases):
    for i, item in enumerate(items):
        assert items[i].name == test_cases[i][1].name
        assert items[i].sell_in == test_cases[i][1].sell_in
        assert items[i].quality == test_cases[i][1].quality


def test_normal():
    test_cases = [              # (before, after)
        (Item("+5 Dexterity Vest", 2, 4),
         Item("+5 Dexterity Vest", 1, 3)),
        (Item('+5 Dexterity Vest', 0, 0),
         Item('+5 Dexterity Vest', -1, 0)),
        (Item('+5 Dexterity Vest', 1, 0),
         Item('+5 Dexterity Vest', 0, 0)),
        (Item('+5 Dexterity Vest', 0, 1),
         Item('+5 Dexterity Vest', -1, 0)),
        (Item('+5 Dexterity Vest', 1, -1),
         Item('+5 Dexterity Vest', 0, -1)),  # VIOLATES SPEC, Q should be >= 0
        (Item('+5 Dexterity Vest', 1, 500),
         Item('+5 Dexterity Vest', 0, 499)),  # VIOLATES SPEC, Q should be <= 50
        (Item("ñoqui", 1, 42),     # test unicode, not part of spec, not TDD
         Item("ñoqui", 0, 41)),
    ]
    items = get_gilded_items(test_cases)
    validate(items, test_cases)
