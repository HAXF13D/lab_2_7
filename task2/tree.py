#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from pathlib import *


@click.command()
@click.option(
    '--dir',
    default=Path.cwd(),
    help='Ввод директории',
    type=str
)
@click.option(
    '--dip',
    default=-1,
    help='Уровень вложенности для отображения в выводе',
    type=int
)
def display_tree(dir, dip):
    print(f"{dir}")
    for path in sorted(Path(dir).rglob('*')):
        depth = len(path.relative_to(dir).parts)
        if depth <= dip or dip == -1:
            spacer = '-' * depth
            print(f'|{spacer}{path.name}')


if __name__ == '__main__':
    display_tree()
