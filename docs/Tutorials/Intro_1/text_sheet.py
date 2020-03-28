"""
This is a lookup table of all the types of text you can use with Matplotlib
from the get go. Made by Quentin Wach.

1. show all fonts written in their names with the name in a neutral font right above (but small)
2. show a small lorem ipsum of that font beneath
3. rate and sort the fonts

search for more fonts on www.1001fonts.com
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np
import os

"""
# list of all ttf and afm fonts that come with Matplotlib (Adobe fonts excluded)
afm_fonts = sorted(set([f.name for f in matplotlib.font_manager.fontManager.afmlist]))
ttf_fonts = sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))
fonts = ttf_fonts
for font in afm_fonts:
    if font not in ttf_fonts:
        fonts.append(font)
print(fonts)
print(len(fonts))
"""

# A3 FIGURE
fig = plt.figure(figsize=(8.25,11.7), dpi=300, frameon=False) #figsize=(11.7,16.5)

color = "silver"
columns = 2
rows = 15 + 1

alphabet = "Aa Bb Cc Dd Ee Ff Gg Hh \n Ii Jj Kk Ll Mm Nn Oo Pp Qq \n Rr Ss Tt Uu Vv Ww Xx Yy Zz"
lorem = "Lorem Ipsum"

fonts = sorted(["Lobster Two","Open Sans" ,"Roboto", "Ani", "Comic Sans MS", "Arial", "Courier New", "Arial Black"])

f_number = 0
for r in range(rows-1):
    for c in range(columns):
        if f_number < len(fonts):
            # create text box
            ax = plt.subplot2grid((rows,columns),(r,c),facecolor="silver")

            try:
                # add font example
                fontname = fonts[f_number]
                font = ax.text(0.5,0.475, s=alphabet, style="normal", family=fontname, size=10, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
                name = ax.text(-0.03,1.06, s=fontname, fontdict={'fontname':"Open Sans"}, style="normal", size=8, horizontalalignment='left', verticalalignment='top', transform=ax.transAxes, backgroundcolor="white")
                #name.set_in_layout(False)
                font.set_in_layout(False)
                ax.set_xticks([])
                ax.set_yticks([])
            except:
                print(str(fontname) +  " did not render...")

            f_number += 1
        else:
            break

# add bottom info        

info = fig.text(0.5,0.5, "@QuentinWach", size=10)
info.set_in_layout(False)

# adjust spacing between subplots
fig.tight_layout()

# save graphic
plt.savefig("text_sheet.png", bbox_inches="tight")


# Lobster Two, Roboto, GFS Theokritos, Ubuntu, "Helvetica","Baskerville", "Times", "Akzidenz Grotesk", "Gotham", "Bodoni", 
# "Didot", "Futura", "Gill Sans", "Frutiger", "Bembo", "Rockwell", 
# "Frankling Gothic", "Sabon", "Georgia", "Garamond", "News Gothic", "Myriad", "Mrs Eaves", "Minion"]
