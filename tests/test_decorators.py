# -*- coding: utf-8 -*-

import matplotlib.dates as mdates

from datetime import datetime

from speedtest_reader import format_timestamps
from speedtest_reader import util

import helpers

__author__ = "Tobias Frei"
__copyright__ = "Tobias Frei"
__license__ = "mit"


def test_format_timestamps():

    # tests for decorators
    f = util.to_Mbit(format_timestamps)  # TODO complete when we have StringIO.

    name = "some_name"
    TS = "1970-01-01 00:00:00.000000+00:00"
    # decoration syntax to use for apps
    f = (util.append_mpldate(colname=name))(helpers.miniframe)
    # print(f(TS))
    assert name in f(TS).columns
    assert datetime.strptime(TS, "%Y-%m-%d %H:%M:%S.%f%z") == mdates.num2date(
        f(TS).iloc[0, 1]
    )

    TS = "2019-06-22 18:43:21.831314+00:00"
    f = (util.append_tslocal())(helpers.miniframe)
    # print(f(TS))
    assert (
        helpers.my_offset
        + datetime.strptime(TS, "%Y-%m-%d %H:%M:%S.%f%z").replace(tzinfo=None)
        == f(TS).iloc[0, 1]
    )
    assert "tslocal" in f(TS).columns
    # end decorators

    # TODO all kind of ts range tests
    #

    # TODO For to_Mbit decorator: test what happens when dealing with dfs:

    # - where only one of "Download", "Upload" is present
    # - neither of these two is present
    #
