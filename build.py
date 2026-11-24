import re,os
MAIN='https://molitademo1.pages.dev'
LG={'de':('Kohlenstoffkette','Doppelbindung'),'fr':('Chaîne de carbones','Double liaison'),'it':('Catena di carbonio','Doppio legame')}
MORE={'de':'Mehr zum Thema','fr':'En savoir plus','it':'Approfondisci'}
STRIP={'de':'Weiterführende Informationen zum Thema','fr':'Informations complémentaires sur le sujet','it':'Informazioni di approfondimento sul tema'}
DISC={'de':'Fjord ist ein Informationsprojekt und mit der Seite','fr':'Fjord est un projet d’information lié au site','it':'Fjord è un progetto informativo collegato al sito'}
def L(l,place,label=None,cls='xl'):
    return f'<a class="{cls}" href="{MAIN}/?utm_source=fjord&amp;utm_medium={l}&amp;utm_content={place}" rel="noopener">{label or MORE[l]}</a>'
def disc(l):
    suf={'de':'verbunden.','fr':'.','it':'.'}[l]
    return '<p class="disc">'+DISC[l]+' '+L(l,'footer','molitademo1.pages.dev','xl2')+(' '+suf if l=='de' else suf)+'</p>'
T={'de':dict(t='Fjord – Omega-3, tief erklärt',d='Wissen über Omega-3-Fettsäuren: was sie sind, wo sie vorkommen und was die Forschung sagt.',nav=['Fettsäuren','Quellen','Forschung','FAQ'],eb='Omega-3-Wissen, klar erklärt',h='Tauche ein in die <em>Tiefe</em> von Omega-3',s='Was sind ALA, EPA und DHA, woher kommen sie – und was sagt die Forschung wirklich? Klar erklärt, ohne Versprechen.',cta='Reise beginnen',st=['Fettsäuren','Quellen','Forschungsfragen'],mq=['ALA · EPA · DHA','Meer & Pflanze','Was die Forschung sagt','Klar statt Werbung','Wissen aus der Tiefe']),
'fr':dict(t='Fjord – Les oméga-3, en profondeur',d='Un savoir sur les acides gras oméga-3 : ce qu’ils sont, où les trouver et ce que dit la recherche.',nav=['Acides gras','Sources','Recherche','FAQ'],eb='Le savoir oméga-3, clairement',h='Plongez dans les <em>profondeurs</em> des oméga-3',s='Que sont l’ALA, l’EPA et le DHA, d’où viennent-ils – et que dit vraiment la recherche ? Expliqué simplement, sans promesses.',cta='Commencer le voyage',st=['Acides gras','Sources','Questions de recherche'],mq=['ALA · EPA · DHA','Mer & plantes','Ce que dit la recherche','Clair, pas publicitaire','Le savoir des profondeurs']),
'it':dict(t='Fjord – Gli omega-3, in profondità',d='Conoscenza sugli acidi grassi omega-3: cosa sono, dove si trovano e cosa dice la ricerca.',nav=['Acidi grassi','Fonti','Ricerca','FAQ'],eb='Il sapere omega-3, chiaro',h='Immergiti nelle <em>profondità</em> degli omega-3',s='Cosa sono ALA, EPA e DHA, da dove arrivano – e cosa dice davvero la ricerca? Spiegato chiaramente, senza promesse.',cta='Inizia il viaggio',st=['Acidi grassi','Fonti','Domande di ricerca'],mq=['ALA · EPA · DHA','Mare & piante','Cosa dice la ricerca','Chiaro, non pubblicità','Sapere dalle profondità'])}
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
S={'de':dict(k='Quellen-Entdecker',h='Woher kommt <em>Omega-3</em>?',p='Wähle eine Welt und vergleiche den Gehalt pro 100 g.',tabs=['Meer','Pflanze','Algen'],u=['g EPA+DHA pro 100 g','g ALA pro 100 g'],alg='Mikroalgenöl liefert DHA, teils auch EPA. Der Gehalt variiert je nach Produkt, deshalb steht hier keine Zahl.',
 sea=['Makrele','Lachs','Hering','Sardine','Forelle','Thunfisch (Dose)'],pl=['Leinöl','Leinsamen','Chiasamen','Walnüsse','Rapsöl'],
 ct='Wie viel ist <em>genug</em>?',cp='Als Orientierung nennt die EFSA für Erwachsene 250 mg EPA+DHA pro Tag, also etwa 1,75 g pro Woche. Die Werte sind Durchschnitte und schwanken je nach Art und Herkunft. Das ist keine individuelle Empfehlung.',cf='Fisch',cn='Portionen à 100 g pro Woche',cr='der Wochen-Orientierung',cg='EPA+DHA pro Woche',lg='de-CH'),
'fr':dict(k='L’explorateur de sources',h='D’où viennent les <em>oméga-3</em> ?',p='Choisissez un monde et comparez la teneur pour 100 g.',tabs=['Mer','Plantes','Algues'],u=['g d’EPA+DHA pour 100 g','g d’ALA pour 100 g'],alg='L’huile de microalgues apporte du DHA, parfois aussi de l’EPA. La teneur varie selon le produit, d’où l’absence de chiffre.',
 sea=['Maquereau','Saumon','Hareng','Sardine','Truite','Thon en conserve'],pl=['Huile de lin','Graines de lin','Graines de chia','Noix','Huile de colza'],
 ct='Combien, <em>c’est assez</em> ?',cp='À titre d’orientation, l’EFSA cite 250 mg d’EPA+DHA par jour pour les adultes, soit environ 1,75 g par semaine. Les valeurs sont des moyennes qui varient selon l’espèce et l’origine. Ce n’est pas une recommandation individuelle.',cf='Poisson',cn='portions de 100 g par semaine',cr='de l’orientation hebdomadaire',cg='d’EPA+DHA par semaine',lg='fr-CH'),
'it':dict(k='L’esploratore delle fonti',h='Da dove arrivano gli <em>omega-3</em>?',p='Scegli un mondo e confronta il contenuto per 100 g.',tabs=['Mare','Piante','Alghe'],u=['g di EPA+DHA per 100 g','g di ALA per 100 g'],alg='L’olio di microalghe fornisce DHA, a volte anche EPA. Il contenuto varia secondo il prodotto, per questo qui non c’è un numero.',
 sea=['Sgombro','Salmone','Aringa','Sardina','Trota','Tonno in scatola'],pl=['Olio di lino','Semi di lino','Semi di chia','Noci','Olio di colza'],
 ct='Quanto è <em>abbastanza</em>?',cp='Come orientamento, l’EFSA indica 250 mg di EPA+DHA al giorno per gli adulti, cioè circa 1,75 g a settimana. I valori sono medie e variano secondo specie e origine. Non è una raccomandazione individuale.',cf='Pesce',cn='porzioni da 100 g a settimana',cr='dell’orientamento settimanale',cg='di EPA+DHA a settimana',lg='it-CH')}
SV=[2.5,2.0,1.7,1.4,1.0,0.3];PV=[53,22,17.5,9,9]
R={'de':dict(k='Forschung',h='Was die Forschung <em>wirklich</em> sagt',p='Vier Fragen, ehrlich und ohne Versprechen beantwortet.',
 r=[('Herz und Kreislauf','Beobachtungsstudien verbinden regelmässigen Fischverzehr oft mit günstigeren Herz-Kreislauf-Werten. Studien mit Omega-3-Präparaten kommen dagegen zu uneinheitlichen Ergebnissen. Ernährung als Ganzes spielt eine grosse Rolle.'),
 ('Gehirn und Augen','DHA ist ein Baustein der Zellmembranen in Gehirn und Netzhaut. Ob eine zusätzliche Zufuhr bei gesunden Erwachsenen messbare Effekte hat, ist in Studien bisher nicht eindeutig belegt.'),
 ('Schwangerschaft und Stillzeit','Fachgesellschaften weisen darauf hin, in dieser Zeit auf eine ausreichende DHA-Zufuhr zu achten. Was für dich passt, klärst du am besten mit einer Fachperson.'),
 ('Wie liest man eine Studie?','Beobachtungsstudien zeigen Zusammenhänge, aber keine Ursachen. Kontrollierte Studien sind aussagekräftiger. Achte auf Dosis, Dauer, Teilnehmende und darauf, wer die Studie finanziert hat.')],
 fk='FAQ',fh='Häufige <em>Fragen</em>',
 f=[('Was ist der Unterschied zwischen ALA, EPA und DHA?','ALA stammt aus Pflanzen, EPA und DHA kommen vor allem aus Fisch und Meeresalgen. EPA und DHA sind länger und komplexer gebaut als ALA.'),
 ('Wandelt der Körper ALA in EPA und DHA um?','Ja, aber nur zu einem kleinen Teil. Deshalb gelten Fisch und Algen als direkte Quellen für EPA und DHA.'),
 ('Ist Algenöl eine Alternative zu Fisch?','Mikroalgen bilden DHA und teils EPA selbst. Fische nehmen diese Fettsäuren über Algen auf. Algenöl ist daher eine pflanzliche Quelle.'),
 ('Brauche ich ein Präparat?','Das hängt von deiner Ernährung ab. Wer regelmässig fetten Fisch isst, deckt den Orientierungswert oft über das Essen. Bei Unsicherheit hilft eine Ärztin, ein Arzt oder eine Ernährungsberatung.')],
 ft='Fjord ist ein Informationsangebot. Die Inhalte dienen der allgemeinen Information und ersetzen keine medizinische Beratung, Diagnose oder Behandlung.'),
'fr':dict(k='Recherche',h='Ce que dit <em>vraiment</em> la recherche',p='Quatre questions, des réponses honnêtes et sans promesses.',
 r=[('Cœur et circulation','Les études d’observation associent souvent une consommation régulière de poisson à de meilleurs indicateurs cardiovasculaires. Les études avec des compléments d’oméga-3 donnent en revanche des résultats variables. L’alimentation dans son ensemble compte beaucoup.'),
 ('Cerveau et yeux','Le DHA est un constituant des membranes cellulaires du cerveau et de la rétine. Un effet mesurable d’un apport supplémentaire chez l’adulte en bonne santé n’est pas clairement établi.'),
 ('Grossesse et allaitement','Les sociétés savantes invitent à veiller à un apport suffisant en DHA pendant cette période. Ce qui vous convient se discute au mieux avec un professionnel de santé.'),
 ('Comment lire une étude ?','Les études d’observation montrent des liens, pas des causes. Les essais contrôlés sont plus solides. Regardez la dose, la durée, les participants et qui a financé l’étude.')],
 fk='FAQ',fh='Questions <em>fréquentes</em>',
 f=[('Quelle différence entre ALA, EPA et DHA ?','L’ALA vient des plantes ; l’EPA et le DHA viennent surtout des poissons et des algues marines. Leur chaîne est plus longue et plus complexe que celle de l’ALA.'),
 ('Le corps transforme-t-il l’ALA en EPA et DHA ?','Oui, mais seulement en petite partie. C’est pourquoi le poisson et les algues sont des sources directes d’EPA et de DHA.'),
 ('L’huile d’algues est-elle une alternative au poisson ?','Les microalgues produisent elles-mêmes du DHA et parfois de l’EPA. Les poissons les absorbent via les algues. L’huile d’algues est donc une source végétale.'),
 ('Ai-je besoin d’un complément ?','Cela dépend de votre alimentation. Qui mange régulièrement du poisson gras couvre souvent l’apport de référence par l’assiette. En cas de doute, demandez conseil à un médecin ou à un diététicien.')],
 ft='Fjord est un site d’information. Les contenus sont généraux et ne remplacent ni conseil médical, ni diagnostic, ni traitement.'),
'it':dict(k='Ricerca',h='Cosa dice <em>davvero</em> la ricerca',p='Quattro domande, risposte oneste e senza promesse.',
 r=[('Cuore e circolazione','Gli studi osservazionali associano spesso il consumo regolare di pesce a valori cardiovascolari più favorevoli. Gli studi con integratori di omega-3 danno invece risultati eterogenei. L’alimentazione nel suo insieme conta molto.'),
 ('Cervello e occhi','Il DHA è un componente delle membrane cellulari di cervello e retina. Un effetto misurabile di un apporto aggiuntivo negli adulti sani non è chiaramente dimostrato.'),
 ('Gravidanza e allattamento','Le società scientifiche invitano a garantire un apporto adeguato di DHA in questo periodo. Cosa è giusto per te lo chiarisci meglio con un professionista.'),
 ('Come si legge uno studio?','Gli studi osservazionali mostrano associazioni, non cause. Gli studi controllati sono più solidi. Guarda dose, durata, partecipanti e chi ha finanziato lo studio.')],
 fk='FAQ',fh='Domande <em>frequenti</em>',
 f=[('Qual è la differenza tra ALA, EPA e DHA?','L’ALA viene dalle piante; EPA e DHA vengono soprattutto da pesce e alghe marine. La loro catena è più lunga e complessa di quella dell’ALA.'),
 ('Il corpo trasforma l’ALA in EPA e DHA?','Sì, ma solo in piccola parte. Per questo pesce e alghe sono fonti dirette di EPA e DHA.'),
 ('L’olio di alghe è un’alternativa al pesce?','Le microalghe producono da sole DHA e a volte EPA. I pesci li assumono tramite le alghe. L’olio di alghe è quindi una fonte vegetale.'),
 ('Ho bisogno di un integratore?','Dipende dalla tua alimentazione. Chi mangia regolarmente pesce grasso spesso copre il valore di riferimento a tavola. In caso di dubbio chiedi a un medico o a un dietista.')],
 ft='Fjord è un sito informativo. I contenuti sono generali e non sostituiscono consulto, diagnosi o cura medica.')}
AR={
'de':dict(slug='algenoel-vs-fischoel',t='Algenöl oder Fischöl? Die Unterschiede erklärt – Fjord',d='Algenöl und Fischöl im Vergleich: Herkunft, Zusammensetzung und worauf man beim Vergleich achten kann. Sachlich erklärt, ohne Versprechen.',
 k='Artikel · 4 Min. Lesezeit',h='Algenöl oder <em>Fischöl</em>?',lead='Beide liefern die langkettigen Omega-3-Fettsäuren EPA und DHA. Der Unterschied liegt vor allem in Herkunft, Zusammensetzung und dem, worauf man beim Vergleich achten kann.',
 secs=[('Woher kommt das Omega-3?','Fische nehmen EPA und DHA über die Nahrungskette auf – am Anfang dieser Kette stehen Mikroalgen. Fischöl wird aus dem Fettgewebe von Fischen wie Makrele, Sardine oder Hering gewonnen. Algenöl stammt direkt aus Mikroalgen, die in kontrollierten Tanks wachsen. Der Umweg über den Fisch entfällt.'),
 ('Was steckt drin?','Fischöl enthält in der Regel EPA und DHA, in je nach Fischart unterschiedlichem Verhältnis. Bei Algenöl kommt es auf den verwendeten Algenstamm an: Viele Produkte enthalten vor allem DHA, andere zusätzlich EPA. Die tatsächliche Menge steht auf der Verpackung und unterscheidet sich von Produkt zu Produkt. Deshalb lohnt der Blick aufs Etikett mehr als der Blick auf die Produktart.'),
 ('Pflanzliches ALA ist etwas anderes','ALA aus Leinsamen, Chia oder Walnüssen ist eine kurzkettige Omega-3-Fettsäure. Der Körper kann sie nur in begrenztem Mass in EPA und DHA umwandeln. Algenöl ist deshalb keine Variante von ALA, sondern liefert EPA und DHA direkt.')],
 th=['','Algenöl','Fischöl'],rows=[('Ursprung','Mikroalgen aus Tanks','Fettgewebe von Fischen'),('Enthält','DHA, teils auch EPA','EPA und DHA'),('Vegan geeignet','Ja','Nein'),('Gehalt','Je nach Algenstamm und Produkt','Je nach Fischart und Produkt')],
 ch='Worauf du beim Vergleich achten kannst',ci=['EPA- und DHA-Menge pro Tagesportion, nicht nur „Omega-3 gesamt“','Form des Öls (zum Beispiel Triglycerid oder Ethylester)','Reinheit: Prüfberichte unabhängiger Labore','Frische: Verpackung, Haltbarkeit, Antioxidantien','Ernährungsform und Allergene (Fisch, vegan)','Preis pro Portion EPA und DHA, nicht pro Packung'],
 bh='Und was ist „besser“?',bp='Eine allgemeingültige Antwort gibt es nicht. Wer keinen Fisch isst, findet in Algenöl eine direkte Quelle für EPA und DHA. Wer Fisch mag, kann beide auch über Mahlzeiten aufnehmen. Ob ein Präparat sinnvoll ist, hängt von Ernährung und persönlicher Situation ab. Eine Fachperson kann das einordnen.',
 note='Dieser Artikel dient der allgemeinen Information. Er ersetzt keine ärztliche Beratung, Diagnose oder Behandlung.',back='← Zurück zu Fjord',
 tk='Artikel',th_='Algenöl <em>oder</em> Fischöl?',tp='Zwei Quellen für EPA und DHA im Vergleich: Herkunft, Zusammensetzung und worauf man achten kann.',tc='Artikel lesen'),
'fr':dict(slug='huile-algues-vs-huile-poisson',t='Huile d’algues ou huile de poisson ? Les différences – Fjord',d='Huile d’algues et huile de poisson comparées : origine, composition et points à vérifier. Expliqué simplement, sans promesses.',
 k='Article · 4 min de lecture',h='Huile d’algues ou <em>huile de poisson</em> ?',lead='Toutes deux apportent les oméga-3 à longue chaîne EPA et DHA. La différence tient surtout à l’origine, à la composition et aux points à vérifier lors d’une comparaison.',
 secs=[('D’où viennent ces oméga-3 ?','Les poissons absorbent l’EPA et le DHA par la chaîne alimentaire, qui commence par des microalgues. L’huile de poisson est extraite des tissus gras de poissons comme le maquereau, la sardine ou le hareng. L’huile d’algues provient directement de microalgues cultivées en cuves contrôlées. L’étape du poisson disparaît.'),
 ('Que contiennent-elles ?','L’huile de poisson contient en général de l’EPA et du DHA, dans des proportions variables selon l’espèce. Pour l’huile d’algues, tout dépend de la souche utilisée : beaucoup de produits contiennent surtout du DHA, d’autres aussi de l’EPA. La quantité réelle figure sur l’emballage et varie d’un produit à l’autre. L’étiquette compte donc davantage que le type de produit.'),
 ('L’ALA végétal, c’est autre chose','L’ALA des graines de lin, du chia ou des noix est un oméga-3 à chaîne courte. Le corps ne le transforme qu’en quantité limitée en EPA et en DHA. L’huile d’algues n’est donc pas une version de l’ALA : elle apporte directement de l’EPA et du DHA.')],
 th=['','Huile d’algues','Huile de poisson'],rows=[('Origine','Microalgues cultivées en cuves','Tissus gras de poissons'),('Contient','DHA, parfois aussi EPA','EPA et DHA'),('Convient aux vegans','Oui','Non'),('Teneur','Selon la souche et le produit','Selon l’espèce et le produit')],
 ch='Points à vérifier pour comparer',ci=['Quantité d’EPA et de DHA par portion quotidienne, pas seulement « oméga-3 total »','Forme de l’huile (par exemple triglycéride ou ester éthylique)','Pureté : rapports d’analyses de laboratoires indépendants','Fraîcheur : emballage, durée de conservation, antioxydants','Régime et allergènes (poisson, vegan)','Prix par portion d’EPA et de DHA, pas par boîte'],
 bh='Et laquelle est « meilleure » ?',bp='Il n’y a pas de réponse universelle. Qui ne mange pas de poisson trouve dans l’huile d’algues une source directe d’EPA et de DHA. Qui aime le poisson peut aussi les apporter par les repas. L’utilité d’un complément dépend de l’alimentation et de la situation personnelle. Un professionnel de santé peut aider à y voir clair.',
 note='Cet article est à visée d’information générale. Il ne remplace ni un avis médical, ni un diagnostic, ni un traitement.',back='← Retour à Fjord',
 tk='Article',th_='Huile d’algues <em>ou</em> huile de poisson ?',tp='Deux sources d’EPA et de DHA comparées : origine, composition et points à vérifier.',tc='Lire l’article'),
'it':dict(slug='olio-alghe-vs-olio-pesce',t='Olio di alghe o olio di pesce? Le differenze – Fjord',d='Olio di alghe e olio di pesce a confronto: origine, composizione e cosa controllare. Spiegato in modo chiaro, senza promesse.',
 k='Articolo · 4 min di lettura',h='Olio di alghe o <em>olio di pesce</em>?',lead='Entrambi forniscono gli omega-3 a catena lunga EPA e DHA. La differenza sta soprattutto nell’origine, nella composizione e in ciò che conviene controllare nel confronto.',
 secs=[('Da dove arrivano questi omega-3?','I pesci assumono EPA e DHA attraverso la catena alimentare, che parte dalle microalghe. L’olio di pesce si ricava dai tessuti grassi di pesci come sgombro, sardina o aringa. L’olio di alghe proviene direttamente da microalghe coltivate in vasche controllate. Il passaggio attraverso il pesce non c’è.'),
 ('Cosa contengono?','L’olio di pesce contiene in genere EPA e DHA, in proporzioni diverse a seconda della specie. Per l’olio di alghe conta il ceppo usato: molti prodotti contengono soprattutto DHA, altri anche EPA. La quantità reale è indicata sulla confezione e cambia da prodotto a prodotto. Per questo conta più l’etichetta che il tipo di prodotto.'),
 ('L’ALA vegetale è un’altra cosa','L’ALA di semi di lino, chia e noci è un omega-3 a catena corta. Il corpo lo trasforma in EPA e DHA solo in misura limitata. L’olio di alghe quindi non è una variante dell’ALA: fornisce direttamente EPA e DHA.')],
 th=['','Olio di alghe','Olio di pesce'],rows=[('Origine','Microalghe coltivate in vasche','Tessuti grassi dei pesci'),('Contiene','DHA, a volte anche EPA','EPA e DHA'),('Adatto ai vegani','Sì','No'),('Contenuto','Secondo il ceppo e il prodotto','Secondo la specie e il prodotto')],
 ch='Cosa controllare nel confronto',ci=['Quantità di EPA e DHA per porzione giornaliera, non solo «omega-3 totali»','Forma dell’olio (ad esempio trigliceride o estere etilico)','Purezza: rapporti di analisi di laboratori indipendenti','Freschezza: confezione, durata, antiossidanti','Regime alimentare e allergeni (pesce, vegano)','Prezzo per porzione di EPA e DHA, non per confezione'],
 bh='E quale è «meglio»?',bp='Non esiste una risposta valida per tutti. Chi non mangia pesce trova nell’olio di alghe una fonte diretta di EPA e DHA. Chi ama il pesce può assumerli anche con i pasti. L’utilità di un integratore dipende dall’alimentazione e dalla situazione personale. Un professionista della salute può aiutare a valutare.',
 note='Questo articolo ha scopo di informazione generale. Non sostituisce consulto, diagnosi o cura medica.',back='← Torna a Fjord',
 tk='Articolo',th_='Olio di alghe <em>o</em> olio di pesce?',tp='Due fonti di EPA e DHA a confronto: origine, composizione e cosa controllare.',tc='Leggi l’articolo'),
}

_n={'de':('Dieser Artikel dient der allgemeinen Information. Er ersetzt keine ärztliche Beratung, Diagnose oder Behandlung.','← Zurück zu Fjord'),'fr':('Cet article est à visée d’information générale. Il ne remplace ni un avis médical, ni un diagnostic, ni un traitement.','← Retour à Fjord'),'it':('Questo articolo ha scopo di informazione generale. Non sostituisce consulto, diagnosi o cura medica.','← Torna a Fjord')}
REL={'de':'Weiterlesen','fr':'À lire aussi','it':'Da leggere anche'}
AR2={
'de':dict(slug='omega3-etikett-lesen',t='Omega-3-Etikett lesen: Was wirklich zählt – Fjord',d='Menge, EPA und DHA, Form, Herkunft: so liest du das Etikett eines Omega-3-Produkts und vergleichst sachlich.',
 k='Artikel · 3 Min. Lesezeit',h='Das Etikett von <em>Omega-3</em> lesen',lead='Auf der Vorderseite fällt oft eine grosse Zahl auf. Entscheidend ist meist, was auf der Rückseite bei den Nährwerten und Zutaten steht.',
 secs=[('Öl ist nicht gleich Omega-3','«1000 mg Fischöl» bedeutet, dass die Kapsel 1000 mg Öl enthält. Davon ist nur ein Teil EPA und DHA. Ihre Menge steht separat auf der Packung und sagt, wie viel der gesuchten Fettsäuren tatsächlich enthalten ist.'),
 ('Pro Kapsel oder pro Portion?','Die Angaben beziehen sich manchmal auf eine Kapsel, manchmal auf die empfohlene Tagesportion, die aus mehreren Kapseln oder einem Teelöffel bestehen kann. Wer vergleicht, rechnet am besten alles auf dieselbe Basis um.'),
 ('Form und Zusatzstoffe','Omega-3-Öle gibt es unter anderem als Triglycerid oder als Ethylester. Zusätzlich können Antioxidantien wie Vitamin E enthalten sein, die das Öl vor dem Verderben schützen. Die Zutatenliste zeigt auch, ob Aromen oder Süssungsmittel dabei sind.')],
 th=['','Angabe','Was dahintersteckt'],rows=[('Menge','«1000 mg Fischöl» oder «Algenöl»','Gesamtmenge des Öls, nicht von EPA und DHA'),('EPA / DHA','Separat angegebene Menge','Gehalt der gesuchten Fettsäuren, pro Kapsel oder Portion prüfen'),('Form','Triglycerid, Ethylester','Chemische Form, in der die Fettsäuren im Öl gebunden sind'),('Herkunft','Fischart oder Algenstamm, Land','Zeigt, woher der Rohstoff stammt; seriöse Anbieter nennen sie')],
 ch='Fünf Fragen vor dem Kauf',ci=['Wie viel EPA und DHA stecken in einer Portion?','Auf wie viele Kapseln bezieht sich die Angabe?','Stammt das Öl aus Fisch oder aus Algen?','Gibt es Prüfberichte zu Reinheit und Frische?','Wie lange ist das Produkt haltbar und wie wird es gelagert?'],
 bh='Kurz gesagt',bp='Das Etikett verrät mehr als die Werbung. Wer Menge, Form und Herkunft kennt, kann Produkte nüchtern vergleichen, ob Fisch- oder Algenöl.',
 tk='Artikel',th_='Das Etikett von <em>Omega-3</em> lesen',tp='Ölmenge, EPA und DHA, Form, Herkunft: was die Packung wirklich sagt.',tc='Artikel lesen'),
'fr':dict(slug='lire-etiquette-omega-3',t='Lire une étiquette d’oméga-3 : ce qui compte – Fjord',d='Quantité, EPA et DHA, forme, origine : comment lire l’étiquette d’un produit oméga-3 et comparer sans parti pris.',
 k='Article · 3 min de lecture',h='Lire l’étiquette des <em>oméga-3</em>',lead='Sur le devant, un grand chiffre attire l’œil. L’essentiel se trouve le plus souvent au dos, dans les valeurs nutritionnelles et la liste des ingrédients.',
 secs=[('Huile ne veut pas dire oméga-3','« 1000 mg d’huile de poisson » signifie que la capsule contient 1000 mg d’huile. Seule une partie est de l’EPA et du DHA. Leur quantité est indiquée séparément sur l’emballage et dit combien des acides gras recherchés le produit contient vraiment.'),
 ('Par capsule ou par portion ?','Les indications portent parfois sur une capsule, parfois sur la portion quotidienne recommandée, qui peut compter plusieurs capsules ou une cuillère à café. Pour comparer, le plus simple est de ramener tout à la même base.'),
 ('Forme et additifs','Les huiles d’oméga-3 existent notamment sous forme de triglycéride ou d’ester éthylique. Des antioxydants comme la vitamine E peuvent être ajoutés pour protéger l’huile de l’oxydation. La liste des ingrédients montre aussi la présence d’arômes ou d’édulcorants.')],
 th=['','Mention','Ce qu’il y a derrière'],rows=[('Quantité','« 1000 mg d’huile de poisson » ou « d’algues »','Quantité totale d’huile, pas d’EPA et de DHA'),('EPA / DHA','Quantité indiquée séparément','Teneur en acides gras recherchés, à vérifier par capsule ou par portion'),('Forme','Triglycéride, ester éthylique','Forme chimique sous laquelle les acides gras sont liés dans l’huile'),('Origine','Espèce de poisson ou souche d’algues, pays','Montre d’où vient la matière première ; les fournisseurs sérieux l’indiquent')],
 ch='Cinq questions avant d’acheter',ci=['Combien d’EPA et de DHA contient une portion ?','À combien de capsules se rapporte l’indication ?','L’huile vient-elle de poisson ou d’algues ?','Existe-t-il des rapports d’analyses sur la pureté et la fraîcheur ?','Jusqu’à quand le produit se conserve-t-il, et comment le stocker ?'],
 bh='En bref',bp='L’étiquette en dit plus que la publicité. Qui connaît la quantité, la forme et l’origine peut comparer les produits sans parti pris, qu’il s’agisse d’huile de poisson ou d’algues.',
 tk='Article',th_='Lire l’étiquette des <em>oméga-3</em>',tp='Quantité d’huile, EPA et DHA, forme, origine : ce que dit vraiment l’emballage.',tc='Lire l’article'),
'it':dict(slug='leggere-etichetta-omega-3',t='Leggere l’etichetta degli omega-3: cosa conta – Fjord',d='Quantità, EPA e DHA, forma, origine: come leggere l’etichetta di un prodotto omega-3 e confrontare con sobrietà.',
 k='Articolo · 3 min di lettura',h='Leggere l’etichetta degli <em>omega-3</em>',lead='Sul fronte spicca un grande numero. L’essenziale di solito sta sul retro, tra valori nutrizionali e ingredienti.',
 secs=[('Olio non significa omega-3','«1000 mg di olio di pesce» vuol dire che la capsula contiene 1000 mg di olio. Solo una parte è EPA e DHA. La loro quantità è indicata a parte sulla confezione e dice quanti degli acidi grassi cercati ci sono davvero.'),
 ('Per capsula o per porzione?','I dati si riferiscono a volte a una capsula, a volte alla porzione giornaliera consigliata, che può comprendere più capsule o un cucchiaino. Per confrontare conviene riportare tutto alla stessa base.'),
 ('Forma e additivi','Gli oli omega-3 esistono tra l’altro come trigliceride o come estere etilico. Possono contenere antiossidanti come la vitamina E, che proteggono l’olio dall’ossidazione. Anche l’elenco degli ingredienti mostra se ci sono aromi o dolcificanti.')],
 th=['','Indicazione','Cosa c’è dietro'],rows=[('Quantità','«1000 mg di olio di pesce» o «di alghe»','Quantità totale di olio, non di EPA e DHA'),('EPA / DHA','Quantità indicata a parte','Contenuto degli acidi grassi cercati, da verificare per capsula o per porzione'),('Forma','Trigliceride, estere etilico','Forma chimica in cui gli acidi grassi sono legati nell’olio'),('Origine','Specie di pesce o ceppo di alghe, paese','Mostra da dove viene la materia prima; i fornitori seri la indicano')],
 ch='Cinque domande prima di comprare',ci=['Quanti EPA e DHA contiene una porzione?','A quante capsule si riferisce il dato?','L’olio viene da pesce o da alghe?','Esistono rapporti di analisi su purezza e freschezza?','Fino a quando si conserva il prodotto e come va conservato?'],
 bh='In breve',bp='L’etichetta dice più della pubblicità. Chi conosce quantità, forma e origine può confrontare i prodotti con sobrietà, che si tratti di olio di pesce o di alghe.',
 tk='Articolo',th_='Leggere l’etichetta degli <em>omega-3</em>',tp='Quantità di olio, EPA e DHA, forma, origine: cosa dice davvero la confezione.',tc='Leggi l’articolo'),
}
for _l in AR2: AR2[_l]['note'],AR2[_l]['back']=_n[_l]
ARS=[AR,AR2]

NC=[(18,3),(20,5),(22,6)]
B='https://fjord-omega3.ch'
for l,c in T.items():
    alt=''.join(f'<link rel="alternate" hreflang="{k}" href="{B}/{k}/">' for k in T)+f'<link rel="alternate" hreflang="x-default" href="{B}/">'
    nav=''.join(f'<a href="#{i}">{n}</a>' for i,n in zip(['acids','sources','research','faq'],c['nav']))
    lang=''.join(f'<a href="/{k}/" class="{"on" if k==l else ""}" hreflang="{k}">{k.upper()}</a>' for k in T)
    mq=''.join(f'<span>{m}</span>' for m in c['mq']*2);xn=L(l,'nav')

    a=A[l];cards=''.join(f'<button class="card rv" data-c="{NC[i][0]}" data-d="{NC[i][1]}" data-i="{i}"><small>{a["dp"][i]}</small><b>{x[0]}</b><span>{x[1]}</span></button>' for i,x in enumerate(a['it']))
    det=''.join(f'<div class="det" data-i="{i}"><h3>{x[1]}</h3><p>{x[2]}</p><p class="src"><strong>{a["src"]}:</strong> {x[3]}</p><p class="xr">{L(l,"acid"+str(i))} →</p></div>' for i,x in enumerate(a['it']))
    acids=f'''<section id="acids" class="deep"><div class="wrap"><span class="eyebrow">{a['k']}</span><h2>{a['h']}</h2><p class="sub">{a['p']}</p>
<div class="cards">{cards}</div><div class="panel"><svg id="chain" viewBox="0 0 900 150" aria-hidden="true"></svg><p class="lgd"><span><i class="ln"></i>{LG[l][0]}</span><span><i class="dt"></i>{LG[l][1]}</span></p><div class="meta"><div><b id="mc">18</b><span>{a['ch']}</span></div><div><b id="md">3</b><span>{a['db']}</span></div></div>{det}</div></div></section>'''

    z=S[l];fx=lambda names,vals,g:''.join(f'<div class="fx rv" data-g="{g}"><span>{n}</span><i style="--w:{v/max(vals)*100:.0f}%"></i><em>{str(v).replace(".",",") if l!="de" else v}</em></div>' for n,v in zip(names,vals))
    tabs=''.join(f'<button class="tab{" on" if i==0 else ""}" data-g="{i}">{t}</button>' for i,t in enumerate(z['tabs']))
    opts=''.join(f'<option value="{v}">{n}</option>' for n,v in zip(z['sea'],SV))
    sources='<section id="sources" class="src-sec"><div class="wrap"><span class="eyebrow">'+z['k']+'</span><h2>'+z['h']+'</h2><p class="sub">'+z['p']+'</p><div class="tabs">'+tabs+'</div>'+\
     '<div class="grp" data-g="0"><img class="pic" src="/assets/img/sea.jpg" alt="'+z['tabs'][0]+'" width="1100" height="615" loading="lazy"><small>'+z['u'][0]+'</small>'+fx(z['sea'],SV,0)+'</div><div class="grp" data-g="1" hidden><small>'+z['u'][1]+'</small>'+fx(z['pl'],PV,1)+'</div><div class="grp alg" data-g="2" hidden><p>'+z['alg']+'</p></div>'+\
     '<div class="calc" id="enough"><h2>'+z['ct']+'</h2><p class="sub">'+z['cp']+'</p><div class="cbox" data-lg="'+z['lg']+'"><label>'+z['cf']+'<select id="cf">'+opts+'</select></label><label><b id="cn">2</b> '+z['cn']+'<input id="cp" type="range" min="0" max="7" value="2"></label>'+\
     '<div class="gauge"><i id="cgb"></i></div><p class="res"><b id="cv">0</b> g '+z['cg']+' · <b id="cpct">0</b> % '+z['cr']+'</p><p class="xr">'+L(l,'calc')+' →</p></div></div></div></section>'

    q=R[l];det=lambda it,c,pl='x':''.join(f'<details class="{c} rv"><summary>{a}</summary><p>{b} {L(l,pl+str(n))} →</p></details>' for n,(a,b) in enumerate(it))
    research='<section id="research" class="res-sec"><div class="wrap"><span class="eyebrow">'+q['k']+'</span><h2>'+q['h']+'</h2><p class="sub">'+q['p']+'</p><div class="acc">'+det(q['r'],'ac','res')+'</div></div></section>'
    faq='<section id="faq" class="res-sec faq"><div class="wrap"><span class="eyebrow">'+q['fk']+'</span><h2>'+q['fh']+'</h2><div class="acc">'+det(q['f'],'ac','faq')+'</div></div></section>'
    teaser='<section id="artikel" class="tz"><div class="wrap">'+''.join(f'<a class="tzc rv" href="/{l}/{X[l]["slug"]}/"><span class="eyebrow">{X[l]["tk"]}</span><h2>{X[l]["th_"]}</h2><p>{X[l]["tp"]}</p><span class="cta">{X[l]["tc"]} →</span></a>' for X in ARS)+'</div></section>'
    fl=''.join(f'<a class="flink" href="/{l}/{X[l]["slug"]}/">{re.sub("<.*?>","",X[l]["th_"])}</a>' for X in ARS)
    foot='<footer class="foot"><div class="wrap"><a class="logo" href="/'+l+'/"><i></i>FJORD</a><div class="fl">'+fl+'</div><p>'+q['ft']+'</p>'+disc(l)+'<div class="lang">'+lang+'</div></div></footer>'
    open(f'{l}/index.html','w',encoding='utf-8').write(f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c['t']}</title><meta name="description" content="{c['d']}"><link rel="canonical" href="{B}/{l}/">{alt}
<meta property="og:title" content="{c['t']}"><meta property="og:description" content="{c['d']}"><meta property="og:image" content="{B}/assets/img/og.jpg">
<link rel="icon" href="/assets/fjord.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css"><script src="/assets/fjord.js" defer></script></head><body>
<header class="nav"><a class="logo" href="/{l}/"><i></i>FJORD</a><nav class="menu">{nav}{xn}<div class="lang">{lang}</div></nav></header>
<main><section class="hero"><canvas id="sea"></canvas><div class="in">
<span class="eyebrow rv">{c['eb']}</span><h1 class="rv">{c['h']}</h1><p class="sub rv">{c['s']}</p><a class="cta rv" href="#acids">{c['cta']} ↓</a>
<div class="stats rv"><div><b data-count="3">0</b><span>{c['st'][0]}</span></div><div><b data-count="3">0</b><span>{c['st'][1]}</span></div><div><b data-count="4">0</b><span>{c['st'][2]}</span></div></div></div><div class="scroll"></div></section>
<div class="band"><div>{mq}</div></div>{acids}{sources}{teaser}{research}{faq}<section class="xs"><div class="wrap"><span>{STRIP[l]}</span>{L(l,'strip')} →</div></section></main>{foot}</body></html>''')


# ---- Artikelseiten ----
def alt_art(AR):
    return ''.join(f'<link rel="alternate" hreflang="{x}" href="{B}/{x}/{AR[x]["slug"]}/">' for x in AR)+f'<link rel="alternate" hreflang="x-default" href="{B}/de/{AR["de"]["slug"]}/">'
def make(AR,others):
    for l,c in T.items():
        a=AR[l];q=R[l]
        nav=''.join(f'<a href="/{l}/#{i}">{n}</a>' for i,n in zip(['acids','sources','research','faq'],c['nav']))
        lang=''.join(f'<a href="/{k}/{AR[k]["slug"]}/" class="{"on" if k==l else ""}" hreflang="{k}">{k.upper()}</a>' for k in T)
        xn=L(l,'nav')
        secs=''.join(f'<h2 class="rv">{h}</h2><p class="rv">{p}{" "+L(l,"art-s"+str(i)) if i==0 else ""}</p>' for i,(h,p) in enumerate(a['secs'][:3]))
        table='<div class="cmpw rv"><table class="cmp"><thead><tr>'+''.join(f'<th>{x}</th>' for x in a['th'])+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+r[0]+'</th><td>'+r[1]+'</td><td>'+r[2]+'</td></tr>' for r in a['rows'])+'</tbody></table></div>'
        checks='<h2 class="rv">'+a['ch']+'</h2><ul class="chk rv">'+''.join(f'<li>{i}</li>' for i in a['ci'])+'</ul>'
        foot='<footer class="foot"><div class="wrap"><a class="logo" href="/'+l+'/"><i></i>FJORD</a><p>'+q['ft']+'</p>'+disc(l)+'<div class="lang">'+lang+'</div></div></footer>'
        rel='<h2 class="rv relh">'+REL[l]+'</h2><div class="tzr">'+''.join(f'<a class="tzc rv" href="/{l}/{X[l]["slug"]}/"><span class="eyebrow">{X[l]["tk"]}</span><h2>{X[l]["th_"]}</h2><p>{X[l]["tp"]}</p><span class="cta">{X[l]["tc"]} →</span></a>' for X in others)+'</div>'
        url=f'{B}/{l}/{a["slug"]}/'
        os.makedirs(f'{l}/{a["slug"]}',exist_ok=True)
        open(f'{l}/{a["slug"]}/index.html','w',encoding='utf-8').write(f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{a['t']}</title><meta name="description" content="{a['d']}"><link rel="canonical" href="{url}">{alt_art(AR)}
    <meta property="og:type" content="article"><meta property="og:title" content="{a['t']}"><meta property="og:description" content="{a['d']}"><meta property="og:image" content="{B}/assets/img/og.jpg">
    <link rel="icon" href="/assets/fjord.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css"><script src="/assets/fjord.js" defer></script></head><body class="art-page">
    <header class="nav solid"><a class="logo" href="/{l}/"><i></i>FJORD</a><nav class="menu">{nav}{xn}<div class="lang">{lang}</div></nav></header>
    <main><section class="art-hero"><div class="in"><a class="back" href="/{l}/">{a['back']}</a><span class="eyebrow">{a['k']}</span><h1>{a['h']}</h1><p class="sub">{a['lead']}</p></div></section>
    <article class="art"><div class="in">{secs}{table}{checks}<h2 class="rv">{a['bh']}</h2><p class="rv">{a['bp']} {L(l,'art-end')}</p><p class="xs2 rv"><span>{STRIP[l]}</span> {L(l,'art-strip')} →</p><p class="note rv">{a['note']}</p>{rel}</div></article></main>{foot}</body></html>''')


for X in ARS:
    make(X,[Y for Y in ARS if Y is not X])

# sitemap
B_=B
home=[(k,f'{B}/{k}/') for k in T]
sm='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
for g in [home]+[[(k,f'{B}/{k}/{X[k]["slug"]}/') for k in X] for X in ARS]:
    for k,u in g: sm+=f'<url><loc>{u}</loc>'+''.join(f'<xhtml:link rel="alternate" hreflang="{kk}" href="{uu}"/>' for kk,uu in g)+'</url>'
open('sitemap.xml','w',encoding='utf-8').write(sm+'</urlset>')
