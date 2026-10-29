"""Une work/out/*.txt en Translation/es/Text/ScheduleI_es.txt validando el formato de XUnity."""
import re, glob, os
seen, lit, rx, bad = set(), [], [], []
def split(line):
    # separa por el primer '=' no escapado
    for m in re.finditer(r"(?<![\x5c])=", line):
        return line[:m.start()], line[m.end():]
    return None
for f in sorted(glob.glob("work/out/c*.txt")):
    for line in open(f, encoding="utf-8-sig"):
        line = line.rstrip("\r\n")
        if not line.strip(): continue
        p = split(line)
        if not p or not p[1].strip(): bad.append((f, line)); continue
        k, v = p
        if k == v: continue
        if k in seen: continue
        seen.add(k)
        if k.startswith(("r:", "sr:")):
            m = re.fullmatch(r'(s?r):"(.*)"', k)
            try: re.compile(m.group(2)); rx.append(line)
            except Exception as e: bad.append((f, line))
        else: lit.append(line)
os.makedirs("Translation/es/Text", exist_ok=True)
with open("Translation/es/Text/ScheduleI_es.txt", "w", encoding="utf-8", newline="\n") as o:
    o.write("\n".join(lit) + "\n")
with open("Translation/es/Text/ScheduleI_es_regex.txt", "w", encoding="utf-8", newline="\n") as o:
    o.write("\n".join(rx) + "\n")
print("literales", len(lit), "regex", len(rx), "descartadas", len(bad))
for b in bad[:15]: print("  ", b)
