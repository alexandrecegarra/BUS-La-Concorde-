"""Find the latest photo of the Skaping webcams used by Crans-Montana (og:image of each camera page)
and write data/webcams.json for the site. Run hourly by .github/workflows/webcams.yml."""
import json, os, re, urllib.request, urllib.parse

ROUNDSHOT = {'montana-360': 'https://lhm.roundshot.com/'}  # 360° camera above Montana (Clinique Lucernoise)
CAMS = {
    'les-violettes': 'https://www.skaping.com/crans-montana/les-violettes',
    'plaine-morte': 'https://www.skaping.com/crans-montana/plaine-morte',
}
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'webcams.json')
prev = json.load(open(path)) if os.path.exists(path) else {}
out = {}
for slug, page in CAMS.items():
    try:
        req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0 (la-concorde-guest-site)'})
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html) or \
            re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', html)
        url = m.group(1)
        t = re.search(r'/(\d{4})/(\d{2})/(\d{2})/large/(\d{2})-(\d{2})\.jpg', url)
        taken = f'{t[1]}-{t[2]}-{t[3]}T{t[4]}:{t[5]}' if t else None
        out[slug] = {'url': url, 'taken': taken, 'page': page}
    except Exception as e:  # keep the previous photo if Skaping is unreachable
        out[slug] = prev.get(slug, {'url': None, 'taken': None, 'page': page})
for slug, page in ROUNDSHOT.items():
    try:
        req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0 (la-concorde-guest-site)'})
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html) or \
            re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', html)
        url = urllib.parse.urljoin(page, m.group(1))
        r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (la-concorde-guest-site)'}), timeout=30)
        ctype = r.headers.get('Content-Type', '')
        final = r.geturl()
        out[slug] = {'url': final if ctype.startswith('image/') else None, 'og': url, 'type': ctype, 'taken': None, 'page': page}
    except Exception as e:
        out[slug] = prev.get(slug, {'url': None, 'taken': None, 'page': page, 'error': str(e)[:200]})
json.dump(out, open(path, 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False))
