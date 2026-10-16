#!/usr/bin/env python3
"""Basistest van dc-r1b: BASIS, C01..C13 en V01..V08 moeten groen blijven."""
import subprocess, sys, pathlib
hier = pathlib.Path(__file__).resolve().parent
ids = ["BASIS"] + ["C%02d" % i for i in range(1, 14)] + ["V%02d" % i for i in range(1, 9)]
rood = []
for i in ids:
    r = subprocess.run([sys.executable, str(hier / "feature.py"), i], capture_output=True, text=True)
    if r.returncode != 0:
        rood.append(i)
print("regressie: %d/%d groen%s" % (len(ids) - len(rood), len(ids), (", rood: " + " ".join(rood)) if rood else ""))
sys.exit(1 if rood else 0)
