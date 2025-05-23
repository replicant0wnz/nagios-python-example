from src.project import ClassName


class TestProject:
    def test_class(self):
        x = ClassName()
        assert isinstance(x, object)
