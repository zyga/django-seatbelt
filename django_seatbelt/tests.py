
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

import sys

from testtools import TestCase

from django_seatbelt import seatbelt


class SeatbeltTests(TestCase):

    def test_fasten_restores_sys_path(self):
        orig_path = sys.path[:]
        with seatbelt.fasten():
            pass
        final_path = sys.path[:]
        self.assertEqual(orig_path, final_path)

    def test_fasten_filters_out_stuff(self):
        sys.path.append("foo")
        self.assertIn("foo", sys.path)
        with seatbelt.fasten([lambda path: path != "foo"]):
            self.assertNotIn("foo", sys.path)
        self.assertIn("foo", sys.path)

    def test_fasten_gets_rid_of_usr_local_by_default(self):
        sys.path.append("/usr/local/SEATBELT")
        with seatbelt.fasten([lambda path: path.__eq__("foo")]):
            self.assertNotIn("/usr/local/SEATBELT", sys.path)

    def test_solder_filters_stuff_forever(self):
        sys.path.append("foo")
        self.assertIn("foo", sys.path)
        seatbelt.solder([lambda path: path != "foo"])
        self.assertNotIn("foo", sys.path)
