#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from design_pytterns.errors import DesignPytternError


def test_str_error_with_message():
    error_message = 'generic error'
    generic_package_error = DesignPytternError(message=error_message)
    assert str(generic_package_error) == error_message
