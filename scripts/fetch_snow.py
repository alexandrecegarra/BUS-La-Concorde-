"""Fetch measured snow depth near Crans-Montana from the SLF measurement API (CC BY 4.0)
and write data/snow.json for the site. Run every two hours by .github/workflows/snow.yml."""
import json, os, urllib.request, datetime

API = 'https://measurement-api.slf.ch/public/api'
STATIONS = [
    # (kind, code, label, elevation m, note)
    ('study-plot', '4MO0', 'Montana', 1590, 'Observer plot in the resort, measured every morning in season'),
    ('imis', 'TRU2', 'Trubelboden', 2459, 'Automatic station, 9 km east of Crans-Montana'),
]

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'la-concorde-guest-site (github.com/alexandrecegarra)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

out = {'updated': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='minutes'),
       'source': 'WSL Institute for Snow and Avalanche Research SLF, www.slf.ch (CC BY 4.0)',
       'stations': []}
for kind, code, label, elev, note in STATIONS:
    entry = {'code': code, 'label': label, 'elevation': elev, 'note': note, 'hs': None, 'date': None, 'new24': None}
    try:
        rows = get(f'{API}/{kind}/station/{code}/measurements?period_in_days=7')
        rows = [r for r in rows if r.get('HS') is not None]
        rows.sort(key=lambda r: r['measure_date'])
        if rows:
            last = rows[-1]
            entry['hs'] = round(float(last['HS']))
            entry['date'] = last['measure_date']
            if last.get('HN_1D') is not None:
                entry['new24'] = round(float(last['HN_1D']))
    except Exception as e:  # keep the previous value if the API is down
        entry['error'] = str(e)[:200]
    out['stations'].append(entry)

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'snow.json')
prev = None
if os.path.exists(path):
    prev = json.load(open(path))
    # do not overwrite a good value with an error
    for i, st in enumerate(out['stations']):
        if 'error' in st and prev and i < len(prev.get('stations', [])) and prev['stations'][i].get('hs') is not None:
            out['stations'][i] = prev['stations'][i]
if prev and prev.get('stations') == out['stations']:
    out['updated'] = prev.get('updated')  # nothing new: keep the file identical, no commit
json.dump(out, open(path, 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False))
