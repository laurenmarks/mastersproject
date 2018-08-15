import sys
import re
import pandas as pd


s=sys.stdin.read()

#var chr_6_area = drawArea('chr_6_area', 'Distribution of variants on chromosome 6', google.visualization.arrayToDataTable([['Position (mb)','Count'],['0',1884],['1',1855],['2',1879],['3',1702],['4',1787],['5',1916],['6',2250],['7',2262],['8',2478],['9',1813],['10',2022],['11',2106],['12',1682],['13',1637],['14',1705],['15',1748],['16',1318],['17',1834],['18',2002],['19',1312],['20',2166],['21',1610],['22',2161],['23',2462],['24',2123],['25',1834],['26',2090],['27',1541],['28',1485],['29',5282],['30',2335],['31',7023],['32',12489],['33',3449],['34',2008],['35',1361],['36',1352],['37',1933],['38',1509],['39',1301],['40',1528],['41',1702],['42',1499],['43',882],['44',1704],['45',1319],['46',1355],['47',1659],['48',1613],['49',1462],['50',1610],['51',1633],['52',1514],['53',1733],['54',1787],['55',1866],['56',1102],['57',12092],['58',1260],['59',0],['60',0],['61',405],['62',2100],['63',2626],['64',953],['65',1627],['66',2659],['67',2819],['68',2281],['69',1946],['70',2008],['71',1203],['72',1491],['73',1470],['74',2337],['75',936],['76',1902],['77',2233],['78',1683],['79',1614],['80',1543],['81',2871],['82',1862],['83',1184],['84',589],['85',2172],['86',1806],['87',1964],['88',1436],['89',1267],['90',1161],['91',1369],['92',1308],['93',1694],['94',1461],['95',1094],['96',1959],['97',1170],['98',1372],['99',1536],['100',1609],['101',2202],['102',1665],['103',2487],['104',1182],['105',1231],['106',1551],['107',1861],['108',1503],['109',1154],['110',987],['111',1235],['112',1220],['113',1761],['114',1540],['115',1888],['116',1286],['117',1758],['118',1630],['119',1584],['120',2247],['121',1609],['122',1572],['123',1672],['124',1609],['125',1339],['126',663],['127',1136],['128',999],['129',1862],['130',1440],['131',848],['132',1020],['133',1149],['134',1591],['135',1223],['136',754],['137',2011],['138',1083],['139',1809],['140',1053],['141',1827],['142',1195],['143',1468],['144',989],['145',1318],['146',789],['147',900],['148',2092],['149',1855],['150',2086],['151',2296],['152',1613],['153',2382],['154',1385],['155',1455],['156',1557],['157',1146],['158',2134],['159',2363],['160',1791],['161',2156],['162',2198],['163',1831],['164',1916],['165',2142],['166',2400],['167',2018],['168',2059],['169',2455],['170',1496],['171',65]]), {hAxis: {title: "Position (mb)", textStyle: {fontSize: 8}}, legend: {position: "none"}});

g=re.compile('var chr_6_area = .*google.visualization.arrayToDataTable\((\[.*\])\).*;').search(s).group(1)

l=eval(g)

h1, h2,=l[0]

d={h1:[],h2:[]}

for x in l[1:]:
	d[h1]+=[x[0]]
	d[h2]+=[x[1]]

df = pd.DataFrame(data=d)
print(df.to_csv(index=False))