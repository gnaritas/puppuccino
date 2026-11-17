#!/usr/bin/env python3
"""Generate the Puppuccino site (template v2 T1, 2026-11-16).
Puppuccino-parlor identity: cream/cocoa/cinnamon, monoline cup-and-swirl art,
geometric display caps over serif body. Zero third-party JS, one local stylesheet.
Copy ONLY from the prospect card's verified facts (Inland NW Business Watch 2026-11-05,
the shop's own FB About tab, Confident K9 sister site, OSM geocode)."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")
ORIGIN = "https://puppuccino-demo.up.railway.app"
NAME = "Puppuccino"
STREET = "5802 E Sprague Ave"
CITYZIP = "Spokane Valley, WA 99212"
NAP = f"{STREET}, {CITYZIP}"
TEL_H, TEL_T = "(509) 768-1353", "+15097681353"
EMAIL = "confidentk9spokane@gmail.com"
LAT, LON = 47.6570047, -117.3271807
FB = "https://www.facebook.com/profile.php?id=61594084052457"
IG = "https://www.instagram.com/puppucinospokane/"
CK9 = "https://confidentk9trainers.com"
Q = f"{STREET.replace(' ', '%20')},%20{CITYZIP.replace(' ', '%20').replace(',', '%2C')}"
DIR = f"https://www.google.com/maps/dir/?api=1&destination={Q}"
MAPSRC = f"https://www.google.com/maps?q={Q}&output=embed"
OG = ORIGIN + "/og.png"

PAW = '<svg class="paw" viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="6.2" cy="9.4" rx="2.1" ry="2.7"/><ellipse cx="11" cy="6.9" rx="2.1" ry="2.8"/><ellipse cx="16" cy="7.9" rx="2" ry="2.6"/><ellipse cx="20" cy="12" rx="1.9" ry="2.3"/><path d="M12.6 13.2c3.4 0 6.4 2.4 6.4 5 0 2.1-1.9 3.2-4.2 3.2h-6c-2.3 0-4.2-1.1-4.2-3.2 0-2.6 4.6-5 8-5z"/></svg>'

BRAND = ('<a class="brand" href="/"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" '
         'stroke="#2E1C12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
         '<path d="M9.5 15.5h13l-1.7 12.2a1.6 1.6 0 0 1-1.6 1.3h-6.4a1.6 1.6 0 0 1-1.6-1.3z" fill="#FFFCF4"/>'
         '<path d="M8 15.5c0-3.4 3.6-5.2 8-5.2s8 1.8 8 5.2" fill="#FFFCF4"/>'
         '<path d="M11 10.6c.4-2.5 2.4-3.9 5-3.9s4.6 1.4 5 3.9" fill="#FFFCF4"/>'
         '<path d="M13.6 6.5c.7-1.6 1.6-2.4 2.4-2.4s1.7.8 2.4 2.4" fill="#FFFCF4"/>'
         '<circle cx="16" cy="2.6" r="1.1" fill="#B93958" stroke="none"/></svg>Puppuccino</a>')

NAV = (f'<nav aria-label="Main">'
       f'<a href="/pup-bar">The Pup Bar</a>'
       f'<a href="/pet-shop">The Pet Shop</a>'
       f'<a href="/training-essentials">Training Gear</a>'
       f'<a href="/contact">Contact</a>'
       f'<a class="tel" href="tel:{TEL_T}">☎ {TEL_H}</a>'
       f'</nav>')

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>Puppuccino</h4>
        <address class="nap">Custom pup cup bar &amp; pet shop<br>
        {STREET}<br>{CITYZIP}<br>
        <a href="tel:{TEL_T}">☎ {TEL_H}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/pup-bar">The Pup Bar</a></li>
          <li><a href="/custom-pup-cups">Custom Pup Cups</a></li>
          <li><a href="/pet-shop">The Pet Shop</a></li>
          <li><a href="/training-essentials">Training Essentials</a></li>
          <li><a href="/contact">Contact &amp; Directions</a></li>
          <li><a href="/privacy">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h4>Follow Along</h4>
        <ul>
          <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="{DIR}" target="_blank" rel="noopener">Get directions</a></li>
        </ul>
      </div>
    </div>
    <div class="footline"><span>© 2026 {NAME} · {NAP} · {TEL_H}</span><span>{PAW} Locally owned &amp; operated</span></div>
  </div>
</footer>"""

def head(title, desc, path, noindex=False):
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{ORIGIN}{path}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{OG}">
  <meta property="og:url" content="{ORIGIN}{path}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/style.css">{robots}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site">
    <div class="bar">
      {BRAND}
      {NAV}
    </div>
  </header>
"""

def ld(blocks):
    return "".join(f'  <script type="application/ld+json">\n{j}\n  </script>\n'
                   for j in (json.dumps(b, indent=1).replace("\n", "\n  ") for b in blocks))

SHOP = {
    "@type": "PetStore", "@id": ORIGIN + "/#shop", "name": NAME,
    "description": "Customizable puppuccino (pup cup) bar and pet retail store — treats, toys and training essentials — in Spokane Valley, WA.",
    "image": OG, "url": ORIGIN + "/", "telephone": "+1-509-768-1353",
    "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": "Spokane Valley",
                "addressRegion": "WA", "postalCode": "99212", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
    "hasMap": DIR,
    "sameAs": [FB, IG],
}

def shop_ref():
    return {"@type": "PetStore", "@id": ORIGIN + "/#shop", "name": NAME, "url": ORIGIN + "/",
            "telephone": "+1-509-768-1353",
            "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": "Spokane Valley",
                        "addressRegion": "WA", "postalCode": "99212", "addressCountry": "US"}}

def crumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                 "name": n, "item": ORIGIN + p} for i, (n, p) in enumerate(items)]}

CTX = {"@context": "https://schema.org"}

def page(path, fname, title, desc, body, blocks, band=None, noindex=False):
    html = head(title, desc, path, noindex)
    html += '<main id="main">\n'
    if band:
        html += band
    html += body + "\n</main>\n" + FOOTER + "\n"
    if blocks:
        html += ld(blocks)
    html += "  <!-- BUILT-2026-11-16 -->\n</body>\n</html>\n"
    # ensure ld lands before closing body; simpler: append before </body>
    os.makedirs(PUB, exist_ok=True)
    with open(os.path.join(PUB, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

# ---------------------------------------------------------------- HOME
HOME_BAND = f"""  <div class="hero">
    <div class="wrap">
      <div>
        <div class="kicker">{PAW} Spokane Valley's puppuccino bar</div>
        <h1>Custom pup cups,<br>built for your dog.</h1>
        <p class="lede" style="margin-top:18px">{NAME} is Spokane's first customizable puppuccino bar —
        a pup cup counter with a pet shop beside it, stocked with treats, toys
        and training essentials. Locally owned and operated.</p>
        <div class="acts">
          <a class="btn" href="tel:{TEL_T}">Call {TEL_H}</a>
          <a class="btn ghost" href="/contact">Plan a visit</a>
        </div>
      </div>
      <div>
        <svg class="cupart" viewBox="0 0 320 340" role="img" aria-label="Illustration of a puppuccino: a cup of soft swirl topped with a berry">
          <path d="M96 168h128l-16 148a12 12 0 0 1-12 10h-72a12 12 0 0 1-12-10z" fill="#FFFCF4" stroke="#2E1C12" stroke-width="5"/>
          <path d="M118 196l-6 120M202 196l6 120" stroke="#B93958" stroke-width="4" stroke-linecap="round" opacity=".45"/>
          <path d="M82 168c0-26 35-41 78-41s78 15 78 41z" fill="#FFFCF4" stroke="#2E1C12" stroke-width="5"/>
          <path d="M104 130c0-21 25-33 56-33s56 12 56 33" fill="#FFFCF4" stroke="#2E1C12" stroke-width="5"/>
          <path d="M122 100c0-16 17-25 38-25s38 9 38 25" fill="#FFFCF4" stroke="#2E1C12" stroke-width="5"/>
          <path d="M138 77c4-12 10-18 22-18s18 6 22 18" fill="#FFFCF4" stroke="#2E1C12" stroke-width="5"/>
          <circle cx="160" cy="44" r="10" fill="#B93958" stroke="#2E1C12" stroke-width="4"/>
          <path d="M120 148q20 10 40 0t40 0" stroke="#C05B1D" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/>
          <path d="M132 118q14 8 28 0t28 0" stroke="#C05B1D" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/>
          <g transform="translate(38 250) scale(1.15)" fill="#C05B1D">
            <ellipse cx="6.2" cy="9.4" rx="2.1" ry="2.7"/><ellipse cx="11" cy="6.9" rx="2.1" ry="2.8"/>
            <ellipse cx="16" cy="7.9" rx="2" ry="2.6"/><ellipse cx="20" cy="12" rx="1.9" ry="2.3"/>
            <path d="M12.6 13.2c3.4 0 6.4 2.4 6.4 5 0 2.1-1.9 3.2-4.2 3.2h-6c-2.3 0-4.2-1.1-4.2-3.2 0-2.6 4.6-5 8-5z"/>
          </g>
        </svg>
      </div>
    </div>
  </div>
  <div class="sprinkle"></div>
"""

HOME_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} Two counters, one suite</div>
      <h2>A pup cup bar with a pet shop attached</h2>
      <p class="lede">At {STREET.replace(' ', '&nbsp;')} in Spokane Valley — the same suite where the owner
      runs <a href="{CK9}" target="_blank" rel="noopener">Confident K9 Training</a> — the shop does two things:
      builds fresh puppuccinos to order, and stocks the goods dog owners actually run out of.</p>
      <div class="cardgrid">
        <div class="card wafer">
          <svg class="ic" viewBox="0 0 40 40"><path d="M11 19h18l-2.2 16.5a2 2 0 0 1-2 1.7h-9.6a2 2 0 0 1-2-1.7z"/><path d="M9 19c0-5 4.9-7.5 11-7.5S31 14 31 19"/><path d="M14 12.5c.5-3 2.6-4.5 6-4.5s5.5 1.5 6 4.5"/><path d="M17 8.8c1-2 2-3 3-3s2 1 3 3"/></svg>
          <h3><a href="/pup-bar">The Pup Bar</a></h3>
          <p>Every puppuccino is built to order at the pup cup bar — customized for the dog in front of you.
          Human drinks and snacks are on the way.</p>
          <a class="more" href="/custom-pup-cups">Custom pup cups →</a>
        </div>
        <div class="card wafer">
          <svg class="ic" viewBox="0 0 40 40"><path d="M12 26c-3.6 0-6.5-2.6-6.5-6S8.4 14 12 14h16c3.6 0 6.5 2.6 6.5 6s-2.9 6-6.5 6z"/><path d="M8.5 14l2-5h19l2 5"/><path d="M20 26v6M14 32h12"/></svg>
          <h3><a href="/pet-shop">The Pet Shop</a></h3>
          <p>Treats, training tools, harnesses, leashes, toys, interactive toys, bowls, plants
          and 3D-printed finds — plus the extras that catch your eye.</p>
          <a class="more" href="/training-essentials">Training essentials →</a>
        </div>
      </div>
      <div class="note">
        <p class="big"><strong>Canine forward, all welcome.</strong> The four-legged guests are the whole point —
        drinks and snacks for their people are in the works, so the plan is a stop the entire pack can enjoy.</p>
      </div>
    </div>
  </section>

  <section class="tight" style="background:var(--paper);border-top:1.5px solid var(--line);border-bottom:1.5px solid var(--line)">
    <div class="wrap">
      <div class="kicker">{PAW} Find the shop</div>
      <h2>Same suite as Confident K9 Training</h2>
      <div class="findgrid">
        <div class="infocard wafer">
          <p class="nap"><strong>{NAME}</strong><br>{STREET}<br>{CITYZIP}<br>
          <a href="tel:{TEL_T}">☎ {TEL_H}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <h4>Reach us</h4>
          <p><a href="{DIR}" target="_blank" rel="noopener">Get directions</a> ·
          <a href="{FB}" target="_blank" rel="noopener">Facebook</a> ·
          <a href="{IG}" target="_blank" rel="noopener">Instagram</a></p>
          <p class="small" style="margin-bottom:0">Call ahead and the counter can tell you what's on today.</p>
        </div>
        <div class="mapcard">
          <iframe src="{MAPSRC}" title="Map showing Puppuccino at {NAP}" loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </section>

  <section class="faq">
    <div class="wrap">
      <div class="kicker">{PAW} Good to know</div>
      <h2>Questions dog owners ask</h2>
      <details open>
        <summary>What exactly is a puppuccino?</summary>
        <div class="a"><p>A frozen pup cup — a dog-sized frozen treat served in a cup — built to order at
        the bar and customized the way your pup likes it.</p></div>
      </details>
      <details>
        <summary>What can I buy in the shop?</summary>
        <div class="a"><p>Treats, training tools, harnesses, leashes, toys, interactive toys, bowls,
        plants and 3D-printed items — the retail side is stocked with the goods owners actually run out of.</p></div>
      </details>
      <details>
        <summary>Are humans welcome too?</summary>
        <div class="a"><p>Yes. The shop is canine forward, and drinks and snacks for people are in the works.</p></div>
      </details>
      <details>
        <summary>Where exactly are you?</summary>
        <div class="a"><p>{STREET}, {CITYZIP} — the same suite where the owner runs the
        <a href="{CK9}" target="_blank" rel="noopener">Confident K9 Training</a> dog-training business.</p></div>
      </details>
      <details>
        <summary>How do I check what's on today?</summary>
        <div class="a"><p>Call <a href="tel:{TEL_T}">{TEL_H}</a> or message the shop on
        <a href="{FB}" target="_blank" rel="noopener">Facebook</a> — that's where the day's specials get posted.</p></div>
      </details>
    </div>
  </section>
"""

HOME_FAQ = {"@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": "What exactly is a puppuccino?",
     "acceptedAnswer": {"@type": "Answer", "text": "A frozen pup cup — a dog-sized frozen treat served in a cup — built to order at the bar and customized the way your pup likes it."}},
    {"@type": "Question", "name": "What can I buy in the shop?",
     "acceptedAnswer": {"@type": "Answer", "text": "Treats, training tools, harnesses, leashes, toys, interactive toys, bowls, plants and 3D-printed items."}},
    {"@type": "Question", "name": "Are humans welcome too?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes. The shop is canine forward, and drinks and snacks for people are in the works."}},
    {"@type": "Question", "name": "Where exactly are you?",
     "acceptedAnswer": {"@type": "Answer", "text": f"{STREET}, {CITYZIP} — the same suite where the owner runs the Confident K9 Training dog-training business."}},
]}

page("/", "index.html",
     f"{NAME} — Custom Pup Cup Bar &amp; Pet Shop, Spokane Valley WA",
     f"{NAME} is Spokane's first customizable puppuccino bar — pup cups built to order, plus a pet shop with treats, toys and training essentials at {NAP}. Call {TEL_H}.",
     HOME_BODY,
     [dict(CTX, **SHOP),
      {**CTX, "@type": "WebSite", "name": NAME, "url": ORIGIN + "/", "publisher": {"@id": ORIGIN + "/#shop"}},
      dict(CTX, **HOME_FAQ)],
     band=HOME_BAND)

# ---------------------------------------------------------------- PUP BAR (hub)
def band(kicker, title, lede, crumb):
    c = " · ".join(f'<a href="{p}">{n}</a>' if p != "#" else n for n, p in crumb)
    return f"""  <div class="band">
    <div class="wrap">
      <div class="crumbs">{c}</div>
      <div class="kicker">{PAW} {kicker}</div>
      <h1>{title}</h1>
      <p class="lede">{lede}</p>
    </div>
  </div>
"""

PUPBAR_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} How the bar works</div>
      <h2>Built the way your dog likes it</h2>
      <div class="steps">
        <div class="step"><span class="num">1</span><h3>Bring your pup</h3>
          <p>Come by the suite at {STREET} — leashed guests are the whole point of the visit.</p></div>
        <div class="step"><span class="num">2</span><h3>Say how they like it</h3>
          <p>The bar is fully customizable: order the puppuccino for the dog standing in front of you, not a fixed menu item.</p></div>
        <div class="step"><span class="num">3</span><h3>They get a cup</h3>
          <p>A fresh puppuccino, made to order at the counter while you wait.</p></div>
      </div>
      <div class="note">
        <p class="big">Drinks and snacks for the humans on leash are in the works — today it's the pups who get the counter,
        soon the rest of the pack will too.</p>
        <p style="margin-bottom:0">Go deeper on the bar: <a href="/custom-pup-cups">custom puppuccinos in Spokane Valley</a>.</p>
      </div>
    </div>
  </section>
"""
page("/pup-bar", "pup-bar.html",
     f"Pup Cup Bar — {NAME}, Spokane Valley WA",
     f"The puppuccino bar at {NAME} in Spokane Valley: every frozen pup cup is built to order and customized for your dog. Call {TEL_H}.",
     PUPBAR_BODY,
     [{**CTX, "@type": "Service", "serviceType": "Custom pup cup bar",
           "name": "Custom Puppuccino Bar", "provider": shop_ref(),
           "areaServed": {"@type": "City", "name": "Spokane Valley, WA"},
           "url": ORIGIN + "/pup-bar"},
      crumbs([("Home", "/"), ("The Pup Bar", "/pup-bar")])],
     band("The pup bar", "A puppuccino,<br>made to order.",
          f"At the pup cup bar, every frozen treat is customized for the dog in front of you — no fixed menu, no guessing what your pup will actually eat.",
          [("Home", "/"), ("The Pup Bar", "#")]))

# ---------------------------------------------------------------- CUSTOM PUP CUPS (detail 1)
CUPS_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} The treat</div>
      <h2>What a puppuccino is</h2>
      <div class="prose">
        <p>A puppuccino is a <strong>pup cup</strong> — a dog-sized frozen treat served in a cup — and here it isn't
        off the menu, it's built your dog's way. The bar at {NAME} is fully customizable, so the cup that lands
        in front of your pup is the one you ordered for them.</p>
        <p>The shop is <strong>canine forward</strong>: these cups are made for dogs, the guests who get the counter.
        Drinks and snacks for their people are in the works.</p>
        <h2>Where to pick one up</h2>
        <p>{NAME} sits at <strong>{STREET}, {CITYZIP}</strong> — the same suite where the owner runs
        <a href="{CK9}" target="_blank" rel="noopener">Confident K9 Training</a> — one owner, both businesses,
        one door on Sprague. Grab a pup cup before a training session, after one, or on the way through the Valley.</p>
        <h2>Not just a treat shop</h2>
        <p>The shelves beside the bar carry treats, toys, bowls and training gear —
        see <a href="/pet-shop">the pet shop</a> — and the shop has hosted Trunk-or-Treat parties for the
        local pack, so watch <a href="{FB}" target="_blank" rel="noopener">Facebook</a> for the next event.</p>
      </div>
      <div class="acts">
        <a class="btn" href="tel:{TEL_T}">Call {TEL_H}</a>
        <a class="btn ghost" href="/contact">Get directions</a>
      </div>
    </div>
  </section>
"""
page("/custom-pup-cups", "custom-pup-cups.html",
     f"Custom Puppuccinos — {NAME}, Spokane Valley WA",
     f"Custom pup cups in Spokane Valley: every puppuccino at {NAME} is built to order for your dog, at {STREET}. Call {TEL_H}.",
     CUPS_BODY,
     [{**CTX, "@type": "Service", "serviceType": "Pup cups — frozen dog treats built to order",
           "name": "Custom Puppuccinos", "provider": shop_ref(),
           "areaServed": {"@type": "City", "name": "Spokane Valley, WA"},
           "url": ORIGIN + "/custom-pup-cups"},
      crumbs([("Home", "/"), ("The Pup Bar", "/pup-bar"), ("Custom Pup Cups", "/custom-pup-cups")])],
     band("Custom pup cups", "Custom pup cups<br>in Spokane Valley.",
          "A frozen treat for your dog, built at the bar the way they like it — this is the counter the shop is named for.",
          [("Home", "/"), ("The Pup Bar", "/pup-bar"), ("Custom Pup Cups", "#")]))

# ---------------------------------------------------------------- PET SHOP (hub)
def tile(icon, title, blurb):
    return (f'<div class="tile"><svg viewBox="0 0 40 40" aria-hidden="true">{icon}</svg>'
            f"<h3>{title}</h3><p>{blurb}</p></div>")

T_ICONS = {
    "treats": '<path d="M12 26c-3.6 0-6.5-2.6-6.5-6S8.4 14 12 14h16c3.6 0 6.5 2.6 6.5 6s-2.9 6-6.5 6z"/><path d="M8.5 14l2-5h19l2 5"/><path d="M20 26v6M14 32h12"/>',
    "training": '<circle cx="14.5" cy="14.5" r="7.5"/><circle cx="14.5" cy="14.5" r="1.6"/><path d="M20 19l13 13"/><path d="M29 22l6 6-3 3-6-6"/>',
    "harness": '<path d="M20 6v28"/><path d="M12 12h16"/><path d="M10 20h20"/><path d="M14 27c0-3 2.7-5 6-5s6 2 6 5"/>',
    "leash": '<path d="M10 31c8-2 14-9 16-18"/><path d="M26 13a5 5 0 1 1 4 4l-4 2"/><path d="M7 28a3 3 0 1 0 6 0 3 3 0 0 0-6 0z"/>',
    "toys": '<circle cx="20" cy="20" r="12"/><path d="M8 15c8 3 16 3 24 0M8 25c8-3 16-3 24 0"/>',
    "interactive": '<rect x="7" y="7" width="26" height="26" rx="7"/><circle cx="15" cy="15" r="3.5"/><circle cx="25.5" cy="15.5" r="3"/><circle cx="20" cy="26" r="3.5"/>',
    "bowls": '<path d="M6 17h28c0 7.7-6.3 14-14 14S6 24.7 6 17z"/><path d="M13 17c0-3.9 3.1-7 7-7s7 3.1 7 7"/><path d="M20 10V6"/>',
    "plants": '<path d="M13 22h14l-2 12h-10z"/><path d="M20 22V9"/><path d="M20 13c-1-4 1-7 5-8 0 4-1 7-5 8zM20 16c1-3.5-1-6.5-5-7 0 3.5 1 6 5 7z"/>',
    "cubed": '<path d="M20 6l12 6v16l-12 6-12-6V12z"/><path d="M8 12l12 6 12-6M20 18v16"/>',
}
PETSHOP_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} The retail side</div>
      <h2>What's on the shelves</h2>
      <p class="lede">Beside the pup cup bar, the shop carries the goods dog owners actually run out of —
      chosen by people who train dogs for a living. And the "and more" is real: browse the racks and see.</p>
      <div class="tiles">
        {tile(T_ICONS["treats"], "Treats", "The reason dogs ask to come in.")}
        {tile(T_ICONS["training"], "Training tools", "Gear picked by the team that runs Confident K9 Training.")}
        {tile(T_ICONS["harness"], "Harnesses", "Walk-ready fits for the Valley stroll.")}
        {tile(T_ICONS["leash"], "Leashes", "Clip on at the door, go straight to the bar.")}
        {tile(T_ICONS["toys"], "Toys", "The fetch-and-chew classics.")}
        {tile(T_ICONS["interactive"], "Interactive toys", "Keep the smart ones busy at home.")}
        {tile(T_ICONS["bowls"], "Bowls", "Mealtime hardware.")}
        {tile(T_ICONS["plants"], "Plants", "Yes, for the humans.")}
        {tile(T_ICONS["cubed"], "3D-printed finds", "One-of-a-kind items you won't spot at the big-box pet store.")}
      </div>
      <div class="note">
        <p class="big"><strong>Picked by a training team.</strong> The shop is run by the owner of
        <a href="{CK9}" target="_blank" rel="noopener">Confident K9 Training</a> — the same suite, the same dogs
        on the schedule — so the wall of training tools is stocked by people who use them every day.</p>
        <p style="margin-bottom:0">More on that wall: <a href="/training-essentials">training essentials &amp; gear</a>.</p>
      </div>
    </div>
  </section>
"""
page("/pet-shop", "pet-shop.html",
     f"Pet Shop — {NAME}, Spokane Valley WA",
     f"Pet shop at {NAME}, {NAP}: treats, training tools, harnesses, leashes, toys, bowls, plants and 3D-printed finds. Call {TEL_H}.",
     PETSHOP_BODY,
     [dict(CTX, **SHOP, hasOfferCatalog={"@type": "OfferCatalog", "name": "Shop inventory",
          "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Thing", "name": n}} for n in
          ["Treats", "Training tools", "Harnesses", "Leashes", "Toys", "Interactive toys", "Bowls", "Plants", "3D-printed items"]]}),
      crumbs([("Home", "/"), ("The Pet Shop", "/pet-shop")])],
     band("The pet shop", "Treats, toys and<br>training essentials.",
          "The retail side of the shop — stocked with the goods owners run out of, beside the counter that makes the puppuccinos.",
          [("Home", "/"), ("The Pet Shop", "#")]))

# ---------------------------------------------------------------- TRAINING ESSENTIALS (detail 2)
TRAIN_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} The training wall</div>
      <h2>Tools, harnesses and leashes — chosen by a trainer</h2>
      <div class="prose">
        <p>The training tools, harnesses and leashes at {NAME} come from the same hands that run
        <a href="{CK9}" target="_blank" rel="noopener">Confident K9 Training</a> in the same suite at
        {STREET}. When the person stocking the wall is the person training the dogs, the gear tends to
        be the stuff that actually works.</p>
        <h2>The pup cup as a reward</h2>
        <p>Training runs on good rewards, and a frozen pup cup built to order makes a memorable one.
        Ask the counter how the regulars put their puppuccinos to use after a session next door —
        the shop and the training business share a door, a suite and a client list.</p>
        <h2>While you're here</h2>
        <p>The rest of the racks: treats, toys, interactive toys, bowls, plants and 3D-printed finds —
        the full shelf list is on <a href="/pet-shop">the pet shop page</a>.</p>
      </div>
      <div class="acts">
        <a class="btn" href="tel:{TEL_T}">Call {TEL_H}</a>
        <a class="btn ghost" href="/contact">Contact &amp; directions</a>
      </div>
    </div>
  </section>
"""
page("/training-essentials", "training-essentials.html",
     f"Dog Training Tools &amp; Gear — {NAME}, Spokane Valley WA",
     f"Training tools, harnesses and leashes at {NAME}, {NAP} — chosen by the owner of Confident K9 Training. Call {TEL_H}.",
     TRAIN_BODY,
     [{**CTX, "@type": "Service", "serviceType": "Dog training tools and gear",
           "name": "Training Essentials", "provider": shop_ref(),
           "areaServed": {"@type": "City", "name": "Spokane Valley, WA"},
           "url": ORIGIN + "/training-essentials"},
      crumbs([("Home", "/"), ("The Pet Shop", "/pet-shop"), ("Training Essentials", "/training-essentials")])],
     band("Training gear", "Training tools,<br>chosen by a trainer.",
          "A training wall stocked by the same team that runs Confident K9 Training — gear that actually works, bought where the pup cups are.",
          [("Home", "/"), ("The Pet Shop", "/pet-shop"), ("Training Essentials", "#")]))

# ---------------------------------------------------------------- CONTACT
CONTACT_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} Contact &amp; directions</div>
      <h2>Come by with your pup</h2>
      <div class="cgrid">
        <div class="infocard wafer">
          <p class="nap"><strong>{NAME}</strong><br>{STREET}<br>{CITYZIP}<br>
          <a href="tel:{TEL_T}">☎ {TEL_H}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <h4>Hours today</h4>
          <p>Call <a href="tel:{TEL_T}">{TEL_H}</a> and the counter will tell you what's on and when the doors are open.</p>
          <h4>Elsewhere</h4>
          <p style="margin-bottom:0"><a href="{FB}" target="_blank" rel="noopener">Facebook</a> ·
          <a href="{IG}" target="_blank" rel="noopener">Instagram</a> ·
          <a href="{DIR}" target="_blank" rel="noopener">Directions</a></p>
        </div>
        <form class="cform" method="post" action="/contact">
          <div>
            <label for="f-name">Your name</label>
            <input id="f-name" name="name" autocomplete="name" required>
          </div>
          <div class="row">
            <div>
              <label for="f-phone">Phone (optional)</label>
              <input id="f-phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div>
              <label for="f-email">Email</label>
              <input id="f-email" name="email" type="email" autocomplete="email">
            </div>
          </div>
          <div>
            <label for="f-message">Your message</label>
            <textarea id="f-message" name="message" required placeholder="A question, a pup-cup order, or just a hello — tell us about your dog."></textarea>
          </div>
          <button class="btn" type="submit">Send the shop a note</button>
          <p class="small" style="margin:0">We answer as fast as the counter allows.</p>
        </form>
      </div>
    </div>
  </section>
  <section class="tight" style="background:var(--paper);border-top:1.5px solid var(--line)">
    <div class="wrap">
      <div class="kicker">{PAW} On the map</div>
      <h2>{STREET}</h2>
      <div class="mapcard" style="margin-top:18px">
        <iframe src="{MAPSRC}" title="Map showing Puppuccino at {NAP}" loading="lazy"></iframe>
      </div>
    </div>
  </section>
"""
page("/contact", "contact.html",
     f"Contact &amp; Directions — {NAME}, Spokane Valley WA",
     f"Contact {NAME}, {NAP}. Call {TEL_H} or email {EMAIL} — pup-cup questions, gear questions, anything dog.",
     CONTACT_BODY,
     [{**CTX, "@type": "ContactPage", "name": f"Contact &amp; Directions — {NAME}", "url": ORIGIN + "/contact",
           "about": shop_ref()},
      crumbs([("Home", "/"), ("Contact & Directions", "/contact")])],
     band("Say hello", "Come by<br>with your pup.",
          "Call the counter, send a note, or just show up leashed — the shop is right on Sprague in the Valley.",
          [("Home", "/"), ("Contact", "#")]))

# ---------------------------------------------------------------- PRIVACY
PRIV_BODY = f"""  <section>
    <div class="wrap">
      <div class="kicker">{PAW} The boring-but-fair part</div>
      <h2>Privacy</h2>
      <div class="prose">
        <p><strong>Last updated:</strong> November 16, 2026. This site collects as little about you as it can.</p>
        <ul>
          <li><strong>Contact form.</strong> The name, phone, email and message you send through the form are used
          only to answer you. They go to {NAME} and nothing else.</li>
          <li><strong>No trackers, no cookies, no ads.</strong> This site loads no third-party scripts and sets no
          tracking cookies. There is nothing to opt out of.</li>
          <li><strong>Google Maps.</strong> The contact page shows an embedded map; when it loads, Google may
          process your IP address like it does for any map on the web.</li>
          <li><strong>Questions?</strong> Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {TEL_H} and a human
          at the shop will answer.</li>
        </ul>
      </div>
    </div>
  </section>
"""
page("/privacy", "privacy.html",
     f"Privacy Policy — {NAME}",
     f"Privacy policy for {NAME}, the custom puppuccino bar and pet shop at {NAP}: no trackers, no cookies, form messages used only to answer you.",
     PRIV_BODY,
     [{**CTX, "@type": "WebPage", "name": "Privacy Policy", "url": ORIGIN + "/privacy",
           "about": {"@id": ORIGIN + "/#shop"}}],
     band("Privacy", "Your business,<br>kept between us.", None,
          [("Home", "/"), ("Privacy", "#")]))

# ---------------------------------------------------------------- 404 + THANKS
E404 = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found — {NAME}</title>
  <meta name="description" content="That page isn't here — back to the puppuccino bar and pet shop in Spokane Valley.">
  <link rel="canonical" href="{ORIGIN}/404"><meta name="robots" content="noindex">
  <meta property="og:title" content="Page Not Found — {NAME}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="stylesheet" href="/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site"><div class="bar">{BRAND}{NAV}</div></header>
  <main id="main">
    <section><div class="wrap prose">
      <div class="kicker">{PAW} 404</div>
      <h1>This page went missing.</h1>
      <p class="lede">It happens — the treats counter, however, is exactly where you left it.
      <a href="/">Back home</a>, <a href="/pup-bar">the pup bar</a>, or <a href="/contact">contact &amp; directions</a>.</p>
    </div></section>
  </main>
{FOOTER}
</body>
</html>"""
with open(os.path.join(PUB, "404.html"), "w", encoding="utf-8") as f: f.write(E404)

THANKS = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Note Sent — {NAME}</title>
  <meta name="description" content="Thanks for reaching out to {NAME}, the custom puppuccino bar and pet shop in Spokane Valley.">
  <link rel="canonical" href="{ORIGIN}/thanks"><meta name="robots" content="noindex">
  <meta property="og:title" content="Note Sent — {NAME}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="stylesheet" href="/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site"><div class="bar">{BRAND}{NAV}</div></header>
  <main id="main">
    <section><div class="wrap prose">
      <div class="kicker">{PAW} Sent</div>
      <h1>Thanks — your note is on its way.</h1>
      <p class="lede">The shop will get back to you as fast as the counter allows. In the meantime:
      <a href="/">back home</a>, or call <a href="tel:{TEL_T}">{TEL_H}</a>.</p>
    </div></section>
  </main>
{FOOTER}
</body>
</html>"""
with open(os.path.join(PUB, "thanks.html"), "w", encoding="utf-8") as f: f.write(THANKS)

# ---------------------------------------------------------------- sitemap / robots / favicon
CORE = ["/", "/pup-bar", "/custom-pup-cups", "/pet-shop", "/training-essentials", "/contact", "/privacy"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in CORE:
    sm.append(f"  <url><loc>{ORIGIN}{p}</loc><lastmod>2026-11-16</lastmod></url>")
sm.append("</urlset>\n")
open(os.path.join(PUB, "sitemap.xml"), "w").write("\n".join(sm))
open(os.path.join(PUB, "robots.txt"), "w").write(
    f"User-agent: *\nAllow: /\nDisallow: /thanks\n\nSitemap: {ORIGIN}/sitemap.xml\n")
open(os.path.join(PUB, "favicon.svg"), "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M9.5 15.5h13l-1.7 12.2a1.6 1.6 0 '
    '0 1-1.6 1.3h-6.4a1.6 1.6 0 0 1-1.6-1.3z" fill="#FFFCF4" stroke="#2E1C12" stroke-width="2" '
    'stroke-linejoin="round"/><path d="M8 15.5c0-3.4 3.6-5.2 8-5.2s8 1.8 8 5.2" fill="#FFFCF4" stroke="#2E1C12" '
    'stroke-width="2"/><path d="M11 10.6c.4-2.5 2.4-3.9 5-3.9s4.6 1.4 5 3.9" fill="#FFFCF4" stroke="#2E1C12" '
    'stroke-width="2"/><path d="M13.6 6.5c.7-1.6 1.6-2.4 2.4-2.4s1.7.8 2.4 2.4" fill="#FFFCF4" stroke="#2E1C12" '
    'stroke-width="2"/><circle cx="16" cy="2.6" r="1.1" fill="#B93958"/></svg>')

print("wrote", len(os.listdir(PUB)), "files to", PUB)
