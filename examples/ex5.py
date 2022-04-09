#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib


path = pathlib.PureWindowsPath(r'C:\Users\gahjelle\realpython\file.txt')
print(path.name)
print(path.parent)
print(path.exists())
