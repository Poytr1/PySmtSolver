#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/05/2018 10:16 PM
# @Author  : Pancras

from .constant import TY


class SMTVar(object):

    def __init__(self, type_, internal, id_, sat_var, width, val=None, e=None):
        if type_ == TY.TY_BOOL:
            self.width = 1
        elif type_ == TY.TY_BITVEC:
            self.width = width
        else:
            raise Exception
        self.type_ = type_
        self.internal = internal
        self.id_ = id_
        self.sat_var = sat_var
        self.val = val
        self.e = e


