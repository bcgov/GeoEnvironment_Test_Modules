# Final best version
class BaseGISTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        def imp(name, mod=None):
            try: return __import__(mod or name)
            except ImportError as e:
                raise unittest.SkipTest(f"{name} unavailable: {e}")
        cls.arcpy = imp("arcpy")
        cls.gpd   = imp("geopandas")
        cls.pd    = imp("pandas")
        cls.plt   = imp("matplotlib").pyplot
        cls.geobc = imp("geobc")

class TestImports(BaseGISTest):
    def test_imports(self): pass  # Just runs setUpClass

class TestFunctionality(BaseGISTest):
    def test_arcpy_basic(self):
        self.assertTrue(hasattr(self.arcpy, "Describe"))
    # ... etc

