# Restaurant guide data (sources checked 11.10.2026)
import html

INTRO = ("Here is our little Crans-Montana restaurant guide. We haven't tried everything yet, but among the places "
         "we have tested, my top picks for dinner would be the Bistrot des Ours, the Kaizen and Madriz. We haven't been "
         "to Le Mont-Blanc or Byakko yet, but they both look excellent. For lunch I'd go with Casy, La Plage or Chetzeron, "
         "which can also be lovely during the day.")

PISTES = [
    ("Chetzeron", "", "The most refined table on the slopes, at the hotel of the same name. Creative cooking built on local produce.", "+41 27 485 08 08", "https://www.chetzeron.ch"),
    ("Cabane des Violettes", "Favourite", "A genuine mountain hut, run by Franck Reynaud and mountain guide Pierrot Bagnoud. Simple cooking that is never ordinary.", "+41 27 481 39 19", "https://www.cabanedesviolettes.ch"),
    ("Zerodix", "", "The trendy lunch spot, which becomes the heart of the après-ski from 3 pm.", "+41 78 220 34 10", "https://zerodix.ch/fr/"),
    ("Le 2006", "", "The Amadeus 2006 restaurant, Mont-Lachaux sector.", "+41 78 655 33 89", "http://amadeus2006.ch/"),
    ("Le Loup Blanc", "Favourite", "A yurt on the slopes with a great view and great music. Counter service, excellent homemade soups, a dish of the day and simple, tasty food. The coolest spot on the mountain, at a reasonable price.", "+41 76 724 95 09", ""),
    ("Chez Erwin", "", "A small chalet on the Chetzeron slope with a south-facing terrace. Raclette, Valais platters and homemade pastries.", "+41 79 479 78 09", "https://www.facebook.com/p/Chez-Erwin-100063775563834/"),
    ("Cabane des Taules", "", "A tiny hut in the middle of the slopes. Raclette and soup, only when the sun is out.", "+41 78 647 87 98", ""),
]

STATION = [
    ("Michelin-starred", [
        ("L'Ours", "Favourite|1 Michelin star|Gault&Millau 18/20", "Franck Reynaud's starred table at the Hostellerie du Pas de l'Ours. Precise cooking, alpine terroir, a Provençal touch. Book well ahead.", "+41 27 485 93 33", "https://www.pasdelours.ch"),
        ("Le Mont-Blanc", "1 Michelin star|Gault&Millau 16/20", "The resort's other starred table, at LeCrans Hôtel & Spa. Contemporary cuisine, panoramic views.", "+41 27 486 60 88", "https://www.lecrans.com"),
    ]),
    ("Fine tables", [
        ("Le Bistrot des Ours", "Favourite|Gault&Millau 14/20", "Franck Reynaud's bistrot, same house as L'Ours. Refined, generous cooking with Provençal roots and local produce, in a more relaxed register but without compromising on quality.", "+41 27 485 93 33", "https://www.pasdelours.ch"),
        ("Le Kaizen", "Favourite|Gault&Millau 13/20", "Fine Japanese dining, three minutes' walk from the apartment. Chef Miguel de Vega. Ask for the bespoke tasting menu.", "+41 27 565 33 80", "https://kaizenrestaurant.com"),
        ("Le Partage", "Gault&Millau 14/20", "At the Aïda hotel, part of the Franck Reynaud world. A tasting menu of small plates to share. The resort's most original concept.", "+41 27 485 41 11", "https://www.aidahotelspa.ch/fr/restaurant-bar.html"),
        ("La Maison", "Gault&Millau 14/20", "At Résidence Le Miedzor, overlooking the golf course. Chef Quentin Philippe, also behind Arakel, 1 Michelin star in Geneva. Refined sharing cuisine, without the formality of a starred restaurant.", "+41 27 481 27 47", "https://lamaisoncrans.ch"),
        ("Casy", "Favourite|Gault&Millau 13/20", "In the centre of Montana, clean lines. A real gem.", "+41 27 481 17 18", "https://www.casy-montana.ch"),
        ("Le Monument", "Gault&Millau 13/20", "A gourmet bistrot on the village square in Lens. Chef Alessandro Bianchi, local produce, terrace.", "+41 27 483 19 82", "https://www.lemonument-lens.com"),
        ("Byakko", "", "The Japanese fusion restaurant at Six Senses. High-end wellness setting.", "+41 58 806 20 20", "https://www.sixsenses.com/en/resorts/crans-montana"),
        ("La Muña", "Gault&Millau 13/20", "The Japanese-Peruvian table at the Crans Ambassador. Nikkei style, lounge atmosphere.", "+41 27 485 48 48", "https://www.cransambassador.ch"),
        ("Five", "Gault&Millau 14/20", "Lebanese cuisine at the Guarda Golf Hotel & Residences, listed in the Michelin Guide.", "+41 27 486 20 00", "https://guardagolf.com/restaurants/"),
    ]),
    ("Convivial & lively", [
        ("Madriz", "Favourite", "Chef Jhonny Setjo's personal cooking, rooted in his Spanish and Balinese origins: the Mediterranean meets Asia in creative, generous plates. Don't miss the tortilla, the beef cheek paella and the extraordinary hazelnut and speculoos cheesecake. A lovely setting on the edge of Lake Grenon.", "+41 77 269 98 65", "https://www.restaurantmadriz.com"),
        ("Easy by Casy", "", "Casy's relaxed sibling next door, in the centre of Montana: aperitifs, tapas and cocktails.", "+41 27 481 17 18", "https://www.casy-montana.ch"),
        ("La Plage", "Favourite", "Saint-Tropez in the mountains. Lunch or dinner on the terrace by Lake Moubra whenever the sun is out, with a very good dry-aged beef menu. The summer address.", "+41 27 481 27 87", ""),
        ("Le Farinet", "", "Italian and seasonal cooking in the centre of Montana.", "+41 27 485 40 70", "https://le-farinet.ch"),
        ("Molino", "", "Italian pizzeria and trattoria on Rue du Pas de l'Ours.", "+41 27 481 90 90", "https://molino.ch"),
        ("Edo", "Bib Gourmand", "Authentic Japanese cooking by a Japanese team, in Bluche just below Montana. Gyoza, nigiri, sushi of the day; some specials, such as the Japanese fondue, must be ordered ahead. Mountain-view terrace, excellent value.", "+41 27 481 70 00", "http://www.edo-tokyo.ch"),
    ]),
]

def fmt(tel):
    d = tel.replace('+41', '0').replace(' ', '')
    return f"{d[:3]} {d[3:6]} {d[6:8]} {d[8:]}"

def card(name, tag, text, tel, url):
    e = html.escape
    t = ''.join(f'<span class="rtag{" fav" if x == "Favourite" else ""}">{e(x)}</span>' for x in tag.split('|')) if tag else ''
    t = f'<span class="tags">{t}</span>' if t else ''
    p = f'<p>{e(text)}</p>' if text else ''
    site = f'<a class="rbtn" href="{e(url)}" target="_blank" rel="noopener">Website</a>' if url else ''
    return (f'<article class="resto"><div class="rhead"><h3>{e(name)}</h3>{t}</div>{p}'
            f'<div class="ract"><a class="rbtn call" href="tel:{tel.replace(" ", "")}">{fmt(tel)}</a>{site}</div></article>')

def section_html():
    out = ['<p class="rintro">Our own selection of places we like, not an exhaustive guide.</p>',
           '<h2 class="rcat">On the slopes</h2>', *[card(*r) for r in PISTES]]
    for cat, items in STATION:
        out.append(f'<h2 class="rcat">{html.escape(cat)}</h2>')
        out += [card(*r) for r in items]
    out.append('<p class="note">Numbers and websites from the restaurants’ own sites, MySwitzerland, the Michelin Guide and the official piste map. Gault&Millau scores are from the 2026 guide. Opening hours vary by season, so a quick call before going avoids surprises.</p>')
    return '\n    '.join(out)
