#!/usr/bin/env python3
"""
Memory Pyramid Integration Test Suite
Tests core functionality of the memory-pyramid-architecture skill
"""

import os
import sys
import json
from pathlib import Path

SKILL_DIR = Path('/home/nikolafc/.openclaw/workspace/skills/memory-pyramid-architecture')
RESULTS = []

def test(name, condition, details=""):
    status = "PASS" if condition else "FAIL"
    RESULTS.append((name, status, details))
    print(f"[{status}] {name}: {details}")

def main():
    print("=" * 50)
    print("Memory Pyramid Integration Test Suite")
    print("=" * 50)
    
    # Test 1: Directory exists
    test("SKILL_DIR exists", SKILL_DIR.exists(), str(SKILL_DIR))
    
    # Test 2: Required files exist
    required = ["SKILL.md", "README.md", "LICENSE", "PACKAGE.md"]
    for f in required:
        path = SKILL_DIR / f
        test(f"File exists: {f}", path.exists(), str(path))
    
    # Test 3: Scripts directory
    scripts_dir = SKILL_DIR / "scripts"
    test("scripts/ exists", scripts_dir.exists(), str(scripts_dir))
    
    if scripts_dir.exists():
        # Test init.py
        init_py = scripts_dir / "init.py"
        test("init.py exists", init_py.exists(), str(init_py))
        
        # Test config.json
        config = scripts_dir / "config.json"
        test("config.json exists", config.exists(), str(config))
        
        if config.exists():
            try:
                data = json.loads(config.read_text())
                test("config.json valid JSON", True, "parsed successfully")
            except Exception as e:
                test("config.json valid JSON", False, str(e))
    
    # Test 4: References directory
    refs_dir = SKILL_DIR / "references"
    test("references/ exists", refs_dir.exists(), str(refs_dir))
    
    # Test 5: Examples directory
    examples_dir = SKILL_DIR / "examples"
    test("examples/ exists", examples_dir.exists(), str(examples_dir))
    
    # Test 6: Multi-language support
    readme_en = SKILL_DIR / "README_EN.md"
    readme_zh = SKILL_DIR / "README_ZH.md"
    test("README_EN.md exists", readme_en.exists(), str(readme_en))
    test("README_ZH.md exists", readme_zh.exists(), str(readme_zh))
    
    # Test 7: Visualization tool
    visualize_py = scripts_dir / "visualize.py" if scripts_dir.exists() else None
    test("visualize.py exists", visualize_py.exists() if visualize_py else False, str(visualize_py) if visualize_py else "scripts dir missing")
    
    # Summary
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    passed = sum(1 for _, s, _ in RESULTS if s == "PASS")
    failed = sum(1 for _, s, _ in RESULTS if s == "FAIL")
    print(f"Total: {len(RESULTS)} | PASS: {passed} | FAIL: {failed}")
    
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
