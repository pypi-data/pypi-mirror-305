# --------------------------------------------------------------------------------------
# Copyright (c) 2013-2024, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# --------------------------------------------------------------------------------------
# This file is auto-generated by setuptools-scm do NOT edit it.

from collections import namedtuple

#: A namedtuple of the version info for the current release.
_version_info = namedtuple("_version_info", "major minor micro status")

parts = "0.18.0".split(".", 3)
version_info = _version_info(
    int(parts[0]),
    int(parts[1]),
    int(parts[2]),
    parts[3] if len(parts) == 4 else "",
)

# Remove everything but the 'version_info' from this module.
del namedtuple, _version_info, parts

__version__ = "0.18.0"
