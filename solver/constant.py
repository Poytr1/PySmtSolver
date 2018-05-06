#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/05/2018 10:04 PM
# @Author  : Pancras

from enum import Enum, auto


class ClauseType(Enum):
    HARD_CLAUSE = auto(),
    SOFT_CLAUSE = auto(),
    COMMENT = auto()


class ExprType(Enum):
    EXPR_ID = auto(),
    EXPR_UNARY = auto(),
    EXPR_BINARY = auto(),
    EXPR_TERNARY = auto(),
    EXPR_CONST = auto(),
    EXPR_ZERO_EXTEND = auto(),
    EXPR_REPEAT = auto(),
    EXPR_EXTRACT = auto()


class TY(Enum):
    TY_BOOL = auto(),
    TY_BITVEC = auto()


class OP(Enum):
    OP_NOT = 0,
    OP_BVSHL = 1,
    OP_BVLSHR = 2,
    OP_BVASHR = 3,
    OP_BVSHL1 = 4,
    OP_BVSHR1 = 5,
    OP_EQ = 6,
    OP_NEQ = 7,
    OP_AND = 8,
    OP_OR = 9,
    OP_XOR = 10,
    OP_BVNOT = 11,
    OP_BVNEG = 12,
    OP_BVXOR = 13,
    OP_BVADD = 14,
    OP_BVAND = 15,
    OP_BVOR = 16,
    OP_BVMUL = 17,
    OP_BVMUL_NO_OVERFLOW = 18,
    OP_BVSUB = 19,
    OP_BVUGE = 20,
    OP_BVUGT = 21,
    OP_BVULE = 22,
    OP_BVULT = 23,
    OP_BVSGE = 24,
    OP_BVSGT = 25,
    OP_BVSLE = 26,
    OP_BVSLT = 27,
    OP_BVSUBGE = 28,
    OP_BVUDIV = 29,
    OP_BVUREM = 30,
    OP_ITE = 31

