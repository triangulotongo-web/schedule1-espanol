import UnityPy, collections
d=r"C:\Program Files (x86)\Steam\steamapps\common\Schedule I\Schedule I_Data"
env=UnityPy.load(d+r"\resources.assets")
c=collections.Counter(o.type.name for o in env.objects); print(c.most_common(15))
for o in env.objects:
    if o.type.name=="MonoBehaviour":
        print("has typetree:", o.serialized_type.node is not None if o.serialized_type else None); break
