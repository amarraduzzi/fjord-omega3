T={'de':dict(t='Fjord – Omega-3, tief erklärt',d='Unabhängiges Wissen über Omega-3-Fettsäuren: was sie sind, wo sie vorkommen und was die Forschung sagt.',nav=['Fettsäuren','Quellen','Forschung','FAQ'],eb='Unabhängiges Omega-3-Wissen',h='Tauche ein in die <em>Tiefe</em> von Omega-3',s='Was sind ALA, EPA und DHA, woher kommen sie – und was sagt die Forschung wirklich? Klar erklärt, ohne Versprechen.',cta='Reise beginnen',st=['Fettsäuren','Quellen','Studien erklärt'],mq=['ALA · EPA · DHA','Meer & Pflanze','Was die Forschung sagt','Klar statt Werbung','Wissen aus der Tiefe']),
'fr':dict(t='Fjord – Les oméga-3, en profondeur',d='Un savoir indépendant sur les acides gras oméga-3 : ce qu’ils sont, où les trouver et ce que dit la recherche.',nav=['Acides gras','Sources','Recherche','FAQ'],eb='Savoir oméga-3 indépendant',h='Plongez dans les <em>profondeurs</em> des oméga-3',s='Que sont l’ALA, l’EPA et le DHA, d’où viennent-ils – et que dit vraiment la recherche ? Expliqué simplement, sans promesses.',cta='Commencer le voyage',st=['Acides gras','Sources','Études décryptées'],mq=['ALA · EPA · DHA','Mer & plantes','Ce que dit la recherche','Clair, pas publicitaire','Le savoir des profondeurs']),
'it':dict(t='Fjord – Gli omega-3, in profondità',d='Conoscenza indipendente sugli acidi grassi omega-3: cosa sono, dove si trovano e cosa dice la ricerca.',nav=['Acidi grassi','Fonti','Ricerca','FAQ'],eb='Sapere omega-3 indipendente',h='Immergiti nelle <em>profondità</em> degli omega-3',s='Cosa sono ALA, EPA e DHA, da dove arrivano – e cosa dice davvero la ricerca? Spiegato chiaramente, senza promesse.',cta='Inizia il viaggio',st=['Acidi grassi','Fonti','Studi spiegati'],mq=['ALA · EPA · DHA','Mare & piante','Cosa dice la ricerca','Chiaro, non pubblicità','Sapere dalle profondità'])}
A={'de':dict(k='Die Tiefe-Reise',h='Drei Fettsäuren, drei <em>Tiefen</em>',p='Tippe auf eine Fettsäure und sieh dir ihre Kette an.',ch='Kohlenstoffe',db='Doppelbindungen',src='Vorkommen',
 it=[('ALA','Alpha-Linolensäure','Die pflanzliche Omega-3-Fettsäure. Der Körper nutzt sie als Baustein und wandelt nur einen kleinen Teil in EPA und DHA um.','Leinsamen, Chiasamen, Walnüsse, Rapsöl'),
 ('EPA','Eicosapentaensäure','Eine langkettige Omega-3-Fettsäure aus dem Meer. Sie ist Gegenstand vieler Studien zu Herz und Kreislauf.','Fetter Fisch, Meeresalgen'),
 ('DHA','Docosahexaensäure','Ein Hauptbestandteil der Zellmembranen in Gehirn und Netzhaut. Die längste und komplexeste der drei Ketten.','Fetter Fisch, Mikroalgen')],dp=['0 m · Oberfläche','200 m · Dämmerzone','1000 m · Tiefsee']),
'fr':dict(k='Le voyage en profondeur',h='Trois acides gras, trois <em>profondeurs</em>',p='Touchez un acide gras pour voir sa chaîne.',ch='Carbones',db='Doubles liaisons',src='Sources',
 it=[('ALA','Acide alpha-linolénique','L’oméga-3 d’origine végétale. Le corps l’utilise comme brique de base et n’en convertit qu’une petite part en EPA et DHA.','Graines de lin, chia, noix, huile de colza'),
 ('EPA','Acide eicosapentaénoïque','Un oméga-3 à longue chaîne venu de la mer, au cœur de nombreuses études sur le cœur et la circulation.','Poissons gras, algues marines'),
 ('DHA','Acide docosahexaénoïque','Un constituant majeur des membranes cellulaires du cerveau et de la rétine. La chaîne la plus longue et la plus complexe des trois.','Poissons gras, microalgues')],dp=['0 m · Surface','200 m · Zone crépusculaire','1000 m · Grands fonds']),
'it':dict(k='Il viaggio in profondità',h='Tre acidi grassi, tre <em>profondità</em>',p='Tocca un acido grasso per vederne la catena.',ch='Carboni',db='Doppi legami',src='Fonti',
 it=[('ALA','Acido alfa-linolenico','L’omega-3 di origine vegetale. Il corpo lo usa come mattone di base e ne converte solo una piccola parte in EPA e DHA.','Semi di lino, chia, noci, olio di colza'),
 ('EPA','Acido eicosapentaenoico','Un omega-3 a catena lunga di origine marina, oggetto di molti studi su cuore e circolazione.','Pesce grasso, alghe marine'),
 ('DHA','Acido docosaesaenoico','Un componente principale delle membrane cellulari di cervello e retina. La catena più lunga e complessa delle tre.','Pesce grasso, microalghe')],dp=['0 m · Superficie','200 m · Zona crepuscolare','1000 m · Grandi profondità'])}
NC=[(18,3),(20,5),(22,6)]
B='https://fjord-omega3.ch'
for l,c in T.items():
    alt=''.join(f'<link rel="alternate" hreflang="{k}" href="{B}/{k}/">' for k in T)+f'<link rel="alternate" hreflang="x-default" href="{B}/">'
    nav=''.join(f'<a href="#{i}">{n}</a>' for i,n in zip(['acids','sources','research','faq'],c['nav']))
    lang=''.join(f'<a href="/{k}/" class="{"on" if k==l else ""}" hreflang="{k}">{k.upper()}</a>' for k in T)
    mq=''.join(f'<span>{m}</span>' for m in c['mq']*2)

    a=A[l];cards=''.join(f'<button class="card rv" data-c="{NC[i][0]}" data-d="{NC[i][1]}" data-i="{i}"><small>{a["dp"][i]}</small><b>{x[0]}</b><span>{x[1]}</span></button>' for i,x in enumerate(a['it']))
    det=''.join(f'<div class="det" data-i="{i}"><h3>{x[1]}</h3><p>{x[2]}</p><p class="src"><strong>{a["src"]}:</strong> {x[3]}</p></div>' for i,x in enumerate(a['it']))
    acids=f'''<section id="acids" class="deep"><div class="wrap"><span class="eyebrow">{a['k']}</span><h2>{a['h']}</h2><p class="sub">{a['p']}</p>
<div class="cards">{cards}</div><div class="panel"><svg id="chain" viewBox="0 0 900 150" aria-hidden="true"></svg><div class="meta"><div><b id="mc">18</b><span>{a['ch']}</span></div><div><b id="md">3</b><span>{a['db']}</span></div></div>{det}</div></div></section>'''
    open(f'{l}/index.html','w',encoding='utf-8').write(f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c['t']}</title><meta name="description" content="{c['d']}"><link rel="canonical" href="{B}/{l}/">{alt}
<meta property="og:title" content="{c['t']}"><meta property="og:description" content="{c['d']}"><meta property="og:image" content="{B}/assets/img/og.jpg">
<link rel="icon" href="/assets/fjord.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css"><script src="/assets/fjord.js" defer></script></head><body>
<header class="nav"><a class="logo" href="/{l}/"><i></i>FJORD</a><nav class="menu">{nav}<div class="lang">{lang}</div></nav></header>
<main><section class="hero"><canvas id="sea"></canvas><div class="in">
<span class="eyebrow rv">{c['eb']}</span><h1 class="rv">{c['h']}</h1><p class="sub rv">{c['s']}</p><a class="cta rv" href="#acids">{c['cta']} ↓</a>
<div class="stats rv"><div><b data-count="3">0</b><span>{c['st'][0]}</span></div><div><b data-count="2">0</b><span>{c['st'][1]}</span></div><div><b data-count="12">0</b><span>{c['st'][2]}</span></div></div></div><div class="scroll"></div></section>
<div class="band"><div>{mq}</div></div>{acids}</main></body></html>''')
