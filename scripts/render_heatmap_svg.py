#!/usr/bin/env python3
import json, html
from pathlib import Path
from datetime import date
p=json.loads(Path('data/contributions.json').read_text())
days=p['days'][-371:]
# Arrange sequential days into columns; first column starts on Sunday.
first=date.fromisoformat(days[0]['date'])
offset=(first.weekday()+1)%7
cells=[None]*offset+days
weeks=(len(cells)+6)//7
W,H=920,174; x0,y0=28,38; cell=11; gap=4
palette=['#161b22','#0e4429','#006d32','#26a641','#39d353']
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="920" height="174" viewBox="0 0 {W} {H}">','<rect width="920" height="174" rx="14" fill="#0d1117" stroke="#30363d"/>','<text x="28" y="25" fill="#c9d1d9" font-family="monospace" font-size="14">CONTRIBUTION ACTIVITY · LAST 12 MONTHS</text>']
for i,d in enumerate(cells):
    if d is None: continue
    col=i//7; row=i%7; lvl=max(0,min(4,int(d.get('level',0))))
    x=x0+col*(cell+gap); y=y0+row*(cell+gap)
    title=html.escape(d['date']+': '+str(d.get('count',0))+' contributions')
    delay=(col+row)*.018
    s.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{palette[lvl]}" opacity="0"><title>{title}</title><animate attributeName="opacity" from="0" to="1" dur=".25s" begin="{delay:.2f}s" fill="freeze"/></rect>')
total=p.get('total',sum(x.get('count',0) for x in days))
s.append(f'<text x="28" y="158" fill="#8b949e" font-family="monospace" font-size="13">{total:,} contributions  ·  Less</text>')
for i,c in enumerate(palette): s.append(f'<rect x="{700+i*20}" y="146" width="12" height="12" rx="2" fill="{c}"/>')
s += ['<text x="815" y="158" fill="#8b949e" font-family="monospace" font-size="13">More</text>','</svg>']
Path('contrib-heatmap.svg').write_text('\n'.join(s))
