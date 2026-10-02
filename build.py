# -*- coding: utf-8 -*-
"""CalcFin — 金融计算器矩阵生成器(4 语言 + 暗黑模式)
运行: python build.py → index + 8 计算器 × 4 语言 + privacy/about × 4 语言 + sitemap.xml
"""
import sys
from pathlib import Path
from i18n import TR, EN_LBL

sys.stdout.reconfigure(encoding="utf-8")
BASE_URL = "https://calcfin-vpg.pages.dev"
LANGS = ["en", "de", "fr", "es"]

CSS = """
  :root { --brand:#0e7490; --brand-soft:#ecfeff; --bg:#f8fafc; --card:#fff; --text:#0f172a; --muted:#475569; --faint:#64748b; --border:#e2e8f0; --shadow:rgba(0,0,0,.07); --ok:#067647; --ok-bg:#ecfdf5; }
  [data-theme="dark"] { --brand:#22d3ee; --brand-soft:#0c2a31; --bg:#0b1220; --card:#111a2c; --text:#e6edf7; --muted:#9fb0c7; --faint:#7c8aa0; --border:#1e293b; --shadow:rgba(0,0,0,.45); --ok:#34d399; --ok-bg:#0c2a22; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif; color:var(--text); background:var(--bg); line-height:1.7; }
  header { position:sticky; top:0; z-index:100; background:var(--card); border-bottom:1px solid var(--border); padding:12px 24px; box-shadow:0 1px 10px var(--shadow); }
  .header-inner { max-width:960px; margin:0 auto; display:flex; align-items:center; justify-content:space-between; }
  .logo { font-weight:800; font-size:20px; color:var(--brand); text-decoration:none; white-space:nowrap; }
  .nav-links { display:flex; align-items:center; gap:22px; }
  .nav-links a { color:var(--muted); text-decoration:none; font-size:14px; white-space:nowrap; }
  .nav-links a:hover { color:var(--brand); }
  .lang { position:relative; }
  #langBtn { display:flex; align-items:center; gap:6px; background:none; border:0; padding:6px 4px; color:var(--text); font-size:14px; font-weight:700; cursor:pointer; white-space:nowrap; }
  #langBtn:hover { color:var(--brand); }
  #langBtn .chev { width:15px; height:15px; fill:none; stroke:currentColor; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round; transition:transform .2s; }
  .lang.open #langBtn .chev { transform:rotate(180deg); }
  .lang-menu { display:none; position:absolute; right:0; top:calc(100% + 8px); background:var(--card); border:1px solid var(--border); border-radius:12px; box-shadow:0 8px 24px var(--shadow); min-width:170px; padding:6px; z-index:60; }
  .lang.open .lang-menu { display:block; }
  .lang-menu a { display:block; padding:8px 14px; border-radius:8px; color:var(--text); text-decoration:none; font-size:14px; }
  .lang-menu a:hover { background:var(--brand-soft); }
  .lang-menu a.cur { color:var(--brand); font-weight:700; }
  .lang-menu a.cur::after { content:" ✓"; }
  #themeBtn { display:flex; align-items:center; justify-content:center; background:var(--card); border:1px solid var(--border); border-radius:10px; width:36px; height:36px; cursor:pointer; color:var(--muted); }
  #themeBtn:hover { color:var(--brand); border-color:var(--brand); }
  #themeBtn svg { width:17px; height:17px; fill:none; stroke:currentColor; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
  #themeBtn .icon-sun { display:none; }
  [data-theme="dark"] #themeBtn .icon-moon { display:none; }
  [data-theme="dark"] #themeBtn .icon-sun { display:block; }
  main { max-width:960px; margin:0 auto; padding:32px 20px 64px; }
  h1 { font-size:28px; margin-bottom:8px; }
  h2 { font-size:20px; margin:30px 0 10px; }
  .sub { color:var(--muted); margin-bottom:24px; font-size:16px; }
  .calc { background:var(--card); border:1px solid var(--border); border-radius:14px; padding:22px; box-shadow:0 1px 4px var(--shadow); }
  .calc label { display:block; font-size:13px; color:var(--muted); margin:12px 0 4px; font-weight:600; }
  .calc input { width:100%; padding:10px 12px; border:1px solid var(--border); border-radius:8px; background:var(--bg); color:var(--text); font-size:15px; }
  .calc input:focus { outline:2px solid var(--brand); border-color:transparent; }
  .btn { margin-top:16px; width:100%; background:var(--brand); color:#fff; border:0; border-radius:10px; padding:12px; font-size:16px; font-weight:700; cursor:pointer; }
  .btn:hover { filter:brightness(1.1); }
  .result { display:none; margin-top:18px; background:var(--ok-bg); border-radius:10px; padding:16px; }
  .result .big { font-size:26px; font-weight:800; color:var(--ok); }
  .result .lbl { font-size:13px; color:var(--muted); }
  .result table { width:100%; margin-top:10px; font-size:14px; border-collapse:collapse; }
  .result td { padding:4px 0; color:var(--muted); }
  .result td:last-child { text-align:right; color:var(--text); font-weight:600; }
  p, li { color:var(--muted); font-size:15px; margin-bottom:10px; }
  ul { padding-left:22px; }
  .formula { background:var(--card); border:1px solid var(--border); border-radius:10px; padding:14px 18px; font-family:Consolas,monospace; font-size:14px; color:var(--text); margin:12px 0; overflow-x:auto; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); gap:14px; margin-top:16px; }
  .grid a { background:var(--card); border:1px solid var(--border); border-radius:12px; padding:16px; text-decoration:none; color:var(--text); font-weight:600; font-size:14px; box-shadow:0 1px 3px var(--shadow); }
  .grid a:hover { border-color:var(--brand); color:var(--brand); }
  .grid a span { display:block; font-weight:400; color:var(--muted); font-size:13px; margin-top:4px; }
  footer { text-align:center; color:var(--faint); font-size:13px; padding:28px; border-top:1px solid var(--border); margin-top:40px; }
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>try{const t=localStorage.getItem('theme');if(t==='dark'||(!t&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.dataset.theme='dark';}catch(e){}</script>
<title>__TITLE__</title>
<meta name="description" content="__META__">
<link rel="canonical" href="__URL__">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CalcFin">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__META__">
<meta property="og:url" content="__URL__">
<meta name="twitter:card" content="summary">
__HREFLANGS__
<script type="application/ld+json">__LD_WEBAPP__</script>
__LD_FAQ__
<style>__CSS__</style>
</head>
<body>
<header><div class="header-inner">
  <a class="logo" href="__HOME_HREF__">💵 CalcFin</a>
  <nav class="nav-links">
    <a href="__PRIVACY_HREF__">__NAV_PRIVACY__</a><a href="__ABOUT_HREF__">__NAV_ABOUT__</a>
    <button id="themeBtn" title="Toggle dark mode" aria-label="Toggle dark mode">
      <svg class="icon-moon" viewBox="0 0 24 24"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
    </button>
    __LANGSWITCH__
  </nav>
</div></header>
<main>
__MAIN__
</main>
<footer>__FOOTER__</footer>
<script>
try {
const themeBtn = document.getElementById('themeBtn');
themeBtn.addEventListener('click', function () {
  const dark = document.documentElement.dataset.theme === 'dark';
  if (dark) delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme = 'dark';
  try { localStorage.setItem('theme', dark ? 'light' : 'dark'); } catch (e) {}
});
const langBox = document.querySelector('.lang');
if (langBox) {
  document.getElementById('langBtn').addEventListener('click', function (e) { e.stopPropagation(); langBox.classList.toggle('open'); });
  document.addEventListener('click', function (e) { if (!langBox.contains(e.target)) langBox.classList.remove('open'); });
}
} catch (e) {}
</script>
</body>
</html>
"""

PRIVACY_BODY = """
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: October 2, 2026</p>
  <p>CalcFin ("we") provides free financial calculators that run <b>entirely in your browser</b>. This policy explains what data is — and is not — collected.</p>
  <h2>1. Your numbers and inputs</h2>
  <p><b>We never see your inputs or results.</b> Every calculation happens locally on your device. Nothing you type is sent to any server, stored, or logged.</p>
  <h2>2. Server logs</h2>
  <p>Our hosting provider (Cloudflare) automatically records standard technical request data — IP address, browser type, requested URL, timestamp — for security and performance. This data is governed by <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare's privacy policy</a> and is not used to identify individual visitors.</p>
  <h2>3. Cookies and advertising</h2>
  <p>We plan to display advertising served by Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on prior visits. You may opt out of personalized advertising via <a href="https://www.google.com/settings/ads">Google Ads Settings</a>, or control cookies in your browser — blocking cookies does not affect the calculators.</p>
  <h2>4. Local storage</h2>
  <p>We may use local storage to remember preferences such as dark mode. This stays on your device.</p>
  <h2>5. Not financial advice</h2>
  <p>Results are mathematical estimates for education and planning. They are not financial advice — consult a qualified professional for decisions.</p>
  <h2>6. Contact</h2>
  <p>Questions: <b>liuyulong667@gmail.com</b>.</p>
"""

ABOUT_BODY = """
  <h1>About CalcFin</h1>
  <p>CalcFin is a collection of fast, free, no-nonsense financial calculators. Every calculator runs <b>entirely in your browser</b> — your numbers never touch a server — and every page explains the formula behind the result.</p>
  <h2>Why CalcFin exists</h2>
  <p>Most finance calculator sites bury the tool under ads, require signups, or hide the math. We do the opposite: clean tools, transparent formulas, honest estimates.</p>
  <h2>Principles</h2>
  <ul>
    <li><b>Local by default.</b> No inputs ever leave your device.</li>
    <li><b>Transparent math.</b> Every page shows the exact formula used.</li>
    <li><b>Free means free.</b> No signup, no paywall, no limits.</li>
  </ul>
  <h2>Not financial advice</h2>
  <p>Results are mathematical estimates for education and planning — consult a qualified professional for decisions.</p>
  <h2>Contact</h2>
  <p>Feedback and bug reports: <b>liuyulong667@gmail.com</b>.</p>
"""

FOOTERS = {
 "en": "CalcFin — free financial calculators. Results are estimates, not financial advice. © 2026",
 "de": "CalcFin — kostenlose Finanzrechner. Ergebnisse sind Schätzungen, keine Finanzberatung. © 2026",
 "fr": "CalcFin — calculateurs financiers gratuits. Les résultats sont des estimations, pas des conseils financiers. © 2026",
 "es": "CalcFin — calculadoras financieras gratis. Los resultados son estimaciones, no asesoría financiera. © 2026",
}

# ---------------- 计算器定义(compute 的 out 调用已 key 化) ----------------
CALCS = [
dict(slug="compound-interest", nav="Compound interest",
 title="Compound Interest Calculator — With Monthly Contributions | CalcFin",
 h1="Compound Interest Calculator",
 meta="Free compound interest calculator with monthly contributions. See how your money grows over time — formula explained, runs in your browser.",
 intro="See how a lump sum plus regular monthly contributions grows with compound interest. Adjust the rate and timeline to compare scenarios instantly.",
 inputs=[("principal","Initial amount ($)","10000"),("rate","Annual interest rate (%)","7"),
         ("years","Years to grow","10"),("monthly","Monthly contribution ($)","200")],
 compute="""const p=+principal.value, r=+rate.value/100, y=+years.value, m=+monthly.value;
const n=12, g=Math.pow(1+r/n, n*y);
const fvP=p*g, fvM=m*((g-1)/(r/n))*(1+r/n);
const total=p+m*12*y, interest=fvP+fvM-total;
out('__main__', F(fvP+fvM), [[L.rows.deposited, F(total)], [L.rows.interest, F(interest)], [L.rows.multiple, (fvP+fvM/Math.max(total,1)).toFixed(2)+'x']]);""",
 formula="FV = P(1+r/n)^(nt) + PMT · [ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
 how=["Compound interest pays interest on your interest. Compounding monthly at an annual rate r means each month grows your balance by r/12.",
      "The first term is your initial lump sum growing for the whole period; the second is the future value of every monthly contribution.",
      "Time matters more than rate: doubling years roughly squares the growth multiple on the lump sum."],
 faq=[("Is the contribution added at the start or end of each month?","This calculator assumes contributions are made at the start of each month (annuity due), which is why the contribution formula includes the extra (1+r/n) factor."),
      ("Does it account for taxes or inflation?","No — results are nominal. For real purchasing power, run the result through the Inflation Calculator."),
      ("What rate should I use?","Historical US stock market returns average roughly 7–10% per year before inflation, but past performance never guarantees future results.")]),

dict(slug="loan-payment", nav="Loan payment",
 title="Loan Payment Calculator — Monthly Payment & Total Interest | CalcFin",
 h1="Loan Payment Calculator",
 meta="Calculate the monthly payment and total interest for any loan. Amortization math explained — free, private, in your browser.",
 intro="Enter a loan amount, annual rate and term to get the fixed monthly payment, total interest, and total cost.",
 inputs=[("amount","Loan amount ($)","25000"),("rate","Annual interest rate (%)","6.5"),("years","Term (years)","5")],
 compute="""const p=+amount.value, r=+rate.value/100/12, n=+years.value*12;
if (r===0) { out('__main__', F(p/n), [[L.rows.interest, F(0)], [L.rows.paid, F(p)]]); }
else { const pay=p*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);
const total=pay*n, interest=total-p;
out('__main__', F(pay), [[L.rows.interest, F(interest)], [L.rows.paid, F(total)], [L.rows.n, String(n)]]); }""",
 formula="Payment = P · r · (1+r)^n / ((1+r)^n − 1)   where r = monthly rate, n = number of months",
 how=["Lenders amortize loans: every payment is partly interest and partly principal.",
      "Early payments are interest-heavy — that's why extra principal payments early in the loan save the most interest.",
      "A 0% rate loan divides the principal evenly across all payments."],
 faq=[("Does this work for car loans, personal loans and student loans?","Yes — any fixed-rate, fully amortizing loan uses this exact formula."),
      ("Why is my lender's number slightly different?","Lenders may add fees, insurance, or use slightly different rounding or day-count conventions."),
      ("How do I pay less interest overall?","Shorten the term, negotiate a lower rate, or make extra principal payments — use this calculator to compare total interest between scenarios.")]),

dict(slug="mortgage-payment", nav="Mortgage payment",
 title="Mortgage Payment Calculator — P&I, Tax & Insurance | CalcFin",
 h1="Mortgage Payment Calculator",
 meta="Estimate your true monthly mortgage payment including property tax, insurance and HOA. Free and private.",
 intro="A mortgage payment is more than principal and interest. Add tax, insurance and HOA to see the number that actually leaves your account each month.",
 inputs=[("price","Home price ($)","400000"),("down","Down payment ($)","80000"),
         ("rate","Interest rate (%)","6.2"),("years","Term (years)","30"),
         ("tax","Property tax per year ($)","4200"),("ins","Insurance per year ($)","1500"),("hoa","HOA per month ($)","0")],
 compute="""const p=+price.value-+down.value, r=+rate.value/100/12, n=+years.value*12;
const pi=r===0 ? p/n : p*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);
const tax=+tax.value/12, ins=+ins.value/12, hoa=+hoa.value;
const total=pi+tax+ins+hoa;
out('__main__', F(total), [[L.rows.pi, F(pi)], [L.rows.tax, F(tax)], [L.rows.ins, F(ins)], [L.rows.hoa, F(hoa)], [L.rows.loan, F(p)]]);""",
 formula="Payment = P&I + (Tax/12) + (Insurance/12) + HOA,  where P&I uses the amortization formula",
 how=["Lenders quote only principal and interest (P&I), but your real payment includes escrowed taxes, insurance and any HOA fees.",
      "A common rule of thumb: budget 1–2% of home value per year for taxes and insurance combined, though it varies a lot by location.",
      "Putting 20% down usually removes private mortgage insurance (PMI) from the equation."],
 faq=[("Does this include PMI?","No — add PMI manually to the HOA field if your down payment is under 20%."),
      ("Is the tax figure accurate for my area?","Property tax rates range from under 0.5% to over 2% of home value per year depending on the state. Check your local rate for precision."),
      ("Should I choose a 15-year or 30-year term?","A 15-year term has a higher payment but far less total interest — run both through this calculator to see the difference.")]),

dict(slug="savings-goal", nav="Savings goal",
 title="Savings Goal Calculator — How Much to Save Each Month | CalcFin",
 h1="Savings Goal Calculator",
 meta="Work out the monthly saving needed to reach a target amount by a deadline, with compound interest included. Free and private.",
 intro="Have a target and a deadline? This tells you the exact monthly contribution needed to get there, assuming compound growth.",
 inputs=[("goal","Savings goal ($)","50000"),("years","Time to reach (years)","5"),
         ("rate","Annual return (%)","5"),("current","Already saved ($)","5000")],
 compute="""const g=+goal.value, r=+rate.value/100/12, n=+years.value*12, cur=+current.value;
const fvCur=cur*Math.pow(1+r, n);
const gap=Math.max(0, g-fvCur);
const pmt=r===0 ? gap/n : gap*r/(Math.pow(1+r,n)-1);
out('__main__', F(pmt), [[L.rows.fv, F(fvCur)], [L.rows.gap, F(gap)], [L.rows.contrib, F(pmt*n)]]);""",
 formula="PMT = (Goal − FV_current) · r / ((1+r)^n − 1)   where r = monthly rate, n = months",
 how=["First, your existing savings are projected forward with compound growth — what they'll be worth by your deadline.",
      "The gap between that future value and your goal is what monthly contributions must fill.",
      "A higher assumed return lowers the required payment, but never plan on rates you can't rely on."],
 faq=[("What if I can't afford the required monthly amount?","Extend the deadline, lower the goal, or look for a better rate — this calculator lets you test each lever instantly."),
      ("Is the contribution made monthly or annually?","Monthly, at the end of each month."),
      ("Can I use this for a house deposit?","Yes — it's commonly used for house down-payment planning.")]),

dict(slug="credit-card-payoff", nav="Credit card payoff",
 title="Credit Card Payoff Calculator — Months to Debt-Free | CalcFin",
 h1="Credit Card Payoff Calculator",
 meta="Find out how long it takes to pay off credit card debt with fixed monthly payments, and how much interest you'll pay. Free.",
 intro="Fixed monthly payments on credit card debt: see exactly how many months until you're debt-free and how much interest the bank collects along the way.",
 inputs=[("balance","Card balance ($)","8000"),("apr","Annual APR (%)","22.9"),("pay","Monthly payment ($)","300")],
 compute="""const b=+balance.value, r=+apr.value/100/12, p=+pay.value;
if (p <= b*r) { out('never', '—', [[L.rows.mi, F(b*r)], [L.rows.need, F(Math.ceil(b*r)+1)]]); }
else { let bal=b, months=0, interest=0;
while (bal>0 && months<1200) { const i=bal*r; interest+=i; bal=bal+i-p; months++; }
out('__main__', String(months), [[L.rows.interest, F(interest)], [L.rows.paid, F(b+interest)], [L.rows.date, months]]); }""",
 formula="Each month: interest = balance × APR/12, then balance = balance + interest − payment, repeated until zero",
 how=["Minimum payments are designed to keep you in debt: at 22.9% APR, interest alone eats most of a small payment.",
      "If your payment is below the first month's interest, the balance grows forever — the calculator flags this instead of looping forever.",
      "Rounding the payment up even slightly can cut months off the payoff."],
 faq=[("What's a good monthly payment for $8,000 at 22.9%?","The minimum interest is about $152/month. Paying $300 takes roughly 3 years; paying $500 cuts it under 2 years and saves thousands."),
      ("Does this assume I stop using the card?","Yes — no new spending is modeled. Add new spending to the balance manually if needed."),
      ("Would a balance transfer help?","If the transfer APR is lower, yes — model it by entering the lower APR and adding any transfer fee to the balance.")]),

dict(slug="inflation", nav="Inflation",
 title="Inflation Calculator — Real Purchasing Power of Money | CalcFin",
 h1="Inflation Calculator",
 meta="See what today's money will actually buy in the future at a given inflation rate. Simple, fast, private.",
 intro="Inflation quietly shrinks purchasing power. Enter an amount, an average inflation rate and a number of years to see what it will really be worth.",
 inputs=[("amount","Amount today ($)","100000"),("rate","Average inflation rate (%)","3"),("years","Years","20")],
 compute="""const a=+amount.value, r=+rate.value/100, y=+years.value;
const real=a/Math.pow(1+r, y);
out('__main__', F(real), [[L.rows.nominal, F(a)], [L.rows.lost, F(a-real)], [L.rows.pct, ((1-1/Math.pow(1+r,y))*100).toFixed(1)+'%']]);""",
 formula="Real value = Amount / (1 + inflation)^years",
 how=["At 3% inflation, prices double roughly every 24 years (rule of 72: 72 ÷ rate ≈ doubling years).",
      "This is why cash under the mattress loses value every year, and why investments that beat inflation matter.",
      "For US history, long-run inflation has averaged around 3%, but it varies a lot by decade."],
 faq=[("What inflation rate should I use?","Long-run US average is about 3%. For conservative planning use 3–4%; recent years have ranged from near 0% to 9%."),
      ("Is this the same as investment returns?","No — this is the opposite side: it shows what inflation does to idle cash. Combine with the Compound Interest Calculator to compare."),
      ("Can I model rising inflation?","This tool uses a flat average rate. For scenarios with changing rates, use the average over the period as an approximation.")]),

dict(slug="roi", nav="ROI",
 title="ROI Calculator — Return on Investment with Annualized Rate | CalcFin",
 h1="ROI Calculator",
 meta="Calculate return on investment (ROI) and the annualized return rate. Understand the real performance of any investment.",
 intro="Simple ROI tells you how much you made; annualized ROI tells you how fast — and that's the number you can actually compare across investments.",
 inputs=[("cost","Amount invested ($)","10000"),("value","Final value ($)","16000"),("years","Holding period (years)","3")],
 compute="""const c=+cost.value, v=+value.value, y=Math.max(0.01, +years.value);
const roi=(v-c)/c*100, annual=(Math.pow(v/c, 1/y)-1)*100;
out('__main__', roi.toFixed(2) + '%', [[L.rows.cagr, annual.toFixed(2) + '%'], [L.rows.profit, F(v-c)], [L.rows.multiple, (v/c).toFixed(2)+'x']]);""",
 formula="ROI = (Final − Cost) / Cost × 100%      CAGR = (Final/Cost)^(1/years) − 1",
 how=["ROI alone can mislead: +50% in 1 year is excellent, +50% in 10 years is mediocre. The annualized figure (CAGR) makes different investments comparable.",
      "CAGR is the constant yearly rate that would take you from cost to final value in the same period.",
      "Remember to include fees, taxes and dividends in the final value for an honest picture."],
 faq=[("What is a good ROI?","It depends on risk and timeframe. Long-run stock averages are ~10% nominal; savings accounts are far lower with far less risk."),
      ("What's the difference between ROI and CAGR?","ROI is total percentage gain; CAGR spreads it per year. Only CAGR allows fair comparison across different holding periods."),
      ("Can ROI be negative?","Yes — a final value below cost gives negative ROI and negative CAGR.")]),

dict(slug="retirement", nav="Retirement savings",
 title="Retirement Savings Calculator — Will You Have Enough? | CalcFin",
 h1="Retirement Savings Calculator",
 meta="Project your retirement savings from current balance, monthly contributions, employer match and growth. Free and private.",
 intro="Project your nest egg at retirement from what you have, what you add each month (including employer match) and an assumed growth rate.",
 inputs=[("current","Current savings ($)","60000"),("monthly","Monthly contribution ($)","600"),
         ("match","Employer match / extra ($)","150"),("rate","Annual return (%)","7"),
         ("years","Years until retirement","25")],
 compute="""const c=+current.value, m=+monthly.value+ +match.value, r=+rate.value/100, y=+years.value;
const n=12, g=Math.pow(1+r/n, n*y);
const fv=c*g, fvm=m*((g-1)/(r/n))*(1+r/n), total=fv+fvm;
out('__main__', F(total), [[L.rows.fv, F(fv)], [L.rows.fvm, F(fvm)], [L.rows.contrib, F(c+m*12*y)], [L.rows.growth, F(total-c-m*12*y)]]);""",
 formula="FV = Current·(1+r/n)^(nt) + Monthly·[ ((1+r/n)^(nt) − 1) / (r/n) ] × (1+r/n)",
 how=["Employer match is free money — include it in your monthly contribution; it can add six figures over a career.",
      "The last decade of compounding usually adds the biggest dollar amounts, which is why starting early matters more than contributing more.",
      "This projects nominal dollars. Run the result through the Inflation Calculator to see it in today's purchasing power."],
 faq=[("What return rate should I assume?","A diversified portfolio historically returned 7–8% nominal. Conservative planning uses 5–6%."),
      ("Does this include Social Security or a pension?","No — this is only your own investments. Add expected pension income separately in your planning."),
      ("How much do I actually need?","A common starting rule is 25× your expected annual spending (the '4% rule'), but personal circumstances vary a lot.")]),
]

LD_FAQ_T = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[__ENTITIES__]}'
LD_WEBAPP_T = '{"@context":"https://schema.org","@type":"WebApplication","name":"__NAME__","url":"__URL__","applicationCategory":"FinanceApplication","operatingSystem":"Any","browserRequirements":"Requires JavaScript","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"description":"__META__"}'

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def page_file(base, lang):
    return (base + ".html") if lang == "en" else (base + "-" + lang + ".html")

def decls_of(c):
    return "\n  ".join("const " + i[0] + " = g('" + i[0] + "');" for i in c["inputs"])

def calc_body(c, tr, lang, lbl_json):
    tp = (tr.get("pages") or {}).get(c["slug"]) if tr else None
    btn = tr["btn"] if tr else "Calculate"
    how_h2 = tr["how_h2"] if tr else "How it works"
    faq_h2 = tr["faq_h2"] if tr else "FAQ"
    rel_h2 = tr["related_h2"] if tr else "Related calculators"
    formula = tp["formula"] if tp else c["formula"]
    how_src = tp["how"] if tp else c["how"]
    faq_src = tp["faq"] if tp else c["faq"]
    h1 = tp["h1"] if tp else c["h1"]
    intro = tp["intro"] if tp else c["intro"]
    inputs = "".join(
        '<label for="' + i[0] + '">' + (tp["inputs"][k] if tp else i[1]) + '</label>\n    '
        + '<input type="number" step="any" id="' + i[0] + '" value="' + i[2] + '">'
        for k, i in enumerate(c["inputs"]))
    how = "".join("<li>" + x + "</li>" for x in how_src)
    faq = "".join('<p><b>' + esc(q) + '</b> ' + esc(a) + '</p>' for q, a in faq_src)
    related = "".join(
        '<a href="/' + o["slug"] + ('' if lang == "en" else '-' + lang) + '.html">'
        + ((tr.get("pages") or {}).get(o["slug"], {}).get("h1", o["nav"]) if tr else o["nav"])
        + '</a>' for o in CALCS if o["slug"] != c["slug"])
    return """
  <h1>""" + h1 + """</h1>
  <p class="sub">""" + intro + """</p>
  <div class="calc">
    """ + inputs + """
    <button class="btn" onclick="calc()">""" + btn + """</button>
    <div class="result" id="res">
      <div class="lbl" id="outLbl"></div>
      <div class="big" id="outBig"></div>
      <table id="outTable"></table>
    </div>
  </div>
  <h2>""" + how_h2 + """</h2>
  <div class="formula">""" + esc(formula) + """</div>
  <ul>""" + how + """</ul>
  <h2>""" + faq_h2 + """</h2>
  """ + faq + """
  <h2>""" + rel_h2 + """</h2>
  <div class="grid">""" + related + """</div>
  <script>
window.__LBL__ = """ + lbl_json + """;
const F = v => '$' + Number(v).toLocaleString('en-US', {maximumFractionDigits: 2, minimumFractionDigits: 2});
function out(mainKey, big, rows) {
  const L = window.__LBL__;
  const label = mainKey === '__main__' ? L.main : (L.rows[mainKey] || mainKey);
  document.getElementById('outLbl').textContent = label;
  document.getElementById('outBig').textContent = big;
  const tb = document.getElementById('outTable'); tb.innerHTML = '';
  (rows || []).forEach(function (r) { tb.innerHTML += '<tr><td>' + (L.rows[r[0]] || r[0]) + '</td><td>' + r[1] + '</td></tr>'; });
  document.getElementById('res').style.display = 'block';
}
function calc() {
  const g = function (id) { return document.getElementById(id); };
""" + decls_of(c) + """
  try {
""" + c["compute"] + """
  } catch (e) { document.getElementById('outLbl').textContent = 'Error: ' + e.message; document.getElementById('res').style.display = 'block'; }
}
</script>
"""

def lang_switcher(cur, href_for):
    hf = href_for or (lambda c: page_file("index", c))
    items = "".join(
        '<a href="' + hf(c) + ('" class="cur"' if c == cur else '"') + '>'
        + (TR.get(c) or {}).get("name", "English") + '</a>'
        for c in LANGS)
    btn = ('<button id="langBtn" aria-haspopup="true" aria-expanded="false">'
           + (TR.get(cur) or {}).get("name", "English")
           + '<svg class="chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg></button>')
    return '<div class="lang">' + btn + '<div class="lang-menu">' + items + '</div></div>'

def render(lang, base, title, meta, body, cur, ld_faq=None, ld_name="CalcFin"):
    tr = TR.get(lang) or {}
    url = BASE_URL + ("/" if base == "index" else "/" + page_file(base, lang).replace(".html", ""))
    ld_w = LD_WEBAPP_T.replace("__NAME__", ld_name).replace("__URL__", url).replace("__META__", meta)
    ent = ""
    if ld_faq:
        ents = ",".join('{"@type":"Question","name":"' + esc(q).replace('"', '\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + esc(a).replace('"', '\\"') + '"}}' for q, a in ld_faq)
        ent = LD_FAQ_T.replace("__ENTITIES__", ents)
    hreflangs = "\n".join(
        '  <link rel="alternate" hreflang="' + c + '" href="' + BASE_URL + '/' + page_file(base, c).replace(".html", "") + '">'
        for c in LANGS) + '\n  <link rel="alternate" hreflang="x-default" href="' + BASE_URL + '/' + page_file(base, "en").replace(".html", "") + '">'
    calc_links = "".join(
        '<a href="/' + c["slug"] + ('' if lang == "en" else '-' + lang) + '.html"'
        + (' class="on"' if cur == c["slug"] else '') + '>'
        + ((tr.get("pages") or {}).get(c["slug"], {}).get("h1", c["nav"]) if tr else c["nav"]) + '</a>'
        for c in CALCS)
    html = (HEAD.replace("__TITLE__", title).replace("__META__", meta)
            .replace("__URL__", url).replace("__CSS__", CSS)
            .replace("__HREFLANGS__", hreflangs)
            .replace("__LD_WEBAPP__", ld_w).replace("__LD_FAQ__", ent)
            .replace("__NAV_PRIVACY__", tr.get("nav_privacy", "Privacy"))
            .replace("__NAV_ABOUT__", tr.get("nav_about", "About"))
            .replace("__LANGSWITCH__", lang_switcher(lang, lambda c: page_file(base, c)))
            .replace("__MAIN__", body)
            .replace("__FOOTER__", FOOTERS.get(lang, FOOTERS["en"])))
    return html

def home_body(lang):
    tr = TR.get(lang)
    def _item(c):
        tp = (tr.get("pages") or {}).get(c["slug"]) if tr else None
        h1 = tp["h1"] if tp else c["nav"]
        intro = (tp["intro"] if tp else c["intro"])[:80] + '…'
        href = '/' + c["slug"] + ('' if lang == "en" else '-' + lang) + '.html'
        return '<a href="' + href + '">' + h1 + '<span>' + intro + '</span></a>'
    grid = "".join(_item(c) for c in CALCS)
    if not tr:
        return """
  <h1>Free Financial Calculators</h1>
  <p class="sub">Fast, private calculators that run <b>entirely in your browser</b> — your numbers never leave your device. Every page shows the exact formula.</p>
  <div class="grid">""" + grid + """</div>
  <h2>No signup. No data collection. Just math.</h2>
  <p>Every calculator on CalcFin runs locally using JavaScript — your inputs are processed on your own device and never sent to any server. Each page also documents the exact formula used, so you can verify the math instead of trusting a black box.</p>
  <p>Results are estimates for planning and education, not financial advice.</p>
"""
    hm = tr["home"]
    return """
  <h1>""" + hm["h1"] + """</h1>
  <p class="sub">""" + hm["sub"] + """</p>
  <div class="grid">""" + grid + """</div>
  <h2>""" + hm["h2"] + """</h2>
  <p>""" + hm["p1"] + """</p>
  <p>""" + hm["p2"] + """</p>
"""

for lang in LANGS:
    tr = TR.get(lang) or {}
    try:
        hb = home_body(lang)
    except Exception as e:
        import traceback; traceback.print_exc()
        print('*** 崩溃语言:', lang, '| pages keys:', list((tr.get('pages') or {}).keys())[:3])
        raise
    if lang == "en":
        ht = "Free Financial Calculators — Loans, Mortgage, Savings, Interest | CalcFin"
        hm_ = "Free online financial calculators: compound interest, loan payments, mortgage, savings goals, credit card payoff, inflation, ROI and retirement. Private, no signup."
    else:
        ht, hm_ = tr["home"]["title"], tr["home"]["meta"]
    write_out = Path(page_file("index", lang))
    write_out.write_text(render(lang, "index", ht, hm_, hb, "home"), encoding="utf-8")
    print("生成:", write_out.name)
    for c in CALCS:
        import json as _j
        trp = (tr.get("pages") or {}).get(c["slug"])
        lbl = trp["lbl"] if trp else EN_LBL[c["slug"]]
        body = calc_body(c, tr or {}, lang, _j.dumps(lbl, ensure_ascii=False))
        title = trp["title"] if trp else c["title"]
        meta = trp["meta"] if trp else c["meta"]
        h1 = trp["h1"] if trp else c["h1"]
        pf = Path(page_file(c["slug"], lang))
        pf.write_text(render(lang, c["slug"], title, meta, body, c["slug"],
              ld_faq=[(q, a) for q, a in (trp["faq"] if trp else c["faq"])], ld_name="CalcFin — " + h1), encoding="utf-8")
        print("生成:", pf.name)
    for kind in ["privacy", "about"]:
        d = tr.get(kind) if tr else None
        body = d["body"] if d else (PRIVACY_BODY if kind == "privacy" else ABOUT_BODY)
        title = d["title"] if d else ("Privacy Policy | CalcFin" if kind == "privacy" else "About CalcFin | CalcFin")
        meta = d["meta"] if d else ("CalcFin privacy policy — local-only calculations, cookies and advertising disclosure." if kind == "privacy" else "About CalcFin — free financial calculators that run in your browser with transparent formulas.")
        pf = Path(page_file(kind, lang))
        pf.write_text(render(lang, kind, title, meta, body, None), encoding="utf-8")
        print("生成:", pf.name)

# sitemap:全语言全部页面
lines = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for lang in LANGS:
    for base in ["index", *[c["slug"] for c in CALCS], "privacy", "about"]:
        loc = BASE_URL + ("/" if base == "index" else "/" + page_file(base, lang).replace(".html", ""))
        lines.append("  <url><loc>" + loc + "</loc></url>")
lines.append("</urlset>")
Path("sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("生成: sitemap.xml")

print("完成:", len(LANGS), "语言 ×", 2 + len(CALCS), "页 =", len(LANGS) * (2 + len(CALCS)), "页")
