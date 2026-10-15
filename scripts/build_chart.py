from PIL import Image, ImageDraw, ImageFont
import glob
F="/usr/share/fonts/opentype/inter/"
def f(n,s):
    import os
    for c in (F+n, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(c): return ImageFont.truetype(c,s)
W,H=1080,1350
BG=(27,15,58);PINK=(255,79,154);CY=(34,211,238);CR=(255,246,229);LAV=(217,208,242)
im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
d.text((70,80),"MEW EX  FUTURISTIC RARE",font=f("Inter-Bold.otf",40),fill=CY)
d.text((70,150),"-91%",font=f("Inter-ExtraBold.otf",230),fill=PINK)
d.text((70,420),"in the first week after release",font=f("Inter-Regular.otf",42),fill=CR)
# chart
x0,x1,y0,y1=90,990,700,1150
pts=[(0,1400),(0.55,119),(1,58)]
def P(x,v): return (x0+x*(x1-x0), y1-(v/1400)*(y1-y0))
for g in (0,.5,1): d.line([(x0,y1-g*(y1-y0)),(x1,y1-g*(y1-y0))],fill=(58,42,107),width=2)
xy=[P(a,b) for a,b in pts]
d.line(xy,fill=PINK,width=8,joint="curve")
for (x,y) in xy: d.ellipse([x-14,y-14,x+14,y+14],fill=CR,outline=PINK,width=5)
lf=f("Inter-Bold.otf",34);sf=f("Inter-Regular.otf",28)
d.text((xy[0][0]+40,xy[0][1]-20),"$1,400",font=lf,fill=CR);d.text((xy[0][0]+80,xy[0][1]+22),"launch week",font=sf,fill=LAV);d.text((xy[0][0]+40,xy[0][1]+22),"",font=sf)
d.text((xy[1][0]+40,xy[1][1]-75),"$119",font=lf,fill=CR);d.text((xy[1][0]+40,xy[1][1]-35),"Sep 25",font=sf,fill=LAV)
d.text((xy[2][0]-130,xy[2][1]-90),"~$56–61",font=lf,fill=CR);d.text((xy[2][0]-130,xy[2][1]-50),"Oct 15*",font=sf,fill=LAV)
# card
c=Image.open("assets/mew_ex_158_128.png").convert("RGBA")
c=c.resize((300,419));
m=Image.new("L",c.size,0);ImageDraw.Draw(m).rounded_rectangle([0,0,*c.size],radius=18,fill=255);c.putalpha(m)
sh=Image.new("RGBA",(c.width+60,c.height+60),(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle([30,40,c.width+30,c.height+40],radius=18,fill=(0,0,0,150))
from PIL import ImageFilter
sh=sh.filter(ImageFilter.GaussianBlur(14))
canvas=Image.new("RGBA",(420,540),(0,0,0,0));canvas.alpha_composite(sh,(30,30));canvas.alpha_composite(c,(60,50))
im.paste(canvas,(640,40),canvas)
d=ImageDraw.Draw(im)
lf2=f("Inter-Bold.otf",30);t="Mew ex FR 158/128"
d.text((640+60+150-d.textlength(t,font=lf2)/2,540),t,font=lf2,fill=CR)
d.text((70,1215),"*Tracker estimates vary.",font=sf,fill=LAV)
d.text((70,1265),"ROD TCG",font=f("Inter-ExtraBold.otf",44),fill=PINK)
im.save("out/oct17_mew_chart.png")
