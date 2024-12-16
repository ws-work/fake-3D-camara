
import pytest

from map import Map

class TestMap:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.map = Map.set_map([[1,2,3],[4,5,6]])
        print(self.map)
        
    def test_get(self):
        assert self.map[0] == [1,2,3]


