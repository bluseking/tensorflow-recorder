# Lint as: python3

# Copyright 2020 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for pandas accessor."""

import unittest

# pylint: disable=unused-import
from tfrutil import accessor
from tfrutil import constants
from tfrutil import test_utils


class DataFrameAccessor(unittest.TestCase):
  """UnitTests For DataFrame Accessor."""

  def setUp(self):
    self.test_df = test_utils.get_test_df()

  def test_accessor(self):
    """Tests pandas accessor."""
    pid = self.test_df.tensorflow.to_tfr(runner="DirectRunner",
                                         output_path="/tmp/train")
    self.assertEqual(pid, "p1234")


if __name__ == "__main__":
  unittest.main()