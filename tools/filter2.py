import json, re
BAD = re.compile(r"(exception|null|parse|index|texture|shader|buffer|seriali[sz]|socket|transport|\bRSA\b|xml|json|regex|stream|connection|\bbytes?\b|hash|\btype\b|method|constructor|argument|assembly|attribute|encoding|culture|\buri\b|http|thread|\block\b|async|\btask\b|array|collection|generic|\bcalled\b|instance|component|gameobject|prefab|\bid\b|\bguid\b|steam(?!ing)|lobby|server|client|packet|rpc|sync|cert|cipher|\bkey\b|delegate|interface|enum|struct|\bfield\b|property|parameter|capacity|offset|\bnode\b|schema|namespace|mesh|material|render|bone|vertex|vertices|atlas|glyph|font asset|sprite|canvas|animator|navmesh|collider|rigidbody|\bscene\b|\bpath\b|directory|file|\bint\b|\bfloat\b|\bbool\b|\bstring\b|object|unable|internal|invalid|failed|cannot|can't find|could not|not found|not supported|must be|should not|attempt|warning|error|debug|\bmono\b|unity|il2cpp|fishnet|network|initiali[sz]|instantiat|destroy|deprecated|obsolete|\bset to\b|\bset as\b|\breceived\b|queue|callback|\bloaded\b|\bloading\b|\bsav(ed|ing)\b|config|registr|\bplugin|module|\bnpc\b|\bpool\b|\bslot\b|\bcount\b|\bquantity\b|addressable|bundle|handler|request|response|\bpoll\b)", re.I)
LOCALE = re.compile(r"^[A-Z][a-z]+( [A-Z][a-z]+)? \([^)]*\)$")
xs = json.load(open("work/code_f.json", encoding="utf-8"))
keep = []
for s in xs:
    t = s.strip()
    if BAD.search(t) or LOCALE.match(t): continue
    if re.fullmatch(r"[a-z][a-z0-9 \-]*", t) and " " not in t: continue
    if re.fullmatch(r"[A-Z][A-Za-z0-9]+", t) and re.search(r"[a-z][A-Z]", t): continue  # PascalCase ids
    if re.match(r"^\[.*?\]", t) or t.endswith(("...", ": ", " = ", "=")) and len(t) < 25 and False: continue
    if re.match(r"^\[", t): continue
    keep.append(s)
json.dump(keep, open("work/code_f2.json","w",encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(keep))
import random; random.seed(3)
for s in random.sample(keep, 60): print(repr(s)[:100])
