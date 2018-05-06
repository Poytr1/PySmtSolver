#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/05/2018 10:24 PM
# @Author  : Pancras


class Expr(object):

    def __init__(self, node_type, type_):
        self.node_type = node_type
        self.type_ = type_