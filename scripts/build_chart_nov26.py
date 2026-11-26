# Nov 26 market post: Mew ex FR 158/128 refresh. Run from repo root.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
F="/usr/share/fonts/opentype/inter/"
def f(n,s):
    for c in (F+n, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(c): return ImageFont.truetype(c,s)
W,H=1080,1350
BG=(27,15,58);PINK=(255,79,154);CY=(34,211,238);CR=(255,246,229);LAV=(217,208,242)
im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
d.text((70,80),"MEW EX  FUTURISTIC RARE",font=f("Inter-Bold.otf",40),fill=CY)
d.text((70,150),"~$31",font=f("Inter-ExtraBold.otf",190),fill=PINK)
d.text((70,420),"tracker price, Nov 26*",font=f("Inter-Regular.otf",42),fill=CR)
d.text((70,480),"Down from about $46 on Oct 23",font=f("Inter-Regular.otf",34),fill=LAV)
x0,x1,y0,y1=110,970,740,1140
# x = days since Sep 25 over the 62 days to Nov 26
pts=[(0,119,"$119","Sep 25"),(22/62,55,"~$55","Oct 17"),(28/62,46,"~$46","Oct 23"),(1,31,"~$31","Nov 26")]
def P(x,v): return (x0+x*(x1-x0), y1-(v/130)*(y1-y0))
for g in (0,.5,1): d.line([(x0,y1-g*(y1-y0)),(x1,y1-g*(y1-y0))],fill=(58,42,107),width=2)
xy=[P(p[0],p[1]) for p in pts]
d.line(xy,fill=PINK,width=8,joint="curve")
for (x,y) in xy: d.ellipse([x-14,y-14,x+14,y+14],fill=CR,outline=PINK,width=5)
lf=f("Inter-Bold.otf",34);sf=f("Inter-Regular.otf",28)
offs=[(25,-85),(-40,-105),(25,-90),(-85,-100)]
for (x,y),p,(dx,dy) in zip(xy,pts,offs):
    d.text((x+dx,y+dy),p[2],font=lf,fill=CR);d.text((x+dx,y+dy+40),p[3],font=sf,fill=LAV)
c=Image.open("assets/mew_ex_158_128.png").convert("RGBA").resize((300,419))
m=Image.new("L",c.size,0);ImageDraw.Draw(m).rounded_rectangle([0,0,*c.size],radius=18,fill=255);c.putalpha(m)
sh=Image.new("RGBA",(c.width+60,c.height+60),(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle([30,40,c.width+30,c.height+40],radius=18,fill=(0,0,0,150))
sh=sh.filter(ImageFilter.GaussianBlur(14))
canvas=Image.new("RGBA",(420,540),(0,0,0,0));canvas.alpha_composite(sh,(30,30));canvas.alpha_composite(c,(60,50))
im.paste(canvas,(640,40),canvas)
d=ImageDraw.Draw(im)
lf2=f("Inter-Bold.otf",30);t="Mew ex FR 158/128"
d.text((640+60+150-d.textlength(t,font=lf2)/2,590),t,font=lf2,fill=CR)
d.text((70,1220),"*Trackers ~$29.50-32 on Nov 26; earlier points approximate.",font=sf,fill=LAV)
d.text((70,1265),"ROD TCG",font=f("Inter-ExtraBold.otf",44),fill=PINK)
im.save("posts/2026-11/nov26_mew_chart.png")
