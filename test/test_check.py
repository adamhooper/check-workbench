from pathlib import Path
import unittest
import numpy as np
import pandas as pd
import json
import sys
from pandas.testing import assert_frame_equal
from check import render, flatten

class FetchResult:
  def __init__(self, dataframe):
    self.dataframe = dataframe
    self.status = None

class TestCheck(unittest.TestCase):
  def setUp(self):
    self.data = json.loads(
        (Path(__file__).parent / 'test_check.json').read_text()
    )

  def test_flatten(self):
    df = flatten(self.data)

  def test_render(self):
    df = flatten(self.data)
    render(df, { 'anonymize': False }, fetch_result=FetchResult(df))
    render(df, { 'anonymize': True }, fetch_result=FetchResult(df))

if __name__ == '__main__':
    unittest.main()
