# !/usr/bin/python3
# coding: utf-8
# File:mytag.py
# 作者：Molip
# 时间：2021-1-10 12:08
# 说明：
from django import template

register = template.Library()


@register.filter('sub1')
def sub(value):
    return value - 1
