# Copyright (C) 2011 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of django-seatbelt.
#
# django-seatbelt is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# django-seatbelt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with django-seatbelt.  If not, see <http://www.gnu.org/licenses/>.

import contextlib
import sys


@contextlib.contextmanager
def fasten(allow_callbacks=None):
    """
    Fasten seatbelts for production.

    With this context manager sys.path will not contain any unwanted junk that
    users happily stick into /usr/local/ and other similar places just a moment
    before calling you to report your application is broken.
    """
    orig_sys_path = sys.path
    sys.path = _filtered_sys_path(allow_callbacks)
    try:
        yield
    finally:
        sys.path = orig_sys_path


def solder(allow_callbacks=None):
    """
    Solder seatbelts for production.

    Like fasten() but without the context manager. That is, the original
    sys.path is never restored. This is perfect for your .wsgi files.
    """
    sys.path = _filtered_sys_path(allow_callbacks)


def _filtered_sys_path(allow_callbacks=None):
    """
    Calculate how sys.path should look like as filtered by the provided
    white-list callbacks.

    :param allow_callbacks:
        List of white-list call-backs that check if a particular path entry is
        permitted or not. If left empty then default of
        :ref:`django_seatbelt.allow_callbacks:DEFAULT_ALLOW_CALLBACKS` is used

    :return:
        The new sys.path (the actual sys.path is not modified)
    """

    if allow_callbacks is None:
        from django_seatbelt.allow_callbacks import DEFAULT_ALLOW_CALLBACKS
        allow_callbacks = DEFAULT_ALLOW_CALLBACKS
    filtered_sys_path = []
    for path in sys.path:
        if any(is_allowed(path) for is_allowed in allow_callbacks):
            filtered_sys_path.append(path)
    return filtered_sys_path
