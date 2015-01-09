# coding: utf-8

from __future__ import absolute_import, division, print_function

from . import BaseBot


class Daniel(BaseBot):

    _NAME = "くらた"
    _ICON = ":penguin:"

    def echo(self):
        """オウム返しをする"""
        if self.msg.command != u"echo":
            return ""
        return " ".join(self.msg.args[2:])

    def yo(self):
        """YO"""
        if self.msg.command != "yo":
            return ""
        return "yo"

    def ohayo_guru(self):
        """オハヨーグルト"""
        if self.msg.command != "おはヨーグルト":
            return ""
        return "おはﾖｰｸﾞﾙﾄｫｵｵ!!"
    