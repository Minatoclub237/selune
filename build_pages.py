# -*- coding: utf-8 -*-
"""Génère les pages secondaires (header/footer communs, un mécanisme propre par page).
   python build_pages.py  → carte, astro, commandes, a-propos, contact, mentions-legales
   + met à jour la nav d'index.html."""
import os, re
from urllib.parse import quote
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MAPS = 'https://www.google.com/maps?cid=17615685143766384162'
IG = 'https://www.instagram.com/selune_patisserie/'
TEL = 'tel:+33630168940'
TEL_TXT = '06 30 16 89 40'
def wa(msg='Bonjour Sélune, '):
    return 'https://wa.me/33630168940?text=' + quote(msg)
ADR = '37 rue du 19 Mars 1962'
VILLE = '84320 Entraigues-sur-la-Sorgue'

NAV_LINKS = [('index.html', 'Accueil'), ('carte.html', 'La carte'), ('astro.html', 'Astro'), ('commandes.html', 'Sur commande'), ('a-propos.html', 'La maison'), ('contact.html', 'Contact')]

IG_ICO = '<svg class="ig-ico" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.4" fill="currentColor"/></svg>'
WA_ICO = '<svg class="wa-ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.47 14.38c-.29-.15-1.7-.84-1.97-.93-.26-.1-.45-.15-.65.14-.19.29-.74.93-.91 1.12-.17.19-.34.22-.62.07-.29-.15-1.22-.45-2.32-1.43-.86-.76-1.44-1.7-1.6-1.99-.17-.29-.02-.44.13-.59.13-.13.29-.34.43-.51.15-.17.19-.29.29-.48.1-.19.05-.36-.02-.51-.07-.15-.65-1.56-.89-2.13-.23-.56-.47-.48-.65-.49h-.55c-.19 0-.5.07-.76.36-.26.29-1 .98-1 2.38s1.02 2.76 1.17 2.95c.15.19 2.01 3.06 4.86 4.29.68.29 1.21.47 1.62.6.68.22 1.3.19 1.79.11.55-.08 1.7-.69 1.94-1.36.24-.67.24-1.24.17-1.36-.07-.12-.26-.19-.55-.34M12.05 21.5h-.01c-1.77 0-3.51-.48-5.03-1.38l-.36-.21-3.74.98 1-3.64-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.89 9.9-9.89 2.64 0 5.13 1.03 7 2.9a9.82 9.82 0 0 1 2.9 6.99c0 5.46-4.44 9.9-9.9 9.9M20.52 3.45A11.76 11.76 0 0 0 12.05 0C5.5 0 .17 5.33.17 11.88c0 2.09.55 4.14 1.59 5.94L.07 24l6.33-1.66a11.85 11.85 0 0 0 5.65 1.44h.01c6.55 0 11.88-5.33 11.88-11.88 0-3.17-1.24-6.16-3.48-8.4"/></svg>'
FAVICON ="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%2317120E'/%3E%3Ccircle cx='15' cy='17' r='9' fill='%23F3E9DA'/%3E%3Ccircle cx='19' cy='14' r='8' fill='%2317120E'/%3E%3Ccircle cx='24' cy='9' r='1.6' fill='%23C9A56B'/%3E%3C/svg%3E"

def head(title, desc, body_class=''):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/hero.webp">
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="fonts/urbanist-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="vendor/lenis.css">
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="pages.css">
</head>
<body class="sub {body_class}">

<div class="grain" aria-hidden="true"></div>
<div class="cursor" aria-hidden="true"><span class="cursor__dot"></span><span class="cursor__ring"><span class="cursor__label"></span></span></div>
'''

def nav(current):
    links = ''.join(f'<a href="{h}"{" aria-current=page" if h == current else ""}>{l}</a>' for h, l in NAV_LINKS)
    return f'''<header class="nav" id="nav">
  <button class="nav__burger" id="burger" aria-label="Menu"><i></i><i></i></button>
  <a class="nav__logo" href="index.html" aria-label="Sélune">
    <img class="nav__logo-img" src="img/logo.webp" alt="Sélune — pâtisserie, salon de thé">
  </a>
  <nav class="nav__links">{links}</nav>
  <a class="btn btn--pill" href="{TEL}" data-cursor="Appeler" data-magnet>{TEL_TXT}</a>
</header>
<div class="menu" id="menu">
  {links}
</div>
<a class="wa-fab" href="{wa()}" target="_blank" rel="noopener" aria-label="Écrire à Sélune sur WhatsApp" data-cursor="WhatsApp">{WA_ICO}</a>
'''

FOOTER = f'''<footer class="footer footer--page">
  <img class="footer__logo" src="img/logo.webp" alt="Sélune — pâtisserie, salon de thé">
  <div class="footer__cols">
    <div><b>Sélune</b><br>{ADR}<br>{VILLE}</div>
    <div>Pâtisserie fine · Salon de thé<br>Plats du jour le midi<br>Sur place ou à emporter</div>
    <div><a href="{TEL}">{TEL_TXT}</a><br><a href="{wa()}" target="_blank" rel="noopener">{WA_ICO}WhatsApp</a><br><a href="{IG}" target="_blank" rel="noopener">{IG_ICO}@selune_patisserie</a><br><a href="{MAPS}" target="_blank" rel="noopener">Fiche Google Maps</a></div>
    <div><a href="index.html">Accueil</a><br><a href="carte.html">La carte</a><br><a href="astro.html">La collection Astro</a><br><a href="commandes.html">Sur commande</a><br><a href="a-propos.html">La maison</a><br><a href="contact.html">Contact</a></div>
  </div>
  <div class="footer__row">
    <span>© 2026 Sélune · SARL · SIRET 106 670 060 00016</span>
    <span><a href="mentions-legales.html">Mentions légales · CGV · Confidentialité</a></span>
  </div>
</footer>
'''

def tail(extra_js=''):
    return f'''
<script src="vendor/gsap.min.js"></script>
<script src="vendor/ScrollTrigger.min.js"></script>
<script src="vendor/lenis.min.js"></script>
<script src="main.js"></script>
{extra_js}
</body>
</html>
'''

ORDER_FORM = f'''<form class="boutique__form" data-reveal id="orderForm">
        <input type="text" name="nom" placeholder="Votre nom" required>
        <input type="tel" name="tel" placeholder="Votre téléphone" required>
        <input type="date" name="date" aria-label="Date souhaitée">
        <textarea name="msg" rows="3" placeholder="Votre commande : grand format de votre signe, nombre de parts, date…" required></textarea>
        <button class="btn btn--wa" type="submit" data-cursor="WhatsApp" data-magnet>Envoyer sur WhatsApp</button>
        <p class="boutique__ok">Votre message s’ouvre dans WhatsApp — il ne reste qu’à l’envoyer.</p>
      </form>'''

# ═══════════════════════════ CARTE ═══════════════════════════
FAMILIES = [
  ('patisserie', 'Pâtisserie fine', '01', 'img/carte-5.webp', 'img/cake-2.webp',
   'Petits gâteaux et entremets faits maison et de saison. Chaque mois, la collection Astro ajoute le gâteau du signe en cours.',
   [('La collection Astro', 'Un petit gâteau par signe astrologique — en ce moment l’Astro Scorpion, sans gluten. <a href="astro.html">Voir la collection</a>'),
    ('Petits gâteaux du jour', 'La vitrine change avec les saisons'),
    ('Grand format', 'Les gâteaux de la collection existent en grand format — <a href="commandes.html">sur commande</a>', 'Sur commande'),
    ('Praliné noisette maison', 'Noisettes torréfiées, caramel et une pointe de fleur de sel, glissé dans les gâteaux')]),
  ('salon', 'Salon de thé & café', '02', 'img/carte-3.webp', 'img/carte-4.webp',
   'Sur place, dans un cadre cosy, chaleureux et moderne — ou à emporter.',
   [('Café de la Torréfaction Maison Bres', 'Torréfié à Sarrians, dans le Vaucluse : artisanal et local'),
    ('Thé', 'Le salon de thé, avec une pâtisserie de la vitrine'),
    ('Chocolat chaud', 'Avec une part de cake ou un cookie'),
    ('Formule goûter', 'Un cookie ou une part de cake, avec un jus Kookabara ou un chocolat chaud (vacances de la Toussaint)', '6 €')]),
  ('midi', 'Le midi', '03', 'img/carte-2.webp', 'img/carte-1.webp',
   'Une petite restauration du midi : le plat du jour, fait maison.',
   [('Plat du jour', 'Annoncé chaque jour en boutique'),
    ('Sur place ou à emporter', 'Au salon de thé, ou à la maison'),
    ('Et un dessert', 'La vitrine est juste à côté')]),
]

def carte():
    fam_nav = ''.join(f'<a href="#{k}">{n}</a>' for k, n, *_ in FAMILIES)
    col_imgs = ['img/sig-1.webp', 'img/maison-framboise.webp', 'img/sig-2.webp', 'img/tart.webp', 'img/maison-hero.webp', 'img/croissant.webp']
    col = ''.join(f'<img src="{i}" alt="" loading="eager">' for i in col_imgs)
    blocks = ''
    for i, (k, n, num, img1, img2, lead, items) in enumerate(FAMILIES):
        lis = ''.join(f'<li data-reveal><h3>{t}</h3><p>{d}</p><b>{p[0] if p else "Prix en boutique"}</b></li>' for t, d, *p in items)
        blocks += f'''
<section class="fam{" fam--alt" if i % 2 else ""}" id="{k}">
  <div class="fam__visual">
    <figure class="fam__fig" data-reveal-clip><img src="{img1}" alt="" loading="lazy" data-parallax-img></figure>
    <figure class="fam__small" data-speed="-0.35" data-reveal-clip><img src="{img2}" alt="" loading="lazy"></figure>
    <span class="fam__num" data-speed="0.25" aria-hidden="true">{num}</span>
  </div>
  <div class="fam__text">
    <p class="eyebrow" data-reveal>{num} — La carte</p>
    <h2 class="h2" data-letters>{n}</h2>
    <p class="fam__lead" data-scrub-words>{lead}</p>
    <ul class="fam__list">{lis}</ul>
  </div>
</section>'''
    return (head('La carte — Sélune, pâtisserie & salon de thé à Entraigues-sur-la-Sorgue', 'Pâtisserie fine, collection Astro, salon de thé, café de Sarrians et plats du jour : la carte de Sélune à Entraigues-sur-la-Sorgue.', 'p-carte')
        + nav('carte.html')
        + f'''<main id="top">
<section class="split-hero">
  <div class="split-hero__text">
    <p class="eyebrow" data-reveal>La carte</p>
    <h1 class="split-hero__title" data-letters>Tout est fait maison</h1>
    <p class="split-hero__lead" data-reveal>Pâtisserie fine, salon de thé et plats du jour. Les prix sont affichés en boutique ; les commandes se passent au {TEL_TXT}.</p>
    <nav class="split-hero__nav" data-reveal>{fam_nav}</nav>
  </div>
  <div class="split-hero__col" aria-hidden="true">
    <div class="vmarquee" data-vmarquee><div class="vmarquee__row">{col}</div><div class="vmarquee__row">{col}</div></div>
  </div>
</section>
{blocks}
<section class="phone-band">
  <p class="eyebrow" data-reveal>Une envie précise ? Un seul numéro</p>
  <a class="phone-band__num" href="{TEL}" data-letters data-cursor="Appeler">{TEL_TXT}</a>
  <p class="phone-band__sub" data-reveal>Sur place ou à emporter · {ADR}, Entraigues-sur-la-Sorgue</p>
  <div class="phone-band__wa" data-reveal><a class="btn btn--wa" href="{wa('Bonjour Sélune, je voudrais passer une commande : ')}" target="_blank" rel="noopener" data-cursor="WhatsApp" data-magnet>Commander sur WhatsApp</a></div>
</section>
</main>''' + FOOTER + tail())

# ═══════════════════════════ SUR COMMANDE ═══════════════════════════
def commandes():
    cards = [('img/scard-1.webp', 'Le grand format', 'Les petits gâteaux de la collection Astro, en version à partager — sur commande'),
             ('img/scard-2.webp', 'Pour le goûter', 'Un cookie ou une part de cake, avec un jus ou un chocolat chaud — et ça marche aussi pour les adultes'),
             ('img/scard-3.webp', 'Une envie précise ?', 'Votre signe, vos goûts, le nombre de parts : dites-nous tout, on vous répond')]
    stack = ''.join(f'''
    <article class="scard">
      <img src="{img}" alt="" loading="lazy">
      <div class="scard__body"><span class="scard__n">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>
    </article>''' for i, (img, t, d) in enumerate(cards))
    return (head('Sur commande — grand format & gâteaux Astro — Sélune', 'Les gâteaux de la collection Astro en grand format, sur commande, à retirer chez Sélune, 37 rue du 19 Mars 1962 à Entraigues-sur-la-Sorgue.', 'p-mariages')
        + nav('commandes.html')
        + f'''<main id="top">
<section class="mhero">
  <div class="mhero__pin">
    <video class="mhero__video" autoplay muted loop playsinline poster="img/mariages-hero.webp" data-hero-img data-src-hd="video/mariages-hero.mp4" data-src-sd="video/mariages-hero-720.mp4"></video>
    <div class="mhero__veil"></div>
    <div class="mhero__slide" data-mslide>
      <p class="eyebrow" data-letters>Sur commande</p>
      <h1 class="mhero__h"><span data-letters>Votre signe</span><span data-letters>en grand</span></h1>
      <p class="mhero__p">Chaque petit gâteau de la collection Astro existe en grand format, sur commande. Et pour une envie précise, on en parle.</p>
      <div class="mhero__cta"><a class="btn btn--light" href="#demande" data-magnet data-cursor="Commander">Faire ma demande</a><a class="btn btn--wa" href="{wa('Bonjour Sélune, je voudrais commander un grand format : ')}" target="_blank" rel="noopener" data-magnet data-cursor="WhatsApp">WhatsApp</a></div>
    </div>
    <div class="mhero__slide" data-mslide><span class="mhero__num" aria-hidden="true">01</span><h2 class="mhero__h"><span data-letters>On en</span><span data-letters>parle</span></h2><p class="mhero__p">Votre signe, le nombre de parts, la date : au {TEL_TXT}, sur WhatsApp, en message sur Instagram, ou avec le formulaire plus bas.</p></div>
    <div class="mhero__slide" data-mslide><span class="mhero__num" aria-hidden="true">02</span><h2 class="mhero__h"><span data-letters>Fait</span><span data-letters>maison</span></h2><p class="mhero__p">Préparé chez Sélune, avec intention — comme tout ce qui passe en vitrine.</p></div>
    <div class="mhero__slide" data-mslide><span class="mhero__num" aria-hidden="true">03</span><h2 class="mhero__h"><span data-letters>Vous le</span><span data-letters>retirez</span></h2><p class="mhero__p">Au {ADR}, à Entraigues-sur-la-Sorgue. Le temps d’un thé, si vous voulez.</p></div>
    <div class="mhero__bar"><i id="mBar"></i></div>
  </div>
</section>

<section class="stackcards">
  <header class="stackcards__head"><p class="eyebrow" data-reveal>Idées de commande</p><h2 class="h2" data-letters>Ce qu’on prépare pour vous</h2></header>
  <div class="stackcards__list">{stack}</div>
</section>

<section class="contact" id="demande">
  <div class="contact__grid">
    <div class="contact__info">
      <p class="eyebrow" data-reveal>Votre demande</p>
      <h2 class="h2" data-letters>Commander</h2>
      <dl class="boutique__info">
        <div data-reveal><dt>Par téléphone</dt><dd><a href="{TEL}">{TEL_TXT}</a></dd></div>
        <div data-reveal><dt>Sur WhatsApp</dt><dd><a href="{wa('Bonjour Sélune, je voudrais passer une commande : ')}" target="_blank" rel="noopener">{WA_ICO}Écrire au {TEL_TXT}</a></dd></div>
        <div data-reveal><dt>Sur Instagram</dt><dd><a href="{IG}" target="_blank" rel="noopener">{IG_ICO}@selune_patisserie</a></dd></div>
      </dl>
      {ORDER_FORM}
    </div>
    <div class="contact__map" data-reveal-clip>
      <iframe title="Plan — Sélune, Entraigues-sur-la-Sorgue" src="https://www.google.com/maps?q=S%C3%A9lune,+37+Rue+du+19+Mars+1962,+84320+Entraigues-sur-la-Sorgue&output=embed&z=16" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="btn btn--light contact__go" href="{MAPS}" target="_blank" rel="noopener" data-magnet>Itinéraire</a>
    </div>
  </div>
</section>

<section class="faq">
  <p class="eyebrow" data-reveal>Questions fréquentes</p>
  <h2 class="h2" data-letters>Avant de commander</h2>
  <div class="faq__list">
    <details data-reveal><summary>Le grand format, c’est possible ?</summary><p>Oui : les gâteaux de la collection Astro existent en grand format, sur commande.</p></details>
    <details data-reveal><summary>Y a-t-il du sans gluten ?</summary><p>L’Astro Scorpion (23 octobre – 22 novembre) est sans gluten. Pour le reste, demandez-nous : allergies et intolérances se signalent à la commande.</p></details>
    <details data-reveal><summary>Sur place ou à emporter ?</summary><p>Les deux : le salon de thé vous accueille sur place, et tout se prend aussi à emporter.</p></details>
    <details data-reveal><summary>Comment commander ?</summary><p>Par téléphone ou sur WhatsApp au {TEL_TXT}, en message sur Instagram (@selune_patisserie), ou avec le formulaire ci-dessus.</p></details>
  </div>
</section>
</main>''' + FOOTER + tail())

# ═══════════════════════════ ASTRO ═══════════════════════════
SIGNS = [
  ('balance', 'Balance', 'Octobre · le Soleil en Balance', '#17120E', '#F3E9DA', 'img/astro-balance.webp', 'L’équilibre, l’harmonie des saveurs et la douceur.', ['Biscuit amande', 'Mousse infusée à la verveine', 'Poire pochée à la vanille']),
  ('scorpion', 'Scorpion', '23 octobre – 22 novembre', '#3A3024', '#F3E9DA', 'img/astro-scorpion.webp', 'Un caractère bien trempé, une gourmandise intense — à découvrir jusqu’à fin novembre.', ['Mousse au chocolat noir relevée au piment d’Espelette', 'Biscuit chocolat', 'Cœur de confit de cerise noire', 'Sans gluten']),
  ('sagittaire', 'Sagittaire', '23 novembre – 21 décembre', '#E3D2B4', '#17120E', 'img/astro-sagittaire.webp', 'Le prochain signe de la collection. Sa recette se dévoile sur Instagram — et vous, quel goût lui donneriez-vous ?', ['Recette à venir', 'Annonce sur @selune_patisserie']),
  ('capricorne', 'Capricorne', '22 décembre – 20 janvier', '#F3E9DA', '#17120E', 'img/astro-capricorne.webp', 'Puis viendra le Capricorne. Douze signes, douze gâteaux : un par mois.', ['Recette à venir', 'Grand format sur commande']),
]

def astro():
    words = ''.join(f'<a href="#{k}" class="type-hero__word" style="--c:{bg if i in (2, 3) else "#C9A56B"}" data-letters>{n}</a>' for i, (k, n, when, bg, *_) in enumerate(SIGNS))
    panels = ''
    for i, (k, n, when, bg, fg, img, lead, items) in enumerate(SIGNS):
        lis = ''.join(f'<li>{x}</li>' for x in items)
        panels += f'''
<section class="panel" id="{k}" style="--bg:{bg};--fg:{fg}" data-panel>
  <div class="panel__inner">
    <span class="panel__ghost" aria-hidden="true">{n}</span>
    <figure class="panel__fig"><img src="{img}" alt="" loading="lazy" data-panel-img></figure>
    <div class="panel__text">
      <p class="eyebrow">{when}</p>
      <h2 class="panel__title" data-letters>{n}</h2>
      <p class="panel__lead">{lead}</p>
      <ul class="panel__list">{lis}</ul>
      <a class="link" href="{wa(f'Bonjour Sélune, je voudrais commander l’Astro {n} en grand format.')}" target="_blank" rel="noopener">{WA_ICO}Commander en grand format <i>→</i></a>
    </div>
    <span class="panel__count">0{i+1} / 0{len(SIGNS)}</span>
  </div>
</section>'''
    ig = ''.join(f'<img src="{i}" alt="" loading="lazy">' for i in ['img/sig-1.webp', 'img/croissant.webp', 'img/sig-2.webp', 'img/maison-framboise.webp', 'img/macaron.webp', 'img/tart.webp', 'img/boutique.webp', 'img/gal-2.webp'])
    return (head('La collection Astro — un gâteau par signe — Sélune', 'Chaque mois, Sélune crée un petit gâteau pour le signe astrologique du moment : Balance, Scorpion sans gluten… Grand format sur commande, à Entraigues-sur-la-Sorgue.', 'p-saisons')
        + nav('astro.html')
        + f'''<main id="top">
<section class="type-hero">
  <p class="eyebrow" data-reveal>La collection Astro</p>
  <div class="type-hero__words">{words}</div>
  <p class="type-hero__lead" data-reveal>Chez Sélune, on a la tête dans les étoiles : un petit gâteau par signe astrologique, renouvelé chaque mois. Grand format sur commande. Cliquez un signe.</p>
</section>
<div class="stack">{panels}</div>
<section class="ig-band">
  <p class="eyebrow" data-reveal>Le journal de Sélune, sur Instagram</p>
  <a class="ig-band__handle" href="{IG}" target="_blank" rel="noopener" data-cursor="Ouvrir"><svg class="ig-ico ig-ico--big" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.4" fill="currentColor"/></svg>@selune_patisserie</a>
  <div class="marquee ig-band__row" aria-hidden="true"><div class="marquee__row" data-marquee><span class="ig-band__set">{ig}</span><span class="ig-band__set">{ig}</span></div></div>
</section>
</main>''' + FOOTER + tail())

# ═══════════════════════════ À PROPOS ═══════════════════════════
IG_BADGE = '<svg class="trev__g" viewBox="0 0 24 24" width="20" height="20" fill="none" aria-label="Instagram"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.4" fill="currentColor"/></svg>'

def apropos():
    moments = [('10 h', 'On ouvre', 'La vitrine se remplit : petits gâteaux du jour, l’Astro du mois, le café de Sarrians.'),
               ('12 h', 'Le midi', 'Petite restauration et plat du jour, sur place ou à emporter.'),
               ('16 h', 'Le goûter', 'Une part de cake, un cookie, un chocolat chaud — la formule goûter marche aussi pour les adultes.'),
               ('18 h', 'À demain', f'Le jeudi, on ferme à 18 h. Les grands formats se commandent au {TEL_TXT}.')]
    mm = ''.join(f'<div class="day__moment" data-moment="{i}"><b>{t}</b><h3>{h}</h3><p>{p}</p></div>' for i, (t, h, p) in enumerate(moments))
    steps = [('18 juin 2026', 'La société', 'SELUNE, SARL, est immatriculée à Entraigues-sur-la-Sorgue, avec Julie Vallier pour gérante.', 'Registre'),
             ('2 sept. 2026', 'L’annonce', '« Ça y est, je peux enfin vous l’annoncer… Sélune ouvrira bientôt ses portes à Entraigues-sur-la-Sorgue ! »', 'Instagram'),
             ('15 sept. 2026', 'La décoration', 'Tasseaux de bois, plantes, tableaux : une ambiance cosy, chaleureuse et moderne prend sa place.', 'Instagram'),
             ('18 sept. 2026', 'Le café', 'Le choix du local : le café de la Torréfaction Maison Bres, à Sarrians.', 'Instagram'),
             ('23 sept. 2026', 'Le praliné', 'Mise en place : noisettes torréfiées, caramel, une pointe de fleur de sel.', 'Instagram'),
             ('1er oct. 2026', 'L’ouverture', 'Jeudi, à midi : « Nous avons hâte de vous accueillir pour partager avec vous nos douceurs maison ! »', 'Instagram')]
    cards = ''.join(f'''
    <article class="trev__card" data-reveal>
      <header>{IG_BADGE}<span class="trev__score">{d}</span></header>
      <p class="trev__quote">{q}</p>
      <footer><b>S</b><div><strong>{t}</strong><span>Sélune · {src}</span></div></footer>
    </article>''' for d, t, q, src in steps)
    return (head('La maison — Sélune, pâtisserie & salon de thé à Entraigues-sur-la-Sorgue', 'Sélune, la pâtisserie artisanale et salon de thé de Julie Vallier, ouverte le 1er octobre 2026 au 37 rue du 19 Mars 1962 à Entraigues-sur-la-Sorgue.', 'p-maison')
        + nav('a-propos.html')
        + f'''<main id="top">
<section class="portrait-hero">
  <div class="portrait-hero__text">
    <p class="eyebrow" data-reveal>La maison</p>
    <h1 class="portrait-hero__title" data-letters>La tête dans les étoiles</h1>
    <p class="portrait-hero__lead" data-reveal>Sélune, c’est le projet de Julie Vallier : une pâtisserie artisanale, un salon de thé et une petite restauration du midi, ouverts le 1er octobre 2026 au {ADR}, à Entraigues-sur-la-Sorgue.</p>
    <div class="facts" data-reveal>
      <div class="fact"><b><span data-count="2026">0</span></b><span class="fact__label">1er octobre 2026 · ouverture</span></div>
      <div class="fact"><b><span class="fact__note">4,9</span><i>/5</i></b><span class="fact__stars" aria-label="4,9 sur 5">★★★★★</span><span class="fact__label">Note Google</span></div>
      <div class="fact"><b><span data-count="3">0</span></b><span class="fact__tags"><i>Pâtisserie</i><i>Salon de thé</i><i>Plats du jour</i></span></div>
    </div>
  </div>
  <figure class="portrait-hero__fig tilt" data-tilt data-reveal-clip>
    <div class="tilt__inner"><img src="img/maison-hero.webp" alt="Un entremets servi avec le thé chez Sélune" data-parallax-img></div>
    <span class="portrait-hero__stamp" data-speed="-0.4">Fait<br>maison</span>
  </figure>
</section>

<section class="quote">
  <p class="quote__mark" aria-hidden="true">«</p>
  <p class="quote__text" data-scrub-words>Une pâtisserie artisanale, un salon de thé et une petite restauration du midi, des créations faites maison et de saison, avec passion et gourmandise, dans un cadre chaleureux et accueillant.</p>
</section>

<section class="day" id="journee">
  <div class="day__pin">
    <div class="day__clock" aria-hidden="true">
      <span class="day__halo"></span>
      <span class="day__glow" id="clockGlow"></span>
      <span class="day__disc">
        <span class="day__ticks" id="clockTicks"></span>
        <i class="day__hand" id="clockHand"><b></b></i>
        <span class="day__time" id="clockTime">10 h</span>
      </span>
    </div>
    <div class="day__text">
      <p class="eyebrow">Une journée chez Sélune</p>
      <div class="day__moments">{mm}</div>
      <div class="day__dots" aria-hidden="true">{''.join('<i></i>' for _ in moments)}</div>
    </div>
  </div>
</section>

<section class="trev">
  <p class="trev__eyebrow" data-reveal>De l’idée à l’ouverture</p>
  <h2 class="trev__title" data-reveal>Sélune, <span>pas à pas</span></h2>
  <div class="trev__grid">{cards}
  </div>
  <div class="trev__more" data-reveal><a class="btn btn--light" href="{IG}" target="_blank" rel="noopener" data-cursor="Ouvrir" data-magnet>Suivre Sélune sur Instagram</a></div>
</section>

<section class="addr-band">
  <p class="eyebrow" data-reveal>Venez la goûter</p>
  <a class="addr-band__line" href="{MAPS}" target="_blank" rel="noopener" data-letters data-cursor="Itinéraire">{ADR}</a>
  <a class="addr-band__line addr-band__line--small" href="{MAPS}" target="_blank" rel="noopener" data-letters>{VILLE}</a>
  <div class="cta-band__actions" data-reveal><a class="btn btn--light" href="contact.html" data-magnet>Horaires &amp; accès</a><a class="btn btn--wa" href="{wa()}" target="_blank" rel="noopener" data-cursor="WhatsApp" data-magnet>WhatsApp</a><a class="btn btn--ghost" href="{TEL}" data-magnet>{TEL_TXT}</a></div>
</section>
</main>''' + FOOTER + tail())

# ═══════════════════════════ CONTACT ═══════════════════════════
def contact():
    return (head('Contact & accès — Sélune, 37 rue du 19 Mars 1962, Entraigues-sur-la-Sorgue', 'Adresse, téléphone et accès de Sélune, pâtisserie et salon de thé à Entraigues-sur-la-Sorgue (84320). Commandes au 06 30 16 89 40.', 'p-contact')
        + nav('contact.html')
        + f'''<main id="top">
<section class="tel-hero">
  <p class="eyebrow" data-reveal>Commandes &amp; questions</p>
  <a class="tel-hero__num" href="{TEL}" data-letters data-cursor="Appeler">{TEL_TXT}</a>
  <p class="tel-hero__now" id="openNow" data-reveal></p>
  <div class="tel-hero__wa" data-reveal><a class="btn btn--wa" href="{wa()}" target="_blank" rel="noopener" data-cursor="WhatsApp" data-magnet>Écrire sur WhatsApp</a></div>
  <div class="tel-hero__alt" data-reveal><a href="{IG}" target="_blank" rel="noopener">{IG_ICO}@selune_patisserie</a> · <a href="{MAPS}" target="_blank" rel="noopener">Fiche Google Maps</a></div>
</section>

<section class="hours">
  <div class="hours__grid">
    <div class="hours__day" data-3d><b>Matin</b><span>Ouverture</span><span>dès 10 h</span></div>
    <div class="hours__day" data-3d><b>Midi</b><span>Plat du jour</span><span>sur place ou à emporter</span></div>
    <div class="hours__day" data-3d><b>Goûter</b><span>Cookies, cakes</span><span>chocolat chaud</span></div>
    <div class="hours__day" data-3d><b>Jeudi</b><span>10 h – 18 h</span></div>
  </div>
</section>

<section class="contact">
  <div class="contact__grid">
    <div class="contact__info">
      <dl class="boutique__info">
        <div data-reveal><dt>Adresse</dt><dd><a href="{MAPS}" target="_blank" rel="noopener" data-cursor="Itinéraire">{ADR}<br>{VILLE}</a></dd></div>
        <div data-reveal><dt>Sur place</dt><dd><small>Salon de thé · pâtisserie fine · plats du jour le midi · tout se prend aussi à emporter</small></dd></div>
      </dl>
      {ORDER_FORM}
    </div>
    <div class="contact__map" data-reveal-clip>
      <iframe title="Plan — Sélune, Entraigues-sur-la-Sorgue" src="https://www.google.com/maps?q=S%C3%A9lune,+37+Rue+du+19+Mars+1962,+84320+Entraigues-sur-la-Sorgue&output=embed&z=16" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="btn btn--light contact__go" href="{MAPS}" target="_blank" rel="noopener" data-magnet>Itinéraire</a>
    </div>
  </div>
</section>
</main>''' + FOOTER + tail())

# ═══════════════════════════ MENTIONS ═══════════════════════════
def mentions():
    return (head('Mentions légales, CGV & confidentialité — Sélune', 'Informations légales, conditions générales de vente pour les commandes et politique de confidentialité de Sélune, Entraigues-sur-la-Sorgue.', 'p-legal')
        + nav('')
        + f'''<main id="top">
<section class="legal-hero">
  <p class="eyebrow" data-reveal>Informations légales</p>
  <h1 data-letters>Mentions légales</h1>
</section>
<section class="legal">
  <nav class="legal__nav" data-reveal><a href="#editeur">Éditeur</a><a href="#cgv">CGV commandes</a><a href="#confidentialite">Confidentialité</a><a href="#credits">Crédits</a></nav>
  <article class="legal__body">
    <h2 id="editeur" data-letters>Éditeur du site</h2>
    <p data-reveal>SELUNE, société à responsabilité limitée.<br>Siège : {ADR}, {VILLE}, France.<br>SIREN 106 670 060 · SIRET 106 670 060 00016 · Code NAF 10.71D (pâtisserie).<br>Capital social, RCS et TVA intracommunautaire : <em>à compléter</em>.<br>Téléphone : {TEL_TXT}.<br>Gérante et directrice de la publication : Julie Vallier.</p>
    <p data-reveal>Hébergement : <em>à compléter (prestataire, adresse, téléphone)</em>.</p>

    <h2 id="cgv" data-letters>Conditions générales de vente — commandes</h2>
    <p data-reveal><strong>Commande.</strong> Les commandes (grands formats, gâteaux de la collection Astro) se passent en boutique, par téléphone ou par message. Une commande est confirmée lorsque Sélune l’a acceptée et en a précisé le prix et la date de retrait.</p>
    <p data-reveal><strong>Prix et paiement.</strong> Prix TTC, affichés en boutique ou indiqués à la commande. Modalités de paiement et d’acompte : <em>à compléter</em>.</p>
    <p data-reveal><strong>Retrait.</strong> Les commandes se retirent à la boutique, {ADR}, {VILLE}, à la date convenue.</p>
    <p data-reveal><strong>Annulation.</strong> Toute annulation doit être signalée au plus tôt. Conditions : <em>à compléter</em>.</p>
    <p data-reveal><strong>Allergènes.</strong> Les recettes peuvent contenir notamment gluten, lait, œufs et fruits à coque (noisette, amande). Signalez toute allergie à la commande.</p>
    <p data-reveal><strong>Conservation.</strong> Les pâtisseries fraîches se conservent au réfrigérateur et se consomment rapidement, selon les indications données au retrait.</p>
    <p data-reveal><strong>Litiges.</strong> En cas de difficulté, contactez d’abord la boutique. Médiation de la consommation : <em>médiateur à désigner</em>. À défaut, les tribunaux compétents sont ceux du ressort d’Avignon.</p>

    <h2 id="confidentialite" data-letters>Données personnelles</h2>
    <p data-reveal>Les formulaires de ce site ouvrent votre application WhatsApp : les informations saisies (nom, téléphone, date, message) sont envoyées par vous-même au {TEL_TXT}, via WhatsApp (Meta), et servent uniquement à traiter votre demande. Le site ne les stocke pas et ne les transmet à aucun autre tiers. Vous pouvez demander leur suppression au même numéro.</p>
    <p data-reveal>Ce site n’utilise pas de cookies de suivi. La carte interactive est fournie par Google Maps, qui peut déposer ses propres cookies lors de son chargement.</p>

    <h2 id="credits" data-letters>Crédits</h2>
    <p data-reveal>Conception et réalisation : <em>à compléter</em>. Photographies : Sélune (Instagram @selune_patisserie) ; visuels et vidéos d’illustration Pexels (licence Pexels), <em>à remplacer par des photos de la boutique</em>. Polices : Urbanist, Inter (licences SIL OFL).</p>
  </article>
</section>
</main>''' + FOOTER + tail())

PAGES = {'carte.html': carte, 'astro.html': astro, 'commandes.html': commandes, 'a-propos.html': apropos, 'contact.html': contact, 'mentions-legales.html': mentions}
for f, fn in PAGES.items():
    open(f, 'w', encoding='utf-8').write(fn())
    print('ecrit', f)

# ── index.html : nav vers les pages ──
p = 'index.html'; s = open(p, encoding='utf-8').read()
links = ''.join(f'<a href="{h}">{l}</a>' for h, l in NAV_LINKS)
s = re.sub(r'<nav class="nav__links">.*?</nav>', f'<nav class="nav__links">{links}</nav>', s, flags=re.S)
s = re.sub(r'<div class="menu" id="menu">.*?</div>', f'<div class="menu" id="menu">\n  {links}\n</div>', s, flags=re.S)
open(p, 'w', encoding='utf-8').write(s)
print('index.html mis a jour')
