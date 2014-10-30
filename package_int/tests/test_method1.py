from ..method1 import functionA
from nose.tools import assert_equal
from mock import Mock

def test_functionA():
  """ Test for integer numbers"""
  # Test something
  #f = Mock(name="myroutine", return_value=2) 
  actual=functionA(4)
  expected=4
  assert_equal(expected,actual)