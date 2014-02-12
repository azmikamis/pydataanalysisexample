from lxml import etree
import pandas as pd

tree = etree.parse("data/plaques_20130119.xml")
root = tree.getroot()

output = {}
output['uri'] = []
output['raw'] = []
output['crs'] = []
output['lon'] = []
output['lat'] = []

for each in root.xpath('/openplaques/plaque/geo'):
    # check what we got back
    output['uri'].append(each.getparent().attrib['uri'])
    output['crs'].append(each.get('reference_system'))
    output['lon'].append(each.get('longitude'))
    output['lat'].append(each.get('latitude'))
    # now go back up to plaque
    r = each.getparent().xpath('inscription/raw')[0]
    if isinstance(r.text, str):
        output['raw'].append(r.text.lstrip().rstrip())
    else:
        output['raw'].append(None)

df = pd.DataFrame(output)

print len(df)
empty = df[pd.isnull(df.raw)]
#empty = df.apply(lambda col: pd.isnull(col))
#df2 = empty[empty.raw == True]
print len(empty)
print empty.tail()

df = df.replace({'raw': 0}, None)
df = df.dropna()
df[['lon', 'lat']] = df[['lon', 'lat']].astype(float)
print len(df)


