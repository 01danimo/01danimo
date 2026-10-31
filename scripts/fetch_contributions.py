#!/usr/bin/env python3
"""Fetch the public GitHub contribution calendar without a personal access token."""
import json, re
from datetime import date, timedelta
from pathlib import Path
import requests
from bs4 import BeautifulSoup
cfg=json.loads(Path('data/profile.json').read_text())
username=cfg['username']
if not username or username=='YOUR_GITHUB_USERNAME':
    raise SystemExit('Edit data/profile.json and set your GitHub username first.')
url=f'https://github.com/users/{username}/contributions'
r=requests.get(url,headers={'User-Agent':'Mozilla/5.0 github-profile-readme'},timeout=30)
r.raise_for_status()
soup=BeautifulSoup(r.text,'html.parser')
days={}
for el in soup.select('[data-date]'):
    d=el.get('data-date')
    if not d: continue
    try: dt=date.fromisoformat(d)
    except ValueError: continue
    level=el.get('data-level','0')
    label=el.get('aria-label','')
    m=re.search(r'(\d+) contributions?',label)
    count=int(m.group(1)) if m else (0 if level=='0' else int(level))
    days[d]={'count':count,'level':int(level) if str(level).isdigit() else 0,'label':label}
if not days:
    raise SystemExit('No contribution cells found. Check username/profile visibility or GitHub markup changes.')
end=max(date.today(), max(date.fromisoformat(x) for x in days))
start=end-timedelta(days=370)
out=[]
cur=start
while cur<=end:
    out.append({'date':cur.isoformat(),**days.get(cur.isoformat(),{'count':0,'level':0,'label':''})})
    cur+=timedelta(days=1)
Path('data/contributions.json').write_text(json.dumps({'username':username,'days':out,'total':sum(x['count'] for x in out)},indent=2))
print(f"Saved {len(out)} days; {sum(x['count'] for x in out)} contributions.")
