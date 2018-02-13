import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
# Lambert Conformal map of lower 48 states.
m = Basemap(width=500000,height=700000,projection='lcc',
            resolution='c',lat_1=30,lat_2=34,lat_0=36,lon_0=127.)

shp_info = m.readshapefile('KOR_adm1','states',drawbounds=True)

popdensity = {
'Chungcheongbuk-do' : 213,
'Chungcheongnam-do' : 251,
'Gangwon-do' : 75,
'Gyeonggi-do' : 1203,
'Gyeongsangbuk-do' : 144,
'Gyeongsangnam-do' : 320,
'Jeollabuk-do' : 236,
'Jeollanam-do' : 163,
'Jeju' : 315,
'Incheon' : 2851,
'Ulsan' : 1057,
'Sejong' : 526,
'Busan' : 4565,
'Seoul' : 16407,
'Daegu' : 2806,
'Daejeon' : 2805,
'Gwangju' : 763
}

# choose a color for each state based on population density.
colors={}
statenames=[]
cmap = plt.cm.hot # use 'hot' colormap
vmin = 0; vmax = 3000 # set range.
for shapedict in m.states_info:
    statename = shapedict['NAME_1']
    # skip DC and Puerto Rico.
    if statename not in ['District of Columbia','Puerto Rico']:
        pop = popdensity[statename]
        # calling colormap with value between 0 and 1 returns
        # rgba value.  Invert color range (hot colors are high
        # population), take sqrt root to spread out colors more.
        colors[statename] = cmap(1.-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
    statenames.append(statename)
# cycle through state names, color each one.
ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(m.states):
    color = rgb2hex(colors[statenames[nshape]]) 
    poly = Polygon(seg,facecolor=color,edgecolor=color)
    ax.add_patch(poly)
plt.title('Korean Population Density')
plt.show()

