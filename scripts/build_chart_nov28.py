# Nov 28 market post: 30th Celebration Classic Collection Charizard + Lugia. Run from repo root.
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/opentype/inter/"
f=lambda n,s: ImageFont.truetype(F+n,s)
W,H=1080,1350
BG=(27,15,58);PINK=(255,79,154);CY=(34,211,238);CR=(255,246,229);LAV=(217,208,242);GRID=(58,42,107);OLD=(104,86,160)
im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
def ctext(cx,y,t,font,fill): d.text((cx-d.textlength(t,font=font)/2,y),t,font=font,fill=fill)
d.text((70,80),"30TH CELEBRATION  CLASSIC COLLECTION",font=f("Inter-Bold.otf",38),fill=CY)
d.text((70,160),"Cooling off",font=f("Inter-ExtraBold.otf",140),fill=PINK)
d.text((70,360),"Charizard and Lugia, past 30 days*",font=f("Inter-Regular.otf",42),fill=CR)
# legend
for x,col,t in ((70,OLD,"30 days earlier"),(420,PINK,"Nov 26")):
    d.rounded_rectangle([x,450,x+34,484],radius=8,fill=col); d.text((x+50,450),t,font=f("Inter-Regular.otf",30),fill=LAV)
base,top,vmax=1050,590,200
d.line([(70,base),(1010,base)],fill=GRID,width=3)
for cx,name,old,new,chg in ((305,"Charizard",156.15,104.86,"-33%"),(775,"Lugia",196.70,120.15,"-39%")):
    for off,v,col in ((-85,old,OLD),(85,new,PINK)):
        y=base-(v/vmax)*(base-top)
        d.rounded_rectangle([cx+off-70,y,cx+off+70,base],radius=16,fill=col,corners=(True,True,False,False))
        ctext(cx+off,y-55,f"${v:.0f}",f("Inter-Bold.otf",40),CR)
    ctext(cx,1075,name,f("Inter-ExtraBold.otf",52),CR)
    ctext(cx,1142,chg,f("Inter-Bold.otf",40),CY)
sf=f("Inter-Regular.otf",28)
d.text((70,1220),"*PokeScope market prices, raw copies. Trackers vary.",font=sf,fill=LAV)
d.text((70,1265),"ROD TCG",font=f("Inter-ExtraBold.otf",44),fill=PINK)
im.save("posts/2026-11/nov28_classic_chart.png")
