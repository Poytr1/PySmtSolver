#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/05/2018 10:19 PM
# @Author  : Pancras

from .constant import TY, ClauseType
from .smtvar import SMTVar
from .clause import Clause


class Ctx(object):

    def __init__(self, vars_):
        self.vars_ = vars_
        self.sat_next_var_no = 1
        self.next_internal_var = 1
        self.clause_t = 0
        self.clauses = []
        self.max_weight = 0
        self.maxsat = False

    def find_var(self, id_: str):
        try:
            return next(v for v in self.vars_ if id_ == v.id_)
        except StopIteration:
            return None

    def get_var_val(self, id_: str):
        v = self.find_var(id_)
        if v:
            return v
        else:
            raise Exception('can\'t find variable %s' % id_)

    def declare_var(self, name: str, type_, width: int, internal: int):
        if type_ == TY.TY_BOOL:
            assert width == 1

        if not self.find_var(name):
            raise Exception('Fatal error: variable %s is already defined')

        v = SMTVar(
            type_=type_,
            id_=name,
            sat_var=self.sat_next_var_no,
            width=width,
            internal=internal)

        self.sat_next_var_no += v.width
        self.vars_.append(v)
        return v

    def create_internal_var(self, prefix, type_, width: int):
        v = self.declare_var(
            '%s!%d' %
            (prefix, self.next_internal_var), type_, width, 1)
        self.next_internal_var += 1
        return v

    def add_soft_clause1(self, weight, v1: int):
        self.clause_t += 1
        c = Clause(ClauseType.SOFT_CLAUSE, weight=weight)
        c.add_vars([v1])
        self.clauses.append(c)
        self.max_weight = max(self.max_weight, weight)
        self.maxsat = True

    def add_clause(self, v_list):
        self.clause_t += 1
        c = Clause(ClauseType.HARD_CLAUSE)
        c.add_vars(v_list)
        self.clauses.append(c)

    def add_comment(self, fmt: str):
        pass

    def dump_all_vars(self):
        pass

    def gen_const(self, val: int, width: int):
        rt = self.create_internal_var('internal', TY.TY_BITVEC, width)
        self.add_comment(
            'gen_const(val={}, width={}). SAT_var=[{}..{}]'.format(
                val, width, rt.sat_var, rt.sat_var + width - 1))
