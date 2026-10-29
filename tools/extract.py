"""Extrae textos candidatos de Schedule I: MonoBehaviours de los assets y literales de global-metadata.dat."""
import UnityPy, struct, re, json, os, collections
D = r"C:\Program Files (x86)\Steam\steamapps\common\Schedule I\Schedule I_Data"
OUT = os.path.join(os.path.dirname(__file__), "..", "work")
os.makedirs(OUT, exist_ok=True)

def scan(raw):
    i, n = 0, len(raw)
    while i + 4 <= n:
        L = struct.unpack_from("<i", raw, i)[0]
        if 2 <= L <= 4000 and i + 4 + L <= n:
            b = raw[i+4:i+4+L]
            try:
                s = b.decode("utf-8")
                if s.isprintable() or "\n" in s:
                    yield s
                    i += 4 + L; i = (i + 3) & ~3; continue
            except UnicodeDecodeError:
                pass
        i += 4

assets = collections.Counter()
mb_names = collections.defaultdict(set)
files = [f for f in os.listdir(D) if f.endswith(".assets") or re.fullmatch(r"level\d+", f)]
for f in files:
    env = UnityPy.load(os.path.join(D, f))
    for o in env.objects:
        if o.type.name != "MonoBehaviour": continue
        try: raw = o.get_raw_data()
        except Exception: continue
        for s in scan(raw[28:]):  # saltar cabecera m_GameObject/m_Enabled/m_Script
            assets[s] += 1
    print(f, len(assets))

# literales de código
m = open(os.path.join(D, r"il2cpp_data\Metadata\global-metadata.dat"), "rb").read()
sanity, ver, litOff, litSize, dataOff, dataSize = struct.unpack_from("<6I", m, 0)
print("metadata v", ver)
code = set()
for k in range(litSize // 8):
    ln, idx = struct.unpack_from("<II", m, litOff + k*8)
    try: code.add(m[dataOff+idx: dataOff+idx+ln].decode("utf-8"))
    except UnicodeDecodeError: pass
json.dump(sorted(assets), open(os.path.join(OUT, "assets_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(sorted(code), open(os.path.join(OUT, "code_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(assets), len(code))
