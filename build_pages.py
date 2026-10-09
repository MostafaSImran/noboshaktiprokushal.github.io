"""Generate all NSP preview pages from a shared template."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" href="profile/nsp-mark.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            kaleo: {{ sand: '#EAE4D9', charcoal: '#1C1C1C', earth: '#2A2A2A', cream: '#F3F0EB', terracotta: '#8C7B6B' }},
          }},
          fontFamily: {{
            display: ['"Cormorant Garamond"', 'serif'],
            body: ['Inter', 'sans-serif'],
          }},
        }},
      }},
    }};
  </script>
  <style>
    html {{ scroll-behavior: smooth; }}
    .reveal {{ opacity: 0; transform: translateY(28px); transition: opacity .8s ease, transform .8s ease; }}
    .reveal.visible {{ opacity: 1; transform: translateY(0); }}
  </style>
</head>
<body class="bg-kaleo-sand font-body text-kaleo-earth antialiased">
"""

NAV_ITEMS = [
    ("index.html", "Home / About"),
    ("products.html", "Products"),
    ("services.html", "Services"),
    ("projects.html", "Projects"),
    ("signature.html", "Signature Projects"),
    ("why-nsp.html", "Why NSP"),
    ("collaboration.html", "Collaboration"),
    ("contact.html", "Contact"),
]

def nav(active):
    links = "\n        ".join(
        f'<a href="{href}" class="{"text-kaleo-terracotta" if href == active else "hover:text-kaleo-terracotta transition-colors"}">{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f"""  <header class="sticky top-0 z-50 bg-kaleo-sand/90 backdrop-blur-md border-b border-kaleo-earth/10">
    <div class="max-w-7xl mx-auto px-6 md:px-8 h-16 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3">
        <img src="profile/nsp-mark.png" alt="NSP logo" class="h-11 w-auto" />
        <span class="leading-tight hidden sm:block">
          <span class="font-display text-lg md:text-xl tracking-wide text-kaleo-earth block">Nobo Shakti <span class="text-kaleo-terracotta">Prokushal</span></span>
          <span class="font-body text-[10px] uppercase tracking-[0.22em] text-kaleo-earth/50 block mt-0.5">Engineering Contractor · Est. 2007</span>
        </span>
      </a>
      <nav class="hidden lg:flex items-center gap-6 font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/70">
        {links}
      </nav>
      <a href="contact.html" class="font-body text-xs uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-5 py-2.5 hover:bg-kaleo-terracotta transition-colors">
        Get a Quote
      </a>
    </div>
  </header>
"""

FOOTER = """
  <footer class="bg-kaleo-charcoal text-kaleo-cream py-20">
    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 md:grid-cols-3 gap-12">
      <div>
        <div class="flex items-center gap-3">
          <img src="profile/nsp-mark.png" alt="NSP logo" class="h-12 w-auto" />
          <div class="leading-tight">
            <p class="font-display text-2xl">Nobo Shakti Prokushal</p>
            <p class="font-body text-[10px] uppercase tracking-[0.22em] text-kaleo-cream/50 mt-1">Engineering Contractor · Est. 2007</p>
          </div>
        </div>
        <p class="font-body text-sm text-kaleo-cream/60 leading-relaxed mt-4">Engineering contractor — healthcare MEP, medical gas, fire protection, acoustics, fabrication and renewable energy. Dhaka, Bangladesh.</p>
      </div>
      <div>
        <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-cream/50">Contact</p>
        <ul class="mt-4 space-y-2 font-body text-sm text-kaleo-cream/75">
          <li><a href="tel:+8801714073604" class="hover:text-kaleo-cream transition-colors">+880 1714 073604</a></li>
          <li><a href="tel:+8801711055476" class="hover:text-kaleo-cream transition-colors">+880 1711 055476</a></li>
          <li><a href="mailto:info@mostafasimran.com" class="hover:text-kaleo-cream transition-colors">info@mostafasimran.com</a></li>
          <li><a href="https://wa.me/8801714073604" class="hover:text-kaleo-cream transition-colors">WhatsApp</a></li>
        </ul>
      </div>
      <div>
        <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-cream/50">Offices</p>
        <p class="font-body text-sm text-kaleo-cream/75 mt-4 leading-relaxed">Corporate: 73/H (GF) Green Road, Dhaka-1205<br />Workshop: House #10, Road #5/B, Middle Nandi Para, Khilgaon, Dhaka-1214</p>
        <p class="font-body text-sm text-kaleo-cream/75 mt-3 leading-relaxed">TIN 653549294117 · BIN 19021092318<br />Trade License 000258 · IRC 104713</p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-6 md:px-8 mt-14 pt-8 border-t border-kaleo-cream/10 flex flex-col md:flex-row items-center justify-between gap-4">
      <p class="font-body text-xs text-kaleo-cream/40">© 2026 Nobo Shakti Prokushal (NSP), Dhaka · Sister concern: NeoMed Healthcare Services</p>
      <p class="font-body text-xs text-kaleo-cream/40">Sister site: <a href="https://www.mostafasimran.com" class="hover:text-kaleo-cream transition-colors">mostafasimran.com</a></p>
    </div>
  </footer>

  <script>
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
  </script>
</body>
</html>
"""

def page_header(label, title, intro):
    return f"""  <section class="bg-kaleo-cream">
    <div class="max-w-7xl mx-auto px-6 md:px-8 py-20 md:py-28 text-center reveal visible">
      <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">{label}</span>
      <h1 class="font-display text-4xl md:text-6xl text-kaleo-earth mt-4 leading-tight">{title}</h1>
      <p class="font-body text-base md:text-lg text-kaleo-earth/70 leading-relaxed max-w-2xl mx-auto mt-6">{intro}</p>
    </div>
  </section>
"""

def write_page(filename, title, desc, active, body):
    html = HEAD.format(title=title, desc=desc) + nav(active) + body + FOOTER
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as fp:
        fp.write(html)
    print("wrote", filename)

# ============================================================ INDEX / ABOUT
index_body = """
  <section class="relative bg-kaleo-cream">
    <div class="max-w-7xl mx-auto px-6 md:px-8 py-24 md:py-36 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div class="reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Engineering Contractor · Est. 2007 · Dhaka, Bangladesh</span>
        <h1 class="font-display text-5xl md:text-7xl leading-[1.02] mt-5 text-kaleo-earth">
          We Build the Systems Hospitals Rely On.
        </h1>
        <p class="font-body text-base md:text-lg text-kaleo-earth/70 leading-relaxed mt-7 max-w-xl">
          Medical gas pipelines, fire protection, HVAC and industrial acoustics — designed, installed and maintained to international code by a 15+ engineer team, for 40+ hospitals and industrial clients across Bangladesh.
        </p>
        <div class="mt-9 flex flex-wrap gap-3">
          <a href="services.html" class="font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-terracotta transition-colors">Our Services</a>
          <a href="signature.html" class="font-body text-sm uppercase tracking-[0.12em] border border-kaleo-earth/25 text-kaleo-earth rounded-full px-8 py-4 hover:border-kaleo-terracotta hover:text-kaleo-terracotta transition-colors">Project Track Record</a>
        </div>
      </div>
      <div class="reveal">
        <div class="rounded-3xl bg-kaleo-earth text-kaleo-cream p-8 md:p-10 shadow-xl relative overflow-hidden">
          <img src="profile/nsp-mark.png" alt="" aria-hidden="true" class="absolute -right-8 -bottom-10 w-44 opacity-10 pointer-events-none" />
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Our Vision</span>
          <p class="font-display text-2xl md:text-[1.75rem] leading-snug mt-4">
            To establish an institute for research and development in the engineering field of Bangladesh — for sustainable development.
          </p>
        </div>
        <div class="rounded-3xl bg-white/70 border border-kaleo-earth/10 p-8 md:p-10 mt-6 shadow-lg relative overflow-hidden">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Our Mission</span>
          <p class="font-body text-base md:text-lg text-kaleo-earth/80 leading-relaxed mt-4">
            To provide quality engineering services for industrial and medical structures across Bangladesh — through Nobo Shakti Prokushal and sister concern NeoMed Healthcare Services.
          </p>
        </div>
        <p class="font-body text-xs text-kaleo-earth/40 mt-4 text-center">Vision &amp; Mission — as stated in the NSP corporate profile</p>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-earth text-kaleo-cream">
    <div class="max-w-7xl mx-auto px-6 md:px-8 py-14 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
      <div class="reveal"><p class="font-display text-4xl md:text-5xl">40+</p><p class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-cream/60 mt-2">Hospitals Served</p></div>
      <div class="reveal"><p class="font-display text-4xl md:text-5xl">15+</p><p class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-cream/60 mt-2">Engineers &amp; Technicians</p></div>
      <div class="reveal"><p class="font-display text-4xl md:text-5xl">20+</p><p class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-cream/60 mt-2">Years of Delivery</p></div>
      <div class="reveal"><p class="font-display text-4xl md:text-5xl">4</p><p class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-cream/60 mt-2">Product Lines</p></div>
    </div>
  </section>

  <section class="bg-kaleo-sand py-24 md:py-32">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="max-w-3xl reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">About NSP</span>
        <h2 class="font-display text-4xl md:text-6xl text-kaleo-earth mt-4">Two Decades of Engineering, One Standard: Code Compliance</h2>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 mt-14">
        <div class="reveal">
          <p class="font-body text-base text-kaleo-earth/75 leading-relaxed">
            Nobo Shakti Prokushal (NSP) is a Dhaka-based engineering contracting firm founded and led by Engr. Mostafa Shawkat Imran — Mechanical Engineer (RUET), MBA (AUST) and Fellow of the Institution of Engineers, Bangladesh. Starting in 2007 as an electromechanical design consultancy, NSP has grown into a full contracting house with its own workshop, fabrication team and field crews.
          </p>
          <p class="font-body text-base text-kaleo-earth/75 leading-relaxed mt-5">
            Our work spans medical gas pipeline systems and fire protection for hospitals, acoustic engineering for industrial plants, custom fabrication from bus bodies to sound pods, and renewable energy systems for rural communities. Every project is delivered to international code — NFPA, HTM, ASME and BNBC — with documentation that survives any inspection. Sister concern NeoMed Healthcare Services extends our reach into medical supply.
          </p>
        </div>
        <div class="reveal grid grid-cols-2 gap-6">
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 aspect-[4/3]"><img src="profile/oxygen-manifold.webp" alt="Oxygen manifold room with cylinder banks" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 aspect-[4/3] mt-6"><img src="profile/chillers.webp" alt="Air-cooled chillers installed on rooftop" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 aspect-[4/3]"><img src="profile/scrub-station.webp" alt="Stainless steel OT scrub station fabricated by NSP" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 aspect-[4/3] mt-6"><img src="profile/workshop.webp" alt="NSP workshop fabrication in progress" class="w-full h-full object-cover" loading="lazy" /></div>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-cream py-20">
    <div class="max-w-4xl mx-auto px-6 md:px-8 text-center reveal">
      <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Leadership</p>
      <h2 class="font-display text-3xl md:text-4xl text-kaleo-earth mt-4">Founded &amp; Led by Engr. Mostafa Shawkat Imran</h2>
      <p class="font-body text-sm md:text-base text-kaleo-earth/70 leading-relaxed mt-5 max-w-2xl mx-auto">
        Mechanical Engineer (RUET), MBA (AUST), Fellow of IEB (F-11718) — with two decades of engineering practice across Bangladesh and Indonesia. NSP executes; the principal leads design review and code compliance on every engagement.
      </p>
      <a href="https://www.mostafasimran.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 mt-7 font-body text-sm uppercase tracking-[0.12em] text-kaleo-terracotta border border-kaleo-terracotta/40 rounded-full px-8 py-3.5 hover:bg-kaleo-terracotta hover:text-kaleo-cream transition-all">
        Executive Profile ↗ mostafasimran.com
      </a>
    </div>
  </section>
"""
write_page("index.html", "Nobo Shakti Prokushal (NSP) — Engineering Contractor, Dhaka",
           "Nobo Shakti Prokushal (NSP) — Bangladesh engineering contractor for medical gas pipeline systems, healthcare MEP, fire protection, industrial acoustics and custom fabrication. 40+ hospitals served, 20+ years of delivery.",
           "index.html", index_body)

# ============================================================ PRODUCTS (unchanged content, logo nav auto)
products_body = page_header(
    "NSP Product Lines",
    "Engineered Products, Built In-House",
    "Four product lines designed and fabricated by NSP — from vehicle body structures to capsule homes and solar systems.",
) + """
  <section class="bg-kaleo-sand py-16 md:py-24 space-y-24">

    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div class="reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Product 01</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">Customized Vehicle Body Structure</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          NSP designs and fabricates complete vehicle body structures — engineered for strength, comfort and road conditions in Bangladesh. Our landmark achievement: the first luxury bus body in Bangladesh, built for Scania.
        </p>
        <ul class="mt-6 space-y-3">
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Bus Body — luxury coach structures, structural framing and interior fit-out</span></li>
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Caravan — customized travel and mobile living units</span></li>
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Golf Cart — purpose-built utility and resort vehicles</span></li>
        </ul>
        <button type="button" data-inquiry="Customized Vehicle Body Structure (Bus Body / Caravan / Golf Cart)" class="inline-block mt-7 font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-7 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
      </div>
      <div class="reveal">
        <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl">
          <img src="scania-bus.webp" alt="Bangladesh's first luxury bus body, designed and built by NSP for Scania" class="w-full object-cover" loading="lazy" />
        </div>
        <p class="font-body text-xs text-kaleo-earth/50 mt-3 text-center">Bangladesh's first luxury bus body — designed and built by NSP for Scania, 2010–2011</p>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 md:px-8 mt-20">
      <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8 md:p-12">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Signature Design Achievement · 2010–2011</span>
        <h3 class="font-display text-3xl md:text-4xl mt-4">Bangladesh's First Luxury Bus Body</h3>
        <p class="font-body text-base text-kaleo-cream/75 leading-relaxed mt-4 max-w-3xl">
          Led the design and implementation of Bangladesh's first luxury bus body structure — a ground-up engineering achievement on the Scania platform that redefined passenger transport standards in the country. From structural framing and chassis integration to passenger ergonomics, safety and finishing — delivered to a standard no Bangladeshi operator had seen before.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-9">
          <div class="border-t-2 border-kaleo-terracotta/40 pt-5">
            <h4 class="font-display text-xl">A National First</h4>
            <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-2">The first luxury bus body structure engineered in Bangladesh — setting a new benchmark for the domestic coachbuilding industry.</p>
          </div>
          <div class="border-t-2 border-kaleo-terracotta/40 pt-5">
            <h4 class="font-display text-xl">End-to-End Leadership</h4>
            <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-2">Owned both design and implementation: structural design, chassis–body integration, and on-site execution through to delivery.</p>
          </div>
          <div class="border-t-2 border-kaleo-terracotta/40 pt-5">
            <h4 class="font-display text-xl">Passenger-Centred Engineering</h4>
            <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-2">Combined ride comfort, safety and premium finishing in a single structure — engineering elegance without compromising durability.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="text-center max-w-2xl mx-auto reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Product 02</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">Sound Pod</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          Acoustic isolation pods for offices, healthcare, education and industry — single occupancy, double occupancy, or fully customized to your space and use case.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl overflow-hidden">
          <div class="aspect-[4/3] overflow-hidden"><img src="soundpod/single-1.webp" alt="NSP single occupancy sound pod" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="p-6"><h3 class="font-display text-xl text-kaleo-earth">Single Pod</h3><p class="font-body text-sm text-kaleo-earth/65 mt-2">One-person acoustic pod for calls, focus work and telehealth.</p></div>
        </div>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl overflow-hidden">
          <div class="aspect-[4/3] overflow-hidden"><img src="soundpod/double-1.webp" alt="NSP double occupancy sound pod" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="p-6"><h3 class="font-display text-xl text-kaleo-earth">Double Pod</h3><p class="font-body text-sm text-kaleo-earth/65 mt-2">Two-person pod for meetings, consultations and interviews.</p></div>
        </div>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl overflow-hidden">
          <div class="aspect-[4/3] overflow-hidden"><img src="soundpod/double-3.webp" alt="Customized NSP sound pod installation" class="w-full h-full object-cover" loading="lazy" /></div>
          <div class="p-6"><h3 class="font-display text-xl text-kaleo-earth">Customized</h3><p class="font-body text-sm text-kaleo-earth/65 mt-2">Bespoke sizes, finishes and integrations — sized to your floor plan.</p></div>
        </div>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
        <div class="reveal rounded-2xl overflow-hidden border border-kaleo-earth/10 aspect-square"><img src="soundpod/single-2.webp" alt="Sound pod interior" class="w-full h-full object-cover" loading="lazy" /></div>
        <div class="reveal rounded-2xl overflow-hidden border border-kaleo-earth/10 aspect-square"><img src="soundpod/double-2.webp" alt="Double sound pod interior" class="w-full h-full object-cover" loading="lazy" /></div>
        <div class="reveal rounded-2xl overflow-hidden border border-kaleo-earth/10 aspect-square"><img src="soundpod/double-4.webp" alt="Sound pod at exhibition" class="w-full h-full object-cover" loading="lazy" /></div>
        <div class="reveal rounded-2xl overflow-hidden border border-kaleo-earth/10 aspect-square"><img src="expo-malaysia.webp" alt="NSP sound pod showcased at international exhibition in Malaysia" class="w-full h-full object-cover" loading="lazy" /></div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-12">
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Single Space</span>
          <h3 class="font-display text-2xl text-kaleo-earth mt-3">Sound Pod · Single</h3>
          <p class="font-body text-sm text-kaleo-earth/65 leading-relaxed mt-3">A compact single-user pod for calls, focused work or quiet breaks — a room within a room that drops into any open floor plan.</p>
          <ul class="mt-5 space-y-2.5">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Acoustic absorptive wall panels with laminated safety glass front</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Integrated ceiling ventilation unit for continuous fresh air</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Built-in work shelf, ready for laptop and video calls</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Soft rounded frame — plug-and-play placement, no construction needed</span></li>
          </ul>
        </div>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Double Space</span>
          <h3 class="font-display text-2xl text-kaleo-earth mt-3">Sound Pod · Double</h3>
          <p class="font-body text-sm text-kaleo-earth/65 leading-relaxed mt-3">A two-person acoustic pod for private meetings, interviews and one-to-one sessions — available in a range of panel finishes to match any interior.</p>
          <ul class="mt-5 space-y-2.5">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Larger twin-seat interior for meetings and collaboration</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Laminated glass front with acoustic absorptive side panels</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Ceiling-mounted ventilation and services module</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Multiple finish options — sage, terracotta, violet and more</span></li>
          </ul>
        </div>
      </div>
      <div class="reveal mt-10 rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl">
        <video src="soundpod/soundpod-ad.mp4" poster="soundpod/double-1.webp" autoplay muted loop playsinline class="w-full aspect-video object-cover"></video>
      </div>
      <p class="font-body text-xs text-kaleo-earth/50 mt-3 text-center">Sound Pod in motion — NSP acoustic solutions</p>
      <div class="text-center mt-10 reveal">
        <button type="button" data-inquiry="Sound Pod (Single / Double / Customized)" class="inline-block font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-7 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="text-center max-w-2xl mx-auto reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Product 03</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">EcoNest 3010 — Capsule Home</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          Self-contained prefabricated living units for eco-resorts, sustainable energy parks and compact urban sites — engineered for quick installation and everyday comfort.
        </p>
      </div>
      <div class="reveal mt-12 rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl">
        <img src="econest-capsule.webp" alt="Prefab capsule home with panoramic glazing in a green eco-resort at golden hour" class="w-full aspect-[16/9] md:aspect-[21/9] object-cover" loading="lazy" />
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 mt-14 items-start">
        <div class="reveal">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Prefab Smart Capsule Home · 30' × 10' × 9'</span>
          <p class="font-display text-2xl md:text-3xl text-kaleo-earth leading-snug mt-4">
            A turnkey smart capsule residence engineered for eco-resorts and sustainable energy parks — factory-built, transportable, and ready to live in from day one.
          </p>
          <p class="font-body text-sm md:text-base text-kaleo-earth/60 leading-relaxed mt-5">
            The EcoNest 3010 pairs a hot-dip galvanized steel frame with an aviation-grade aluminum shell and panoramic low-E glazing, fully fitted with smart home systems, heated stone-crystal flooring and a fresh-air climate system — a complete product of precision engineering and sustainable design thinking.
          </p>
          <a href="papers/econest-3010-capsule-home-catalogue.pdf" download class="inline-flex items-center gap-2 mt-7 font-body text-sm uppercase tracking-wider text-kaleo-cream bg-kaleo-terracotta rounded-full px-8 py-4 hover:opacity-90 transition-opacity">⬇ Download Catalogue</a>
          <p class="font-body text-xs text-kaleo-earth/40 mt-2">PDF · full specifications</p>
          <div class="mt-6">
            <button type="button" data-inquiry="Capsule Homes (EcoNest 3010)" class="inline-block font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-7 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
          </div>
        </div>
        <div class="reveal">
          <ul class="space-y-7">
            <li class="border-t-2 border-kaleo-terracotta/30 pt-5">
              <h4 class="font-display text-xl text-kaleo-earth">Engineered Shell</h4>
              <p class="font-body text-sm text-kaleo-earth/60 leading-relaxed mt-2">Hot-dip galvanized steel frame (3–4 mm) with 2 mm fluorocarbon-coated aviation aluminum panels and 100 mm+ cyclopentane insulation.</p>
            </li>
            <li class="border-t-2 border-kaleo-terracotta/30 pt-5">
              <h4 class="font-display text-xl text-kaleo-earth">Panoramic Comfort</h4>
              <p class="font-body text-sm text-kaleo-earth/60 leading-relaxed mt-2">Double low-E tempered glass, heated stone-crystal flooring, and a fresh-air system with integrated climate control.</p>
            </li>
            <li class="border-t-2 border-kaleo-terracotta/30 pt-5">
              <h4 class="font-display text-xl text-kaleo-earth">Smart by Default</h4>
              <p class="font-body text-sm text-kaleo-earth/60 leading-relaxed mt-2">One-touch master power, voice control, electric curtains and a motorized projection system — a resort-ready smart home.</p>
            </li>
          </ul>
        </div>
      </div>
      <figure class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center mt-14">
        <div class="md:col-span-8 rounded-3xl overflow-hidden border border-kaleo-earth/10">
          <img src="capsule-build.webp" alt="Actual steel-frame fabrication of the EcoNest capsule structure" class="w-full aspect-[16/9] object-cover" loading="lazy" />
        </div>
        <figcaption class="md:col-span-4 font-body text-sm text-kaleo-earth/60 leading-relaxed">
          Photo: actual steel-frame fabrication of the EcoNest capsule home — hand-built structure in the NSP workshop.
        </figcaption>
      </figure>
    </div>

    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div class="reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Product 04</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">Solar Home System</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          Reliable off-grid and hybrid solar packages for homes and small businesses — designed for Bangladesh's climate and grid conditions, installed and maintained by NSP field teams.
        </p>
        <ul class="mt-6 space-y-3">
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">200 solar DC home packages (25–40 W) installed across Kurigram District</span></li>
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Solar, hydroponic and organic fertilizer integration for rooftop gardening</span></li>
          <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Hybrid configurations with battery backup and generator interlock</span></li>
        </ul>
        <button type="button" data-inquiry="Solar Home System" class="inline-block mt-7 font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-7 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
      </div>
      <div class="reveal">
        <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl">
          <img src="card-energy.webp" alt="Solar and biogas renewable energy installation by NSP" class="w-full object-cover" loading="lazy" />
        </div>
        <p class="font-body text-xs text-kaleo-earth/50 mt-3 text-center">NSP renewable energy installations — solar and biogas hybrid systems</p>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-cream py-16 md:py-24 border-t border-kaleo-earth/10">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="text-center max-w-2xl mx-auto reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">For Prospective Clients</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-4">Plan Your Project</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          A little preparation makes your inquiry faster to quote. Here is what to have ready for each product — then send it in one structured form.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
        <div class="reveal bg-kaleo-sand border border-kaleo-earth/10 rounded-3xl p-8 flex flex-col">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">EcoNest 3010</span>
          <h3 class="font-display text-xl text-kaleo-earth mt-3">Site Requirements</h3>
          <ul class="mt-4 space-y-2.5 flex-1">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Site location — address or GPS coordinates</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Land type — urban, rural, resort or industrial zone</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Utility access — power, water and road connectivity</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Environment — soil condition, flood level, green certifications</span></li>
          </ul>
          <button type="button" data-inquiry="Capsule Homes (EcoNest 3010)" class="mt-6 w-full font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-6 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
        </div>
        <div class="reveal bg-kaleo-sand border border-kaleo-earth/10 rounded-3xl p-8 flex flex-col">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Sound Pod</span>
          <h3 class="font-display text-xl text-kaleo-earth mt-3">Installation Environments</h3>
          <ul class="mt-4 space-y-2.5 flex-1">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Where it works — home, office, plant, powerplant, substation, food processing</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Current noise level in dB (if measured)</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Room dimensions and ventilation provision</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Target noise reduction and budget range</span></li>
          </ul>
          <button type="button" data-inquiry="Sound Pod (Single / Double / Customized)" class="mt-6 w-full font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-6 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
        </div>
        <div class="reveal bg-kaleo-sand border border-kaleo-earth/10 rounded-3xl p-8 flex flex-col">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Bus Body</span>
          <h3 class="font-display text-xl text-kaleo-earth mt-3">Design &amp; Development</h3>
          <ul class="mt-4 space-y-2.5 flex-1">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Intended use — public transport, school, luxury coach, staff</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Passenger capacity and preferred material</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Structural standards and safety features</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/70">Compliance needs of your transport authority</span></li>
          </ul>
          <button type="button" data-inquiry="Customized Vehicle Body Structure (Bus Body / Caravan / Golf Cart)" class="mt-6 w-full font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-6 py-3.5 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Send Inquiry modal -->
  <div id="inquiry-modal" class="fixed inset-0 z-[100] hidden items-center justify-center p-4" role="dialog" aria-modal="true" aria-labelledby="inquiry-title">
    <div class="absolute inset-0 bg-kaleo-charcoal/60 backdrop-blur-sm" data-close></div>
    <div class="relative bg-kaleo-cream rounded-3xl max-w-lg w-full p-7 md:p-9 shadow-2xl border border-kaleo-earth/10 max-h-[90vh] overflow-y-auto">
      <button type="button" data-close aria-label="Close" class="absolute top-4 right-4 w-9 h-9 rounded-full border border-kaleo-earth/20 text-kaleo-earth/60 hover:text-kaleo-earth hover:border-kaleo-terracotta transition-colors font-body text-lg leading-none">&times;</button>
      <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Product Inquiry</span>
      <h3 id="inquiry-title" class="font-display text-2xl md:text-3xl text-kaleo-earth mt-2">Send an Inquiry</h3>
      <p class="font-body text-sm text-kaleo-earth/60 mt-2">Product: <strong id="inq-product-label" class="text-kaleo-earth"></strong></p>
      <form id="inquiry-form" class="mt-6 space-y-4">
        <input type="hidden" name="product" id="inq-product" />
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <label class="block">
            <span class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60">Your Name *</span>
            <input type="text" name="name" required class="mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors" />
          </label>
          <label class="block">
            <span class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60">Email *</span>
            <input type="email" name="email" required class="mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors" />
          </label>
          <label class="block">
            <span class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60">Phone</span>
            <input type="tel" name="phone" class="mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors" />
          </label>
          <label class="block">
            <span class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60">Company / Organization</span>
            <input type="text" name="company" class="mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors" />
          </label>
        </div>
        <div id="inq-extra" class="space-y-4"></div>
        <label class="block">
          <span class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60">Your Requirements *</span>
          <textarea name="message" rows="4" required placeholder="Quantity, dimensions, site conditions, timeline — the more detail, the faster our quote." class="mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors resize-y"></textarea>
        </label>
        <button type="submit" id="inq-submit" class="w-full font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-terracotta transition-colors">Send Inquiry</button>
        <p id="inq-status" class="font-body text-sm text-center min-h-[1.25rem]"></p>
        <p class="font-body text-xs text-kaleo-earth/40 text-center">Prefer chat? <a href="https://wa.me/8801714073604" target="_blank" rel="noopener noreferrer" class="text-kaleo-terracotta hover:underline">WhatsApp +880 1714 073604</a></p>
      </form>
    </div>
  </div>
  <script>
    (function () {
      var modal = document.getElementById('inquiry-modal');
      var form = document.getElementById('inquiry-form');
      var status = document.getElementById('inq-status');
      var submitBtn = document.getElementById('inq-submit');
      var productInput = document.getElementById('inq-product');
      var productLabel = document.getElementById('inq-product-label');
      var extra = document.getElementById('inq-extra');

      var FIELD_SETS = {
        'Customized Vehicle Body Structure (Bus Body / Caravan / Golf Cart)': [
          { key: 'use_type', label: 'Intended use', type: 'select', required: true, options: ['Public transport', 'School bus', 'Luxury coach', 'Staff / industrial transport', 'Caravan / motorhome', 'Golf cart / utility vehicle'] },
          { key: 'capacity', label: 'Passenger capacity', type: 'number' },
          { key: 'material', label: 'Preferred material (steel / aluminium / composite)' },
          { key: 'compliance', label: 'Compliance requirements (transport authority)' }
        ],
        'Sound Pod (Single / Double / Customized)': [
          { key: 'site_type', label: 'Installation site type', type: 'select', required: true, options: ['Home', 'Office', 'Industry / plant', 'Powerplant / substation', 'Food processing'] },
          { key: 'noise_level', label: 'Current noise level (dB, if known)', type: 'number' },
          { key: 'performance', label: 'Required noise reduction (dB)', type: 'number' },
          { key: 'dimensions', label: 'Space dimensions (L×W×H)' },
          { key: 'budget', label: 'Budget range' }
        ],
        'Capsule Homes (EcoNest 3010)': [
          { key: 'site_location', label: 'Site address / location', required: true },
          { key: 'home_type', label: 'Type of home required', type: 'select', options: ['Single-family', 'Duplex', 'Resort unit(s)'] },
          { key: 'floor_area', label: 'Expected floor area (sq ft)', type: 'number' },
          { key: 'certifications', label: 'Green certifications desired (e.g. LEED)' }
        ],
        'Solar Home System': [
          { key: 'site_location', label: 'Installation address / location', required: true },
          { key: 'load', label: 'Expected load (W or kW)' },
          { key: 'backup', label: 'Backup requirement (hours)' },
          { key: 'budget', label: 'Budget range' }
        ]
      };

      var inputClass = 'mt-1.5 w-full font-body text-sm text-kaleo-earth bg-kaleo-sand/60 border border-kaleo-earth/20 rounded-xl px-4 py-3 outline-none focus:border-kaleo-terracotta transition-colors';

      function renderExtraFields(product) {
        extra.innerHTML = '';
        var fields = FIELD_SETS[product] || [];
        fields.forEach(function (f) {
          var label = document.createElement('label');
          label.className = 'block';
          var span = document.createElement('span');
          span.className = 'font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60';
          span.textContent = f.label + (f.required ? ' *' : '');
          label.appendChild(span);
          if (f.type === 'select') {
            var sel = document.createElement('select');
            sel.name = f.key;
            if (f.required) sel.required = true;
            sel.className = inputClass;
            sel.innerHTML = '<option value="">—</option>' + f.options.map(function (o) { return '<option value="' + o + '">' + o + '</option>'; }).join('');
            label.appendChild(sel);
          } else {
            var inp = document.createElement('input');
            inp.type = f.type === 'number' ? 'number' : 'text';
            inp.name = f.key;
            if (f.required) inp.required = true;
            inp.className = inputClass;
            label.appendChild(inp);
          }
          extra.appendChild(label);
        });
      }

      function openModal(product) {
        productInput.value = product;
        productLabel.textContent = product;
        renderExtraFields(product);
        status.textContent = '';
        status.className = 'font-body text-sm text-center min-h-[1.25rem]';
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';
      }
      function closeModal() {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
      }

      document.querySelectorAll('[data-inquiry]').forEach(function (btn) {
        btn.addEventListener('click', function () { openModal(btn.getAttribute('data-inquiry')); });
      });
      modal.querySelectorAll('[data-close]').forEach(function (el) {
        el.addEventListener('click', closeModal);
      });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending…';
        status.textContent = '';
        var data = {};
        new FormData(form).forEach(function (v, k) { if (v) data[k] = v; });
        data._subject = 'NSP Product Inquiry — ' + data.product;
        data._template = 'table';
        data._captcha = 'false';
        data._autoresponse = 'Dear ' + data.name + ',\\n\\nThank you for contacting Nobo Shakti Prokushal (NSP). Your inquiry about "' + data.product + '" has been received. Our engineering team will respond within one business day.\\n\\n— Nobo Shakti Prokushal (NSP), Dhaka\\nPhone / WhatsApp: +880 1714 073604\\nwww.noboshaktiprokushal.com';
        fetch('https://formsubmit.co/ajax/info@noboshaktiprokushal.com', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(data)
        }).then(function (res) {
          if (!res.ok) throw new Error('failed');
          status.textContent = 'Inquiry sent — thank you! A confirmation email is on its way to your inbox.';
          status.className = 'font-body text-sm text-center min-h-[1.25rem] text-green-700';
          form.reset();
          renderExtraFields(productInput.value);
        }).catch(function () {
          status.innerHTML = 'Something went wrong. Please email <a class="text-kaleo-terracotta underline" href="mailto:info@noboshaktiprokushal.com">info@noboshaktiprokushal.com</a> or WhatsApp +880 1714 073604.';
          status.className = 'font-body text-sm text-center min-h-[1.25rem] text-red-700';
        }).finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Send Inquiry';
        });
      });
    })();
  </script>
"""
write_page("products.html", "Products — Nobo Shakti Prokushal (NSP)",
           "NSP products: customized vehicle body structures (bus body, caravan, golf cart), Sound Pod acoustic pods, capsule homes and solar home systems.",
           "products.html", products_body)

# ============================================================ SERVICES (now with 3D printing + machine design)
def service_card(title, desc, items, chips):
    lis = "\n".join(f'            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">{i}</span></li>' for i in items)
    ch = "\n".join(f'            <span class="font-body text-[11px] uppercase tracking-wider text-kaleo-terracotta bg-kaleo-terracotta/10 rounded-full px-3 py-1">{c}</span>' for c in chips)
    return f"""        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 md:p-10 flex flex-col">
          <h2 class="font-display text-3xl text-kaleo-earth">{title}</h2>
          <p class="font-body text-sm text-kaleo-earth/65 leading-relaxed mt-3">{desc}</p>
          <ul class="mt-5 space-y-3 flex-1">
{lis}
          </ul>
          <div class="flex flex-wrap gap-2 mt-6">
{ch}
          </div>
        </div>"""

services_body = page_header(
    "NSP Services",
    "Design, Documentation &amp; Engineering Services",
    "Complete engineering services — design and documentation for every building type, plus 3D printing and machine design from our own workshop.",
) + f"""
  <section class="bg-kaleo-sand py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

{service_card("Hospital", "Healthcare facility design to international clinical engineering codes — from OT/ICU ventilation to medical gas and life safety.",
  ["Medical Gas Pipeline System design (oxygen, nitrous oxide, medical air, vacuum) to NFPA-99 / HTM-2022 / ISO 7396-1",
   "OT/ICU HVAC and pressure-cascade design to ASHRAE 170 principles",
   "Fire protection, nurse call and DGHS licensing documentation"],
  ["NFPA-99", "HTM-2022", "ISO 7396-1"])}

{service_card("Commercial", "Office buildings, retail and mixed-use facilities — efficient, maintainable MEP design focused on lifecycle cost.",
  ["HVAC, electrical distribution and plumbing design",
   "Fire detection and evacuation design to BNBC",
   "Acoustic treatment for plant rooms and offices"],
  ["BNBC", "ASHRAE", "NFPA 101"])}

{service_card("Industrial", "Factories, process plants and utilities — heavy-duty engineering for continuous operation and code compliance.",
  ["Boiler, pressure vessel and piping design to ASME BPVC / B31.3",
   "Thermal oil systems, HFO fuel handling and heat recovery",
   "Sound attenuation and vibration isolation engineering"],
  ["ASME BPVC", "ASME B31.3", "ISO 50001"])}

{service_card("Residential", "Homes, apartments and residential compounds — comfortable, safe and energy-conscious building services.",
  ["HVAC and hot/chilled water system design",
   "Electrical design, solar integration and generator backup",
   "Fire safety and gas safety documentation"],
  ["BNBC", "Solar"])}

{service_card("3D Printing &amp; Prototyping", "Rapid prototyping and short-run production from NSP's engineering workshop — from concept model to functional part.",
  ["Functional prototypes for machine parts, fittings and enclosures",
   "Architectural and product scale models for client approvals",
   "Custom jigs, fixtures and one-off components to drawing"],
  ["Rapid Prototyping", "Scale Models", "Custom Parts"])}

{service_card("Machine Design", "Custom machinery and equipment designed by NSP engineers and fabricated in our own workshop — from hatchery incubators to process equipment.",
  ["Hatchery incubators and poultry processing equipment",
   "Hospital equipment — trolleys, beds, scrub stations, distribution boards",
   "Process machinery — tanks, headers, expansion and buffer vessels"],
  ["AutoCAD / SolidWorks", "In-House Fabrication", "Testing & Handover"])}

      </div>

      <div class="reveal mt-14 bg-kaleo-earth text-kaleo-cream rounded-3xl p-8 md:p-10 text-center">
        <h3 class="font-display text-2xl md:text-3xl">Every Design Includes Full Documentation</h3>
        <p class="font-body text-sm md:text-base text-kaleo-cream/70 leading-relaxed max-w-2xl mx-auto mt-4">
          Drawings, specifications, bill of quantities, compliance statements and as-built records — the complete package regulators, lenders and contractors need.
        </p>
        <a href="contact.html" class="inline-block mt-6 font-body text-sm uppercase tracking-[0.12em] bg-kaleo-terracotta text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-cream hover:text-kaleo-earth transition-all">Start a Design Project</a>
      </div>
    </div>
  </section>
"""
write_page("services.html", "Services — Design, 3D Printing & Machine Design — NSP",
           "NSP services: design and documentation for hospitals, commercial, industrial and residential projects — plus 3D printing, prototyping and custom machine design.",
           "services.html", services_body)

# ============================================================ PROJECTS
projects_body = page_header(
    "NSP Projects",
    "Installation &amp; Commissioning",
    "Two execution disciplines, one standard: systems and machines that start up right the first time — and keep running.",
) + """
  <section class="bg-kaleo-sand py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8 space-y-16">

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
        <div class="reveal">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Discipline 01</span>
          <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">System Installation &amp; Commissioning</h2>
          <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
            Complete building services systems — installed, tested, commissioned and handed over with full documentation and operator training.
          </p>
          <ul class="mt-6 space-y-3">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Medical Gas Pipeline Systems — manifold to bedside, purity and pressure tested</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Fire protection — hydrant, sprinkler, detection and alarm systems</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">HVAC and ventilation — OT/ICU pressure cascades, cleanroom airflow</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Hot and chilled water systems, thermal oil loops and heat recovery</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Water, effluent and sewerage treatment plants</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Gas regulator metering stations — pressure regulation, slam-shut safety, metering</span></li>
          </ul>
        </div>
        <div class="reveal space-y-4">
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl"><img src="profile/oxygen-manifold.webp" alt="Oxygen manifold room commissioned by NSP" class="w-full object-cover" loading="lazy" /></div>
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl"><img src="profile/sprinkler.webp" alt="Fire sprinkler pipework installation" class="w-full object-cover" loading="lazy" /></div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
        <div class="reveal order-2 lg:order-1 space-y-4">
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl"><img src="profile/blower-silencers.webp" alt="Blowers with acoustic silencers installed by NSP" class="w-full object-cover" loading="lazy" /></div>
          <div class="rounded-3xl overflow-hidden border border-kaleo-earth/10 shadow-xl"><img src="profile/chiller-plant.webp" alt="Chiller plant machine installation" class="w-full object-cover" loading="lazy" /></div>
        </div>
        <div class="reveal order-1 lg:order-2">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Discipline 02</span>
          <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-3">Machine Installation &amp; Commissioning</h2>
          <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
            Heavy machinery and process equipment — set, aligned, isolated and commissioned to manufacturer specification and applicable code.
          </p>
          <ul class="mt-6 space-y-3">
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Generators and power plants — base frames, vibration isolation, exhaust systems</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Boilers and pressure equipment — ASME BPVC compliant installation</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Blowers, compressors and chillers — with acoustic enclosures and silencers</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Hatchery incubators and poultry processing lines</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Medical equipment — manifold equipment, nurse call and monitoring systems</span></li>
            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">Performance testing and operator handover training</span></li>
          </ul>
        </div>
      </div>

      <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8 md:p-10 text-center">
        <h3 class="font-display text-2xl md:text-3xl">Have a System or Machine to Commission?</h3>
        <a href="contact.html" class="inline-block mt-6 font-body text-sm uppercase tracking-[0.12em] bg-kaleo-terracotta text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-cream hover:text-kaleo-earth transition-all">Request a Commissioning Quote</a>
      </div>
    </div>
  </section>
"""
write_page("projects.html", "Projects — Installation & Commissioning — NSP",
           "NSP system installation and commissioning (medical gas, fire protection, HVAC, gas metering, treatment plants) and machine installation (generators, boilers, blowers) across Bangladesh.",
           "projects.html", projects_body)

# ============================================================ SIGNATURE + CLIENT LIST
def sig_card(img, alt, year, title, text):
    return f"""        <div class="reveal group bg-kaleo-sand border border-kaleo-earth/10 rounded-3xl overflow-hidden">
          <div class="relative overflow-hidden aspect-[4/3]">
            <img src="{img}" alt="{alt}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" />
            <span class="absolute top-4 left-4 font-body text-[11px] uppercase tracking-[0.15em] bg-kaleo-charcoal/80 text-kaleo-cream rounded-full px-4 py-1.5">{year}</span>
          </div>
          <div class="p-7">
            <h3 class="font-display text-xl text-kaleo-earth">{title}</h3>
            <p class="font-body text-sm text-kaleo-earth/65 mt-2">{text}</p>
          </div>
        </div>"""

CLIENTS = [
    ("Healthcare", [
        ("Global Edge Ltd", "Medical gas pipeline installation — Shaheed Monsur Ali Medical College Hospital, Uttara"),
        ("Khidma Hospital (Pvt.) Ltd", "Plumbing, electrical, HVAC and fire protection design; SDB and cable tray supply &amp; installation"),
        ("Selima Medical College Hospital (BRB Group), Kushtia", "Fire protection and detection system design consultancy"),
        ("Nexus Cardiac Care Hospital, Mymensingh", "Architectural, structural and utility design of the entire hospital; structural supervision to 7th floor"),
        ("Anifco Healthcare, Sylhet", "Design and construction supervision of ICU, CCU, NICU, post-operative and operation theatre"),
        ("Abdul Monem Ltd", "Medical equipment and furniture supply — Padma Bridge Project Health Complex, Mowa &amp; Madaripur"),
        ("Famous Hospital &amp; Diagnostic Center", "OT curtains supply; post-operative and OT floor and wall renovation"),
        ("Ayesha Memorial Hospital", "OT scrub station supply"),
    ]),
    ("Industrial", [
        ("TM Textile Ltd, Gazipur", "Acoustic room design for 2 MW power plant; 4 nos. 10'×10' acoustic sliding doors; 4 sound traps"),
        ("MASCO Exports Ltd, Narsingdi", "Sound attenuation system design and installation"),
        ("Abir Poultry &amp; Hatchery, Trishal", "Hot and chilled water system design for hatchery incubators; chiller, boiler and pump installation"),
        ("RAKS Fashion Ltd, Narayanganj", "Existing electrical system assessment and redesign; correction supervision"),
        ("BETELCO (Pvt.) Ltd", "Factory steel structure design (BSCIC Kachpur); CCTV supply and installation"),
        ("Fakir Apparel Ltd, Habiganj", "20 kW solar panel system with 24-hour backup"),
    ]),
    ("Commercial &amp; Buildings", [
        ("Navana Real Estate Ltd, Gulshan", "Design consultancy — plumbing and swimming pool"),
        ("Megacity Engineers &amp; Architects", "MEP design consultancy across projects; residential building construction"),
        ("7-one Properties Ltd", "Plumbing, electrical, HVAC and fire protection design consultancy"),
        ("Allex Furniture, Banani", "Showroom raised floor"),
        ("Architect Forum, Dhanmondi", "Fire protection and detection system design consultancy"),
        ("Shimanto Square Market (BGB), Dhanmondi", "Ongoing system maintenance"),
        ("Pivot Engineering Ltd", "H-beam supply (imported)"),
        ("Nexus Power &amp; Telecommunication Ltd", "25 kW UPS installation at Metropolitan Hospital"),
    ]),
    ("Energy &amp; Community", [
        ("Sonar Bangla, Kurigram", "200 sets of 25–40 W solar DC home systems"),
    ]),
    ("Transport", [
        ("Shohagh Motors Ltd", "Luxury Scania bus body structure design and supervision of 4 buses"),
    ]),
]

def client_table(cat, rows):
    trs = "\n".join(
        f'              <tr class="border-t border-kaleo-earth/10"><td class="py-3.5 pr-4 font-body text-sm font-medium text-kaleo-earth align-top">{name}</td><td class="py-3.5 font-body text-sm text-kaleo-earth/70 align-top">{work}</td></tr>'
        for name, work in rows
    )
    return f"""        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-7 md:p-9">
          <h3 class="font-display text-2xl text-kaleo-terracotta">{cat}</h3>
          <table class="w-full mt-4">
            <tbody>
{trs}
            </tbody>
          </table>
        </div>"""

client_blocks = "\n\n".join(client_table(cat, rows) for cat, rows in CLIENTS)

signature_body = page_header(
    "Signature Projects",
    "Work That Speaks in Results",
    "Landmark engagements from NSP's two decades — healthcare, transport, energy, telecom and industry.",
) + f"""
  <section class="bg-kaleo-sand py-16 md:py-20">
    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 md:grid-cols-3 gap-6">
{sig_card("/scania-bus.webp", "Bangladesh first luxury bus body built for Scania", "2010–2011", "Scania Bus Body Development", "Design and implementation lead — Bangladesh's first luxury bus body, engineered and built by NSP.")}
{sig_card("/profile/icu-ward.webp", "Hospital ICU ward interior completed by NSP", "Multi-year", "Hospital MGPS & ICU Fit-Out", "Medical gas pipeline, fire protection and ICU interior works for hospitals nationwide.")}
{sig_card("/project-manifold.webp", "Oxygen manifold room at upazila health complex", "2022–2023", "Oxygen Manifold Systems — Save the Children", "Led personally by NSP's founder as individual consultant to Save the Children: central medical gas pipeline establishment at 20 Upazila Health Complexes, with QA plans and staff training.")}
{sig_card("/project-masco.webp", "MASCO blower room sound attenuation", "2016", "Industrial Sound Attenuation — MASCO", "Blower-room silencers, acoustic louvers and duct attenuation — approximately 22 dB(A) noise reduction.")}
{sig_card("/project-sgcl-rms.webp", "Gas regulator metering station for SGCL at Bhola", "2026", "Regulator Metering Station — SGCL", "Pressure regulation, slam-shut safety and metering train at Notun Bangla Power Plant, Bhola — with O&amp;M training.")}
{sig_card("/profile/raised-floor.webp", "Raised floor structure installation", "Various", "Raised Floors &amp; Acoustic Fit-Outs", "Showroom and control-room raised floors, acoustic doors, sound traps and wall treatments.")}
    </div>
  </section>

  <section class="bg-kaleo-cream py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="text-center max-w-2xl mx-auto reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Complete Client List</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-4">Previous Projects from the NSP Profile</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">Every engagement from the corporate profile, organized by sector.</p>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-12">
{client_blocks}
      </div>
    </div>
  </section>
"""
write_page("signature.html", "Signature Projects & Client List — NSP",
           "NSP signature projects and complete client list: Scania bus body, hospital medical gas systems, founder's Save the Children oxygen program consultancy, MASCO acoustics, SGCL RMS and more.",
           "signature.html", signature_body)

# ============================================================ WHY NSP
why_body = page_header(
    "Why NSP",
    "A Contractor Built on Code Compliance",
    "The reasons hospitals, factories and operators across Bangladesh keep NSP on speed dial.",
) + """
  <section class="bg-kaleo-earth text-kaleo-cream py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
      <div class="reveal">
        <h3 class="font-display text-2xl">In-House Team</h3>
        <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-3">15+ qualified engineers, architects, technicians and foremen — design and execution under one roof.</p>
      </div>
      <div class="reveal">
        <h3 class="font-display text-2xl">Verified Credentials</h3>
        <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-3">TIN 653549294117, BIN 19021092318, Trade License 000258, IRC 104713, incorporation 2037 (2015) — fully documented contracting entity.</p>
      </div>
      <div class="reveal">
        <h3 class="font-display text-2xl">Code-First Delivery</h3>
        <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-3">NFPA, HTM, ASME and BNBC compliance built into every design — not added after inspection.</p>
      </div>
      <div class="reveal">
        <h3 class="font-display text-2xl">After-Sales Support</h3>
        <p class="font-body text-sm text-kaleo-cream/65 leading-relaxed mt-3">AMC contracts, operator training and rapid troubleshooting — long after handover.</p>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-sand py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="text-center reveal"><h2 class="font-display text-3xl md:text-5xl text-kaleo-earth">Team &amp; Workshop</h2></div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <h3 class="font-display text-xl text-kaleo-earth">Leadership</h3>
          <ul class="mt-4 space-y-2.5 font-body text-sm text-kaleo-earth/70">
            <li><strong class="text-kaleo-earth">Engr. Mostafa Shawkat Imran</strong> — Proprietor &amp; CEO, B.Sc. ME (RUET), MBA, Fellow IEB (F-11718)</li>
            <li><strong class="text-kaleo-earth">Engr. Md. Shofiqul Hoque</strong> — Head of Operation, MBA; ex-Plant Engineer, Akij Food</li>
            <li><strong class="text-kaleo-earth">Tajkia Jahan Rumana</strong> — Manager, Finance, Accounts &amp; Admin</li>
            <li><strong class="text-kaleo-earth">Shahriar Afsar Khan</strong> — Head of Marketing, MBA</li>
          </ul>
        </div>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <h3 class="font-display text-xl text-kaleo-earth">Engineering</h3>
          <ul class="mt-4 space-y-2.5 font-body text-sm text-kaleo-earth/70">
            <li><strong class="text-kaleo-earth">Dilruba Hossain</strong> — Architect, MIAB (H-189)</li>
            <li><strong class="text-kaleo-earth">A.S.M. Hadiul Islam</strong> — Architect, MIAB (I-149)</li>
            <li><strong class="text-kaleo-earth">Md. Neyamotullah</strong> — Junior Architect (10 yrs)</li>
            <li><strong class="text-kaleo-earth">Md. Saidur Rahman</strong> — B.Sc. EEE (17 yrs, 3 yrs abroad)</li>
            <li><strong class="text-kaleo-earth">Md. Robiul Alam</strong> — B.Sc. CE (15 yrs)</li>
            <li><strong class="text-kaleo-earth">Md. Masudul Amin</strong> — B.Sc. CE (15 yrs)</li>
            <li>2 CAD draftsmen · 6 technicians · 5 office staff</li>
          </ul>
        </div>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <h3 class="font-display text-xl text-kaleo-earth">Workshop &amp; Equipment</h3>
          <p class="font-body text-sm text-kaleo-earth/70 mt-4 leading-relaxed">1,680 sft workshop at Khilgaon, Dhaka with welding rigs (arc, TIG, gas), cutting and drilling machines, scaffolding, chain pulleys and a full set of measurement instruments — decibel meters, tachometers, calipers and more.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-cream py-20">
    <div class="max-w-4xl mx-auto px-6 md:px-8 text-center reveal">
      <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Ready to Work Together?</p>
      <a href="contact.html" class="inline-block mt-6 font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-10 py-4 hover:bg-kaleo-terracotta transition-colors">Contact NSP</a>
    </div>
  </section>
"""
write_page("why-nsp.html", "Why NSP — Nobo Shakti Prokushal",
           "Why clients choose NSP: in-house engineering team, verified credentials, code-first delivery, own workshop and after-sales support.",
           "why-nsp.html", why_body)

# ============================================================ COLLABORATION
collab_cards = [
    ("Sister Concerns &amp; Group", [
        "NeoMed Healthcare Services (est. 2014) — medical supply and healthcare support",
        "PT Sun Moon Ecosystem — Indonesia (regional operations and eco-tourism engineering)",
    ]),
    ("Partner Companies", [
        "Cooltech Corporation",
        "Ferrotech Bangladesh",
        "Allex Design and Interior",
    ]),
]

def collab_block(title, items):
    lis = "\n".join(f'            <li class="flex items-start gap-3"><span class="text-kaleo-terracotta mt-1">—</span><span class="font-body text-sm text-kaleo-earth/75">{i}</span></li>' for i in items)
    return f"""        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 md:p-10">
          <h2 class="font-display text-2xl md:text-3xl text-kaleo-earth">{title}</h2>
          <ul class="mt-5 space-y-3">
{lis}
          </ul>
        </div>"""

collab_html = "\n\n".join(collab_block(t, i) for t, i in collab_cards)

collaboration_body = page_header(
    "Collaboration",
    "Stronger Together",
    "NSP works with sister concerns and specialist partner companies across Bangladesh and beyond — and is open to new collaborations.",
) + f"""
  <section class="bg-kaleo-cream py-16 md:py-24 border-b border-kaleo-earth/10">
    <div class="max-w-7xl mx-auto px-6 md:px-8">
      <div class="max-w-3xl reveal">
        <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Our Vision · Digital Manufacturing Platform</span>
        <h2 class="font-display text-3xl md:text-5xl text-kaleo-earth mt-4 leading-tight">A Collaborative Innovation Ecosystem for Bangladesh</h2>
        <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-5">
          Grounded in NSP's research — <em>"Scalable Collaborative Innovation in Bangladesh's Industrial and Healthcare Sectors: Addressing Access and Skills Challenges for Sustainable Growth"</em> — we are building a digital platform that carries a product from the design notebook straight to the client's hands, unifying engineers, SME cottage manufacturers, universities and clients in a single trusted network.
        </p>
      </div>

      <h3 class="font-display text-2xl md:text-3xl text-kaleo-earth mt-14 reveal">The Product Realization Pipeline</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-5 mt-8">
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phase 01</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Design Notebook</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Secure upload of sketches, CAD models and theoretical design notebooks into a protected cloud workspace.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phase 02</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">SME Integration</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Bills of materials decomposed and routed to verified SME cottage-industry clusters (Bogura, Keraniganj) — import-substitution manufacturing.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phase 03</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Prototyping</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">University students and research labs convert breakdown spares into advanced machinery prototypes via the academic integration module.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phase 04</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Smart Assembly</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Production milestones, sensor data and automated test logs tracked on real-time supervisory dashboards.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phase 05</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Client Handover</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Final delivery with digital twins, maintenance manuals and ongoing IoT telemetry support.</p>
        </div>
      </div>

      <h3 class="font-display text-2xl md:text-3xl text-kaleo-earth mt-14 reveal">The "InnoChain &amp; Match" Protocol</h3>
      <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-4 max-w-3xl reveal">The network protocol behind the platform operates across three synchronized layers — automating trust, precision and efficiency.</p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
        <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Layer 1</span>
          <h4 class="font-display text-xl mt-3">Intelligent Discovery &amp; Routing</h4>
          <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">An AI matching engine pairs project parameters with verified engineers and manufacturers — by skill set, machine bandwidth, geographic proximity and track record.</p>
        </div>
        <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Layer 2</span>
          <h4 class="font-display text-xl mt-3">Secure Ledger &amp; Transparent Execution</h4>
          <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">A permissioned blockchain core runs smart contracts for milestone payments and design-IP protection, with tamper-proof audit trails.</p>
        </div>
        <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Layer 3</span>
          <h4 class="font-display text-xl mt-3">Real-Time Operational Telemetry</h4>
          <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">Lightweight MQTT/WebSocket tracking for milestones, inventory alerts and instant engineer–workshop–client communication.</p>
        </div>
      </div>

      <h3 class="font-display text-2xl md:text-3xl text-kaleo-earth mt-14 reveal">Inside the Matching Engine</h3>
      <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-4 max-w-3xl reveal">A multi-attribute utility scoring model pairs each project with the most qualified engineers, manufacturers and SME cottage industries — moving far beyond basic keyword search.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mt-8">
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <p class="font-display text-4xl text-kaleo-terracotta">35%</p>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Skill Compatibility</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Technical competencies — electromechanical design, CAD modelling, gas separation, automation programming — scored against verified skill profiles.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <p class="font-display text-4xl text-kaleo-terracotta">25%</p>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Workshop Capacity</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Machine bandwidth, tool availability and operational scale — verifying tolerance, material (SS316, carbon steel) and batch volume capability.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <p class="font-display text-4xl text-kaleo-terracotta">20%</p>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Logistics Proximity</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Distance and transport corridors between raw material source, manufacturing units and the client delivery site — minimizing delay and cost.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-6">
          <p class="font-display text-4xl text-kaleo-terracotta">20%</p>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Performance &amp; Compliance</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Past delivery times, quality audit results, client satisfaction and adherence to ISO 9001 and ASME codes.</p>
        </div>
      </div>
      <div class="reveal mt-6 bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-6 text-center">
        <p class="font-body text-sm text-kaleo-earth/60 uppercase tracking-[0.15em]">Total Match Score</p>
        <p class="font-display text-xl md:text-2xl text-kaleo-earth mt-2">(0.35 × Skill) + (0.25 × Capacity) + (0.20 × Logistics) + (0.20 × Performance)</p>
      </div>

      <h3 class="font-display text-2xl md:text-3xl text-kaleo-earth mt-14 reveal">Smart Contract Conditions</h3>
      <p class="font-body text-base text-kaleo-earth/70 leading-relaxed mt-4 max-w-3xl reveal">Across each project lifecycle milestone, the permissioned blockchain executes automated smart contracts — turning trust into code.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mt-8">
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-7">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Condition 1</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Design Notebook IP Protection</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">On upload of CAD files or design notes, the contract encrypts the IP, logs a cryptographic hash with timestamp, and enforces digitally signed NDAs before decryption keys are granted.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-7">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Condition 2</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Milestone-Based Escrow Release</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Funds held in escrow are released to cottage industries or suppliers only when IoT sensor data, quality logs or client sign-offs are validated on the ledger.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-7">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Condition 3</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Quality &amp; Material Certification Check</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">Material test reports and NDT results are cross-referenced against specifications — NACE MR0175, ASME grades — halting assembly workflows if tolerances fall outside limits.</p>
        </div>
        <div class="reveal bg-white/70 border border-kaleo-earth/10 rounded-3xl p-7">
          <span class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Condition 4</span>
          <h4 class="font-display text-xl text-kaleo-earth mt-3">Automated Handover &amp; Warranty</h4>
          <p class="font-body text-sm text-kaleo-earth/70 leading-relaxed mt-2">On final client acceptance, the contract transfers digital ownership titles, issues verified digital warranties and starts the telemetry and maintenance logging schedule.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-kaleo-sand py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 md:grid-cols-3 gap-6">
{collab_html}
    </div>

    <div class="max-w-7xl mx-auto px-6 md:px-8 mt-14">
      <div class="reveal bg-kaleo-earth text-kaleo-cream rounded-3xl p-8 md:p-12">
        <h2 class="font-display text-2xl md:text-4xl text-center">Ways to Collaborate with NSP</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mt-10">
          <div>
            <h3 class="font-display text-xl text-kaleo-terracotta">Joint Ventures</h3>
            <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">Partner with NSP on hospital, industrial and infrastructure tenders in Bangladesh.</p>
          </div>
          <div>
            <h3 class="font-display text-xl text-kaleo-terracotta">Subcontracting</h3>
            <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">Reliable execution arm for MEP, medical gas, acoustics and commissioning scopes.</p>
          </div>
          <div>
            <h3 class="font-display text-xl text-kaleo-terracotta">Supply Partnership</h3>
            <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">NSP imports pipes, fittings, valves, hospital equipment and solar components — and distributes quality products.</p>
          </div>
          <div>
            <h3 class="font-display text-xl text-kaleo-terracotta">Research Collaboration</h3>
            <p class="font-body text-sm text-kaleo-cream/70 leading-relaxed mt-2">Applied R&amp;D in bi-fuel engines, renewable energy and healthcare engineering — open to university and institutional research partnerships.</p>
          </div>
        </div>
        <div class="text-center mt-10">
          <a href="contact.html" class="inline-block font-body text-sm uppercase tracking-[0.12em] bg-kaleo-terracotta text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-cream hover:text-kaleo-earth transition-all">Propose a Collaboration</a>
        </div>
      </div>
    </div>
  </section>
"""
write_page("collaboration.html", "Collaboration — Nobo Shakti Prokushal (NSP)",
           "Collaborate with NSP: sister concerns (NeoMed, PT Sun Moon Ecosystem), partner companies, joint ventures, subcontracting, supply and research.",
           "collaboration.html", collaboration_body)

# ============================================================ CONTACT
contact_body = page_header(
    "Contact NSP",
    "Let's Talk About Your Project",
    "Call, email or WhatsApp — or send the form and we will respond within one business day.",
) + """
  <section class="bg-kaleo-sand py-16 md:py-24">
    <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12">

      <div class="space-y-6">
        <a href="tel:+8801714073604" class="reveal block bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 hover:border-kaleo-terracotta/50 transition-colors">
          <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Phone</p>
          <p class="font-display text-2xl md:text-3xl text-kaleo-earth mt-2">+880 1714 073604</p>
          <p class="font-body text-sm text-kaleo-earth/60 mt-1">+880 1711 055476</p>
        </a>
        <a href="https://wa.me/8801714073604" class="reveal block bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 hover:border-kaleo-terracotta/50 transition-colors">
          <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">WhatsApp</p>
          <p class="font-display text-2xl md:text-3xl text-kaleo-earth mt-2">Chat with NSP</p>
        </a>
        <a href="mailto:info@mostafasimran.com" class="reveal block bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 hover:border-kaleo-terracotta/50 transition-colors">
          <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Email</p>
          <p class="font-display text-2xl md:text-3xl text-kaleo-earth mt-2">info@mostafasimran.com</p>
        </a>
        <div class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8">
          <p class="font-body text-xs uppercase tracking-[0.2em] text-kaleo-terracotta">Offices</p>
          <p class="font-body text-sm text-kaleo-earth/75 mt-3 leading-relaxed"><strong class="text-kaleo-earth">Corporate:</strong> 73/H (GF) Green Road, Dhaka-1205<br /><strong class="text-kaleo-earth">Workshop:</strong> House #10, Road #5/B, Middle Nandi Para, Khilgaon, Dhaka-1214</p>
          <p class="font-body text-xs text-kaleo-earth/50 mt-4">TIN 653549294117 · BIN 19021092318 · Trade License 000258 · IRC 104713</p>
        </div>
      </div>

      <form action="https://formsubmit.co/info@noboshaktiprokushal.com" method="POST" class="reveal bg-kaleo-cream border border-kaleo-earth/10 rounded-3xl p-8 md:p-10 space-y-5">
        <input type="hidden" name="_subject" value="NSP Website Inquiry" />
        <input type="hidden" name="_captcha" value="false" />
        <input type="hidden" name="_template" value="table" />
        <input type="hidden" name="_autoresponse" value="Thank you for contacting Nobo Shakti Prokushal (NSP). Your inquiry has been received — our team will respond within one business day. — NSP, Dhaka | +880 1714 073604 | www.noboshaktiprokushal.com" />
        <div>
          <label class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60" for="name">Your Name</label>
          <input id="name" name="name" required class="mt-2 w-full bg-kaleo-sand border border-kaleo-earth/15 rounded-xl px-4 py-3.5 font-body text-sm text-kaleo-earth focus:outline-none focus:border-kaleo-terracotta" />
        </div>
        <div>
          <label class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60" for="email">Email</label>
          <input id="email" name="email" type="email" required class="mt-2 w-full bg-kaleo-sand border border-kaleo-earth/15 rounded-xl px-4 py-3.5 font-body text-sm text-kaleo-earth focus:outline-none focus:border-kaleo-terracotta" />
        </div>
        <div>
          <label class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60" for="interest">I'm interested in</label>
          <select id="interest" name="interest" class="mt-2 w-full bg-kaleo-sand border border-kaleo-earth/15 rounded-xl px-4 py-3.5 font-body text-sm text-kaleo-earth focus:outline-none focus:border-kaleo-terracotta">
            <option>Products — Vehicle Body Structure</option>
            <option>Products — Sound Pod</option>
            <option>Products — Capsule Homes</option>
            <option>Products — Solar Home</option>
            <option>Services — Design &amp; Documentation</option>
            <option>Services — 3D Printing &amp; Prototyping</option>
            <option>Services — Machine Design</option>
            <option>Projects — System Installation &amp; Commissioning</option>
            <option>Projects — Machine Installation &amp; Commissioning</option>
            <option>Collaboration</option>
            <option>Other</option>
          </select>
        </div>
        <div>
          <label class="font-body text-xs uppercase tracking-[0.15em] text-kaleo-earth/60" for="message">Message</label>
          <textarea id="message" name="message" rows="5" class="mt-2 w-full bg-kaleo-sand border border-kaleo-earth/15 rounded-xl px-4 py-3.5 font-body text-sm text-kaleo-earth focus:outline-none focus:border-kaleo-terracotta"></textarea>
        </div>
        <button type="submit" class="w-full font-body text-sm uppercase tracking-[0.12em] bg-kaleo-earth text-kaleo-cream rounded-full px-8 py-4 hover:bg-kaleo-terracotta transition-colors">
          Send Inquiry
        </button>
      </form>
    </div>
  </section>
"""
write_page("contact.html", "Contact — Nobo Shakti Prokushal (NSP)",
           "Contact NSP: phone, WhatsApp, email and inquiry form for engineering products, design services, installation projects and collaboration in Bangladesh.",
           "contact.html", contact_body)

print("done")
