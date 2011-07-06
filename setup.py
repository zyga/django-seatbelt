#!/usr/bin/python
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

from setuptools import setup, find_packages


setup(
    name="django-seatbelt",
    version=":versiontools:django_seatbelt:",
    description=('Simple sandbox that isolates production applications from'
                 ' things users stick in /usr/local/'),
    author='Zygmunt Krynicki',
    author_email='zygmunt.krynicki@canonical.com',
    url='http://github.com/zyga/django-seatbelt',
    test_suite='django_seatbelt.tests',
    long_description="""
    Reduce support calls by isolating your production application from user's
    mismanagement and stuff they put inside /usr/local/.
    """,
    packages=find_packages(),
    setup_requires=["versiontools >= 1.4"],
    tests_require=["testtools >= 0.9.2"],
    license="LGPL3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General Public"
         " License (LGPL)"),
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    zip_safe=True,
)
