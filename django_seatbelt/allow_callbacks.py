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


def allow_usr_lib(path):
    """
    White-list helper that allows anything installed in /usr/lib/
    """
    return path.startswith("/usr/lib/")


DEFAULT_ALLOW_CALLBACKS = [allow_usr_lib]
