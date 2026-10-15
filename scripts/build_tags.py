from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
F="/usr/share/fonts/opentype/inter/"
f=lambda n,s: ImageFont.truetype(F+n,s)
W,H=1080,1350
BG=(27,15,58);PINK=(255,79,154);CY=(34,211,238);CR=(255,246,229);LAV=(217,208,242)
P="photos/"; O="out/"
def ctext(d,cx,y,t,font,fill):
    w=d.textlength(t,font=font); d.text((cx-w/2,y),t,font=font,fill=fill)
CROP={"186357cb":(19,24,13,22),"2a087cb5":(3,0,0,0),"86a3adcf":(14,3,0,0),"992dda34":(3,3,0,0),"e7b64a48":(0,0,12,5)}
def card(fn,width=560):
    c=Image.open(P+fn).convert("RGBA"); l,t,r,b=CROP[fn[:8]]
    c=c.crop((l,t,c.width-r,c.height-b))
    c=c.resize((width,round(width*1.4)),Image.LANCZOS)
    m=Image.new("L",c.size,0);ImageDraw.Draw(m).rounded_rectangle([0,0,*c.size],radius=26,fill=255);c.putalpha(m)
    return c
def tag(fn,name,num,rar,price,out):
    im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
    c=card(fn); x=(W-c.width)//2; y=320
    sh=Image.new("RGBA",(c.width+120,c.height+120),(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle([60,75,c.width+60,c.height+75],radius=22,fill=(0,0,0,160))
    sh=sh.filter(ImageFilter.GaussianBlur(18)); im.paste(sh,(x-60,y-60),sh); im.paste(c,(x,y),c)
    d=ImageDraw.Draw(im)
    # NEW label
    d.rounded_rectangle([60,70,330,140],radius=35,fill=CY); d.text((95,84),"NEW · NM",font=f("Inter-ExtraBold.otf",36),fill=BG)
    # price sticker
    s=Image.new("RGBA",(300,300),(0,0,0,0));sd=ImageDraw.Draw(s)
    sd.ellipse([8,8,292,292],fill=PINK+(255,),outline=CR+(255,),width=8)
    pf=f("Inter-ExtraBold.otf",74); t=f"${price}"
    sd.text((150-sd.textlength(t,font=pf)/2,100),t,font=pf,fill=CR)
    s=s.rotate(12,expand=True,resample=Image.BICUBIC); im.paste(s,(740,90),s)
    d=ImageDraw.Draw(im)
    ctext(d,W/2,y+c.height+55,f"{name} {num}",f("Inter-ExtraBold.otf",56),CR)
    d.text((70,H-95),f"ROD TCG · {rar}",font=f("Inter-ExtraBold.otf",36),fill=PINK)
    im.save(O+out); print(out,c.size)
tag("e7b64a48fab22796037f562b4f8f4838.jpg","Maushold","146/128","Illustration Rare","14.99","oct19_s2_maushold.png")
tag("992dda3441f683df9a27afc70eca0a48.jpg","Zapdos","133/128","Illustration Rare","9.99","oct19_s3_zapdos.png")
tag("186357cb03f6b1ac51f97bb1ebec105c.jpg","Articuno","132/128","Illustration Rare","8.99","oct19_s4_articuno.png")
tag("2a087cb5e66f42fecef892c9f778f2eb.jpg","Morpeko","135/128","Illustration Rare","7.99","oct19_s5_morpeko.png")
tag("86a3adcf38231847bb470b30ac31d987.jpg","Clefairy","094/088","Perfect Order · Illustration Rare","18.99","oct21_clefairy.png")
# cover
im=Image.new("RGB",(W,H),PINK);d=ImageDraw.Draw(im)
d.rounded_rectangle([70,90,560,160],radius=35,fill=BG); d.text((105,104),"JUST LISTED · ALL NM",font=f("Inter-ExtraBold.otf",36),fill=CY)
d.text((70,380),"30th\nCelebration\nIllustration\nRares",font=f("Inter-Black.otf",130),fill=BG,spacing=0)
d.text((70,1060),"Swipe →",font=f("Inter-ExtraBold.otf",70),fill=CR)
d.text((70,H-95),"ROD TCG",font=f("Inter-ExtraBold.otf",44),fill=BG)
im.save(O+"oct19_s1_cover.png")
