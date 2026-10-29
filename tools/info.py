import UnityPy, sys
d=r"C:\Program Files (x86)\Steam\steamapps\common\Schedule I\Schedule I_Data"
env=UnityPy.load(d+r"\globalgamemanagers")
for o in env.objects:
    if o.type.name=="PlayerSettings":
        t=o.read_typetree()
        print("bundleVersion",t.get("bundleVersion"),"product",t.get("productName"))
    if o.type.name=="BuildSettings":
        t=o.read_typetree(); print("unity",t.get("m_Version"))
