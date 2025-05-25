from src.http_cluster.http_cluster import HTTPCluster

class TestHTTPCluster:
    def test_httpcluster(self):
        x = HTTPCluster
        assert isinstance(x, object)
