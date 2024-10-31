#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author  : Hu Ji
@file    : setup.py
@time    : 2018/11/25
@site    :
@software: PyCharm

              ,----------------,              ,---------,
         ,-----------------------,          ,"        ,"|
       ,"                      ,"|        ,"        ,"  |
      +-----------------------+  |      ,"        ,"    |
      |  .-----------------.  |  |     +---------+      |
      |  |                 |  |  |     | -==----'|      |
      |  | $ sudo rm -rf / |  |  |     |         |      |
      |  |                 |  |  |/----|`---=    |      |
      |  |                 |  |  |   ,/|==== ooo |      ;
      |  |                 |  |  |  // |(((( [33]|    ,"
      |  `-----------------'  |," .;'| |((((     |  ,"
      +-----------------------+  ;;  | |         |,"
         /_)______________(_/  //'   | +---------+
    ___________________________/___  `,
   /  oooooooooooooooo  .o.  oooo /,   `,"-----------
  / ==ooooooooooooooo==.o.  ooo= //   ,``--{)B     ,"
 /_==__==========__==_ooo__ooo=_/'   /___________,"
"""
import os

import yaml
from setuptools import setup


def get_root_path(*paths):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)


def get_src_path(*paths):
    return get_root_path("src", "linktools-cntr", *paths)


if __name__ == '__main__':

    release = os.environ.get("RELEASE", "false").lower() == "true"
    version = os.environ.get("VERSION", "0.0.1.dev0")
    if version.startswith("v"):
        version = version[len("v"):]

    with open(get_root_path("requirements.yml"), "rt", encoding="utf-8") as fd:
        data = yaml.safe_load(fd)
        # install_requires = dependencies + dev-dependencies
        install_requires = data.get("dependencies")
        install_requires.extend(data.get("release-dependencies") if release else data.get("dev-dependencies"))
        # extras_require = optional-dependencies
        extras_require = data.get("optional-dependencies")
        all_requires = []
        for requires in extras_require.values():
            all_requires.extend(requires)
        extras_require["all"] = all_requires

    setup(
        version=version,
        install_requires=install_requires,
        extras_require=extras_require,
        entry_points={
            "console_scripts": ["ct-cntr = linktools_cntr.__main__:command.main"],
            "linktools_scripts": ["ct-cntr = linktools_cntr.__main__:command.main"],
        },
    )
