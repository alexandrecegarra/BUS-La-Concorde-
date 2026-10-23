# La Concorde — guest site

Mobile web app for guests and family of La Concorde, Alexandre's apartment in Crans-Montana
(Route du Golf 28, 3963 Crans VS). Published with GitHub Pages from the `main` branch, repo root:
https://alexandrecegarra.github.io/BUS-La-Concorde-/

Alexandre works from his iPhone only and does not edit code. He asks for changes in conversation
(in French); Claude edits, rebuilds, commits and pushes.

## How to change the site

1. Edit the sources in `src/` — never edit `index.html` by hand, it is generated.
   - `src/web_template.html`: layout, CSS, all UI text, bus timetable data and logic (JS), Slopes and Contacts sections.
   - `src/restos.py`: the restaurant guide (Eat section). Tags are `|`-separated: `Favourite`, `1 Michelin star`, `Gault&Millau 13/20`.
   - `src/logo64.txt`: CM2027 logo (base64 PNG). `src/icon-1024.png`: master of the home-screen icon.
2. Rebuild: `python3 src/build.py` (writes `index.html` and `manifest.webmanifest`).
3. Check at phone width (393 px and 320 px) with Playwright: no horizontal scroll, each section shows/hides correctly.
4. Commit and push to `main`. GitHub Pages republishes in 1–2 minutes.

## Content rules (decided with Alexandre)

- Site language: English. Some French is fine (official timetable images, proper names).
- Sections (bottom bar): Bus, Slopes, Eat, Contacts. Bus tabs are "To town" / "Back home".
- Bus data: 2027 timetable (valid 13.12.2026 → 11.12.2027), from 08:00 onwards.
  432/433 board at Les Ehripis; 432 returns from Grand-Place, 433 from Mérignou.
  353 (PostBus) boards at Pirraparc = Lens, Centre d'art + 5 min; returns from Le Mérignou (departures towards Sion).
  353 days: weekday/Sat/Sun differ; public holidays follow Sunday (Valais list incl. 19.3, 27.5, 1.11, 8.12; 26.3 runs as a weekday).
- Colour codes: 432 bright red, 433 dark red (the favourite line), 353 PostBus yellow; CM2027 navy/sky blue/red.
- Restaurants: Alexandre's personal selection (not exhaustive). Favourites and descriptions come from him; keep them short.
  Gault&Millau scores are from the 2026 guide; update when the 2027 scores are accessible.
- Contacts: only business/official numbers. Never add private numbers, door codes or Wi-Fi passwords (public site and public repo).
  Ask before adding the concierge (Axelle / CosyHome).
- The live slopes map is an embedded infosnow iframe; the piste map links to the official PDF (replace each season).
- Weather & snow (top of Slopes): MeteoSwiss ICON-CH1/CH2 forecast (Open-Meteo `models=meteoswiss_icon_seamless`, fallback to best match) fetched by the viewer's browser (no key), at 1500 / 2200 / 3000 m like the resort's weather page: current conditions, model snow cover (Open-Meteo estimate, labelled as such), fresh snow forecast per day and 5-day total; links to the measured snow report (skiinfo) and the official forecast. The container cannot reach the API, so test with mocked responses in Playwright.
- Measured snow depth: `.github/workflows/snow.yml` runs `scripts/fetch_snow.py` every two hours (GitHub Actions) and commits `data/snow.json`
  from the SLF measurement API (CC BY 4.0, credit SLF): study plot 4MO0 Montana 1590 m (observer, daily morning reading; confirmed returning data in Oct 2026) and IMIS TRU2 Trubelboden 2459 m.
  The site reads `data/snow.json`. If it stops updating, check the Actions tab (GitHub disables scheduled workflows after 60 days without repo activity).
  The workflow can be triggered with `gh api -X POST repos/alexandrecegarra/BUS-La-Concorde-/actions/workflows/snow.yml/dispatches -f ref=main`.
- Webcam inside the weather card, following the altitude buttons: 1500 m = Golf-Club Crans-sur-Sierre driving range
  (live image `https://www.golfcrans.ch/fr/api/webcam/Driving`, cache-busted every 10 min); 2200 m = Skaping Les Violettes;
  3000 m = Skaping Plaine Morte (2880 m). Skaping photo times vary (e.g. 09:02), so `.github/workflows/webcams.yml` runs
  `scripts/fetch_webcams.py` hourly: it reads the og:image of each Skaping page and writes `data/webcams.json` (keeps the previous photo on failure).
  The page shows the photo date/time and credits the source; tap opens the camera's own viewer (Skaping, which can be turned), and at 1500 m the Roundshot 360° camera of the resort (https://lhm.roundshot.com/, Clinique Lucernoise), never the resort's webcam list page. These are the cameras listed on https://www.crans-montana.ch/fr/webcam.
- Section headings and labels: Slopes (weather with webcam, live map, piste map, lift ticket number).

## Contents at a glance

- Contacts: La Concorde address card with Google Maps link (top), emergencies, health (two medical centres,
  osteopath Manon Barras, pharmacies), resort (lifts, tourist office, SMC), practical (Cry d'Er ski lockers, Fougirs recycling centre).
- Eat: on the slopes, Michelin-starred, Fine tables, Convivial & lively. Alexandre chose not to add other categories.

## Open points to check later

- Gault&Millau 2027 scores (guide published 5 Oct 2026): update the tags in `src/restos.py`; Byakko entered the 2027 guide.
- Each season: new piste map PDF link; new bus timetables from mid-December 2027 (2028 timetable year).

## Git

Commit as `alexandrecegarra <alexandrecegarra@users.noreply.github.com>`.
