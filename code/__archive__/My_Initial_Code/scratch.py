class BaseGISTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arcpy = cls._import_or_skip('arcpy')
        cls.gpd = cls._import_or_skip('geopandas')
        cls.pd = cls._import_or_skip('pandas')
        cls.plt = cls._import_or_skip('matplotlib').pyplot
        cls.geobc = cls._import_or_skip('geobc', 'geobc')

    @staticmethod
    def _import_or_skip(name, module_name=None):
        module_name = module_name or name
        try:
            return __import__(module_name)
        except ImportError as e:
            raise unittest.SkipTest(f"{name} not available: {e}")

class TestImports(BaseGISTest):
    def test_all_imports_work(self):
        # Just proves they were imported
        self.assertTrue(hasattr(self.arcpy, "Describe"))
        self.assertTrue(hasattr(self.gpd, "GeoDataFrame"))

class TestFunctionality(BaseGISTest):
    def test_arcpy_basic(self):
        self.assertTrue(hasattr(self.arcpy, "Describe"))

    def test_geopandas_basic(self):
        from shapely.geometry import Point
        gdf = self.gpd.GeoDataFrame(geometry=[Point(0,0)], crs=4326)
        self.assertEqual(len(gdf), 1)
    # ... etc