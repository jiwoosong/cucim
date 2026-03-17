# SPDX-FileCopyrightText: Copyright (c) 2023, NVIDIA CORPORATION.
# SPDX-License-Identifier: Apache-2.0

import configparser

from setuptools import setup
from setuptools.dist import Distribution as _Distribution


# Python 3.12 removed configparser.SafeConfigParser.
# Keep an alias for legacy packaging helpers that may still import it during
# installation from source on Windows.
if not hasattr(configparser, "SafeConfigParser"):
    configparser.SafeConfigParser = configparser.ConfigParser


# As we vendored a shared object that links to a specific Python version,
# make sure it is treated as impure so the wheel is named properly.
class Distribution(_Distribution):
    def has_ext_modules(self):
        return True


setup(
    distclass=Distribution,
)
