#! /usr/bin/env python
#-*- encoding:utf-8 -*-

""" some utilities """

class Printer(object):
    """ some customized terminal output methods """

    RED_COLOR = '\033[1;31m'
    GREEN_COLOR = '\033[1;32m'
    YELLOW_COLOR = '\033[1;33m'
    BLUE_COLOR = '\033[1;34m'
    END_COLOR = '\033[0m'
    BOLD_COLOR = '\033[1m'
    UNDERLINE_COLOR = '\033[4m'

    @staticmethod
    def red(msg):
        """ output by red """
        print "%s%s%s" % (Printer.RED_COLOR, str(msg), Printer.END_COLOR)

    @staticmethod
    def green(msg):
        """ output by green """
        print "%s%s%s" % (Printer.GREEN_COLOR, str(msg), Printer.END_COLOR)

    @staticmethod
    def yellow(msg):
        """ output by yellow """
        print "%s%s%s" % (Printer.YELLOW_COLOR, str(msg), Printer.END_COLOR)

    @staticmethod
    def blue(msg):
        """ output by blue """
        print "%s%s%s" % (Printer.BLUE_COLOR, str(msg), Printer.END_COLOR)

    @staticmethod
    def bold(msg):
        """ output by bold font """
        print "%s%s%s" % (Printer.BLUE_COLOR, str(msg), Printer.END_COLOR)
