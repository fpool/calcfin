# -*- coding: utf-8 -*-
"""CalcFin 多语言数据:de / fr / es(英文为默认语言,见 build.py 的 CALCS)"""

# 英文结果标签基准(key → label)
EN_LBL = {
 "compound-interest": {"main":"Future value","rows":{"deposited":"Total deposited","interest":"Interest earned","multiple":"Growth multiple"}},
 "loan-payment": {"main":"Monthly payment","rows":{"interest":"Total interest","paid":"Total paid","n":"Number of payments"}},
 "mortgage-payment": {"main":"Total monthly payment","rows":{"pi":"Principal & interest","tax":"Property tax (monthly)","ins":"Insurance (monthly)","hoa":"HOA (monthly)","loan":"Loan amount"}},
 "savings-goal": {"main":"Required monthly saving","rows":{"fv":"Future value of current savings","gap":"Gap to fill","contrib":"Total contributions"}},
 "credit-card-payoff": {"main":"Months to be debt-free","rows":{"interest":"Total interest paid","paid":"Total paid","date":"Debt-free estimate","never":"Never paid off","mi":"Monthly interest","need":"Raise payment above"}},
 "inflation": {"main":"Real purchasing power","rows":{"nominal":"Nominal amount","lost":"Purchasing power lost","pct":"Loss percentage"}},
 "roi": {"main":"Total ROI","rows":{"cagr":"Annualized return (CAGR)","profit":"Net profit","multiple":"Growth multiple"}},
 "retirement": {"main":"Projected retirement savings","rows":{"fv":"From current savings","fvm":"From contributions","contrib":"Total contributed","growth":"Growth earned"}},
}

TR = {
"de": {
 "name":"Deutsch",
 "nav_home":"Alle Rechner","nav_privacy":"Datenschutz","nav_about":"Über uns",
 "btn":"Berechnen","related_h2":"Verwandte Rechner","how_h2":"So funktioniert es","faq_h2":"Häufige Fragen",
 "home":{"title":"Kostenlose Finanzrechner — Zinseszins, Kredit, Hypothek, Sparen | CalcFin",
   "meta":"Kostenlose Online-Finanzrechner: Zinseszins, Kreditraten, Hypothek, Sparziele, Kreditkarte, Inflation, Rendite und Rente. Privat, ohne Anmeldung.",
   "h1":"Kostenlose Finanzrechner","sub":"Schnelle, private Rechner, die <b>vollständig in Ihrem Browser</b> laufen — Ihre Zahlen verlassen niemals Ihr Gerät. Jede Seite zeigt die exakte Formel.",
   "h2":"Keine Anmeldung. Keine Datensammlung. Nur Mathe.",
   "p1":"Jeder Rechner auf CalcFin läuft lokal per JavaScript — Ihre Eingaben werden auf Ihrem eigenen Gerät verarbeitet und niemals an einen Server gesendet. Jede Seite dokumentiert die verwendete Formel, damit Sie die Mathematik prüfen können, statt einer Black Box zu vertrauen.",
   "p2":"Ergebnisse sind Schätzungen für Planung und Bildung, keine Finanzberatung."},
 "privacy":{"title":"Datenschutzerklärung | CalcFin","meta":"Datenschutzerklärung von CalcFin — lokale Berechnungen, Cookies und Werbe-Hinweise.",
   "body":"""
  <h1>Datenschutzerklärung</h1>
  <p class="updated">Zuletzt aktualisiert: 2. Oktober 2026</p>
  <p>CalcFin („wir“) bietet kostenlose Finanzrechner an, die <b>vollständig in Ihrem Browser</b> laufen. Diese Erklärung erklärt, welche Daten erhoben werden — und welche nicht.</p>
  <h2>1. Ihre Eingaben</h2>
  <p><b>Wir sehen Ihre Eingaben und Ergebnisse niemals.</b> Jede Berechnung erfolgt lokal auf Ihrem Gerät. Nichts wird gesendet, gespeichert oder protokolliert.</p>
  <h2>2. Serverprotokolle</h2>
  <p>Unser Hosting-Anbieter (Cloudflare) zeichnet automatisch technische Standarddaten auf — IP-Adresse, Browsertyp, URL, Zeitstempel — für Sicherheit und Performance. Diese Daten unterliegen der <a href="https://www.cloudflare.com/privacypolicy/">Datenschutzerklärung von Cloudflare</a>.</p>
  <h2>3. Cookies und Werbung</h2>
  <p>Wir planen, Werbung von Google AdSense anzuzeigen. Drittanbieter, einschließlich Google, verwenden Cookies für auf frühere Besuche basierende Werbung. Deaktivierbar über <a href="https://www.google.com/settings/ads">Google Anzeigeneinstellungen</a>; das Blockieren von Cookies beeinträchtigt die Rechner nicht.</p>
  <h2>4. Keine Finanzberatung</h2>
  <p>Ergebnisse sind mathematische Schätzungen für Bildung und Planung — keine Finanzberatung.</p>
  <h2>5. Kontakt</h2>
  <p>Fragen: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Über CalcFin | CalcFin","meta":"Über CalcFin — kostenlose Finanzrechner im Browser mit transparenten Formeln.",
   "body":"""
  <h1>Über CalcFin</h1>
  <p>CalcFin ist eine Sammlung schneller, kostenloser, unkomplizierter Finanzrechner. Jeder Rechner läuft <b>vollständig in Ihrem Browser</b> — Ihre Zahlen berühren keinen Server — und jede Seite erklärt die Formel hinter dem Ergebnis.</p>
  <h2>Warum CalcFin existiert</h2>
  <p>Die meisten Finanzrechner-Seiten begraben das Werkzeug unter Werbung, verlangen Anmeldungen oder verstecken die Mathematik. Wir machen das Gegenteil: saubere Werkzeuge, transparente Formeln, ehrliche Schätzungen.</p>
  <h2>Prinzipien</h2>
  <ul><li><b>Lokal als Standard.</b> Eingaben verlassen niemals Ihr Gerät.</li>
  <li><b>Transparente Mathematik.</b> Jede Seite zeigt die exakte Formel.</li>
  <li><b>Kostenlos heißt kostenlos.</b> Keine Anmeldung, keine Paywall, keine Limits.</li></ul>
  <h2>Kontakt</h2>
  <p>Feedback und Fehlermeldungen: <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"Zinseszinsrechner — mit monatlichen Sparraten | CalcFin","h1":"Zinseszinsrechner",
   "meta":"Kostenloser Zinseszinsrechner mit monatlichen Sparraten. Sehen Sie, wie Ihr Geld wächst — Formel erklärt, privat im Browser.",
   "intro":"Sehen Sie, wie ein Startbetrag plus monatliche Sparraten durch Zinseszins wächst. Passen Sie Zins und Laufzeit an, um Szenarien sofort zu vergleichen.",
   "inputs":["Startbetrag ($)","Jahreszins (%)","Jahre","Monatliche Sparrate ($)"],
   "how":["Zinseszins zahlt Zinsen auf Zinsen. Bei monatlicher Verzinsung zum Jahreszins r wächst das Guthaben monatlich um r/12.",
     "Der erste Term ist der Startbetrag über die gesamte Laufzeit; der zweite ist der Endwert aller monatlichen Sparraten.",
     "Zeit ist wichtiger als Zins: doppelte Jahre quadrieren etwa den Wachstumsfaktor des Startbetrags."],
   "formula":"EW = A(1+r/n)^(nt) + R · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Wird die Rate am Anfang oder Ende des Monats eingezahlt?","Dieser Rechner geht von Zahlungen am Monatsanfang aus (vorschüssige Rente) — daher der zusätzliche Faktor (1+r/n) in der Formel."),
     ("Werden Steuern oder Inflation berücksichtigt?","Nein — die Ergebnisse sind nominal. Für die reale Kaufkraft nutzen Sie den Inflationsrechner."),
     ("Welchen Zins soll ich annehmen?","Historisch lag die Rendite des US-Aktienmarkts bei etwa 7–10 % pro Jahr vor Inflation — vergangene Renditen garantieren aber keine zukünftigen.")],
   "lbl":{"main":"Endwert","rows":{"deposited":"Eingezahlt gesamt","interest":"Zinsertrag","multiple":"Wachstumsfaktor"}}},
  "loan-payment":{"title":"Kreditratenrechner — Rate & Zinskosten | CalcFin","h1":"Kreditratenrechner",
   "meta":"Berechnen Sie die monatliche Rate und die Zinskosten für jeden Kredit. Annuitätenformel erklärt — kostenlos und privat.",
   "intro":"Kreditbetrag, Jahreszins und Laufzeit eingeben — Sie erhalten die feste monatliche Rate, die Gesamtzinsen und die Gesamtkosten.",
   "inputs":["Kreditbetrag ($)","Jahreszins (%)","Laufzeit (Jahre)"],
   "how":["Kredite werden annuitätisch getilgt: Jede Rate besteht aus Zins- und Tilgungsanteil.",
     "Frühe Raten sind zinslastig — deshalb sparen Sondertilgungen am Anfang am meisten Zinsen.",
     "Bei 0 % Zins teilt sich der Kredit gleichmäßig auf alle Raten."],
   "formula":"Rate = K · r · (1+r)^n / ((1+r)^n − 1)   wobei r = Monatszins, n = Anzahl der Raten",
   "faq":[("Funktioniert das für Autokredite und Ratenkredite?","Ja — jeder festverzinsliche, annuitätisch getilgte Kredit nutzt genau diese Formel."),
     ("Warum weicht die Zahl meines Kreditgebers leicht ab?","Kreditgeber rechnen Gebühren, Versicherungen oder leicht andere Rundungen und Zinstage ein."),
     ("Wie zahle ich insgesamt weniger Zinsen?","Kürzere Laufzeit, niedrigerer Zins oder Sondertilgungen — vergleichen Sie die Gesamtzinsen mehrerer Szenarien mit diesem Rechner.")],
   "lbl":{"main":"Monatsrate","rows":{"interest":"Zinskosten gesamt","paid":"Gesamtkosten","n":"Anzahl der Raten"}}},
  "mortgage-payment":{"title":"Hypothekenrechner — Rate, Steuer & Versicherung | CalcFin","h1":"Hypothekenrechner",
   "meta":"Schätzen Sie Ihre echte monatliche Hypothekenrate inklusive Grundsteuer, Versicherung und Hausgeld. Kostenlos und privat.",
   "intro":"Eine Hypothekenrate besteht aus mehr als Zins und Tilgung. Addieren Sie Steuer, Versicherung und Hausgeld, um die Zahl zu sehen, die tatsächlich jeden Monat abgebucht wird.",
   "inputs":["Kaufpreis ($)","Anzahlung ($)","Zins (%)","Laufzeit (Jahre)","Grundsteuer pro Jahr ($)","Versicherung pro Jahr ($)","Hausgeld pro Monat ($)"],
   "how":["Banken nennen nur Zins und Tilgung — die echte Rate enthält escrowte Steuern, Versicherung und Hausgeld.",
     "Faustregel: Planen Sie 1–2 % des Hauswerts pro Jahr für Steuern und Versicherung ein, regional aber sehr unterschiedlich.",
     "20 % Anzahlung entfernt in der Regel die PMI-Versicherung aus der Rechnung."],
   "formula":"Rate = Zins+Tilgung + (Steuer/12) + (Versicherung/12) + Hausgeld",
   "faq":[("Ist PMI enthalten?","Nein — ergänzen Sie PMI manuell im Hausgeld-Feld, wenn die Anzahlung unter 20 % liegt."),
     ("Ist der Steuersatz für meine Region korrekt?","Grundsteuersätze reichen von unter 0,5 % bis über 2 % des Hauswerts pro Jahr — prüfen Sie Ihren lokalen Satz."),
     ("15 oder 30 Jahre Laufzeit?","15 Jahre bedeuten höhere Raten, aber deutlich weniger Gesamtzinsen — rechnen Sie beide Varianten durch.")],
   "lbl":{"main":"Monatsrate gesamt","rows":{"pi":"Zins und Tilgung","tax":"Grundsteuer (monatlich)","ins":"Versicherung (monatlich)","hoa":"Hausgeld (monatlich)","loan":"Kreditbetrag"}}},
  "savings-goal":{"title":"Sparziel-Rechner — benötigte Monatssparrate | CalcFin","h1":"Sparziel-Rechner",
   "meta":"Berechnen Sie die nötige monatliche Sparrate für ein Sparziel mit Zinseszins. Kostenlos und privat.",
   "intro":"Sie haben ein Ziel und einen Termin? Dieser Rechner zeigt die genaue monatliche Sparrate — inklusive Zinseszins.",
   "inputs":["Sparziel ($)","Zeitraum (Jahre)","Jahresrendite (%)","Bereits gespart ($)"],
   "how":["Zuerst wird Ihr vorhandenes Sparguthaben mit Zinseszins bis zum Stichtag projiziert.",
     "Die Lücke zwischen diesem Endwert und Ihrem Ziel füllen die monatlichen Sparraten.",
     "Eine höhere angenommene Rendite senkt die Rate — planen Sie aber nur mit Zinsen, auf die Sie sich verlassen können."],
   "formula":"R = (Ziel − EW_ist) · r / ((1+r)^n − 1)   wobei r = Monatszins, n = Monate",
   "faq":[("Was, wenn ich die Rate nicht tragen kann?","Verlängern Sie den Zeitraum, senken Sie das Ziel oder suchen Sie einen besseren Zins — testen Sie jeden Hebel sofort."),
     ("Wird monatlich oder jährlich gespart?","Monatlich, jeweils am Monatsende."),
     ("Geht das auch für eine Eigenkapital-Anzahlung?","Ja — wird häufig genau dafür genutzt.")],
   "lbl":{"main":"Benötigte Monatssparrate","rows":{"fv":"Endwert des vorhandenen Guthabens","gap":"Zu schließende Lücke","contrib":"Einzahlungen gesamt"}}},
  "credit-card-payoff":{"title":"Kreditkarten-Tilgungsrechner — Monate bis schuldenfrei | CalcFin","h1":"Kreditkarten-Tilgungsrechner",
   "meta":"Wie lange dauert die Tilgung von Kreditkartenschulden mit fester Rate — und wie viel Zins zahlen Sie? Kostenlos.",
   "intro":"Feste monatliche Raten bei Kreditkartenschulden: Sehen Sie genau, wie viele Monate bis schuldenfrei bleiben — und wie viel Zins die Bank dabei einnimmt.",
   "inputs":["Saldo ($)","Jahreszins (APR %)","Monatliche Rate ($)"],
   "how":["Mindestraten sind darauf ausgelegt, Sie in Schulden zu halten: Bei 22,9 % APR frisst der Zins allein den Großteil einer kleinen Rate.",
     "Liegt die Rate unter den Monatszinsen, wächst der Saldo ewig — der Rechner weist darauf hin, statt endlos zu rechnen.",
     "Schon eine leicht erhöhte Rate verkürzt die Tilgung um Monate."],
   "formula":"Jeden Monat: Zins = Saldo × APR/12, dann Saldo = Saldo + Zins − Rate, wiederholt bis null",
   "faq":[("Was ist eine gute Rate für 8.000 $ bei 22,9 %?","Die Zinsen allein liegen bei etwa 152 $/Monat. 300 $/Monat bedeuten rund 3 Jahre; 500 $/Monat unter 2 Jahre und tausende Dollar Ersparnis."),
     ("Geht der Rechner davon aus, dass ich die Karte nicht mehr nutze?","Ja — neue Ausgaben sind nicht modelliert. Rechnen Sie neue Ausgaben manuell auf den Saldo."),
     ("Würde ein Schuldenumzug helfen?","Wenn der neue Zins niedriger ist: ja — modellieren Sie ihn über den niedrigeren APR plus Transfergebühr im Saldo.")],
   "lbl":{"main":"Monate bis schuldenfrei","rows":{"interest":"Zinsen gesamt","paid":"Gezahlt gesamt","date":"Schuldenfrei voraussichtlich","never":"Nie schuldenfrei","mi":"Monatszins","need":"Rate erhöhen auf"}}},
  "inflation":{"title":"Inflationsrechner — reale Kaufkraft | CalcFin","h1":"Inflationsrechner",
   "meta":"Sehen Sie, was heutiges Geld bei einer Inflationsrate künftig wirklich wert ist. Einfach, schnell, privat.",
   "intro":"Inflation schrumpft die Kaufkraft still. Betrag, durchschnittliche Inflationsrate und Jahre eingeben — und sehen, was wirklich übrig bleibt.",
   "inputs":["Betrag heute ($)","Ø Inflationsrate (%)","Jahre"],
   "how":["Bei 3 % Inflation verdoppeln sich die Preise etwa alle 24 Jahre (Regel der 72: 72 ÷ Rate ≈ Verdopplungsjahre).",
     "Deshalb verliert Bargeld unterm Kopfkissen jedes Jahr an Wert — und warum Anlagen, die die Inflation schlagen, wichtig sind.",
     "Langfristig lag die US-Inflation im Schnitt bei etwa 3 %, allerdings je Jahrzehnt sehr unterschiedlich."],
   "formula":"Realwert = Betrag / (1 + Inflation)^Jahre",
   "faq":[("Welche Inflationsrate soll ich nehmen?","Langfristiger US-Durchschnitt etwa 3 %. Konservativ planen Sie mit 3–4 %; einzelne Jahre lagen zwischen fast 0 % und 9 %."),
     ("Ist das dasselbe wie eine Rendite?","Nein — es ist die Gegenseite: was Inflation mit idleem Geld macht. Vergleichen Sie mit dem Zinseszinsrechner."),
     ("Steigende Inflation modellierbar?","Dieses Werkzeug nutzt einen festen Durchschnittssatz — als Näherung den Durchschnitt des Zeitraums.")],
   "lbl":{"main":"Reale Kaufkraft","rows":{"nominal":"Nominalbetrag","lost":"Kaufkraftverlust","pct":"Verlust in Prozent"}}},
  "roi":{"title":"Renditerechner — ROI & jährliche Verzinsung | CalcFin","h1":"Renditerechner (ROI)",
   "meta":"Berechnen Sie die Gesamrendite (ROI) und die jährliche Verzinsung (CAGR). Vergleichen Sie Investitionen fair.",
   "intro":"Einfacher ROI zeigt, wie viel Sie verdient haben; die jährliche Verzinsung zeigt, wie schnell — und nur die ist zwischen Investments vergleichbar.",
   "inputs":["Investiert ($)","Endwert ($)","Haltedauer (Jahre)"],
   "how":["ROI allein täuscht: +50 % in 1 Jahr ist stark, +50 % in 10 Jahren mäßig. Die annualisierte Zahl (CAGR) macht verschiedene Investments vergleichbar.",
     "CAGR ist der konstante Jahreszins, der vom Einsatz zum Endwert führt.",
     "Rechnen Sie Gebühren, Steuern und Dividenden in den Endwert ein — sonst wird das Bild geschönt."],
   "formula":"ROI = (End − Einsatz) / Einsatz × 100 %      CAGR = (End/Einsatz)^(1/Jahre) − 1",
   "faq":[("Was ist eine gute Rendite?","Je nach Risiko und Zeitraum. Aktienmärkte lieferten langfristig ~10 % nominal; Sparbuch deutlich weniger bei weniger Risiko."),
     ("ROI oder CAGR — was ist der Unterschied?","ROI ist der Gesamtgewinn in Prozent; CAGR verteilt ihn auf die Jahre. Nur CAGR erlaubt faire Vergleiche verschiedener Haltedauern."),
     ("Kann ROI negativ sein?","Ja — liegt der Endwert unter dem Einsatz, sind ROI und CAGR negativ.")],
   "lbl":{"main":"Gesamtrendite (ROI)","rows":{"cagr":"Jährliche Rendite (CAGR)","profit":"Nettogewinn","multiple":"Wachstumsfaktor"}}},
  "retirement":{"title":"Rentenrechner — reicht das Sparziel? | CalcFin","h1":"Rentenrechner",
   "meta":"Projizieren Sie Ihr Rentensparen aus Guthaben, Sparrate, Arbeitgeberzuschuss und Rendite. Kostenlos und privat.",
   "intro":"Projizieren Sie Ihr Nestegg zum Renteneintritt: aus dem vorhandenen Guthaben, der monatlichen Sparrate (inklusive Arbeitgeberzuschuss) und einer angenommenen Rendite.",
   "inputs":["Aktuelles Guthaben ($)","Monatliche Sparrate ($)","Arbeitgeberzuschuss ($)","Jahresrendite (%)","Jahre bis zur Rente"],
   "how":["Arbeitgeberzuschuss ist geschenktes Geld — rechnen Sie ihn zur Sparrate; über eine Karriere können das sechsstellige Beträge sein.",
     "Das letzte Jahrzehnt der Verzinsung bringt meist die größten Beträge — früher anfangen schlägt mehr einzahlen.",
     "Das Ergebnis ist nominal. Nutzen Sie den Inflationsrechner, um es in heutiger Kaufkraft zu sehen."],
   "formula":"EW = Guthaben·(1+r/n)^(nt) + Monatsrate·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Welche Rendite soll ich annehmen?","Ein diversifiziertes Portfolio brachte historisch 7–8 % nominal. Konservativ planen Sie mit 5–6 %."),
     ("Ist die Rente enthalten?","Nein — hier geht es nur um eigene Investments. Erwartete Rentenzahlungen rechnen Sie separat ein."),
     ("Wie viel brauche ich überhaupt?","Eine gängige Startregel ist das 25-Fache der erwarteten Jahresausgaben („4-%-Regel“) — individuell sehr unterschiedlich.")],
   "lbl":{"main":"Projiziertes Rentenguthaben","rows":{"fv":"Aus vorhandenem Guthaben","fvm":"Aus Einzahlungen","contrib":"Eingezahlt gesamt","growth":"Erwirtschaftete Erträge"}}},
 }
},
"fr": {
 "name":"Français",
 "nav_home":"Tous les calculateurs","nav_privacy":"Confidentialité","nav_about":"À propos",
 "btn":"Calculer","related_h2":"Calculateurs liés","how_h2":"Comment ça marche","faq_h2":"FAQ",
 "home":{"title":"Calculateurs financiers gratuits — Intérêts, crédit, épargne | CalcFin",
   "meta":"Calculateurs financiers gratuits en ligne : intérêts composés, mensualités de crédit, immobilier, épargne, carte bancaire, inflation, rendement et retraite. Privé, sans inscription.",
   "h1":"Calculateurs financiers gratuits","sub":"Des calculateurs rapides et privés qui fonctionnent <b>entièrement dans votre navigateur</b> — vos chiffres ne quittent jamais votre appareil. Chaque page montre la formule exacte.",
   "h2":"Sans inscription. Sans collecte de données. Juste des maths.",
   "p1":"Chaque calculateur de CalcFin fonctionne localement en JavaScript — vos saisies sont traitées sur votre propre appareil et jamais envoyées à un serveur. Chaque page documente la formule exacte utilisée, pour vérifier les calculs au lieu de faire confiance à une boîte noire.",
   "p2":"Les résultats sont des estimations pour la planification et la pédagogie, pas des conseils financiers."},
 "privacy":{"title":"Politique de confidentialité | CalcFin","meta":"Politique de confidentialité de CalcFin — calculs locaux, cookies et publicité.",
   "body":"""
  <h1>Politique de confidentialité</h1>
  <p class="updated">Dernière mise à jour : 2 octobre 2026</p>
  <p>CalcFin (« nous ») propose des calculateurs financiers gratuits qui fonctionnent <b>entièrement dans votre navigateur</b>. Cette politique explique quelles données sont — et ne sont pas — collectées.</p>
  <h2>1. Vos saisies</h2>
  <p><b>Nous ne voyons jamais vos saisies ni vos résultats.</b> Chaque calcul s'effectue localement sur votre appareil. Rien n'est envoyé, stocké ou enregistré.</p>
  <h2>2. Journaux serveur</h2>
  <p>Notre hébergeur (Cloudflare) enregistre automatiquement les données techniques standard — adresse IP, type de navigateur, URL, horodatage — à des fins de sécurité et de performance, conformément à la <a href="https://www.cloudflare.com/privacypolicy/">politique de confidentialité de Cloudflare</a>.</p>
  <h2>3. Cookies et publicité</h2>
  <p>Nous prévoyons d'afficher de la publicité servie par Google AdSense. Des tiers, dont Google, utilisent des cookies pour diffuser des annonces selon les visites précédentes. Désactivables via <a href="https://www.google.com/settings/ads">les paramètres des annonces Google</a> ; bloquer les cookies n'affecte pas les calculateurs.</p>
  <h2>4. Pas un conseil financier</h2>
  <p>Les résultats sont des estimations mathématiques à des fins éducatives — pas des conseils financiers.</p>
  <h2>5. Contact</h2>
  <p>Questions : <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"À propos de CalcFin | CalcFin","meta":"À propos de CalcFin — des calculateurs financiers gratuits dans le navigateur avec des formules transparentes.",
   "body":"""
  <h1>À propos de CalcFin</h1>
  <p>CalcFin est une collection de calculateurs financiers rapides, gratuits et sans détour. Chaque calculateur fonctionne <b>entièrement dans votre navigateur</b> — vos chiffres ne touchent aucun serveur — et chaque page explique la formule derrière le résultat.</p>
  <h2>Pourquoi CalcFin existe</h2>
  <p>La plupart des sites de calculateurs enterrent l'outil sous la publicité, exigent des inscriptions ou cachent les maths. Nous faisons l'inverse : des outils propres, des formules transparentes, des estimations honnêtes.</p>
  <h2>Principes</h2>
  <ul><li><b>Local par défaut.</b> Vos saisies ne quittent jamais votre appareil.</li>
  <li><b>Des maths transparentes.</b> Chaque page montre la formule exacte.</li>
  <li><b>Gratuit veut dire gratuit.</b> Sans inscription, sans paywall, sans limite.</li></ul>
  <h2>Contact</h2>
  <p>Retours et bugs : <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"Calculateur d'intérêts composés — avec versements mensuels | CalcFin","h1":"Calculateur d'intérêts composés",
   "meta":"Calculateur d'intérêts composés gratuit avec versements mensuels. Voyez votre argent fructifier — formule expliquée, dans votre navigateur.",
   "intro":"Voyez comment un capital initial plus des versements mensuels fructifient avec les intérêts composés. Ajustez le taux et la durée pour comparer instantanément.",
   "inputs":["Capital initial ($)","Taux annuel (%)","Années","Versement mensuel ($)"],
   "how":["Les intérêts composés paient des intérêts sur les intérêts. Avec capitalisation mensuelle au taux annuel r, le solde croît chaque mois de r/12.",
     "Le premier terme est le capital initial sur toute la période ; le second est la valeur future de tous les versements mensuels.",
     "Le temps compte plus que le taux : doubler les années élève fortement le multiple de croissance du capital."],
   "formula":"VF = C(1+r/n)^(nt) + V · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Le versement est-il en début ou fin de mois ?","Ce calculateur suppose un versement en début de mois (annuités à échéance anticipée) — d'où le facteur (1+r/n) supplémentaire."),
     ("Les impôts et l'inflation sont-ils inclus ?","Non — les résultats sont nominaux. Pour la puissance d'achat réelle, utilisez le calculateur d'inflation."),
     ("Quel taux choisir ?","Historiquement, le marché boursier US rapporte environ 7–10 % par an avant inflation — mais les performances passées ne garantissent rien.")],
   "lbl":{"main":"Valeur future","rows":{"deposited":"Total versé","interest":"Intérêts gagnés","multiple":"Multiple de croissance"}}},
  "loan-payment":{"title":"Calculateur de mensualités — coût total du crédit | CalcFin","h1":"Calculateur de mensualités",
   "meta":"Calculez la mensualité et le coût total des intérêts pour tout crédit. Formule d'amortissement expliquée — gratuit et privé.",
   "intro":"Saisissez un montant, un taux annuel et une durée pour obtenir la mensualité fixe, le total des intérêts et le coût total.",
   "inputs":["Montant du prêt ($)","Taux annuel (%)","Durée (années)"],
   "how":["Les prêts sont amortis : chaque mensualité comprend des intérêts et du capital.",
     "Les premières mensualités sont chargées en intérêts — c'est pourquoi un remboursement anticipé précoce économise le plus.",
     "À 0 % d'intérêt, le capital se divise simplement par le nombre de mensualités."],
   "formula":"Mensualité = P · r · (1+r)^n / ((1+r)^n − 1)   où r = taux mensuel, n = nombre de mensualités",
   "faq":[("Cela marche-t-il pour auto, conso, études ?","Oui — tout prêt à taux fixe amorti utilise exactement cette formule."),
     ("Pourquoi mon prêteur affiche un chiffre légèrement différent ?","Les prêteurs ajoutent frais et assurances ou arrondissent différemment."),
     ("Comment payer moins d'intérêts au total ?","Raccourcir la durée, baisser le taux, rembourser par anticipation — comparez le total des intérêts entre scénarios.")],
   "lbl":{"main":"Mensualité","rows":{"interest":"Intérêts totaux","paid":"Coût total","n":"Nombre de mensualités"}}},
  "mortgage-payment":{"title":"Calculateur de mensualité immobilière — taxe et assurance | CalcFin","h1":"Calculateur de mensualité immobilière",
   "meta":"Estimez votre vraie mensualité immobilière avec taxe foncière, assurance et charges. Gratuit et privé.",
   "intro":"Une mensualité immobilière dépasse capital et intérêts. Ajoutez taxe, assurance et charges pour voir le montant réellement prélevé chaque mois.",
   "inputs":["Prix du bien ($)","Apport ($)","Taux (%)","Durée (années)","Taxe foncière / an ($)","Assurance / an ($)","Charges / mois ($)"],
   "how":["Les banques n'affichent que capital et intérêts, mais la vraie mensualité inclut taxe foncière, assurance et charges.",
     "Règle courante : budgétez 1–2 % de la valeur du bien par an pour taxes et assurance, selon les régions.",
     "Un apport de 20 % supprime en général l'assurance PMI."],
   "formula":"Mensualité = C+I + (Taxe/12) + (Assurance/12) + Charges",
   "faq":[("La PMI est-elle incluse ?","Non — ajoutez-la manuellement dans le champ charges si l'apport est inférieur à 20 %."),
     ("Le taux de taxe est-il exact pour ma région ?","Les taux varient de moins de 0,5 % à plus de 2 % de la valeur par an — vérifiez votre taux local."),
     ("15 ou 30 ans ?","15 ans : mensualité plus élevée mais intérêts totaux bien moindres — comparez les deux scénarios.")],
   "lbl":{"main":"Mensualité totale","rows":{"pi":"Capital et intérêts","tax":"Taxe foncière (mensuelle)","ins":"Assurance (mensuelle)","hoa":"Charges (mensuelles)","loan":"Montant du prêt"}}},
  "savings-goal":{"title":"Calculateur d'objectif d'épargne — combien épargner par mois | CalcFin","h1":"Calculateur d'objectif d'épargne",
   "meta":"Calculez l'épargne mensuelle nécessaire pour atteindre un montant à une échéance, avec intérêts composés. Gratuit et privé.",
   "intro":"Vous avez un objectif et une échéance ? Voici le versement mensuel exact nécessaire, en supposant des intérêts composés.",
   "inputs":["Objectif ($)","Durée (années)","Rendement annuel (%)","Déjà épargné ($)"],
   "how":["D'abord, votre épargne actuelle est projetée avec intérêts composés jusqu'à l'échéance.",
     "L'écart entre cette valeur future et l'objectif est comblé par les versements mensuels.",
     "Un rendement supérieur réduit la mensualité — mais ne planifiez pas sur des taux incertains."],
   "formula":"V = (Objectif − VF_actuel) · r / ((1+r)^n − 1)   où r = taux mensuel, n = mois",
   "faq":[("Et si je ne peux pas assumer la mensualité ?","Prolongez l'échéance, réduisez l'objectif ou cherchez un meilleur rendement — testez chaque levier instantanément."),
     ("L'épargne est-elle mensuelle ou annuelle ?","Mensuelle, en fin de mois."),
     ("Utilisable pour un apport immobilier ?","Oui — c'est un usage très courant.")],
   "lbl":{"main":"Épargne mensuelle requise","rows":{"fv":"Valeur future de l'épargne actuelle","gap":"Écart à combler","contrib":"Versements totaux"}}},
  "credit-card-payoff":{"title":"Calculateur de remboursement de carte — mois avant zéro dette | CalcFin","h1":"Calculateur de remboursement de carte",
   "meta":"Combien de temps pour rembourser une dette de carte bancaire avec des mensualités fixes, et combien d'intérêts ? Gratuit.",
   "intro":"Mensualités fixes sur une dette de carte : voyez exactement combien de mois avant d'être à zéro dette, et combien d'intérêts la banque encaisse.",
   "inputs":["Solde ($)","TAEG annuel (%)","Mensualité ($)"],
   "how":["Les paiements minimums sont conçus pour vous endetter : à 22,9 % de TAEG, les intérêts seuls absorbent l'essentiel d'une petite mensualité.",
     "Si votre mensualité est inférieure aux intérêts du premier mois, le solde croît à l'infini — le calculateur le signale.",
     "Arrondir la mensualité au-dessus coupe des mois entiers de remboursement."],
   "formula":"Chaque mois : intérêts = solde × TAEG/12, puis solde = solde + intérêts − mensualité, jusqu'à zéro",
   "faq":[("Quelle mensualité pour 8 000 $ à 22,9 % ?","Les intérêts seuls représentent environ 152 $/mois. À 300 $/mois : environ 3 ans ; à 500 $/mois : moins de 2 ans et des milliers d'économies."),
     ("Le calcul suppose que je n'utilise plus la carte ?","Oui — aucune nouvelle dépense n'est modélisée."),
     ("Un rachat de crédit aiderait-il ?","Si le nouveau TAEG est plus bas, oui — modélisez-le avec le TAEG inférieur plus les frais dans le solde.")],
   "lbl":{"main":"Mois avant zéro dette","rows":{"interest":"Intérêts payés","paid":"Total payé","date":"Zéro dette estimé","never":"Jamais remboursé","mi":"Intérêts mensuels","need":"Augmenter la mensualité au-dessus de"}}},
  "inflation":{"title":"Calculateur d'inflation — pouvoir d'achat réel | CalcFin","h1":"Calculateur d'inflation",
   "meta":"Voyez ce que l'argent d'aujourd'hui achètera vraiment à terme selon l'inflation. Simple, rapide, privé.",
   "intro":"L'inflation ronge silencieusement le pouvoir d'achat. Saisissez un montant, un taux moyen et une durée pour voir ce qu'il vaudra réellement.",
   "inputs":["Montant aujourd'hui ($)","Inflation moyenne (%)","Années"],
   "how":["À 3 % d'inflation, les prix doublent environ tous les 24 ans (règle des 72 : 72 ÷ taux ≈ années de doublement).",
     "C'est pourquoi l'argent sous le matelas perd de la valeur chaque année — et pourquoi battre l'inflation compte.",
     "Historiquement, l'inflation US moyenne tourne autour de 3 %, avec de fortes variations par décennie."],
   "formula":"Valeur réelle = Montant / (1 + inflation)^années",
   "faq":[("Quel taux d'inflation choisir ?","La moyenne US long terme est d'environ 3 %. Pour planifier prudemment : 3–4 % ; certaines années vont de presque 0 % à 9 %."),
     ("C'est la même chose qu'un rendement ?","Non — c'est le revers : ce que fait l'inflation sur l'argent immobile. Comparez avec le calculateur d'intérêts composés."),
     ("Inflation croissante modélisable ?","Cet outil utilise un taux moyen constant — approximez avec la moyenne de la période.")],
   "lbl":{"main":"Pouvoir d'achat réel","rows":{"nominal":"Montant nominal","lost":"Pouvoir d'achat perdu","pct":"Perte en pourcentage"}}},
  "roi":{"title":"Calculateur de ROI — rendement total et annualisé | CalcFin","h1":"Calculateur de ROI",
   "meta":"Calculez le retour sur investissement (ROI) et le rendement annualisé. Comparez les investissements équitablement.",
   "intro":"Le ROI simple dit combien vous avez gagné ; le rendement annualisé dit à quelle vitesse — et c'est le seul chiffre comparable entre placements.",
   "inputs":["Montant investi ($)","Valeur finale ($)","Durée de détention (années)"],
   "how":["Le ROI seul trompe : +50 % en 1 an est excellent, +50 % en 10 ans est médiocre. Le rendement annualisé (CAGR) rend les placements comparables.",
     "Le CAGR est le taux annuel constant qui mène du coût à la valeur finale sur la même durée.",
     "Incluez frais, impôts et dividendes dans la valeur finale pour un tableau honnête."],
   "formula":"ROI = (Final − Coût) / Coût × 100 %      CAGR = (Final/Coût)^(1/années) − 1",
   "faq":[("Quel ROI est bon ?","Selon le risque et la durée. Les actions rapportent ~10 % nominal à long terme ; l'épargne bien moins avec bien moins de risque."),
     ("ROI ou CAGR ?","Le ROI est le gain total en pourcentage ; le CAGR l'étale par année. Seul le CAGR permet une comparaison équitable entre durées."),
     ("Le ROI peut-il être négatif ?","Oui — une valeur finale inférieure au coût donne ROI et CAGR négatifs.")],
   "lbl":{"main":"ROI total","rows":{"cagr":"Rendement annualisé (CAGR)","profit":"Bénéfice net","multiple":"Multiple de croissance"}}},
  "retirement":{"title":"Calculateur d'épargne retraite — assez pour la retraite ? | CalcFin","h1":"Calculateur d'épargne retraite",
   "meta":"Projetez votre épargne retraite à partir du solde actuel, des versements, de l'abondement employeur et du rendement. Gratuit et privé.",
   "intro":"Projetez votre capital à la retraite à partir de ce que vous avez, de ce que vous ajoutez chaque mois (abondement employeur inclus) et d'un rendement supposé.",
   "inputs":["Épargne actuelle ($)","Versement mensuel ($)","Abondement employeur ($)","Rendement annuel (%)","Années avant la retraite"],
   "how":["L'abondement employeur est de l'argent gratuit — incluez-le dans votre versement ; sur une carrière, cela peut représenter des dizaines de milliers.",
     "La dernière décennie de capitalisation apporte généralement les plus gros montants — commencer tôt compte plus que verser plus.",
     "Le résultat est nominal. Passez-le au calculateur d'inflation pour le voir en pouvoir d'achat actuel."],
   "formula":"VF = Actuel·(1+r/n)^(nt) + Mensuel·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Quel rendement supposer ?","Un portefeuille diversifié a historiquement rapporté 7–8 % nominal. Planification prudente : 5–6 %."),
     ("Les retraites publiques sont-elles incluses ?","Non — il s'agit uniquement de vos investissements. Ajoutez les pensions attendues séparément."),
     ("De combien ai-je besoin ?","Règle de départ courante : 25× vos dépenses annuelles prévues (« règle des 4 % »), mais cela varie beaucoup.")],
   "lbl":{"main":"Épargne retraite projetée","rows":{"fv":"Depuis l'épargne actuelle","fvm":"Depuis les versements","contrib":"Versements totaux","growth":"Intérêts gagnés"}}},
 }
},
"es": {
 "name":"Español",
 "nav_home":"Todas las calculadoras","nav_privacy":"Privacidad","nav_about":"Acerca de",
 "btn":"Calcular","related_h2":"Calculadoras relacionadas","how_h2":"Cómo funciona","faq_h2":"Preguntas frecuentes",
 "home":{"title":"Calculadoras financieras gratis — Interés, préstamos, hipoteca | CalcFin",
   "meta":"Calculadoras financieras gratuitas: interés compuesto, cuotas de préstamo, hipoteca, metas de ahorro, tarjeta de crédito, inflación, ROI y jubilación. Privado, sin registro.",
   "h1":"Calculadoras financieras gratis","sub":"Calculadoras rápidas y privadas que funcionan <b>enteramente en tu navegador</b> — tus números nunca salen de tu dispositivo. Cada página muestra la fórmula exacta.",
   "h2":"Sin registro. Sin recopilación de datos. Solo matemáticas.",
   "p1":"Cada calculadora de CalcFin funciona localmente con JavaScript — tus datos se procesan en tu propio dispositivo y nunca se envían a ningún servidor. Cada página documenta la fórmula exacta, para verificar la matemática en lugar de confiar en una caja negra.",
   "p2":"Los resultados son estimaciones para planificación y educación, no asesoría financiera."},
 "privacy":{"title":"Política de privacidad | CalcFin","meta":"Política de privacidad de CalcFin — cálculos locales, cookies y publicidad.",
   "body":"""
  <h1>Política de privacidad</h1>
  <p class="updated">Última actualización: 2 de octubre de 2026</p>
  <p>CalcFin («nosotros») ofrece calculadoras financieras gratuitas que funcionan <b>enteramente en tu navegador</b>. Esta política explica qué datos se recopilan — y cuáles no.</p>
  <h2>1. Tus datos</h2>
  <p><b>Nunca vemos tus datos ni tus resultados.</b> Cada cálculo ocurre localmente en tu dispositivo. Nada se envía, guarda ni registra.</p>
  <h2>2. Registros del servidor</h2>
  <p>Nuestro proveedor de alojamiento (Cloudflare) registra automáticamente datos técnicos estándar — IP, tipo de navegador, URL, fecha — con fines de seguridad y rendimiento, conforme a la <a href="https://www.cloudflare.com/privacypolicy/">política de privacidad de Cloudflare</a>.</p>
  <h2>3. Cookies y publicidad</h2>
  <p>Planeamos mostrar publicidad servida por Google AdSense. Terceros, incluido Google, usan cookies para anuncios basados en visitas previas. Desactivables en <a href="https://www.google.com/settings/ads">Configuración de anuncios de Google</a>; bloquear cookies no afecta las calculadoras.</p>
  <h2>4. No es asesoría financiera</h2>
  <p>Los resultados son estimaciones matemáticas para educación y planificación — no asesoría financiera.</p>
  <h2>5. Contacto</h2>
  <p>Preguntas: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Acerca de CalcFin | CalcFin","meta":"Acerca de CalcFin — calculadoras financieras gratuitas en el navegador con fórmulas transparentes.",
   "body":"""
  <h1>Acerca de CalcFin</h1>
  <p>CalcFin es una colección de calculadoras financieras rápidas, gratuitas y sin rodeos. Cada calculadora funciona <b>enteramente en tu navegador</b> — tus números nunca tocan un servidor — y cada página explica la fórmula detrás del resultado.</p>
  <h2>Por qué existe CalcFin</h2>
  <p>La mayoría de los sitios de calculadoras entierran la herramienta bajo publicidad, exigen registros u ocultan las matemáticas. Nosotros hacemos lo contrario: herramientas limpias, fórmulas transparentes, estimaciones honestas.</p>
  <h2>Principios</h2>
  <ul><li><b>Local por defecto.</b> Tus datos nunca salen de tu dispositivo.</li>
  <li><b>Matemáticas transparentes.</b> Cada página muestra la fórmula exacta.</li>
  <li><b>Gratis significa gratis.</b> Sin registro, sin muro de pago, sin límites.</li></ul>
  <h2>Contacto</h2>
  <p>Comentarios y errores: <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"Calculadora de interés compuesto — con aportes mensuales | CalcFin","h1":"Calculadora de interés compuesto",
   "meta":"Calculadora de interés compuesto gratis con aportes mensuales. Mira cómo crece tu dinero — fórmula explicada, en tu navegador.",
   "intro":"Mira cómo un capital inicial más aportes mensuales crece con interés compuesto. Ajusta la tasa y el plazo para comparar escenarios al instante.",
   "inputs":["Capital inicial ($)","Tasa anual (%)","Años","Aporte mensual ($)"],
   "how":["El interés compuesto paga intereses sobre los intereses. Con capitalización mensual a una tasa anual r, el saldo crece cada mes r/12.",
     "El primer término es tu capital inicial creciendo todo el período; el segundo es el valor futuro de cada aporte mensual.",
     "El tiempo importa más que la tasa: duplicar los años eleva mucho el múltiplo de crecimiento del capital."],
   "formula":"VF = C(1+r/n)^(nt) + A · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("¿El aporte se hace al inicio o al final del mes?","Esta calculadora asume aportes al inicio de cada mes (anualidad anticipada) — por eso la fórmula incluye el factor (1+r/n) extra."),
     ("¿Incluye impuestos o inflación?","No — los resultados son nominales. Para poder adquisitivo real, usa la Calculadora de inflación."),
     ("¿Qué tasa debería usar?","El mercado bursátil de EE. UU. rindió históricamente ~7–10 % anual antes de inflación — pero el pasado no garantiza el futuro.")],
   "lbl":{"main":"Valor futuro","rows":{"deposited":"Total aportado","interest":"Intereses ganados","multiple":"Múltiplo de crecimiento"}}},
  "loan-payment":{"title":"Calculadora de cuotas de préstamo — interés total | CalcFin","h1":"Calculadora de cuotas de préstamo",
   "meta":"Calcula la cuota mensual y el interés total de cualquier préstamo. Fórmula de amortización explicada — gratis y privado.",
   "intro":"Introduce un monto, una tasa anual y un plazo para obtener la cuota fija mensual, el interés total y el costo total.",
   "inputs":["Monto del préstamo ($)","Tasa anual (%)","Plazo (años)"],
   "how":["Los préstamos se amortizan: cada cuota incluye intereses y capital.",
     "Las primeras cuotas son de intereses — por eso los pagos extra al capital al inicio ahorran más.",
     "Con tasa 0 %, el capital se divide en partes iguales entre todas las cuotas."],
   "formula":"Cuota = P · r · (1+r)^n / ((1+r)^n − 1)   donde r = tasa mensual, n = número de cuotas",
   "faq":[("¿Funciona para préstamos de auto o personales?","Sí — todo préstamo a tasa fija con amortización usa exactamente esta fórmula."),
     ("¿Por qué mi banco muestra un número distinto?","Los bancos añaden comisiones y seguros o usan redondeos y días ligeramente distintos."),
     ("¿Cómo pago menos intereses en total?","Plazo más corto, tasa menor o pagos extra a capital — compara el interés total entre escenarios.")],
   "lbl":{"main":"Cuota mensual","rows":{"interest":"Intereses totales","paid":"Total pagado","n":"Número de cuotas"}}},
  "mortgage-payment":{"title":"Calculadora de hipoteca — cuota, impuesto y seguro | CalcFin","h1":"Calculadora de hipoteca",
   "meta":"Estima tu cuota hipotecaria real incluyendo impuesto, seguro y comunidad. Gratis y privado.",
   "intro":"Una cuota hipotecaria es más que capital e intereses. Añade impuesto, seguro y comunidad para ver lo que realmente sale de tu cuenta cada mes.",
   "inputs":["Precio de la vivienda ($)","Entrada ($)","Tasa (%)","Plazo (años)","Impuesto anual ($)","Seguro anual ($)","Comunidad mensual ($)"],
   "how":["Los bancos citan solo capital e intereses, pero la cuota real incluye impuestos, seguro y comunidad escrowados.",
     "Regla común: presupuesta 1–2 % del valor de la vivienda al año en impuestos y seguro, aunque varía mucho por región.",
     "Un 20 % de entrada suele eliminar el seguro PMI de la ecuación."],
   "formula":"Cuota = C+I + (Impuesto/12) + (Seguro/12) + Comunidad",
   "faq":[("¿Incluye el PMI?","No — añádelo manualmente en el campo de comunidad si tu entrada es menor al 20 %."),
     ("¿El impuesto es exacto para mi zona?","Las tasas varían de menos de 0,5 % a más de 2 % del valor al año — revisa tu tasa local."),
     ("¿15 o 30 años?","15 años: cuota más alta pero mucho menos interés total — compara ambos escenarios.")],
   "lbl":{"main":"Cuota mensual total","rows":{"pi":"Capital e intereses","tax":"Impuesto (mensual)","ins":"Seguro (mensual)","hoa":"Comunidad (mensual)","loan":"Monto del préstamo"}}},
  "savings-goal":{"title":"Calculadora de meta de ahorro — cuánto ahorrar al mes | CalcFin","h1":"Calculadora de meta de ahorro",
   "meta":"Calcula el ahorro mensual necesario para alcanzar un monto en una fecha, con interés compuesto. Gratis y privado.",
   "intro":"¿Tienes una meta y una fecha? Esto te dice el aporte mensual exacto para lograrla, asumiendo interés compuesto.",
   "inputs":["Meta de ahorro ($)","Tiempo para lograrlo (años)","Rendimiento anual (%)","Ya ahorrado ($)"],
   "how":["Primero, tus ahorros actuales se proyectan con interés compuesto hasta la fecha límite.",
     "La brecha entre ese valor futuro y tu meta la llenan los aportes mensuales.",
     "Un rendimiento mayor reduce la cuota, pero no planifiques con tasas que no puedas garantizar."],
   "formula":"A = (Meta − VF_actual) · r / ((1+r)^n − 1)   donde r = tasa mensual, n = meses",
   "faq":[("¿Y si no puedo asumir la cuota?","Alarga el plazo, reduce la meta o busca mejor rendimiento — prueba cada palanca al instante."),
     ("¿El ahorro es mensual o anual?","Mensual, al final de cada mes."),
     ("¿Sirve para la entrada de una casa?","Sí — es un uso muy común.")],
   "lbl":{"main":"Ahorro mensual requerido","rows":{"fv":"Valor futuro del ahorro actual","gap":"Brecha por cubrir","contrib":"Aportes totales"}}},
  "credit-card-payoff":{"title":"Calculadora para saldar tarjeta — meses hasta cero deuda | CalcFin","h1":"Calculadora para saldar tarjeta",
   "meta":"Cuánto tardas en saldar una deuda de tarjeta con cuotas fijas, y cuánto interés pagas. Gratis.",
   "intro":"Cuotas fijas sobre deuda de tarjeta: mira exactamente cuántos meses hasta estar libre de deuda y cuánto interés cobra el banco de camino.",
   "inputs":["Saldo ($)","TIN anual (%)","Cuota mensual ($)"],
   "how":["Los pagos mínimos están diseñados para mantenerte en deuda: al 22,9 % de TIN, los intereses solos se comen la mayor parte de una cuota pequeña.",
     "Si tu cuota es menor que los intereses del primer mes, el saldo crece para siempre — la calculadora lo avisa en lugar de iterar eternamente.",
     "Redondear la cuota hacia arriba apenas un poco recorta meses del pago."],
   "formula":"Cada mes: interés = saldo × TIN/12, luego saldo = saldo + interés − cuota, repetido hasta cero",
   "faq":[("¿Cuál es una buena cuota para $8.000 al 22,9 %?","Los intereses solos son ~152 $/mes. Con 300 $/mes: unos 3 años; con 500 $/mes: menos de 2 años y miles de ahorro."),
     ("¿Asume que dejo de usar la tarjeta?","Sí — no se modelan gastos nuevos. Añádelos al saldo manualmente si hace falta."),
     ("¿Ayudaría una transferencia de saldo?","Si el nuevo TIN es menor, sí — modela la tasa menor más la comisión dentro del saldo.")],
   "lbl":{"main":"Meses hasta cero deuda","rows":{"interest":"Intereses pagados","paid":"Total pagado","date":"Libre de deuda estimado","never":"Nunca se salda","mi":"Interés mensual","need":"Subir la cuota por encima de"}}},
  "inflation":{"title":"Calculadora de inflación — poder adquisitivo real | CalcFin","h1":"Calculadora de inflación",
   "meta":"Mira lo que el dinero de hoy comprará realmente en el futuro a una tasa de inflación dada. Simple, rápido, privado.",
   "intro":"La inflación encoge silenciosamente el poder adquisitivo. Introduce un monto, una tasa media y unos años para ver lo que valdrá de verdad.",
   "inputs":["Monto hoy ($)","Inflación media (%)","Años"],
   "how":["Con un 3 % de inflación, los precios se duplican aproximadamente cada 24 años (regla del 72: 72 ÷ tasa ≈ años de duplicación).",
     "Por eso el dinero bajo el colchón pierde valor cada año — y por qué importan inversiones que superen la inflación.",
     "Históricamente la inflación de EE. UU. promedia ~3 %, con grandes variaciones por década."],
   "formula":"Valor real = Monto / (1 + inflación)^años",
   "faq":[("¿Qué tasa de inflación usar?","La media de EE. UU. a largo plazo es ~3 %. Para planificar con prudencia: 3–4 %; algunos años oscilaron entre casi 0 % y 9 %."),
     ("¿Es lo mismo que un rendimiento?","No — es el lado contrario: lo que hace la inflación con el dinero quieto. Compáralo con la calculadora de interés compuesto."),
     ("¿Puedo modelar inflación creciente?","Esta herramienta usa una tasa media constante — aproxima con la media del período.")],
   "lbl":{"main":"Poder adquisitivo real","rows":{"nominal":"Monto nominal","lost":"Poder adquisitivo perdido","pct":"Pérdida en porcentaje"}}},
  "roi":{"title":"Calculadora de ROI — retorno total y anualizado | CalcFin","h1":"Calculadora de ROI",
   "meta":"Calcula el retorno de la inversión (ROI) y la tasa anualizada. Compara inversiones de forma justa.",
   "intro":"El ROI simple dice cuánto ganaste; el anualizado dice qué tan rápido — y ese es el número comparable entre inversiones.",
   "inputs":["Invertido ($)","Valor final ($)","Período (años)"],
   "how":["El ROI solo engaña: +50 % en 1 año es excelente, +50 % en 10 años es mediocre. La tasa anualizada (CAGR) hace comparables inversiones distintas.",
     "El CAGR es la tasa anual constante que llevaría del costo al valor final en el mismo período.",
     "Incluye comisiones, impuestos y dividendos en el valor final para una foto honesta."],
   "formula":"ROI = (Final − Costo) / Costo × 100 %      CAGR = (Final/Costo)^(1/años) − 1",
   "faq":[("¿Qué ROI es bueno?","Depende del riesgo y el plazo. Las acciones rindieron ~10 % nominal a largo plazo; el ahorro mucho menos con mucho menos riesgo."),
     ("¿ROI o CAGR?","El ROI es la ganancia total en porcentaje; el CAGR la reparte por año. Solo el CAGR permite comparar plazos distintos."),
     ("¿Puede ser negativo?","Sí — un valor final por debajo del costo da ROI y CAGR negativos.")],
   "lbl":{"main":"ROI total","rows":{"cagr":"Retorno anualizado (CAGR)","profit":"Beneficio neto","multiple":"Múltiplo de crecimiento"}}},
  "retirement":{"title":"Calculadora de jubilación — tendrás suficiente? | CalcFin","h1":"Calculadora de jubilación",
   "meta":"Proyecta tus ahorros para la jubilación desde el saldo actual, aportes, aporte del empleador y rendimiento. Gratis y privado.",
   "intro":"Proyecta tu nido a la fecha de jubilación desde lo que tienes, lo que aportas cada mes (incluido el aporte del empleador) y un rendimiento asumido.",
   "inputs":["Ahorro actual ($)","Aporte mensual ($)","Aporte del empleador ($)","Rendimiento anual (%)","Años hasta jubilarte"],
   "how":["El aporte del empleador es dinero gratis — inclúyelo en tu cuota mensual; en una carrera puede sumar seis cifras.",
     "La última década de capitalización suele aportar los montos mayores — empezar temprano importa más que aportar más.",
     "El resultado es nominal. Pásalo por la calculadora de inflación para verlo en poder adquisitivo actual."],
   "formula":"VF = Actual·(1+r/n)^(nt) + Mensual·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Qué rendimiento asumir?","Una cartera diversificada rindió históricamente 7–8 % nominal. Planificación prudente: 5–6 %."),
     ("¿Incluye la pensión pública?","No — esto es solo tus inversiones. Las pensiones esperadas se calculan aparte."),
     ("Cuánto necesito realmente?","Regla inicial común: 25× tu gasto anual previsto («regla del 4 %»), aunque varía mucho según el caso.")],
   "lbl":{"main":"Ahorro proyectado para la jubilación","rows":{"fv":"Del ahorro actual","fvm":"De los aportes","contrib":"Aportado en total","growth":"Intereses ganados"}}},
 }
},
}
