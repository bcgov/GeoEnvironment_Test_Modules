# ------------------------------------------------------------------------------
# - SUMMARY
# A unittest module to test the geospatial environment for problems. Main focus is to test the
# scripting environment, however we could also include other types of tests.

# First we simply try to import each module and report any errors
# Second we check basic functionality of each library if it imports

# - USEAGE
# FROM WITHIN IDE:
# Run everything
#     >> unittest.main()
# Run only one class
#     >> unittest.main(defaultTest="TestImports")
# Run only specific tests
#     >> unittest.main(defaultTest=["TestImports.test_import_arcpy", "FunctionTests.test_pandas_basic"])
# FROM COMMAND LINE: 
#     >> python -m unittest test_module.py TestImports
#     >> python -m unittest test_module.py FunctionTests.test_pandas_basic
# Discover and run all tests in a package    
#     >> python -m unittest discover

# - REQUIREMENTS

# - INPUTS

# - OUTPUTS

# ------------------------------------------------------------------------------
# - NOTES // FUTURE IMPROVEMENTS

# ------------------------------------------------------------------------------
# - HISTORY

#   Date      Initial/IDIR  Description
# | ----------------------------------------------------------------------------
#   yyyy-mm-dd    iii       Yada yada...................
#
# Don't need this section if using git.
# ------------------------------------------------------------------------------

# ** IMPORTS
# import sys
import unittest

# import path: geobc custom libraries
geobc_library_path = r"\\spatialfiles.bcgov\WORK\ilmb\dss\dsswhse\Resources\Scripts\Python\Library"
sys.path.insert(0, geobc_library_path)

# ** INTERNALS
# pyright settings
# --------------------------------------
# pyright: reportUnusedImport=false
# pyright: reportMissingImports=false
# pyright: reportUnusedCallResult=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# --------------------------------------

# ** PARAMETERS
global test_list
test_list = []

# ** TESTS
class ImportTests(unittest.TestCase):
    """Test that all important libraries and the geobc module can be imported."""

    def test_import_arcpy(self):
        # # # @unittest.skipIf('arcpy' not in sys.modules, 
        # # # "arcpy not available – skipping functionality tests")
        with self.subTest(library="arcpy"):
            try:
                import arcpy
                test_list.append("FunctionTests.test_arcpy_basic")
            except ImportError as e:
                self.fail(f"Failed to import arcpy: {e}")

    def test_import_geopandas(self):
        with self.subTest(library="geopandas"):
            try:
                import geopandas  
                test_list.append("FunctionTests.test_geopandas_basic")
            except ImportError as e:
                self.fail(f"Failed to import geopandas: {e}")

    def test_import_pandas(self):
        with self.subTest(library="pandas"):
            try:
                import pandas  
                test_list.append("FunctionTests.test_pandas_basic")
            except ImportError as e:
                self.fail(f"Failed to import pandas: {e}")

    def test_import_matplotlib(self):
        with self.subTest(library="matplotlib"):
            try:
                import matplotlib  
                test_list.append("FunctionTests.test_matplotlib_basic")
            except ImportError as e:
                self.fail(f"Failed to import matplotlib: {e}")

    def test_import_geobc(self):
        with self.subTest(library="geobc"):
            try:
                import geobc  
                test_list.append("FunctionTests.test_geobc_basic")
            except ImportError as e:
                self.fail(f"Failed to import local module 'geobc': {e}")


class FunctionTests(unittest.TestCase):
    """Individual tests to confirm core functionality of each library."""

    def test_arcpy_basic(self):
        import arcpy
        self.assertTrue(hasattr(arcpy, "Describe"), "arcpy.Describe is missing")
        self.assertTrue(hasattr(arcpy, "env"), "arcpy.env is missing")

    def test_geopandas_basic(self):
        import geopandas as gpd
        from shapely.geometry import Point
        gdf = gpd.GeoDataFrame(geometry=[Point(1, 1)], crs="EPSG:4326")
        self.assertEqual(len(gdf), 1)
        self.assertEqual(gdf.crs.to_epsg(), 4326)

    def test_pandas_basic(self):
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        self.assertEqual(df.shape, (3, 2))
        self.assertEqual(df["A"].sum(), 6)

    def test_matplotlib_basic(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        self.assertIsNotNone(fig)
        plt.close(fig)  # Clean up

    def test_geobc_basic(self):
        import geobc
        # Replace/adapt the following checks based on what geobc actually exposes
        self.assertTrue(hasattr(geobc, "__name__"), "geobc module appears broken")
        # Example additional checks (uncomment and adjust as needed):
        # self.assertTrue(callable(geobc.some_function), "geobc.some_function not found")
        # self.assertIn("version", dir(geobc))

if __name__ == "__main__":

    # # # # Run all tests
    # # # unittest.main(
    # # #     verbosity=2,      # detail of unittest reporting to terminal
    # # #     buffer=True,      # suppresses stdout/stderr from tests (cleaner output)
    # # #     failfast=False,   # set to True if you want to stop on first failure
    # # #     exit=True         # default; makes script exit with correct code
    # # #     )
    
    # # # # Run one test
    # # # unittest.main(defaultTest="TestImports")
    
    # # # # Run specific tests
    # # # unittest.main(defaultTest=["TestImports.test_import_arcpy", "FunctionTests.test_pandas_basic"])

    # Test all imports first. Only run further tests on successfully imported libraries.
    unittest.main(
        defaultTest="ImportTests",  # define what to run (by the class name)
        verbosity=2,                # detail of unittest reporting to terminal
        buffer=True,                # suppresses stdout/stderr from tests (cleaner output)
        failfast=False,             # set to True if you want to stop on first failure
        exit=True                   # default; makes script exit with correct code
        )
    if test_list:
        unittest.main(
            defaultTest=test_list,  # run list of tests defined by successful imports above
            verbosity=2,            # detail of unittest reporting to terminal
            buffer=True,            # suppresses stdout/stderr from tests (cleaner output)
            failfast=False,         # set to True if you want to stop on first failure
            exit=True               # default; makes script exit with correct code
            )

