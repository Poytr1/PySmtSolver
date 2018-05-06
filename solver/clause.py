#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/05/2018 10:13 PM
# @Author  : Pancras


class Clause(object):

    def __init__(self, type_, s=None, weight=None):
        self.type_ = type_
        self.s = s
        self.weight = weight
        self.li = []

    def add_vars(self, v: list):
        if len(v) <= 4:
            self.li.extend(v)

