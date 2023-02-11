# from json import load
# with open("db.json","r",encoding="utf-8")as f:
#     data=load(f)


# with open("db.json","r") as f:
#     data=load(f)
#
# print(data)
#
# print(len(data))
#
# print([m.get("title") for m in data])
#
# print([m.get("title") for m in data if m.get("year")=="2002"])
#
# print([m.get("name") for m in data if m.get("genres")=="comedy"])

# print([m.get("title") for m in data if m.get("year")=="2002"])

from json import load
with open("db.json") as f:
    data=load(f)

lengthy_movie=max(data,key=lambda m:int(m.get("runtime")))
print(lengthy_movie)

shortmovie=min(data,key=lambda m:int(m.get("runtime")))
print(shortmovie)

mc={}
for m in data:
    year=m.get("year")
    if year in mc:
        mc[year]+=1
    else:
        mc[year]=1
print(mc)

#print max
print(max(mc.items(),key=lambda t:t[1]))