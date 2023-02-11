from products.models import mobiles
#
# print(len(mobiles))
#
# for mob in mobiles:
#     print(mob["name"])

# print([m.get("name") for m in mobiles ])
# def get_name(obj):
#     return obj.get("price")
print([m.get('name')for m in mobiles if 'samsung' in m.get("brand")])


print(max(mobiles,key=lambda x:x['price']))

print(sorted(mobiles,reverse=True,key=lambda x:x['price']))



