import struct, json
D = r"C:\Program Files (x86)\Steam\steamapps\common\Schedule I\Schedule I_Data\il2cpp_data\Metadata\global-metadata.dat"
m = open(D,"rb").read()
_,_,litOff,litSize,dataOff,_ = struct.unpack_from("<6I", m, 0)
L=[]
for k in range(litSize//8):
    ln, idx = struct.unpack_from("<II", m, litOff+k*8)
    L.append(m[dataOff+idx:dataOff+idx+ln].decode("utf-8","replace"))
json.dump(L, open("work/lits_ordered.json","w",encoding="utf-8"), ensure_ascii=False, indent=0)
for key in [" has been revived.","Raise boiling flask above burner","Sideways slip: ","Spanish (Colombia)","Multiple self-reference within an attribute group is redefined."," set as recruited","Playing effect","Unlock next region"]:
    print(key, [i for i,s in enumerate(L) if s==key])
print(len(L))
