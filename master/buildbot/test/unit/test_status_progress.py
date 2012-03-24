# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

from zope.interface import implements
import mock
from twisted.trial import unittest
from buildbot.status import progress

class TestExpectations(unittest.TestCase):

    def test_addNewStep(self):
        """
        http://trac.buildbot.net/ticket/2252
        """
        buildProgress = progress.BuildProgress([])
        expectations = progress.Expectations(buildProgress)
        stepProgress = progress.StepProgress("step", ["metric"])
        newProgress = progress.BuildProgress([stepProgress])
        stepProgress.start()
        stepProgress.finish()
        stepProgress.setProgress("metric", 42)
        expectations.update(newProgress)