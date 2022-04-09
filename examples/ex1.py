#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections
import pathlib


print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
