#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'SECURITY.md', 'package.json', 'docusaurus.config.js', 'sidebars.js', 'docs/intro.md']
errors = []
for rel in required:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')


for js in ['docusaurus.config.js', 'sidebars.js']:
    text = (root / js).read_text()
    if 'module.exports' not in text:
        errors.append(f'{js} should export configuration')

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    sys.exit(1)
print('OK: T15_R02')
