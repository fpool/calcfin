# -*- coding: utf-8 -*-
"""CalcFin 扩展语言:ja / it / pt(build.py 会 TR.update(EXTRA))"""

EXTRA = {
"ja": {
 "name":"日本語",
 "nav_home":"すべての計算機","nav_privacy":"プライバシー","nav_about":"このサイトについて",
 "btn":"計算する","related_h2":"関連する計算機","how_h2":"計算の仕組み","faq_h2":"よくある質問",
 "home":{"title":"無料の金融計算機 — 複利・ローン・住宅ローン・貯蓄 | CalcFin",
   "meta":"無料オンライン金融計算機:複利、ローン返済、住宅ローン、貯蓄目標、カード支払い、インフレ、ROI、老後資金。非公開、登録不要。",
   "h1":"無料の金融計算機","sub":"<b>ブラウザ内で完全に動作</b>する高速・プライベートな計算機 — 入力した数字が端末の外に出ることはありません。各ページで正確な計算式を公開しています。",
   "h2":"登録不要。データ収集なし。ただの計算。",
   "p1":"CalcFin のすべての計算機は JavaScript でローカル実行されます — 入力内容はお客様のデバイスで処理され、サーバーに送信されることはありません。各ページで使用している計算式を公開しているので、ブラックボックスを信頼する代わりに数式そのものを確認できます。",
   "p2":"結果は計画・学習のための推定値であり、金融アドバイスではありません。"},
 "privacy":{"title":"プライバシーポリシー | CalcFin","meta":"CalcFin のプライバシーポリシー — ローカル計算、Cookie、広告について。",
   "body":"""
  <h1>プライバシーポリシー</h1>
  <p class="updated">最終更新:2026年10月2日</p>
  <p>CalcFin(「当社」)は <b>ブラウザ内で完全に動作する</b> 無料の金融計算機を提供しています。本ポリシーは、収集されるデータ — および収集されないデータ — について説明します。</p>
  <h2>1. 入力内容</h2>
  <p><b>入力内容や結果を当社が見ることはありません。</b>すべての計算はお客様のデバイス上でローカルに実行されます。入力がサーバーに送信・保存・記録されることはありません。</p>
  <h2>2. サーバーログ</h2>
  <p>ほぼすべてのウェブサイトと同様、ホスティング事業者(Cloudflare)はセキュリティとパフォーマンスのため、IP アドレス、ブラウザ種別、URL、タイムスタンプ等の標準的な技術データを自動記録します。このデータは <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare のプライバシーポリシー</a>に準拠します。</p>
  <h2>3. Cookie と広告</h2>
  <p>Google AdSense による広告を表示する予定です。Google を含む第三者は、過去のアクセスに基づく広告配信に Cookie を使用します。パーソナライズ広告は <a href='https://www.google.com/settings/ads'>Google 広告設定</a>で無効化できます。Cookie をブロックしても計算機の機能には影響しません。</p>
  <h2>4. 金融アドバイスではない</h2>
  <p>結果は教育・計画のための数値推定であり、金融アドバイスではありません。</p>
  <h2>5. お問い合わせ</h2>
  <p>ご質問: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"CalcFin について | CalcFin","meta":"CalcFin について — ブラウザ内で動作し、計算式が透明な無料金融計算機。",
   "body":"""
  <h1>CalcFin について</h1>
  <p>CalcFin は、高速で無料、無駄のない金融計算機のコレクションです。すべての計算機は <b>ブラウザ内で完全に動作</b>し — 数字がサーバーに触れることはなく — 各ページで結果の裏にある計算式を説明しています。</p>
  <h2>なぜ CalcFin なのか</h2>
  <p>ほとんどの金融計算機サイトは、広告の下にツールを埋め込んだり、登録を求めたり、計算式を隠したりします。私たちは逆を行きます:クリーンなツール、透明な数式、正直な推定。</p>
  <h2>原則</h2>
  <ul><li><b>ローカルがデフォルト。</b>入力は端末の外に出ません。</li>
  <li><b>透明な計算式。</b>各ページで正確な式を公開。</li>
  <li><b>無料は無料。</b>登録なし、ペイウォールなし、制限なし。</li></ul>
  <h2>お問い合わせ</h2>
  <p>フィードバックとバグ報告: <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"複利計算機 — 毎月の積立付き | CalcFin","h1":"複利計算機",
   "meta":"毎月の積立付きの無料複利計算機。お金がどう増えるかを確認 — 計算式を解説、ブラウザ内で動作。",
   "intro":"元本と毎月の積立が複利でどう増えるかを確認できます。利率と期間を調整して、シナリオを即座に比較しましょう。",
   "inputs":["元本 ($)","年利 (%)","年数","毎月の積立 ($)"],
   "how":["複利は「利息に対する利息」を生みます。年利 r を月複利にすると、毎月残高は r/12 ずつ増加します。",
     "第 1 項は元本が全期間で増加したもの、第 2 項は毎月の積立の将来価値です。",
     "時間は利率より重要:年数を倍にすると、元本の成長倍率はほぼ 2 乗になります。"],
   "formula":"将来価値 = 元本(1+r/n)^(nt) + 積立 · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("積立は月初ですか月末ですか?","この計算機は月初の積立(期首払い)を想定しています — そのため計算式に (1+r/n) の係数が含まれます。"),
     ("税金やインフレは考慮されますか?","いいえ — 結果は名目です。実質購買力はインフレ計算機でご確認ください。"),
     ("利率はいくらにすれば?","米国株式市場の過去の年平均リターンは約 7〜10 %(インフレ前)ですが、過去の実績は将来を保証しません。")],
   "lbl":{"main":"将来価値","rows":{"deposited":"累計拠出額","interest":"運用益","multiple":"成長倍率"}}},
  "loan-payment":{"title":"ローン返済計算機 — 月返済額と総利息 | CalcFin","h1":"ローン返済計算機",
   "meta":"あらゆるローンの月返済額と総利息を計算。元利均等の計算式を解説 — 無料、ブラウザ内で動作。",
   "intro":"借入額・年利・期間を入力すると、固定の月返済額、総利息、総返済額がわかります。",
   "inputs":["借入額 ($)","年利 (%)","期間 (年)"],
   "how":["ローンは元利均等返済です:毎回の返済は利息と元本の両方を含みます。",
     "初期の返済は利息が大部分 — だから繰り上げ返済は初期に行うほど利息を大きく節約できます。",
     "金利 0 % のローンは元本を返済回数で均等割りします。"],
   "formula":"月返済額 = P · r · (1+r)^n / ((1+r)^n − 1)   ここで r = 月利、n = 返済回数",
   "faq":[("マイカーローンや教育ローンでも使えますか?","はい — 固定金利・元利均等のローンならすべてこの計算式です。"),
     ("貸し手の数字と少し違うのはなぜ?","貸し手は手数料や保険を加算したり、丸めや日数計算が少し異なる場合があります。"),
     ("総利息を減らすには?","期間を短く、金利を下げる、繰り上げ返済 — この計算機でシナリオごとの総利息を比較できます。")],
   "lbl":{"main":"月返済額","rows":{"interest":"総利息","paid":"総返済額","n":"返済回数"}}},
  "mortgage-payment":{"title":"住宅ローン計算機 — 元利・税・保険込み | CalcFin","h1":"住宅ローン計算機",
   "meta":"固定資産税・保険・管理費を含む、実際の毎月の住宅ローン返済額を試算。無料で非公開。",
   "intro":"住宅ローンの返済は元利だけではありません。税・保険・管理費を加えて、毎月実際に引き落とされる金額を確認しましょう。",
   "inputs":["物件価格 ($)","頭金 ($)","金利 (%)","期間 (年)","固定資産税 (年額 $)","保険 (年額 $)","管理費 (月額 $)"],
   "how":["金融機関が提示するのは元利のみですが、実際の返済には税・保険・管理費が含まれます。",
     "目安として、税と保険合わせて物件価格の年 1〜2 % を予算化します(地域差大)。",
     "頭金 20 % 以上で通常は PMI(民間保険)が不要になります。"],
   "formula":"返済額 = 元利 + (税/12) + (保険/12) + 管理費",
   "faq":[("PMI は含まれますか?","いいえ — 頭金が 20 % 未満の場合は、管理費フィールドに PMI を手動で加えてください。"),
     ("税率は私の地域で正確ですか?","固定資産税率は物件価格の年 0.5 % 未満から 2 % 超まで地域差があります — お住まいの税率をご確認ください。"),
     ("15 年か 30 年か?","15 年は月返済が高い代わりに総利息が大幅に少なくなります — 両方をこの計算機で比較してみてください。")],
   "lbl":{"main":"月返済額合計","rows":{"pi":"元利合計","tax":"固定資産税(月額)","ins":"保険(月額)","hoa":"管理費(月額)","loan":"借入額"}}},
  "savings-goal":{"title":"貯蓄目標計算機 — 毎月の必要積立額 | CalcFin","h1":"貯蓄目標計算機",
   "meta":"目標金額と期限から、複利を含めて必要な毎月の積立額を計算。無料で非公開。",
   "intro":"目標と期限があれば、複利を前提に「到達するために必要な毎月の積立額」を正確に算出します。",
   "inputs":["目標額 ($)","達成期間 (年)","年利回り (%)","既に貯蓄済み ($)"],
   "how":["まず、既存の貯蓄が複利で期限までどう増えるかを試算します。",
     "その将来価値と目標の差額を、毎月の積立で埋めます。",
     "想定利回りが高いと必要額は下がりますが、頼れない利率で計画しないでください。"],
   "formula":"積立額 = (目標 − 現貯蓄の将来価値) · r / ((1+r)^n − 1)   ここで r = 月利、n = 月数",
   "faq":[("必要額を払えない場合は?","期間を延ばす、目標を下げる、金利を上げる — この計算機で各レバーを即座に試せます。"),
     ("積立は毎月ですか年次ですか?","毎月、月末に積み立てます。"),
     ("住宅頭金の計画にも使えますか?","はい — 頭金の計画によく使われます。")],
   "lbl":{"main":"必要な毎月積立額","rows":{"fv":"現貯蓄の将来価値","gap":"埋めるべき差額","contrib":"累計積立額"}}},
  "credit-card-payoff":{"title":"カード支払い計算機 — 完済までの月数 | CalcFin","h1":"カード支払い計算機",
   "meta":"固定の毎月返済でカード残高を完済するまでの月数と総利息を計算。無料。",
   "intro":"カード残高への固定返済:何ヶ月で完済できるか、その間に銀行がいくら利息を受け取るかを正確に表示します。",
   "inputs":["残高 ($)","年率 APR (%)","毎月の返済 ($)"],
   "how":["最低返済額は借地に留まらせる設計です:APR 22.9 % では利息だけで小さな返済の大部分を食べます。",
     "返済額が初月の利息を下回ると残高は永久に増え続けます — 無限ループの代わりにその旨を表示します。",
     "返済額を少しでも増やすと、完済までの月数が大きく短縮されます。"],
   "formula":"毎月:利息 = 残高 × APR/12、残高 = 残高 + 利息 − 返済、ゼロまで繰り返し",
   "faq":[("残高 8,000 $・APR 22.9 % の適切な返済は?","利息だけで約 152 $/月です。300 $/月なら約 3 年、500 $/月なら 2 年未満で数千ドルの節約。"),
     ("カードの使用を止める前提ですか?","はい — 新規利用はモデルに含まれません。必要なら残高に加算してください。"),
     ("残高移行は有効?","新しい APR が低ければ有効です — 低い APR と移行手数料を残高に加えてモデル化してください。")],
   "lbl":{"main":"完済までの月数","rows":{"interest":"支払利息総額","paid":"総返済額","date":"完済目安","never":"完済不可能","mi":"月あたり利息","need":"返済額をこれ以上に"}}},
  "inflation":{"title":"インフレ計算機 — お金の実質購買力 | CalcFin","h1":"インフレ計算機",
   "meta":"一定のインフレ率で、今のお金が将来本当にどれだけの価値になるかを確認。シンプル、高速、非公開。",
   "intro":"インフレは購買力を静かに縮めます。金額・平均インフレ率・年数を入力して、実質価値を確認しましょう。",
   "inputs":["現在の金額 ($)","平均インフレ率 (%)","年数"],
   "how":["インフレ 3 % では物価は約 24 年で倍になります(72 の法則:72 ÷ 率 ≈ 倍化年数)。",
     "だからこそ寝かせた現金は毎年価値を失い、インフレに勝る運用が重要です。",
     "米国の長期平均インフレは約 3 % ですが、年代により大きく異なります。"],
   "formula":"実質価値 = 金額 / (1 + インフレ)^年数",
   "faq":[("インフレ率はいくらにすれば?","米国の長期平均は約 3 %。保守的には 3〜4 % で計画。近年は 0 % 近くから 9 % まで幅があります。"),
     ("投資リターンと同じですか?","いいえ — 逆側です:インフレが idle な現金に何をするか。複利計算機と組み合わせて比較してください。"),
     ("上昇するインフレはモデル化できますか?","このツールは固定平均率です — 期間の平均を近似に使ってください。")],
   "lbl":{"main":"実質購買力","rows":{"nominal":"名目金額","lost":"失われた購買力","pct":"目減り率"}}},
  "roi":{"title":"ROI 計算機 — 総リターンと年率換算 | CalcFin","h1":"ROI 計算機",
   "meta":"投資Return(ROI)と年率換算リターンを計算。投資の実力を正しく理解する。",
   "intro":"単純 ROI は「いくら儲かったか」、年率換算は「どの速さか」— 投資間を公平に比較できるのは後者です。",
   "inputs":["投資額 ($)","最終価値 ($)","保有期間 (年)"],
   "how":["ROI だけでは誤解します:+50 % が 1 年なら優秀、10 年なら平凡。年率換算(CAGR)が投資を比較可能にします。",
     "CAGR は同じ期間でコストから最終価値へ至る一定の年率です。",
     "手数料・税・配当を最終価値に含めて、正直な数字を計算しましょう。"],
   "formula":"ROI = (最終 − コスト) / コスト × 100 %      CAGR = (最終/コスト)^(1/年数) − 1",
   "faq":[("良い ROI とは?","リスクと期間によります。長期の株式平均は名目 ~10 %。預貯金はリスクがはるかに低い代わりに大きく下回ります。"),
     ("ROI と CAGR の違いは?","ROI は総利益率、CAGR はそれを年数に均したもの。異なる保有期間を公平に比べられるのは CAGR だけです。"),
     ("ROI はマイナスになり得ますか?","はい — 最終価値がコストを下回れば ROI と CAGR はマイナスです。")],
   "lbl":{"main":"総リターン(ROI)","rows":{"cagr":"年率換算リターン(CAGR)","profit":"純利益","multiple":"成長倍率"}}},
  "retirement":{"title":"老後資金計算機 — 足りるか試算 | CalcFin","h1":"老後資金計算機",
   "meta":"現預金・毎月の積立(勤務先マッチ込み)・運用利回りから退職時の資産を試算。無料で非公開。",
   "intro":"現在の貯蓄、毎月の積立(勤務先のマッチ込み)、想定利回りから、退職時点の資産を試算します。",
   "inputs":["現在の貯蓄 ($)","毎月の積立 ($)","勤務先マッチ ($)","年利回り (%)","退職までの年数"],
   "how":["勤務先のマッチはタダ同然の金 — 積立に含めましょう;キャリアを通じて六桁の差になることも。",
     "複利の最後の 10 年が最大の金額を生みます — 多く積むより早く始めるほうが重要です。",
     "結果は名目額です。インフレ計算機で現在の購買力に換算して確認しましょう。"],
   "formula":"将来価値 = 現貯蓄·(1+r/n)^(nt) + 月積立·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("利回りはいくらを想定すべき?","分散ポートフォリオの過去リターンは名目 7〜8 %。保守的には 5〜6 % で計画。"),
     ("公的年金は含まれますか?","いいえ — ここは自分の投資のみ。期待される年金は別途計上してください。"),
     ("実際いくら必要?","一般的な目安は想定年支出の 25 倍(「4 % ルール」)— ただし個人差が大きいです。")],
   "lbl":{"main":"退職時の試算資産","rows":{"fv":"現貯蓄から","fvm":"積立から","contrib":"累計拠出額","growth":"運用益"}}},
 }
},
"it": {
 "name":"Italiano",
 "nav_home":"Tutti i calcolatori","nav_privacy":"Privacy","nav_about":"Chi siamo",
 "btn":"Calcola","related_h2":"Calcolatori correlati","how_h2":"Come funziona","faq_h2":"Domande frequenti",
 "home":{"title":"Calcolatori finanziari gratuiti — Interessi, prestiti, mutuo, risparmio | CalcFin",
   "meta":"Calcolatori finanziari online gratuiti: interesse composto, rata prestito, mutuo, obiettivo di risparmio, carta di credito, inflazione, ROI e pensione. Privati, senza registrazione.",
   "h1":"Calcolatori finanziari gratuiti","sub":"Calcolatori rapidi e privati che funzionano <b>interamente nel tuo browser</b> — i tuoi numeri non lasciano mai il dispositivo. Ogni pagina mostra la formula esatta.",
   "h2":"Senza registrazione. Senza raccolta dati. Solo matematica.",
   "p1":"Ogni calcolatore di CalcFin gira localmente in JavaScript — i tuoi dati vengono elaborati sul tuo dispositivo e mai inviati a un server. Ogni pagina documenta la formula esatta, così puoi verificare i calcoli invece di fidarti di una scatola nera.",
   "p2":"I risultati sono stime per pianificazione ed educazione, non consulenza finanziaria."},
 "privacy":{"title":"Informativa sulla privacy | CalcFin","meta":"Informativa sulla privacy di CalcFin — calcoli locali, cookie e pubblicità.",
   "body":"""
  <h1>Informativa sulla privacy</h1>
  <p class="updated">Ultimo aggiornamento: 2 ottobre 2026</p>
  <p>CalcFin («noi») offre calcolatori finanziari gratuiti che funzionano <b>interamente nel tuo browser</b>. Questa informativa spiega quali dati vengono — e non vengono — raccolti.</p>
  <h2>1. I tuoi dati</h2>
  <p><b>Non vediamo mai i tuoi dati né i risultati.</b> Ogni calcolo avviene localmente sul tuo dispositivo. Nulla viene inviato, salvato o registrato.</p>
  <h2>2. Log del server</h2>
  <p>Come quasi tutti i siti, il nostro provider (Cloudflare) registra automaticamente dati tecnici standard — IP, tipo di browser, URL, data — per sicurezza e prestazioni, conformemente all'<a href="https://www.cloudflare.com/privacypolicy/">informativa sulla privacy di Cloudflare</a>.</p>
  <h2>3. Cookie e pubblicità</h2>
  <p>Prevediamo di mostrare pubblicità servita da Google AdSense. Terze parti, incluso Google, usano cookie per annunci basati sulle visite precedenti. Disattivabili da <a href="https://www.google.com/settings/ads">Impostazioni annunci Google</a>; bloccare i cookie non influisce sui calcolatori.</p>
  <h2>4. Non è consulenza finanziaria</h2>
  <p>I risultati sono stime matematiche per educazione e pianificazione — non consulenza finanziaria.</p>
  <h2>5. Contatti</h2>
  <p>Domande: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Chi siamo — CalcFin | CalcFin","meta":"CalcFin — calcolatori finanziari gratuiti nel browser con formule trasparenti.",
   "body":"""
  <h1>Chi siamo — CalcFin</h1>
  <p>CalcFin è una raccolta di calcolatori finanziari veloci, gratuiti e diretti. Ogni calcolatore funziona <b>interamente nel tuo browser</b> — i tuoi numeri non toccano mai un server — e ogni pagina spiega la formula dietro il risultato.</p>
  <h2>Perché esiste CalcFin</h2>
  <p>La maggior parte dei siti di calcolatori seppellisce lo strumento sotto la pubblicità, richiede registrazioni o nasconde la matematica. Noi facciamo il contrario: strumenti puliti, formule trasparenti, stime oneste.</p>
  <h2>Principi</h2>
  <ul><li><b>Locale per impostazione predefinita.</b> I dati non lasciano mai il dispositivo.</li>
  <li><b>Matematica trasparente.</b> Ogni pagina mostra la formula esatta.</li>
  <li><b>Gratis significa gratis.</b> Senza registrazione, senza paywall, senza limiti.</li></ul>
  <h2>Contatti</h2>
  <p>Feedback e bug: <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"Calcolatore interesse composto — con versamenti mensili | CalcFin","h1":"Calcolatore interesse composto",
   "meta":"Calcolatore di interesse composto gratuito con versamenti mensili. Guarda come crescono i tuoi soldi — formula spiegata, nel browser.",
   "intro":"Vedi come un capitale iniziale più versamenti mensili cresce con l'interesse composto. Regola tasso e durata per confrontare scenari all'istante.",
   "inputs":["Capitale iniziale ($)","Tasso annuo (%)","Anni","Versamento mensile ($)"],
   "how":["L'interesse composto paga interessi sugli interessi. Con capitalizzazione mensile al tasso annuo r, il saldo cresce ogni mese di r/12.",
     "Il primo termine è il capitale iniziale per tutto il periodo; il secondo è il valore futuro di ogni versamento mensile.",
     "Il tempo conta più del tasso: raddoppiare gli anni eleva quasi al quadrato il multiple del capitale."],
   "formula":"VF = C(1+r/n)^(nt) + V · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Il versamento è a inizio o fine mese?","Questo calcolatore assume versamenti a inizio mese (rendita anticipata) — per questo la formula include il fattore (1+r/n) extra."),
     ("Include tasse o inflazione?","No — i risultati sono nominali. Per il potere d'acquisto reale usa il Calcolatore di inflazione."),
     ("Quale tasso usare?","Storicamente il mercato azionario USA rende ~7–10 % annuo prima dell'inflazione — ma i rendimenti passati non garantiscono i futuri.")],
   "lbl":{"main":"Valore futuro","rows":{"deposited":"Totale versato","interest":"Interessi maturati","multiple":"Multiple di crescita"}}},
  "loan-payment":{"title":"Calcolatore rata prestito — quota e interessi totali | CalcFin","h1":"Calcolatore rata prestito",
   "meta":"Calcola la rata mensile e gli interessi totali di qualsiasi prestito. Formula di ammortamento spiegata — gratis e privato.",
   "intro":"Inserisci importo, tasso annuo e durata per ottenere la rata fissa mensile, gli interessi totali e il costo complessivo.",
   "inputs":["Importo del prestito ($)","Tasso annuo (%)","Durata (anni)"],
   "how":["I prestiti sono ammortizzati: ogni rata comprende interessi e capitale.",
     "Le prime rate sono cariche di interessi — per questo un'estinzione anticipata all'inizio risparmia il massimo.",
     "Con tasso 0 % il capitale si divide equamente tra tutte le rate."],
   "formula":"Rata = P · r · (1+r)^n / ((1+r)^n − 1)   dove r = tasso mensile, n = numero di rate",
   "faq":[("Funziona per auto, personali, studenti?","Sì — qualsiasi prestito a tasso fisso con ammortamento usa esattamente questa formula."),
     ("Perché la mia banca mostra un numero leggermente diverso?","Le banche aggiungono commissioni e assicurazioni o usano arrotondamenti diversi."),
     ("Come pago meno interessi in totale?","Durata più breve, tasso più basso, estinzioni anticipate — confronta gli interessi totali tra scenari.")],
   "lbl":{"main":"Rata mensile","rows":{"interest":"Interessi totali","paid":"Totale pagato","n":"Numero di rate"}}},
  "mortgage-payment":{"title":"Calcolatore rata mutuo — quota, tasse e assicurazione | CalcFin","h1":"Calcolatore rata mutuo",
   "meta":"Stima la tua vera rata mensile del mutuo con tasse, assicurazione e spese condominiali. Gratis e privato.",
   "intro":"La rata del mutuo è più di capitale e interessi. Aggiungi tasse, assicurazione e spese per vedere il numero che esce davvero dal conto ogni mese.",
   "inputs":["Prezzo casa ($)","Acconto ($)","Tasso (%)","Durata (anni)","Imposta annua ($)","Assicurazione annua ($)","Spese mensili ($)"],
   "how":["Le banche quotano solo capitale e interessi, ma la rata reale include tasse, assicurazione e spese in escrow.",
     "Regola pratica: budgeta 1–2 % del valore dell'immobile all'anno per tasse e assicurazione, anche se varia molto per zona.",
     "Un acconto del 20 % di solito elimina l'assicurazione PMI dall'equazione."],
   "formula":"Rata = C+I + (Tasse/12) + (Assicurazione/12) + Spese",
   "faq":[("La PMI è inclusa?","No — aggiungila manualmente nel campo spese se l'acconto è sotto il 20 %."),
     ("L'imposta è accurata per la mia zona?","Le aliquote vanno da meno di 0,5 % a oltre 2 % del valore all'anno — verifica la tua aliquota locale."),
     ("15 o 30 anni?","15 anni: rata più alta ma interessi totali molto minori — confronta entrambi gli scenari.")],
   "lbl":{"main":"Rata mensile totale","rows":{"pi":"Capitale e interessi","tax":"Imposta (mensile)","ins":"Assicurazione (mensile)","hoa":"Spese (mensili)","loan":"Importo del mutuo"}}},
  "savings-goal":{"title":"Calcolatore obiettivo risparmio — quanto mettere da parte | CalcFin","h1":"Calcolatore obiettivo risparmio",
   "meta":"Calcola il risparmio mensile necessario per raggiungere un obiettivo entro una scadenza, con interessi composti. Gratis e privato.",
   "intro":"Hai un obiettivo e una scadenza? Ecco il versamento mensile esatto per arrivarci, assumendo interessi composti.",
   "inputs":["Obiettivo ($)","Tempo (anni)","Rendimento annuo (%)","Già risparmiato ($)"],
   "how":["Prima, i tuoi risparmi attuali sono proiettati con interessi composti fino alla scadenza.",
     "Il divario tra quel valore futuro e l'obiettivo è coperto dai versamenti mensili.",
     "Un rendimento superiore riduce la rata — ma non pianificare su tassi incerti."],
   "formula":"V = (Obiettivo − VF_attuale) · r / ((1+r)^n − 1)   dove r = tasso mensile, n = mesi",
   "faq":[("E se non posso permettermi la rata?","Allunga la scadenza, riduci l'obiettivo o cerca un rendimento migliore — prova ogni leva all'istante."),
     ("Il versamento è mensile o annuale?","Mensile, a fine mese."),
     ("Si può usare per l'acconto casa?","Sì — è un uso molto comune.")],
   "lbl":{"main":"Risparmio mensile richiesto","rows":{"fv":"Valore futuro del risparmio attuale","gap":"Divario da colmare","contrib":"Versamenti totali"}}},
  "credit-card-payoff":{"title":"Calcolatore estinzione carta — mesi fino a zero debito | CalcFin","h1":"Calcolatore estinzione carta",
   "meta":"Quanto tempo serve per estinguere un debito di carta con rate fisse, e quanti interessi paghi. Gratis.",
   "intro":"Rate fisse su un debito di carta: vedi esattamente quanti mesi fino a zero debito e quanti interessi incassa la banca.",
   "inputs":["Saldo ($)","TAEG annuo (%)","Rata mensile ($)"],
   "how":["I pagamenti minimi sono progettati per tenerti in debito: al 22,9 % di TAEG gli interessi da soli assorbono la maggior parte di una piccola rata.",
     "Se la rata è inferiore agli interessi del primo mese, il saldo cresce all'infinito — il calcolatore lo segnala invece di iterare all'infinito.",
     "Arrotondare la rata leggermente verso l'alto taglia mesi interi."],
   "formula":"Ogni mese: interessi = saldo × TAEG/12, poi saldo = saldo + interessi − rata, ripetuto fino a zero",
   "faq":[("Che rata per 8.000 $ al 22,9 %?","Gli interessi da soli sono ~152 $/mese. A 300 $/mese: circa 3 anni; a 500 $/mese: meno di 2 anni e migliaia di risparmio."),
     ("Assume che smetta di usare la carta?","Sì — nuove spese non sono modellate. Aggiungile manualmente al saldo."),
     ("Un trasferimento del saldo aiuterebbe?","Se il nuovo TAEG è più basso, sì — modelalo con il TAEG inferiore più le commissioni nel saldo.")],
   "lbl":{"main":"Mesi fino a zero debito","rows":{"interest":"Interessi pagati","paid":"Totale pagato","date":"Zero debito stimato","never":"Mai estinguibile","mi":"Interessi mensili","need":"Alza la rata sopra"}}},
  "inflation":{"title":"Calcolatore inflazione — potere d'acquisto reale | CalcFin","h1":"Calcolatore inflazione",
   "meta":"Vedi cosa comprerà davvero il denaro di oggi in futuro a un dato tasso di inflazione. Semplice, veloce, privato.",
   "intro":"L'inflazione erode silenziosamente il potere d'acquisto. Inserisci un importo, un tasso medio e un numero di anni per vedere il valore reale.",
   "inputs":["Importo oggi ($)","Inflazione media (%)","Anni"],
   "how":["Con un'inflazione del 3 %, i prezzi raddoppiano circa ogni 24 anni (regola del 72: 72 ÷ tasso ≈ anni di raddoppio).",
     "Ecco perché i contanti nel cassetto perdono valore ogni anno — e perché contano gli investimenti che battono l'inflazione.",
     "Storicamente l'inflazione USA media è ~3 %, ma varia molto per decennio."],
   "formula":"Valore reale = Importo / (1 + inflazione)^anni",
   "faq":[("Quale tasso di inflazione usare?","La media USA a lungo termine è ~3 %. Per pianificare con prudenza 3–4 %; alcuni anni tra quasi 0 % e 9 %."),
     ("È la stessa cosa di un rendimento?","No — è il lato opposto: cosa fa l'inflazione ai contanti fermi. Confronta con il calcolatore di interesse composto."),
     ("Inflazione crescente modellabile?","Questo strumento usa un tasso medio fisso — approssima con la media del periodo.")],
   "lbl":{"main":"Potere d'acquisto reale","rows":{"nominal":"Importo nominale","lost":"Potere d'acquisto perso","pct":"Perdita in percentuale"}}},
  "roi":{"title":"Calcolatore ROI — rendimento totale e annualizzato | CalcFin","h1":"Calcolatore ROI",
   "meta":"Calcola il ritorno sull'investimento (ROI) e il rendimento annualizzato. Confronta gli investimenti in modo equo.",
   "intro":"Il ROI semplice dice quanto hai guadagnato; il ROI annualizzato dice quanto velocemente — ed è l'unico numero confrontabile tra investimenti.",
   "inputs":["Importo investito ($)","Valore finale ($)","Periodo di detenzione (anni)"],
   "how":["Il ROI da solo inganna: +50 % in 1 anno è ottimo, +50 % in 10 anni è mediocre. La figura annualizzata (CAGR) rende gli investimenti confrontabili.",
     "Il CAGR è il tasso annuo costante che porta dal costo al valore finale nello stesso periodo.",
     "Includi commissioni, tasse e dividendi nel valore finale per un quadro onesto."],
   "formula":"ROI = (Finale − Costo) / Costo × 100 %      CAGR = (Finale/Costo)^(1/anni) − 1",
   "faq":[("Che ROI è buono?","Dipende da rischio e durata. Le azioni rendono ~10 % nominale a lungo termine; il risparmio molto meno con molto meno rischio."),
     ("ROI o CAGR?","Il ROI è il guadagno totale in percentuale; il CAGR lo distribuisce per anno. Solo il CAGR permette confronti equi tra durate diverse."),
     ("Il ROI può essere negativo?","Sì — un valore finale sotto il costo dà ROI e CAGR negativi.")],
   "lbl":{"main":"ROI totale","rows":{"cagr":"Rendimento annualizzato (CAGR)","profit":"Profitto netto","multiple":"Multiple di crescita"}}},
  "retirement":{"title":"Calcolatore pensione — basterà il risparmio? | CalcFin","h1":"Calcolatore pensione",
   "meta":"Proietta i tuoi risparmi previdenziali da saldo attuale, versamenti, contributo datore di lavoro e rendimento. Gratis e privato.",
   "intro":"Proietta il tuo gruzzolo alla pensione da ciò che hai, ciò che aggiungi ogni mese (incluso il contributo del datore di lavoro) e un rendimento assunto.",
   "inputs":["Risparmi attuali ($)","Versamento mensile ($)","Contributo datore di lavoro ($)","Rendimento annuo (%)","Anni fino alla pensione"],
   "how":["Il contributo del datore di lavoro è denaro gratis — includilo nel versamento mensile; in una carriera può valere sei cifre.",
     "L'ultimo decennio di capitalizzazione di solito aggiunge gli importi maggiori — iniziare presto conta più di versare di più.",
     "Il risultato è nominale. Passalo al calcolatore di inflazione per vederlo in potere d'acquisto attuale."],
   "formula":"VF = Attuale·(1+r/n)^(nt) + Mensile·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Quale rendimento assumere?","Un portafoglio diversificato ha storicamente reso 7–8 % nominale. Pianificazione prudente: 5–6 %."),
     ("Include la pensione pubblica?","No — qui sono solo i tuoi investimenti. Le pensioni attese vanno calcolate a parte."),
     ("Quanto mi serve davvero?","Regola di partenza comune: 25× la spesa annuale prevista («regola del 4 %»), ma varia molto.")],
   "lbl":{"main":"Risparmi previdenziali previsti","rows":{"fv":"Dal risparmio attuale","fvm":"Dai versamenti","contrib":"Versato in totale","growth":"Interessi guadagnati"}}},
 }
},
"pt": {
 "name":"Português",
 "nav_home":"Todas as calculadoras","nav_privacy":"Privacidade","nav_about":"Sobre",
 "btn":"Calcular","related_h2":"Calculadoras relacionadas","how_h2":"Como funciona","faq_h2":"Perguntas frequentes",
 "home":{"title":"Calculadoras financeiras grátis — Juros, empréstimos, imóveis, poupança | CalcFin",
   "meta":"Calculadoras financeiras online grátis: juros compostos, prestação de empréstimo, financiamento, meta de poupança, cartão, inflação, ROI e aposentadoria. Privado, sem cadastro.",
   "h1":"Calculadoras financeiras grátis","sub":"Calculadoras rápidas e privadas que funcionam <b>inteiramente no seu navegador</b> — seus números nunca saem do dispositivo. Cada página mostra a fórmula exata.",
   "h2":"Sem cadastro. Sem coleta de dados. Só matemática.",
   "p1":"Cada calculadora do CalcFin roda localmente em JavaScript — seus dados são processados no seu próprio dispositivo e nunca enviados a servidor algum. Cada página documenta a fórmula exata, para você verificar a matemática em vez de confiar numa caixa preta.",
   "p2":"Os resultados são estimativas para planejamento e educação, não consultoria financeira."},
 "privacy":{"title":"Política de Privacidade | CalcFin","meta":"Política de privacidade do CalcFin — cálculos locais, cookies e publicidade.",
   "body":"""
  <h1>Política de Privacidade</h1>
  <p class="updated">Última atualização: 2 de outubro de 2026</p>
  <p>CalcFin («nós») oferece calculadoras financeiras gratuitas que funcionam <b>inteiramente no seu navegador</b>. Esta política explica quais dados são — e não são — coletados.</p>
  <h2>1. Seus dados</h2>
  <p><b>Nunca vemos seus dados nem seus resultados.</b> Cada cálculo acontece localmente no seu dispositivo. Nada é enviado, salvo ou registrado.</p>
  <h2>2. Registros do servidor</h2>
  <p>Nosso provedor de hospedagem (Cloudflare) registra automaticamente dados técnicos padrão — IP, tipo de navegador, URL, data — para segurança e desempenho, conforme a <a href="https://www.cloudflare.com/privacypolicy/">política de privacidade do Cloudflare</a>.</p>
  <h2>3. Cookies e publicidade</h2>
  <p>Planejamos exibir publicidade servida pelo Google AdSense. Terceiros, incluindo o Google, usam cookies para anúncios baseados em visitas anteriores. Desativáveis em <a href="https://www.google.com/settings/ads">Configurações de anúncios do Google</a>; bloquear cookies não afeta as calculadoras.</p>
  <h2>4. Não é consultoria financeira</h2>
  <p>Os resultados são estimativas matemáticas para educação e planejamento — não consultoria financeira.</p>
  <h2>5. Contato</h2>
  <p>Dúvidas: <b>liuyulong667@gmail.com</b>.</p>"""},
 "about":{"title":"Sobre o CalcFin | CalcFin","meta":"Sobre o CalcFin — calculadoras financeiras gratuitas no navegador com fórmulas transparentes.",
   "body":"""
  <h1>Sobre o CalcFin</h1>
  <p>CalcFin é uma coleção de calculadoras financeiras rápidas, gratuitas e sem rodeios. Cada calculadora funciona <b>inteiramente no seu navegador</b> — seus números nunca tocam um servidor — e cada página explica a fórmula por trás do resultado.</p>
  <h2>Por que o CalcFin existe</h2>
  <p>A maioria dos sites de calculadoras enterra a ferramenta sob publicidade, exige cadastro ou esconde a matemática. Nós fazemos o oposto: ferramentas limpas, fórmulas transparentes, estimativas honestas.</p>
  <h2>Princípios</h2>
  <ul><li><b>Local por padrão.</b> Seus dados nunca saem do dispositivo.</li>
  <li><b>Matemática transparente.</b> Cada página mostra a fórmula exata.</li>
  <li><b>Grátis significa grátis.</b> Sem cadastro, sem paywall, sem limites.</li></ul>
  <h2>Contato</h2>
  <p>Feedback e bugs: <b>liuyulong667@gmail.com</b>.</p>"""},
 "pages":{
  "compound-interest":{"title":"Calculadora de juros compostos — com aportes mensais | CalcFin","h1":"Calculadora de juros compostos",
   "meta":"Calculadora de juros compostos gratuita com aportes mensais. Veja como seu dinheiro cresce — fórmula explicada, no navegador.",
   "intro":"Veja como um valor inicial mais aportes mensais crescem com juros compostos. Ajuste a taxa e o prazo para comparar cenários na hora.",
   "inputs":["Valor inicial ($)","Taxa anual (%)","Anos","Aporte mensal ($)"],
   "how":["Juros compostos pagam juros sobre os juros. Com capitalização mensal à taxa anual r, o saldo cresce r/12 por mês.",
     "O primeiro termo é o valor inicial crescendo por todo o período; o segundo é o valor futuro de cada aporte mensal.",
     "O tempo importa mais que a taxa: dobrar os anos eleva quase ao quadrado o múltiplo de crescimento."],
   "formula":"VF = C(1+r/n)^(nt) + A · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("O aporte é no início ou no fim do mês?","Esta calculadora assume aportes no início do mês (anuidade antecipada) — por isso a fórmula inclui o fator (1+r/n) extra."),
     ("Inclui impostos ou inflação?","Não — os resultados são nominais. Para poder de compra real, use a Calculadora de inflação."),
     ("Que taxa usar?","Historicamente o mercado acionário dos EUA rende ~7–10 % ao ano antes da inflação — mas desempenho passado não garante o futuro.")],
   "lbl":{"main":"Valor futuro","rows":{"deposited":"Total aportado","interest":"Juros ganhos","multiple":"Múltiplo de crescimento"}}},
  "loan-payment":{"title":"Calculadora de prestação — parcela e juros totais | CalcFin","h1":"Calculadora de prestação",
   "meta":"Calcule a prestação mensal e os juros totais de qualquer empréstimo. Fórmula de amortização explicada — grátis e privado.",
   "intro":"Informe o valor, a taxa anual e o prazo para obter a prestação fixa mensal, os juros totais e o custo total.",
   "inputs":["Valor do empréstimo ($)","Taxa anual (%)","Prazo (anos)"],
   "how":["Empréstimos são amortizados: cada prestação inclui juros e principal.",
     "As primeiras parcelas são carregadas de juros — por isso amortizações antecipadas no início economizam mais.",
     "Com taxa 0 %, o principal se divide igualmente entre todas as parcelas."],
   "formula":"Prestação = P · r · (1+r)^n / ((1+r)^n − 1)   onde r = taxa mensal, n = número de parcelas",
   "faq":[("Funciona para veículos, pessoais, estudantis?","Sim — qualquer empréstimo a taxa fixa com amortização usa exatamente esta fórmula."),
     ("Por que meu banco mostra um número um pouco diferente?","Bancos adicionam taxas e seguros ou usam arredondamentos e contagem de dias ligeiramente diferentes."),
     ("Como pago menos juros no total?","Prazo menor, taxa menor ou amortizações antecipadas — compare os juros totais entre cenários.")],
   "lbl":{"main":"Prestação mensal","rows":{"interest":"Juros totais","paid":"Total pago","n":"Número de parcelas"}}},
  "mortgage-payment":{"title":"Calculadora de financiamento imobiliário — parcela, imposto e seguro | CalcFin","h1":"Calculadora de financiamento imobiliário",
   "meta":"Estime sua parcela mensal real do imóvel incluindo IPTU, seguro e condomínio. Grátis e privado.",
   "intro":"A parcela do imóvel é mais que principal e juros. Some IPTU, seguro e condomínio para ver o número que realmente sai da sua conta todo mês.",
   "inputs":["Preço do imóvel ($)","Entrada ($)","Taxa (%)","Prazo (anos)","IPTU anual ($)","Seguro anual ($)","Condomínio mensal ($)"],
   "how":["Os bancos citam apenas principal e juros, mas a parcela real inclui IPTU, seguro e condomínio.",
     "Regra prática: planeje 1–2 % do valor do imóvel por ano em impostos e seguro, embora varie muito por região.",
     "Entrada de 20 % geralmente elimina o seguro PMI da equação."],
   "formula":"Parcela = C+J + (IPTU/12) + (Seguro/12) + Condomínio",
   "faq":[("O PMI está incluído?","Não — adicione manualmente no campo condomínio se a entrada for menor que 20 %."),
     ("O imposto é preciso para minha região?","As alíquotas vão de menos de 0,5 % a mais de 2 % do valor por ano — verifique a sua alíquota local."),
     ("15 ou 30 anos?","15 anos: parcela maior mas juros totais bem menores — compare os dois cenários.")],
   "lbl":{"main":"Parcela mensal total","rows":{"pi":"Principal e juros","tax":"IPTU (mensal)","ins":"Seguro (mensal)","hoa":"Condomínio (mensal)","loan":"Valor financiado"}}},
  "savings-goal":{"title":"Calculadora de meta de poupança — quanto poupar por mês | CalcFin","h1":"Calculadora de meta de poupança",
   "meta":"Calcule o aporte mensal necessário para atingir um valor em uma data, com juros compostos. Grátis e privado.",
   "intro":"Tem uma meta e um prazo? Isto mostra o aporte mensal exato para chegar lá, assumindo juros compostos.",
   "inputs":["Meta ($)","Prazo (anos)","Rendimento anual (%)","Já poupado ($)"],
   "how":["Primeiro, suas economias atuais são projetadas com juros compostos até a data limite.",
     "A diferença entre esse valor futuro e a meta é preenchida pelos aportes mensais.",
     "Rendimento maior reduz o aporte — mas não planeje com taxas que não possa garantir."],
   "formula":"A = (Meta − VF_atual) · r / ((1+r)^n − 1)   onde r = taxa mensal, n = meses",
   "faq":[("E se eu não puder arcar com o aporte?","Estique o prazo, reduza a meta ou busque melhor rendimento — teste cada alavanca na hora."),
     ("O aporte é mensal ou anual?","Mensal, no fim de cada mês."),
     ("Serve para entrada de imóvel?","Sim — é um uso muito comum.")],
   "lbl":{"main":"Aporte mensal necessário","rows":{"fv":"Valor futuro do saldo atual","gap":"Diferença a cobrir","contrib":"Total aportado"}}},
  "credit-card-payoff":{"title":"Calculadora de quitação de cartão — meses até zero | CalcFin","h1":"Calculadora de quitação de cartão",
   "meta":"Quanto tempo leva para quitar uma dívida de cartão com parcelas fixas, e quanto de juros você paga. Grátis.",
   "intro":"Parcelas fixas sobre dívida de cartão: veja exatamente quantos meses até estar livre de dívida e quanto de juros o banco cobra no caminho.",
   "inputs":["Saldo ($)","Taxa anual (%)","Parcela mensal ($)"],
   "how":["Os pagamentos mínimos são desenhados para te manter endividado: a 22,9 % ao ano, os juros sozinhos comem a maior parte de uma parcela pequena.",
     "Se sua parcela é menor que os juros do primeiro mês, o saldo cresce para sempre — a calculadora avisa em vez de iterar eternamente.",
     "Arredondar a parcela um pouco para cima corta meses inteiros."],
   "formula":"Cada mês: juros = saldo × taxa/12, depois saldo = saldo + juros − parcela, repetido até zero",
   "faq":[("Qual parcela para $8.000 a 22,9 %?","Só os juros são ~152 $/mês. Com 300 $/mês: cerca de 3 anos; com 500 $/mês: menos de 2 anos e milhares de economia."),
     ("Assume que paro de usar o cartão?","Sim — novos gastos não são modelados. Some manualmente ao saldo se precisar."),
     ("Uma transferência de saldo ajudaria?","Se a nova taxa for menor, sim — modele com a taxa menor mais a tarifa dentro do saldo.")],
   "lbl":{"main":"Meses até quitar","rows":{"interest":"Juros pagos","paid":"Total pago","date":"Sem dívida estimado","never":"Nunca quita","mi":"Juros mensais","need":"Aumentar a parcela acima de"}}},
  "inflation":{"title":"Calculadora de inflação — poder de compra real | CalcFin","h1":"Calculadora de inflação",
   "meta":"Veja o que o dinheiro de hoje realmente comprará no futuro a uma taxa de inflação. Simples, rápido, privado.",
   "intro":"A inflação encolhe silenciosamente o poder de compra. Informe um valor, uma taxa média e anos para ver o que realmente restará.",
   "inputs":["Valor hoje ($)","Inflação média (%)","Anos"],
   "how":["Com inflação de 3 %, os preços dobram aproximadamente a cada 24 anos (regra do 72: 72 ÷ taxa ≈ anos para dobrar).",
     "Por isso dinheiro parado perde valor todo ano — e por que importam investimentos que vencem a inflação.",
     "Historicamente a inflação dos EUA média ~3 %, mas varia muito por década."],
   "formula":"Valor real = Valor / (1 + inflação)^anos",
   "faq":[("Que taxa de inflação usar?","A média de longo prazo dos EUA é ~3 %. Para planejamento conservador use 3–4 %; alguns anos variaram de quase 0 % a 9 %."),
     ("É o mesmo que rendimento?","Não — é o lado oposto: o que a inflação faz com dinheiro parado. Compare com a calculadora de juros compostos."),
     ("Inflação crescente modelável?","Esta ferramenta usa taxa média fixa — aproxime com a média do período.")],
   "lbl":{"main":"Poder de compra real","rows":{"nominal":"Valor nominal","lost":"Poder de compra perdido","pct":"Perda em porcentagem"}}},
  "roi":{"title":"Calculadora de ROI — retorno total e anualizado | CalcFin","h1":"Calculadora de ROI",
   "meta":"Calcule o retorno sobre o investimento (ROI) e a taxa anualizada. Compare investimentos de forma justa.",
   "intro":"O ROI simples diz quanto você ganhou; o ROI anualizado diz quão rápido — e esse é o número comparável entre investimentos.",
   "inputs":["Valor investido ($)","Valor final ($)","Período de posse (anos)"],
   "how":["O ROI sozinho engana: +50 % em 1 ano é excelente, +50 % em 10 anos é medíocre. A taxa anualizada (CAGR) torna investimentos comparáveis.",
     "O CAGR é a taxa anual constante que levaria do custo ao valor final no mesmo período.",
     "Inclua taxas, impostos e dividendos no valor final para um quadro honesto."],
   "formula":"ROI = (Final − Custo) / Custo × 100 %      CAGR = (Final/Custo)^(1/anos) − 1",
   "faq":[("Que ROI é bom?","Depende do risco e do prazo. Ações rendem ~10 % nominal a longo prazo; poupança bem menos com bem menos risco."),
     ("ROI ou CAGR?","O ROI é o ganho total em percentual; o CAGR distribui por ano. Só o CAGR permite comparação justa entre prazos."),
     ("O ROI pode ser negativo?","Sim — valor final abaixo do custo dá ROI e CAGR negativos.")],
   "lbl":{"main":"ROI total","rows":{"cagr":"Retorno anualizado (CAGR)","profit":"Lucro líquido","multiple":"Múltiplo de crescimento"}}},
  "retirement":{"title":"Calculadora de aposentadoria — vai dar para viver? | CalcFin","h1":"Calculadora de aposentadoria",
   "meta":"Projete sua poupança de aposentadoria a partir do saldo atual, aportes, contribuição da empresa e rendimento. Grátis e privado.",
   "intro":"Projete seu patrimônio na aposentadoria a partir do que você tem, do que adiciona por mês (incluindo a contribuição da empresa) e um rendimento assumido.",
   "inputs":["Poupança atual ($)","Aporte mensal ($)","Contribuição da empresa ($)","Rendimento anual (%)","Anos até aposentar"],
   "how":["A contribuição da empresa é dinheiro de graça — inclua no aporte mensal; numa carreira pode somar seis dígitos.",
     "A última década de capitalização costuma trazer os maiores valores — começar cedo importa mais que aportar mais.",
     "O resultado é nominal. Passe pela calculadora de inflação para ver em poder de compra atual."],
   "formula":"VF = Atual·(1+r/n)^(nt) + Mensal·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
   "faq":[("Que rendimento assumir?","Uma carteira diversificada rendeu historicamente 7–8 % nominal. Planejamento conservador: 5–6 %."),
     ("Inclui a previdência pública?","Não — aqui são só seus investimentos. Aposentadorias esperadas entram à parte."),
     ("Quanto preciso de fato?","Regra inicial comum: 25× seu gasto anual previsto («regra dos 4 %»), mas varia muito de pessoa para pessoa.")],
   "lbl":{"main":"Poupança projetada para aposentadoria","rows":{"fv":"Do saldo atual","fvm":"Dos aportes","contrib":"Total aportado","growth":"Juros ganhos"}}},
 }
},
}
