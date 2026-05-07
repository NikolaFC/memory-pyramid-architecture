#!/usr/bin/env python3
"""Core verification suite for Memory Pyramid Architecture."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    print("\n$", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> int:
    for script in sorted((ROOT / "scripts").glob("*.py")):
        run([sys.executable, "-m", "py_compile", str(script.relative_to(ROOT))])

    run([sys.executable, "scripts/test_integration.py"])
    print("\nverify_suite: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
