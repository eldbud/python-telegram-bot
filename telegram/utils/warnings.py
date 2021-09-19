#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2021
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains a class which is used for deprecation warnings."""
import warnings
from typing import Type


class PTBUserWarning(UserWarning):
    """
    Custom user warning class used for warnings in this library.

    .. versionadded:: 14.0
    """

    __slots__ = ()


class PTBRuntimeWarning(PTBUserWarning, RuntimeWarning):
    """
    Custom runtime warning class used for warnings in this library.
    """

    __slots__ = ()


# https://www.python.org/dev/peps/pep-0565/ recommends to use a custom warning class derived from
# DeprecationWarning. We also subclass from TGUserWarning so users can easily 'switch off' warnings
class PTBDeprecationWarning(PTBUserWarning, DeprecationWarning):
    """Custom warning class for deprecations in this library."""

    __slots__ = ()


def warn(message: str, category: Type[Warning] = PTBUserWarning, stacklevel: int = 1) -> None:
    """Helper function used as a shortcut for warning with default values."""
    warnings.warn(message, category=category, stacklevel=stacklevel)
