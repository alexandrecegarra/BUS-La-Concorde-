"""Build the La Concorde site: python3 src/build.py (from the repo root or anywhere).

Reads src/web_template.html, src/restos.py and src/logo64.txt, and writes
index.html and manifest.webmanifest at the repo root. Timetable images live in fiches/.
"""
import json, os, sys
SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
import restos

T = open(os.path.join(SRC, 'web_template.html'), encoding='utf-8').read()
T = T.replace('__LOGO__', open(os.path.join(SRC, 'logo64.txt')).read().strip())
T = T.replace('__RESTOS__', restos.section_html())
for n in ['432', '433-1', '433-2', '353-1', '353-2', '353-3', '353-4']:
    T = T.replace(f'__IMG_{n}__', f'fiches/{n}.jpg')

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="La Concorde">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#F3F6FA">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)} body{margin:0}</style>
'''
i = T.index('<div class="wrap"')
doc = HEAD + T[:i] + '</head>\n<body>\n' + T[i:] + '\n</body>\n</html>\n'
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(doc)
json.dump({"name": "La Concorde", "short_name": "La Concorde", "lang": "en", "start_url": "./", "display": "standalone",
           "background_color": "#F3F6FA", "theme_color": "#F3F6FA",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(ROOT, 'manifest.webmanifest'), 'w'), ensure_ascii=False, indent=2)
print('index.html built')
