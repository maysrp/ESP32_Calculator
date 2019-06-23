import time
from machine import Pin,I2C
from esp8266_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(scl=Pin(018), sda=Pin(05), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
a=''
b=''
c=''
d=0
r1=[1,2,3,'a']
r2=[4,5,6,'b']
r3=[7,8,9,'c']
r4=['*',0,'#','d']
dx={'a':'+','b':'-','c':'x','d':'/'}
zx=''
m=False
while 1:
    o1=Pin(26,Pin.OUT)
    o2=Pin(25,Pin.OUT)
    o3=Pin(33,Pin.OUT)
    o4=Pin(32,Pin.OUT)
    v1=Pin(13,Pin.IN,Pin.PULL_UP)
    v2=Pin(12,Pin.IN,Pin.PULL_UP)
    v3=Pin(14,Pin.IN,Pin.PULL_UP)
    v4=Pin(27,Pin.IN,Pin.PULL_UP)
    if not v1.value()&v2.value()&v3.value()&v4.value():
        if v1.value()==0:
            v1o=Pin(13,Pin.OUT)
            o1=Pin(26,Pin.IN,Pin.PULL_UP)
            o2=Pin(25,Pin.IN,Pin.PULL_UP)
            o3=Pin(33,Pin.IN,Pin.PULL_UP)
            o4=Pin(32,Pin.IN,Pin.PULL_UP)
            z=[o1.value(),o2.value(),o3.value(),o4.value()]
            j=0
            for i in z:
                if i==0:
                    # print(r1[j])
                    k=r1[j]
                j+=1
        elif v2.value()==0:
            v2o=Pin(12,Pin.OUT)
            o1=Pin(26,Pin.IN,Pin.PULL_UP)
            o2=Pin(25,Pin.IN,Pin.PULL_UP)
            o3=Pin(33,Pin.IN,Pin.PULL_UP)
            o4=Pin(32,Pin.IN,Pin.PULL_UP)
            z=[o1.value(),o2.value(),o3.value(),o4.value()]
            j=0
            for i in z:
                if i==0:
                    k=r2[j]            
                j+=1
        elif v3.value()==0:
            v3o=Pin(14,Pin.OUT)
            o1=Pin(26,Pin.IN,Pin.PULL_UP)
            o2=Pin(25,Pin.IN,Pin.PULL_UP)
            o3=Pin(33,Pin.IN,Pin.PULL_UP)
            o4=Pin(32,Pin.IN,Pin.PULL_UP)
            z=[o1.value(),o2.value(),o3.value(),o4.value()]
            j=0
            for i in z:
                if i==0:
                    # print(r3[j])
                    k=r3[j]            
                j+=1
        else:
            v4o=Pin(27,Pin.OUT)
            o1=Pin(26,Pin.IN,Pin.PULL_UP)
            o2=Pin(25,Pin.IN,Pin.PULL_UP)
            o3=Pin(33,Pin.IN,Pin.PULL_UP)
            o4=Pin(32,Pin.IN,Pin.PULL_UP)
            z=[o1.value(),o2.value(),o3.value(),o4.value()]
            j=0
            for i in z:
                if i==0:
                    k=r4[j]
                j+=1
        if type(k)==int or k=='*':
            if len(b)==0:
                if k =='*' and '.' not in a:
                    if len(a)==0:
                        a+='0.'
                    else:
                        a+='.'
                else:
                    a+=str(k)
                zx=a
            else:
                if k =='*' and '.' not in c:
                    if len(c)==0:
                        c+='0.'
                    else:
                        c+='.'
                else:
                    c+=str(k)
                zx=a+dx[b]+c
        elif k in ['a','b','c','d'] and len(a)!=0 and len(c)==0:
            b=k
            zx=a+dx[b]
        elif k in ['a','b','c','d'] and len(a)==len(c)==0:
            a=str(d)
            b=k
            zx=a+dx[b]
        elif k in ['a','b','c','d'] and len(c)>0:
            aa=a
            cc=c
            a=float(a)
            c=float(c)
            if b=='a':
                d=a+c
            elif b=='b':
                d=a-c
            elif b=='c':
                d=a*c
            else:
                if c!=0:
                    d=a/c
                else:
                    c=''
            print('END',aa,dx[b],cc,'=',d)
            zx=aa+dx[b]+cc+'='+str(d)
            a=str(d)
            b=k
            c=''
            m=True
        elif k =='#' and len(c)!=0:
            aa=a
            cc=c
            a=float(a)
            c=float(c)
            if b=='a':
                d=a+c
            elif b=='b':
                d=a-c
            elif b=='c':
                d=a*c
            else:
                if c!=0:
                    d=a/c
                else:
                    c=''
            print('END',aa,dx[b],cc,'=',d)
            zx=aa+dx[b]+cc+'='+str(d)
            a=''
            b=''
            c=''
            m=True
        else:
            zx=''
            a=''
            b=''
            c=''
            d=''
        time.sleep(0.4)
        lcd.clear()
        lcd.putstr(zx)
        if m:
            if len(a)>0 and len(b)>0:
                zx=a+dx[b]
            else:
                zx=''
            m=False
