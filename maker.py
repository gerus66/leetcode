#!/usr/bin/python3

import argparse
from enum import Enum
import os
from typing import List


class WrongName(Exception):
    pass


class TaskName:
    Level = Enum('Level', ['easy', 'medium', 'hard'])

    words: List
    level: Level

    def __init__(self, name, level):
        self.words = name.lower().split()
        self.words[0] = ''.join(sign for sign in self.words[0] if sign.isdigit())
        if not self.words[0]:
            raise WrongName(f'name of task should start with number')
        for e in self.Level:
            if e.name[0] == level:
                self.level = e
                return
        raise WrongName(f'level should be one of {[e.name for e in self.Level]}')

    def get_link(self) -> str:
        base = "https://leetcode.com/problems/"
        return base + '-'.join(self.words[1:])

    def get_file_path(self) -> str:
        return os.path.join(os.getcwd(), self.level.name, '_'.join(self.words) + '.py')

    def get_level(self) -> str:
        return self.level.name


def make_template(name: str, level: str, context: str):
    try:
        task_name = TaskName(name, level)
    except WrongName as ex:
        print(f'\033[91m-> Error: {ex}\033[0m')
        return

    buf = list()
    buf.append(f'# {task_name.get_link()}\n')
    buf.append(f'# {task_name.get_level()}\n')
    buf.append(f'# {context}\n')

    with open(task_name.get_file_path(), 'w+') as f:
        f.write(''.join(buf))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="maker",
        description="Make file by template"
    )
    parser.add_argument('name', help='name of task, should start with number')
    parser.add_argument('-l', '--level', choices=['e', 'm', 'h'], default='e',
                        help='level of task: [e]asy, [m]edium or [h]ard')
    parser.add_argument('-c', '--context', help='some context about task, for example: daily, contest N, etc.')
    args = parser.parse_args()
    make_template(args.name, args.level, args.context)
