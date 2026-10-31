#!/usr/bin/env python3
import json, html
from pathlib import Path
p=json.loads(Path('data/profile.json').read_text())
rows=[('USER',p['display_name']),('ROLE',p['headline']),('NOW',p['now']),('PREV',p['previous']),('STACK',p['stack']),('FOCUS',p['focus']),('BADGES',p['highlights'])]
W,H=900,410
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="410" viewBox="0 0 {W} {H}">',
'<rect width="900" height="410" rx="14" fill="#0d1117" stroke="#30363d"/>',
'<rect x="0" y="0" width="900" height="42" rx="14" fill="#161b22"/>',
'<circle cx="22" cy="21" r="6" fill="#ff5f56"/><circle cx="43" cy="21" r="6" fill="#ffbd2e"/><circle cx="64" cy="21" r="6" fill="#27c93f"/>',
'<text x="88" y="27" fill="#8b949e" font-family="monospace" font-size="15">profile@github:~$ neofetch</text>',
'<g font-family="Consolas,Monaco,monospace" font-size="19">']
for i,(k,v) in enumerate(rows):
    y=86+i*43
    delay=i*.18
    s.append(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur=".35s" begin="{delay:.2f}s" fill="freeze"/><text x="34" y="{y}" fill="#58a6ff">{html.escape(k):<8}</text><text x="160" y="{y}" fill="#c9d1d9">{html.escape(v)}</text></g>')
s += ['</g>','<text x="34" y="382" fill="#3fb950" font-family="monospace" font-size="15">● system ready  |  keep building, keep learning</text>','</svg>']
Path('assets/info-card.svg').write_text('\n'.join(s))
