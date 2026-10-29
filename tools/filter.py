import json, re, os
W = os.path.join(os.path.dirname(__file__), "..", "work")
def ok(s):
    t = s.strip()
    if len(t) < 2 or len(t) > 1500: return False
    if not re.search(r"[A-Za-z]{2}", t): return False
    if re.fullmatch(r"[A-Za-z0-9_.\-/:]+", t) and not re.fullmatch(r"[A-Z][a-z]+", t) and not re.fullmatch(r"[A-Z]{2,}", t): return False  # identificadores
    if re.search(r"[{}<>]", t) and not re.search(r"<(b|i|u|color|size|br|/)", t) and "{0" not in t: return False
    if re.search(r"(\|https?://|\.(cs|dll|png|json|prefab|asset)\b|::|__|=>|\(\)|;\s*$)", t): return False
    if re.fullmatch(r"[a-z]+[A-Z]\w*", t): return False  # camelCase
    if re.fullmatch(r"[A-Za-z]+_[A-Za-z_0-9]+", t): return False
    if "Il2Cpp" in t or "System." in t or "Unity" in t[:6]: return False
    return True
for name in ("assets", "code"):
    xs = [s for s in json.load(open(os.path.join(W, name+"_raw.json"), encoding="utf-8")) if ok(s)]
    json.dump(xs, open(os.path.join(W, name+"_f.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(name, len(xs))
