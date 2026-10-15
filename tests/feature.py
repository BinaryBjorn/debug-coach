#!/usr/bin/env python3
"""Draai de tests van één feature (ID in de testnaam). Faalt als er nul tests liepen.
Gebruik: python3 tests/feature.py C01   (of BASIS)"""
import sys, unittest, pathlib

def main():
    if len(sys.argv) != 2:
        print("gebruik: python3 tests/feature.py <ID>"); return 2
    fid = sys.argv[1]
    here = pathlib.Path(__file__).resolve().parent
    loader = unittest.TestLoader()
    loader.testNamePatterns = ["*_%s_*" % fid]
    suite = loader.discover(str(here), pattern="test_*.py", top_level_dir=str(here))
    res = unittest.TextTestRunner(verbosity=1).run(suite)
    if res.testsRun == 0:
        print("FOUT: geen enkele test voor %s gevonden" % fid); return 1
    return 0 if res.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(main())
