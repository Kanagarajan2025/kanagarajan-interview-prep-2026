"""
_build_html.py  v2 – self-contained interactive HTML viewer
=============================================================
* No CDN / internet required — 100% offline
* Inline syntax highlighting (Java + SQL)
* Virtual scroll for all 2044 questions (fast)
* Search + category filter
* Per-question tabs: Problem / Code / Memory Model / Execution Flow
* Copy-code button
* Correct language detection from code-fence tag
"""
import re, json, os

FILE = r'C:\Users\Kanag\kanagarajan_interview_preparation_may15_2026\Java_Backend_20_LPA_Complete.md'
OUT  = r'C:\Users\Kanag\kanagarajan_interview_preparation_may15_2026\Java_Backend_20_LPA_Complete.html'

# ── Category map ──────────────────────────────────────────────────────────────
CATS = [
    (1,    100,  'Core Java Basics',        '#4CAF50'),
    (101,  200,  'Numbers & Math',          '#2196F3'),
    (201,  300,  'Patterns',                '#9C27B0'),
    (301,  500,  'Strings & Arrays',        '#FF9800'),
    (501,  700,  'Search & Sort',           '#F44336'),
    (701,  900,  'Trees & Graphs',          '#00BCD4'),
    (901,  1000, 'DP & Backtracking',       '#FF5722'),
    (1001, 1200, 'Streams & Collections',   '#607D8B'),
    (1201, 1400, 'Multithreading',          '#E91E63'),
    (1401, 1600, 'File I/O & Exceptions',   '#795548'),
    (1601, 1700, 'Design Patterns',         '#3F51B5'),
    (1701, 1800, 'SQL & Databases',         '#009688'),
    (1801, 1900, 'Spring Boot & REST',      '#8BC34A'),
    (1901, 1944, 'Microservices & Cloud',   '#FFC107'),
    (1945, 1984, 'LLD',                     '#673AB7'),
    (1985, 2024, 'HLD',                     '#F44336'),
    (2025, 2044, 'AI & GenAI',              '#00E5FF'),
]

def get_cat(n):
    for s, e, name, color in CATS:
        if s <= n <= e:
            return name, color
    return 'Other', '#888'

# ── Memory analyzer ───────────────────────────────────────────────────────────
def analyze_memory(code, lang):
    if lang == 'sql':
        return {'stack': [], 'heap': ['Result Set', 'Query Plan'], 'static': ['Table metadata'], 'rec': False, 'note': 'SQL executes in DB engine; no JVM stack/heap.'}
    stack, heap, static = [], [], []
    for m in re.finditer(r'\b(int|long|double|float|boolean|char|byte|short)\s+(\w+)\s*[=;,)]', code):
        e = {'name': m.group(2), 'type': m.group(1)}
        if e not in stack: stack.append(e)
    for m in re.finditer(r'\b(String|List|Map|Set|Queue|Deque|ArrayList|HashMap|LinkedList|TreeMap|TreeSet|HashSet|Stack|PriorityQueue|StringBuilder|int\[\]|long\[\]|char\[\]|boolean\[\]|String\[\])\s+(\w+)\s*[=;]', code):
        e = {'name': m.group(2)+'->heap', 'type': m.group(1)}
        if e not in stack: stack.append(e)
    for m in re.finditer(r'\bnew\s+([\w<>,\s]+?)\s*[\(\[]', code):
        obj = m.group(1).strip().split('<')[0]
        if obj not in heap and obj not in ('int','long','char','byte'): heap.append(obj)
    if re.search(r'\bnew\s+\w+\s*\[', code) and 'array[]' not in heap: heap.append('array[]')
    for m in re.finditer(r'\bstatic\s+(?:final\s+)?\w+\s+(\w+)', code):
        if m.group(1) not in static: static.append(m.group(1))
    methods = re.findall(r'(?:void|int|long|String|boolean|List|Map|double|char)\s+(\w+)\s*\(', code)
    rec = any(len(re.findall(r'\b' + mn + r'\s*\(', code)) > 1 for mn in methods if mn not in ('if','while','for'))
    return {'stack': stack[:8], 'heap': heap[:6], 'static': static[:4], 'rec': rec, 'note': ''}

# ── Step extractor ────────────────────────────────────────────────────────────
def extract_steps(explanation, code):
    steps = []
    numbered = re.findall(r'(?:^|\n)\s*(\d+)[.)]\s+(.+?)(?=\n\s*\d+[.)]|\Z)', '\n'+explanation, re.DOTALL)
    if len(numbered) >= 2:
        steps = [s[1].strip().replace('\n', ' ')[:130] for s in numbered[:8]]
    else:
        parts = re.split(r';\s*|(?<=[a-z\)])\.\s+(?=[A-Z])', explanation)
        steps = [p.strip()[:130] for p in parts if len(p.strip()) > 15][:7]
    trace = []
    is_sql = bool(re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE)\b', code, re.I))
    if is_sql:
        for clause in ['SELECT', 'FROM', 'JOIN', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY', 'LIMIT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'WITH']:
            for line in code.split('\n'):
                s = line.strip()
                if re.match(r'(?i)' + re.escape(clause) + r'\b', s):
                    trace.append(s[:90]); break
    else:
        for line in code.split('\n'):
            s = line.strip()
            if not s or s.startswith('//') or s.startswith('/*') or s.startswith('*'): continue
            if (s.startswith('return ') or
                    re.match(r'(int|long|boolean|String|char|double|float|List|Map|Set|var)\s+\w+\s*[=;]', s) or
                    s.startswith('for ') or s.startswith('while ') or
                    s.startswith('if (') or s.startswith('if(') or
                    s.startswith('System.out') or s.startswith('throw ')):
                trace.append(s[:90])
            if len(trace) == 12: break
    return steps, trace

# ── Parser ────────────────────────────────────────────────────────────────────
QUESTION_PAT = re.compile(
    r'### (\d+)\. (.+?)\n'
    r'\*\*ID:\*\* `([^`]+)`\n\n'
    r'\*\*Problem:\*\* (.+?)\n\n'
    r'\*\*Example Input:\*\* (.+?)\n\n'
    r'\*\*Example Output:\*\* (.+?)\n\n'
    r'\*\*Explanation:\*\* (.+?)\n\n'
    r'\*\*Answer:\*\*\n```(\w*)\n(.*?)```\n\n'
    r'> \*\*Time:\*\* (.+?) &nbsp; \*\*Space:\*\* ([^\n]+)',
    re.DOTALL,
)

def parse_questions(content):
    qs = []
    for m in QUESTION_PAT.finditer(content):
        qnum  = int(m.group(1))
        lang  = m.group(8).strip() or 'java'
        code  = m.group(9).strip()
        expl  = m.group(7).strip()
        cat, col = get_cat(qnum)
        steps, trace = extract_steps(expl, code)
        mem = analyze_memory(code, lang)
        qs.append({
            'n':    qnum,
            't':    m.group(2).strip(),
            'id':   m.group(3).strip(),
            'p':    m.group(4).strip(),
            'inp':  m.group(5).strip(),
            'out':  m.group(6).strip(),
            'ex':   expl,
            'lang': lang,
            'c':    code,
            'tc':   m.group(10).strip(),
            'sc':   m.group(11).strip(),
            'cat':  cat,
            'col':  col,
            'mem':  mem,
            'steps': steps,
            'trace': trace,
        })
    return qs

# ── HTML template ─────────────────────────────────────────────────────────────
# NOTE: __QS__ and __CM__ are replaced by Python — no JS template literals used
HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Java Backend Interview Prep 2026 \u2013 2044 Questions</title>
<style>
:root{--bg:#0d1117;--bg2:#161b22;--bg3:#21262d;--bg4:#30363d;--border:#30363d;
--text:#e6edf3;--dim:#8b949e;--accent:#58a6ff;--green:#3fb950;--orange:#d29922;
--red:#f85149;--purple:#d2a8ff}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column}
#hdr{background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 14px;display:flex;align-items:center;gap:10px;flex-shrink:0}
#hdr h1{font-size:.92rem;font-weight:700;color:var(--accent);white-space:nowrap}
#hdr small{font-size:.7rem;color:var(--dim);white-space:nowrap}
#search{flex:1;background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:6px 12px;color:var(--text);font-size:.84rem;outline:none;min-width:0}
#search:focus{border-color:var(--accent)}
#search::placeholder{color:var(--dim)}
#cnt{background:var(--accent);color:#000;font-weight:700;border-radius:20px;padding:3px 10px;font-size:.72rem;white-space:nowrap}
#layout{display:flex;flex:1;overflow:hidden}
#sb{width:210px;min-width:140px;background:var(--bg2);border-right:1px solid var(--border);overflow-y:auto;flex-shrink:0}
.sb-h{font-size:.65rem;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);padding:10px 12px 5px}
.ci{padding:6px 10px;cursor:pointer;font-size:.77rem;display:flex;align-items:center;gap:7px;border-left:3px solid transparent;user-select:none}
.ci:hover{background:var(--bg3)}
.ci.active{background:var(--bg3);border-left-color:var(--accent)}
.ci-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.ci-lbl{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ci-cnt{font-size:.67rem;color:var(--dim);background:var(--bg4);border-radius:8px;padding:1px 6px;flex-shrink:0}
#main{flex:1;overflow:hidden;display:flex;flex-direction:column}
#lv{flex:1;overflow-y:auto;padding:8px}
.qc{background:var(--bg2);border:1px solid var(--border);border-radius:7px;padding:10px 13px;margin-bottom:7px;cursor:pointer}
.qc:hover{border-color:var(--accent)}
.qc-top{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.qnum{font-size:.7rem;color:var(--dim);min-width:30px;font-family:monospace}
.qtitle{font-size:.87rem;font-weight:600;flex:1}
.qid{font-size:.67rem;color:var(--dim);font-family:monospace;background:var(--bg3);padding:1px 6px;border-radius:3px}
.bcat{font-size:.67rem;padding:2px 7px;border-radius:10px;font-weight:600}
.btc{font-size:.67rem;padding:2px 7px;border-radius:10px;background:#3fb95018;border:1px solid #3fb95044;color:#3fb950}
.bsc{font-size:.67rem;padding:2px 7px;border-radius:10px;background:#d2992218;border:1px solid #d2992244;color:#d29922}
.qprev{font-size:.77rem;color:var(--dim);margin-top:5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#no-res{display:none;text-align:center;padding:48px;color:var(--dim)}
#dv{flex:1;overflow:hidden;display:none;flex-direction:column}
#dv-hdr{background:var(--bg2);border-bottom:1px solid var(--border);padding:9px 14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;flex-shrink:0}
#dv-hdr h2{font-size:.92rem;flex:1;line-height:1.4}
#back{background:var(--bg3);border:1px solid var(--border);border-radius:5px;padding:4px 11px;color:var(--text);cursor:pointer;font-size:.77rem}
#back:hover{background:var(--bg4)}
.tabs{display:flex;border-bottom:1px solid var(--border);background:var(--bg2);flex-shrink:0}
.tab{padding:8px 14px;cursor:pointer;font-size:.8rem;color:var(--dim);border-bottom:2px solid transparent;user-select:none}
.tab.active{color:var(--accent);border-bottom-color:var(--accent)}
.tab:hover{color:var(--text)}
#tc{flex:1;overflow-y:auto;padding:14px}
.tp{display:none}
.tp.active{display:block}
.flbl{font-size:.67rem;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:3px;margin-top:10px}
.flbl:first-child{margin-top:0}
.fbox{background:var(--bg3);border:1px solid var(--border);border-radius:5px;padding:9px 12px;font-size:.84rem;line-height:1.6;white-space:pre-wrap;word-break:break-word}
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.cpill{padding:5px 14px;border-radius:7px;font-size:.8rem;font-weight:600;display:inline-block;margin-right:8px;margin-top:6px}
.tc-pill{background:#3fb95018;border:1px solid #3fb95044;color:#3fb950}
.sc-pill{background:#d2992218;border:1px solid #d2992244;color:#d29922}
.code-wrap{position:relative;border-radius:7px;overflow:hidden;border:1px solid var(--border)}
.code-lang{position:absolute;top:6px;left:10px;font-size:.63rem;text-transform:uppercase;color:var(--dim);letter-spacing:.06em;pointer-events:none}
.copy-btn{position:absolute;top:5px;right:8px;background:var(--bg4);border:1px solid var(--border);border-radius:4px;padding:3px 9px;font-size:.7rem;color:var(--dim);cursor:pointer}
.copy-btn:hover{color:var(--text)}
.nav-btn{background:var(--bg3);border:1px solid var(--border);border-radius:5px;padding:4px 10px;color:var(--dim);cursor:pointer;font-size:.82rem;flex-shrink:0}
.nav-btn:hover{color:var(--text);background:var(--bg4)}
pre.hl{background:#0d1117;padding:28px 14px 14px;overflow-x:auto;font-family:'Cascadia Code','Consolas','Courier New',monospace;font-size:.78rem;line-height:1.65;white-space:pre;margin:0;color:#e6edf3}
pre.hl .k{color:#ff7b72}
pre.hl .s{color:#a5d6ff}
pre.hl .c{color:#8b949e;font-style:italic}
pre.hl .n{color:#79c0ff}
pre.hl .an{color:#d2a8ff}
.jmm{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px}
.jz{border-radius:6px;padding:8px;text-align:center;font-size:.74rem}
.jz-t{font-weight:700;margin-bottom:3px}
.jz-d{font-size:.66rem;color:var(--dim);line-height:1.4}
.jz-sk{background:#58a6ff18;border:1px solid #58a6ff44;color:#58a6ff}
.jz-hp{background:#3fb95018;border:1px solid #3fb95044;color:#3fb950}
.jz-ma{background:#d2a8ff18;border:1px solid #d2a8ff44;color:#d2a8ff}
.jz-pc{background:#d2992218;border:1px solid #d2992244;color:#d29922}
.mgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:10px}
.mbox{background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:10px}
.mbox-h{font-size:.68rem;text-transform:uppercase;letter-spacing:.05em;margin-bottom:7px;padding-bottom:5px;border-bottom:1px solid var(--border)}
.stk .mbox-h{color:#58a6ff}
.hp .mbox-h{color:#3fb950}
.sta .mbox-h{color:#d2a8ff}
.me{background:var(--bg4);border-radius:3px;padding:3px 7px;margin-bottom:3px;font-size:.74rem;font-family:monospace;display:flex;justify-content:space-between;gap:6px}
.me-type{color:var(--dim);font-size:.67rem}
.rec-badge{background:#f8514918;border:1px solid #f8514944;color:#f85149;border-radius:4px;padding:3px 8px;font-size:.71rem;text-align:center;margin-top:6px}
.mem-note{font-size:.74rem;color:var(--dim);margin-bottom:8px;padding:7px 10px;background:var(--bg3);border-radius:5px;border:1px solid var(--border)}
.fsec{margin-bottom:18px}
.fsec-h{font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:8px;padding-bottom:5px;border-bottom:1px solid var(--border)}
.step{display:flex;gap:10px;margin-bottom:8px}
.step-n{background:var(--accent);color:#000;border-radius:50%;width:20px;height:20px;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.step-t{background:var(--bg3);border:1px solid var(--border);border-radius:5px;padding:7px 11px;font-size:.8rem;flex:1;line-height:1.5}
.arr{color:var(--dim);font-size:.75rem;margin-left:30px;margin-bottom:3px}
.tr{display:flex;gap:10px;margin-bottom:6px}
.tr-n{background:#3fb95018;color:#3fb950;border:1px solid #3fb95044;border-radius:50%;width:20px;height:20px;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.tr-c{background:var(--bg3);border:1px solid #3fb95022;border-radius:4px;padding:4px 9px;font-size:.75rem;font-family:monospace;flex:1;white-space:pre-wrap;word-break:break-all}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:3px}
</style>
</head>
<body>
<div id="hdr">
  <h1>&#9749; Java Interview Prep 2026</h1>
  <small>2044 Questions &bull; 17 Categories</small>
  <input id="search" type="search" placeholder="&#128269;  Search title, ID, topic, Q-number..." autocomplete="off"/>
  <span id="cnt">2044</span>
</div>
<div id="layout">
  <div id="sb">
    <div class="sb-h">Categories</div>
    <div class="ci active" data-cat="ALL" onclick="filterCat('ALL',this)">
      <span class="ci-dot" style="background:#888"></span>
      <span class="ci-lbl">All Categories</span>
      <span class="ci-cnt" id="cnt-ALL">2044</span>
    </div>
    <div id="cat-list"></div>
  </div>
  <div id="main">
    <div id="lv">
      <div id="vt"></div>
      <div id="no-res">No questions match your search.</div>
      <div id="cards"></div>
      <div id="vb"></div>
    </div>
    <div id="dv">
      <div id="dv-hdr">
        <button id="back" onclick="showList()">&#8592; Back</button>
        <button class="nav-btn" onclick="navQ(-1)">&#8249; Prev</button>
        <h2 id="dv-title"></h2>
        <span id="dv-nav" style="font-size:.68rem;color:var(--dim);white-space:nowrap"></span>
        <span id="dv-id" class="qid"></span>
        <span id="dv-cat" class="bcat"></span>
        <span id="dv-tc" class="btc"></span>
        <span id="dv-sc" class="bsc"></span>
        <button class="nav-btn" onclick="navQ(1)">Next &#8250;</button>
      </div>
      <div class="tabs">
        <div class="tab active" onclick="showTab('prob',this)">&#128196; Problem</div>
        <div class="tab"        onclick="showTab('code',this)">&#128187; Code</div>
        <div class="tab"        onclick="showTab('mem', this)">&#129504; Memory</div>
        <div class="tab"        onclick="showTab('flow',this)">&#9654; Flow</div>
      </div>
      <div id="tc">
        <div id="tp-prob" class="tp active"></div>
        <div id="tp-code" class="tp"></div>
        <div id="tp-mem"  class="tp"></div>
        <div id="tp-flow" class="tp"></div>
      </div>
    </div>
  </div>
</div>
<script>
const QS=__QS__;
const CM=__CM__;

// ── Inline syntax highlighting ───────────────────────────────────────────────
const JKW=new Set(['abstract','assert','boolean','break','byte','case','catch','char','class',
'const','continue','default','do','double','else','enum','extends','final','finally','float',
'for','goto','if','implements','import','instanceof','int','interface','long','native','new',
'null','package','private','protected','public','return','short','static','strictfp','super',
'switch','synchronized','this','throw','throws','transient','try','var','void','volatile',
'while','true','false','record','sealed','permits','yield']);

function eh(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function hlJava(raw){
  const lines=raw.split('\\n'), out=[];
  let inBlock=false;
  for(let line of lines){
    let r='', i=0;
    if(inBlock){
      const end=line.indexOf('*/');
      if(end===-1){out.push('<span class="c">'+eh(line)+'</span>');continue;}
      r+='<span class="c">'+eh(line.slice(0,end+2))+'</span>';
      i=end+2; inBlock=false;
    }
    while(i<line.length){
      if(line[i]==='/'&&line[i+1]==='/'){r+='<span class="c">'+eh(line.slice(i))+'</span>';i=line.length;break;}
      if(line[i]==='/'&&line[i+1]==='*'){
        const end=line.indexOf('*/',i+2);
        if(end===-1){r+='<span class="c">'+eh(line.slice(i))+'</span>';i=line.length;inBlock=true;break;}
        r+='<span class="c">'+eh(line.slice(i,end+2))+'</span>';i=end+2;continue;
      }
      if(line[i]==='"'){
        let j=i+1;
        while(j<line.length&&line[j]!=='"'){if(line.charCodeAt(j)===92)j++;j++;}
        r+='<span class="s">'+eh(line.slice(i,j+1))+'</span>';i=j+1;continue;
      }
      if(line[i]==="'"){
        let j=i+1;
        while(j<line.length&&line[j]!=="'"){if(line.charCodeAt(j)===92)j++;j++;}
        r+='<span class="s">'+eh(line.slice(i,j+1))+'</span>';i=j+1;continue;
      }
      if(line[i]==='@'){
        let j=i+1;while(j<line.length&&/\\w/.test(line[j]))j++;
        r+='<span class="an">'+eh(line.slice(i,j))+'</span>';i=j;continue;
      }
      if(/[a-zA-Z_$]/.test(line[i])){
        let j=i;while(j<line.length&&/\\w/.test(line[j]))j++;
        const w=line.slice(i,j);
        r+=JKW.has(w)?'<span class="k">'+w+'</span>':eh(w);
        i=j;continue;
      }
      if(/\\d/.test(line[i])){
        let j=i;while(j<line.length&&/[\\d_.xXlLdDfFbBoO]/.test(line[j]))j++;
        r+='<span class="n">'+eh(line.slice(i,j))+'</span>';i=j;continue;
      }
      r+=eh(line[i]);i++;
    }
    out.push(r);
  }
  return out.join('\\n');
}

const SKW=new Set(['SELECT','FROM','WHERE','JOIN','ON','GROUP','ORDER','BY','HAVING',
'INSERT','UPDATE','DELETE','CREATE','DROP','ALTER','TABLE','INDEX','VIEW','PROCEDURE',
'FUNCTION','INNER','LEFT','RIGHT','OUTER','FULL','CROSS','UNION','ALL','DISTINCT','AS',
'NOT','AND','OR','IN','IS','NULL','LIMIT','OFFSET','ASC','DESC','CASE','WHEN','THEN',
'ELSE','END','WITH','RETURN','BEGIN','SET','DECLARE','IF','WHILE','EXISTS','BETWEEN',
'LIKE','INTO','VALUES','COUNT','SUM','AVG','MAX','MIN','COALESCE','RANK','ROW_NUMBER',
'DENSE_RANK','PARTITION','OVER','RETURNS','INT','VARCHAR','TEXT','DATE','TIMESTAMP']);

function hlSQL(raw){
  let s=eh(raw);
  s=s.replace(/(--[^\\n]*)/g,'<span class="c">$1</span>');
  s=s.replace(/('(?:[^'\\\\]|\\\\.)*')/g,'<span class="s">$1</span>');
  s=s.replace(/\\b([A-Za-z_][A-Za-z_0-9]*)\\b/g,(m)=>SKW.has(m.toUpperCase())?'<span class="k">'+m+'</span>':m);
  s=s.replace(/\\b(\\d+)\\b/g,'<span class="n">$1</span>');
  return s;
}

const PKW=new Set(['False','None','True','and','as','assert','async','await','break',
'class','continue','def','del','elif','else','except','finally','for','from','global',
'if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try',
'while','with','yield','print','self','super','len','range','type','isinstance']);

function hlPython(raw){
  const lines=raw.split('\\n'), out=[];
  for(let line of lines){
    let r='', i=0;
    while(i<line.length){
      if(line[i]==='#'){r+='<span class="c">'+eh(line.slice(i))+'</span>';i=line.length;break;}
      if(line[i]==='"'||line[i]==="'"){
        const q=line[i];
        // triple quote?
        if(line.slice(i,i+3)===q+q+q){
          let j=i+3;while(j<line.length&&line.slice(j,j+3)!==q+q+q)j++;
          r+='<span class="s">'+eh(line.slice(i,j+3))+'</span>';i=j+3;continue;
        }
        let j=i+1;while(j<line.length&&line[j]!==q){if(line.charCodeAt(j)===92)j++;j++;}
        r+='<span class="s">'+eh(line.slice(i,j+1))+'</span>';i=j+1;continue;
      }
      if(/[a-zA-Z_]/.test(line[i])){
        let j=i;while(j<line.length&&/\\w/.test(line[j]))j++;
        const w=line.slice(i,j);
        r+=PKW.has(w)?'<span class="k">'+w+'</span>':eh(w);
        i=j;continue;
      }
      if(/\\d/.test(line[i])){
        let j=i;while(j<line.length&&/[\\d_.eEjJ]/.test(line[j]))j++;
        r+='<span class="n">'+eh(line.slice(i,j))+'</span>';i=j;continue;
      }
      r+=eh(line[i]);i++;
    }
    out.push(r);
  }
  return out.join('\\n');
}

function hl(code,lang){
  if(!code)return '';
  if(lang==='sql')return hlSQL(code);
  if(lang==='python')return hlPython(code);
  return hlJava(code);
}

// ── State ────────────────────────────────────────────────────────────────────
let filtered=QS.slice(), curCat='ALL', curQ=null, curIdx=-1;
const PAGE=25, CARD_H=85;
let startIdx=0;

// ── Sidebar ──────────────────────────────────────────────────────────────────
(function buildSidebar(){
  const cl=document.getElementById('cat-list');
  CM.forEach(([s,e,name,col])=>{
    const cnt=QS.filter(q=>q.n>=s&&q.n<=e).length;
    const d=document.createElement('div');
    d.className='ci';d.dataset.cat=name;d.onclick=()=>filterCat(name,d);
    d.innerHTML='<span class="ci-dot" style="background:'+col+'"></span><span class="ci-lbl">'+esc(name)+'</span><span class="ci-cnt">'+cnt+'</span>';
    cl.appendChild(d);
  });
})();

function filterCat(cat,el){
  curCat=cat;
  document.querySelectorAll('.ci').forEach(e=>e.classList.remove('active'));
  el.classList.add('active');
  applyFilter();
}

// ── Search ────────────────────────────────────────────────────────────────────
let _st, _term='';
document.getElementById('search').addEventListener('input',e=>{
  clearTimeout(_st);
  _st=setTimeout(()=>{_term=e.target.value.toLowerCase().trim();applyFilter();},180);
});

function applyFilter(){
  filtered=QS.filter(q=>{
    if(curCat!=='ALL'&&q.cat!==curCat)return false;
    if(!_term)return true;
    return String(q.n).includes(_term)||q.t.toLowerCase().includes(_term)||
           q.id.toLowerCase().includes(_term)||q.cat.toLowerCase().includes(_term)||
           q.p.toLowerCase().includes(_term);
  });
  startIdx=0;
  document.getElementById('cnt').textContent=filtered.length;
  renderCards();
}

// ── Virtual scroll ────────────────────────────────────────────────────────────
function renderCards(){
  const nr=document.getElementById('no-res');
  const vt=document.getElementById('vt');
  const vb=document.getElementById('vb');
  const cc=document.getElementById('cards');
  if(!filtered.length){
    cc.innerHTML='';vt.style.height='0';vb.style.height='0';nr.style.display='block';return;
  }
  nr.style.display='none';
  const end=Math.min(startIdx+PAGE,filtered.length);
  vt.style.height=(startIdx*CARD_H)+'px';
  vb.style.height=(Math.max(0,filtered.length-end)*CARD_H)+'px';
  const frag=document.createDocumentFragment();
  for(let i=startIdx;i<end;i++){
    const q=filtered[i], d=document.createElement('div');
    d.className='qc';d.onclick=()=>showDetail(q);
    d.innerHTML='<div class="qc-top">'+
      '<span class="qnum">#'+q.n+'</span>'+
      '<span class="qtitle">'+esc(q.t)+'</span>'+
      '<span class="qid">'+esc(q.id)+'</span>'+
      '<span class="bcat" style="background:'+q.col+'28;border:1px solid '+q.col+'55;color:'+q.col+'">'+esc(q.cat)+'</span>'+
      '<span class="btc">&#x23F1; '+esc(q.tc)+'</span>'+
      '<span class="bsc">&#x1F4BE; '+esc(q.sc)+'</span>'+
      '</div><div class="qprev">'+esc(q.p.slice(0,140))+(q.p.length>140?'...':'')+'</div>';
    frag.appendChild(d);
  }
  cc.innerHTML='';cc.appendChild(frag);
}

document.getElementById('lv').addEventListener('scroll',function(){
  if(!filtered.length)return;
  const ratio=this.scrollTop/(this.scrollHeight-this.clientHeight||1);
  const ns=Math.floor(ratio*filtered.length/PAGE)*PAGE;
  if(ns!==startIdx){startIdx=Math.min(ns,Math.max(0,filtered.length-PAGE));renderCards();}
});

// ── Detail view ───────────────────────────────────────────────────────────────
function showList(){
  document.getElementById('lv').style.display='block';
  document.getElementById('dv').style.display='none';
}

function showDetail(q,idx){
  curQ=q;curIdx=idx!=null?idx:filtered.indexOf(q);
  document.getElementById('lv').style.display='none';
  document.getElementById('dv').style.display='flex';
  document.getElementById('dv-title').textContent='Q'+q.n+'. '+q.t;
  document.getElementById('dv-id').textContent=q.id;
  const dc=document.getElementById('dv-cat');
  dc.textContent=q.cat;dc.style.cssText='background:'+q.col+'28;border:1px solid '+q.col+'55;color:'+q.col;
  document.getElementById('dv-tc').textContent='Time: '+q.tc;
  document.getElementById('dv-sc').textContent='Space: '+q.sc;
  const dv=document.getElementById('dv-nav');if(dv)dv.textContent=curIdx>=0?(curIdx+1)+' / '+filtered.length:'';
  renderProb(q);renderCode(q);renderMem(q);renderFlow(q);
  showTab('prob',document.querySelector('.tab'));
  document.getElementById('tc').scrollTop=0;
}

function navQ(dir){
  if(!filtered.length)return;
  const ni=Math.max(0,Math.min(filtered.length-1,(curIdx<0?0:curIdx)+dir));
  showDetail(filtered[ni],ni);
}

function showTab(name,el){
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tp').forEach(p=>p.classList.remove('active'));
  if(el)el.classList.add('active');
  document.getElementById('tp-'+name).classList.add('active');
}

// ── Tabs ─────────────────────────────────────────────────────────────────────
function renderProb(q){
  document.getElementById('tp-prob').innerHTML=
    '<div class="flbl">Problem Statement</div><div class="fbox">'+esc(q.p)+'</div>'+
    '<div class="io">'+
    '<div><div class="flbl">Example Input</div><div class="fbox" style="font-family:monospace;font-size:.79rem">'+esc(q.inp)+'</div></div>'+
    '<div><div class="flbl">Example Output</div><div class="fbox" style="font-family:monospace;font-size:.79rem">'+esc(q.out)+'</div></div>'+
    '</div>'+
    '<div class="flbl">Explanation</div><div class="fbox">'+esc(q.ex)+'</div>'+
    '<div class="flbl">Complexity</div>'+
    '<span class="cpill tc-pill">&#x23F1; Time: '+esc(q.tc)+'</span>'+
    '<span class="cpill sc-pill">&#x1F4BE; Space: '+esc(q.sc)+'</span>';
}

function renderCode(q){
  document.getElementById('tp-code').innerHTML=
    '<div class="code-wrap">'+
    '<span class="code-lang">'+esc(q.lang||'java')+'</span>'+
    '<button class="copy-btn" onclick="copyCode()">&#128203; Copy</button>'+
    '<pre class="hl">'+hl(q.c,q.lang)+'</pre>'+
    '</div>';
}

function copyCode(){
  if(!curQ)return;
  const btn=document.querySelector('.copy-btn');
  const done=()=>{if(btn){btn.textContent='Copied!';setTimeout(()=>{btn.innerHTML='&#128203; Copy';},1500);}};
  if(navigator.clipboard){navigator.clipboard.writeText(curQ.c).then(done).catch(()=>fallbackCopy(done));}
  else fallbackCopy(done);
}
function fallbackCopy(cb){
  const ta=document.createElement('textarea');
  ta.value=curQ.c;ta.style.position='fixed';ta.style.opacity='0';
  document.body.appendChild(ta);ta.select();
  try{document.execCommand('copy');}catch(e){}
  document.body.removeChild(ta);if(cb)cb();
}

function renderMem(q){
  const m=q.mem||{};
  if(q.lang==='sql'){
    const hr=(m.heap||[]).map(h=>'<div class="me"><span>'+esc(h)+'</span><span class="me-type">DB zone</span></div>').join('')||'<div class="me" style="color:var(--dim)">Result Set, Join Buffer</div>';
    const str=(m.static||[]).map(s=>'<div class="me"><span>'+esc(s)+'</span><span class="me-type">catalog</span></div>').join('')||'<div class="me" style="color:var(--dim)">Table metadata, indexes</div>';
    document.getElementById('tp-mem').innerHTML=
      '<div class="mem-note">'+esc(m.note||'SQL executes in DB engine; no JVM stack/heap.')+'</div>'+
      '<div class="jmm">'+
      '<div class="jz jz-sk"><div class="jz-t">Buffer Pool</div><div class="jz-d">Table &amp; index pages cached in RAM.</div></div>'+
      '<div class="jz jz-hp"><div class="jz-t">Sort Buffer</div><div class="jz-d">ORDER BY / GROUP BY temp workspace.</div></div>'+
      '<div class="jz jz-ma"><div class="jz-t">Result Set</div><div class="jz-d">Rows returned to the client cursor.</div></div>'+
      '<div class="jz jz-pc"><div class="jz-t">Query Plan</div><div class="jz-d">Optimizer execution plan (cached).</div></div>'+
      '</div>'+
      '<div class="mgrid">'+
      '<div class="mbox hp"><div class="mbox-h">&#128308; Working Memory</div>'+hr+'</div>'+
      '<div class="mbox sta"><div class="mbox-h">&#9660; System Catalog</div>'+str+'</div>'+
      '</div>'+
      '<div class="fbox" style="font-size:.77rem;color:var(--dim)">Space: <span style="color:#58a6ff">'+esc(q.sc)+'</span> &#8212; DB allocates temp tables &amp; sort buffers proportional to result set size.</div>';
    return;
  }
  const sr=(m.stack||[]).map(v=>'<div class="me"><span>'+esc(v.name)+'</span><span class="me-type">'+esc(v.type)+'</span></div>').join('')||'<div class="me" style="color:var(--dim)">No locals detected</div>';
  const hr=(m.heap||[]).map(h=>'<div class="me"><span>'+esc(h)+'</span><span class="me-type">heap</span></div>').join('')||'<div class="me" style="color:var(--dim)">No heap allocs</div>';
  const str=(m.static||[]).map(s=>'<div class="me"><span>'+esc(s)+'</span><span class="me-type">static</span></div>').join('')||'<div class="me" style="color:var(--dim)">None</div>';
  const rec=m.rec?'<div class="rec-badge">&#9650; Recursive &#8212; multiple stack frames</div>':'';
  const note=m.note?'<div class="mem-note">'+esc(m.note)+'</div>':'';
  const sc=q.sc||'';
  const scd=sc.includes('O(1)')?'<span style="color:#3fb950">'+esc(sc)+'</span> &#8212; constant extra memory.':
             sc.includes('O(n)')?'<span style="color:#d29922">'+esc(sc)+'</span> &#8212; linear extra memory; grows with input.':
             '<span style="color:#58a6ff">'+esc(sc)+'</span>';
  document.getElementById('tp-mem').innerHTML=
    '<div class="jmm">'+
    '<div class="jz jz-sk"><div class="jz-t">Stack</div><div class="jz-d">Local vars, frames. Per-thread. LIFO.</div></div>'+
    '<div class="jz jz-hp"><div class="jz-t">Heap</div><div class="jz-d">Objects (new), arrays. Shared. GC managed.</div></div>'+
    '<div class="jz jz-ma"><div class="jz-t">Method Area</div><div class="jz-d">Class bytecode, statics. Shared.</div></div>'+
    '<div class="jz jz-pc"><div class="jz-t">PC Register</div><div class="jz-d">Instruction pointer. Per-thread.</div></div>'+
    '</div>'+
    note+
    '<div class="mgrid">'+
    '<div class="mbox stk"><div class="mbox-h">&#9650; Stack Frame</div>'+sr+rec+'</div>'+
    '<div>'+
    '<div class="mbox hp" style="margin-bottom:10px"><div class="mbox-h">&#128308; Heap Allocations</div>'+hr+'</div>'+
    '<div class="mbox sta"><div class="mbox-h">&#9660; Method Area (Static)</div>'+str+'</div>'+
    '</div></div>'+
    '<div class="fbox" style="font-size:.77rem;color:var(--dim)">Space: '+scd+' Primitives live on stack; reference types have stack pointer + heap object.</div>';
}

function renderFlow(q){
  const steps=q.steps||[], trace=q.trace||[];
  if(q.lang==='sql'){
    const SQL_ORDER=['FROM / JOIN &#8212; load &amp; join source tables','WHERE &#8212; filter individual rows','GROUP BY &#8212; aggregate rows into groups','HAVING &#8212; filter aggregated groups','SELECT &#8212; project &amp; compute output columns','DISTINCT &#8212; remove duplicate rows','ORDER BY &#8212; sort the result set','LIMIT / OFFSET &#8212; paginate output'];
    const sqlSteps=SQL_ORDER.map((s,i)=>(i>0?'<div class="arr">&#8595;</div>':'')+
      '<div class="step"><div class="step-n">'+(i+1)+'</div><div class="step-t">'+s+'</div></div>').join('');
    const th=trace.length?trace.map((l,i)=>'<div class="tr"><div class="tr-n">'+(i+1)+'</div><div class="tr-c">'+esc(l)+'</div></div>').join(''):
      '<div style="color:var(--dim);font-size:.8rem">Key SQL clauses from the query above.</div>';
    const extra=steps.length?'<div class="fsec"><div class="fsec-h">&#128218; Explanation Notes</div>'+
      steps.map((s,i)=>'<div class="step"><div class="step-n">'+(i+1)+'</div><div class="step-t">'+esc(s)+'</div></div>').join('')+'</div>':'';
    document.getElementById('tp-flow').innerHTML=
      '<div class="fsec"><div class="fsec-h">&#128204; SQL Logical Execution Order</div>'+sqlSteps+'</div>'+extra+
      '<div class="fsec"><div class="fsec-h">&#128187; Query Clauses Trace</div>'+th+'</div>'+
      '<div class="fbox" style="font-size:.77rem;color:var(--dim)">Time complexity: <span style="color:#3fb950">'+esc(q.tc)+'</span> &#8212; typically O(n log n) for sort, O(n) for full scan.</div>';
    return;
  }
  const sh=steps.length?steps.map((s,i)=>(i>0?'<div class="arr">&#8595;</div>':'')+
    '<div class="step"><div class="step-n">'+(i+1)+'</div><div class="step-t">'+esc(s)+'</div></div>').join(''):
    '<div style="color:var(--dim);font-size:.8rem">Steps extracted from explanation.</div>';
  const th=trace.length?trace.map((l,i)=>'<div class="tr"><div class="tr-n">'+(i+1)+'</div><div class="tr-c">'+esc(l)+'</div></div>').join(''):
    '<div style="color:var(--dim);font-size:.8rem">Key code statements.</div>';
  document.getElementById('tp-flow').innerHTML=
    '<div class="fsec"><div class="fsec-h">&#128218; Algorithm Steps (from explanation)</div>'+sh+'</div>'+
    '<div class="fsec"><div class="fsec-h">&#128187; Code Execution Trace</div>'+th+'</div>'+
    '<div class="fbox" style="font-size:.77rem;color:var(--dim)">Time complexity: <span style="color:#3fb950">'+esc(q.tc)+'</span> &#8212; total iterations across all steps.</div>';
}

function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}

// ── Init ──────────────────────────────────────────────────────────────────────
applyFilter();
document.addEventListener('keydown',function(e){
  if(e.key==='Escape'&&curQ){showList();}
  else if(e.key==='ArrowRight'&&curQ){navQ(1);}
  else if(e.key==='ArrowLeft'&&curQ){navQ(-1);}
});
</script>
</body>
</html>"""

# ── Build ─────────────────────────────────────────────────────────────────────
def generate_html(questions):
    cats_meta = [[s, e, name, col] for s, e, name, col in CATS]
    q_json = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))
    q_json = q_json.replace('</', '<\\/')   # prevent </script> from breaking HTML parser
    c_json = json.dumps(cats_meta, ensure_ascii=False, separators=(',', ':'))
    html = HTML.replace('__QS__', q_json).replace('__CM__', c_json)
    return html

if __name__ == '__main__':
    print('Reading MD file...')
    with open(FILE, encoding='utf-8') as f:
        content = f.read()
    print('Parsing questions...')
    questions = parse_questions(content)
    print(f'  Parsed: {len(questions)} / 2044')
    if len(questions) < 2044:
        print(f'  WARNING: missing {2044 - len(questions)} questions!')
    print('Generating HTML...')
    html = generate_html(questions)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    mb = os.path.getsize(OUT) / 1_048_576
    sc = html.count('</script>')
    print(f'  Output : {OUT}')
    print(f'  Size   : {mb:.1f} MB')
    print(f'  </script> tags: {sc} (expected 1)')
    print('Done!')
