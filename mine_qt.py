#!/usr/bin/python3

from tkinter import *


root = Tk()
root.geometry('400x150')

cvar = 1
svar = 1


def shiftf():
    global svar
    svar = svar+1
    root.focus_set()
    return svar

def minusf():
    if svar % 2 == 0:
        print("_")
    else:
        print("-")
    root.focus_set()


def plusf():
    if svar % 2 == 0:
        print("+")
    else:
        print("=")
    root.focus_set()


def opbrf():
    if svar % 2 == 0:
        print("{")
    else:
        print("[")
    root.focus_set()


def clbrf():
    if svar % 2 == 0:
        print("}")
    else:
        print("]")
    root.focus_set()


def bcslashf():
    if svar % 2 == 0:
        print("|")
    else:
        print("\\")
    root.focus_set()


def quesf():
    if svar % 2 == 0:
        print("?")
    else:
        print("/")
    root.focus_set()


def colmf():
    if svar % 2 == 0:
        print(":")
    else:
        print(";")
    root.focus_set()


def aphf():
    if svar % 2 == 0:
        print('"')
    else:
        print("'")
    root.focus_set()


def grf():
    if svar % 2 == 0:
        print("<")
    else:
        print(",")
    root.focus_set()


def lessf():
    if svar % 2 == 0:
        print(">")
    else:
        print(".")
    root.focus_set()


def tildf():
    print("~")
    root.focus_set()


def onef():
    print(int("1"))
    root.focus_set()


def twof():
    print(int("2"))
    root.focus_set()


def threef():
    print(int("3"))
    root.focus_set()


def fourf():
    print(int("4"))
    root.focus_set()


def fivef():
    print(int("5"))
    root.focus_set()


def sixf():
    print(int("6"))
    root.focus_set()


def sevenf():
    print(int("7"))
    root.focus_set()


def eightf():
    print(int("8"))
    root.focus_set()


def ninef():
    print(int("9"))
    root.focus_set()


def zerof():
    print(int("0"))
    root.focus_set()


def backf():
    print("\b")
    root.focus_set()


def tabf():
    print("    ")
    root.focus_set()


def enterf():
    print("\n")
    root.focus_set()


def space():
    print(" ")
    root.focus_set()


def capsf():
    global cvar
    cvar = cvar+1
    root.focus_set()
    return cvar


def af():
    global cvar
    if cvar % 2 == 0:
        print("A")
    else:
        print("a")
    root.focus_set()


def bf():
    global cvar
    if cvar % 2 == 0:
        print("B")
    else:
        print("b")
    root.focus_set()


def cf():
    global cvar
    if cvar % 2 == 0:
        print("C")
    else:
        print("c")
    root.focus_set()


def df():
    global cvar
    if cvar % 2 == 0:
        print("D")
    else:
        print("d")
    root.focus_set()


def ef():
    global cvar
    if cvar % 2 == 0:
        print("E")
    else:
        print("e")
    root.focus_set()


def ff():
    global cvar
    if cvar % 2 == 0:
        print("F")
    else:
        print("f")
    root.focus_set()


def gf():
    global cvar
    if cvar % 2 == 0:
        print("G")
    else:
        print("g")
    root.focus_set()


def hf():
    global cvar
    if cvar % 2 == 0:
        print("H")
    else:
        print("h")
    root.focus_set()


def iff():
    global cvar
    if cvar % 2 == 0:
        print("I")
    else:
        print("i")
    root.focus_set()


def jf():
    global cvar
    if cvar % 2 == 0:
        print("J")
    else:
        print("j")
    root.focus_set()


def kf():
    global cvar
    if cvar % 2 == 0:
        print("K")
    else:
        print("k")
    root.focus_set()


def lf():
    global cvar
    if cvar % 2 == 0:
        print("L")
    else:
        print("l")
    root.focus_set()


def mf():
    global cvar
    if cvar % 2 == 0:
        print("M")
    else:
        print("m")
    root.focus_set()


def nf():
    global cvar
    if cvar % 2 == 0:
        print("N")
    else:
        print("n")
    root.focus_set()


def of():
    global cvar
    if cvar % 2 == 0:
        print("O")
    else:
        print("o")
    root.focus_set()


def pf():
    global cvar
    if cvar % 2 == 0:
        print("P")
    else:
        print("p")
    root.focus_set()


def qf():
    global cvar
    if cvar % 2 == 0:
        print("Q")
    else:
        print("q")
    root.focus_set()


def rf():
    global cvar
    if cvar % 2 == 0:
        print("R")
    else:
        print("r")
    root.focus_set()


def sf():
    global cvar
    if cvar % 2 == 0:
        print("S")
    else:
        print("s")
    root.focus_set()


def tf():
    global cvar
    if cvar % 2 == 0:
        print("T")
    else:
        print("t")
    root.focus_set()


def uf():
    global cvar
    if cvar % 2 == 0:
        print("U")
    else:
        print("u")
    root.focus_set()


def vf():
    global cvar
    if cvar % 2 == 0:
        print("V")
    else:
        print("v")
    root.focus_set()


def wf():
    global cvar
    if cvar % 2 == 0:
        print("W")
    else:
        print("w")
    root.focus_set()


def xf():
    global cvar
    if cvar % 2 == 0:
        print("X")
    else:
        print("x")
    root.focus_set()


def yf():
    global cvar
    if cvar % 2 == 0:
        print("Y")
    else:
        print("y")
    root.focus_set()


def zf():
    global cvar
    if cvar % 2 == 0:
        print("Z")
    else:
        print("z")
    root.focus_set()

frame = Frame(root)
frame.pack(side=TOP)

width = '1'

tild = Button(frame, text="~", width=width, bg="black", fg="white", command=tildf)
tild.pack(side=LEFT)

one = Button(frame, text="1", width=width, bg="black", fg="white", command=onef)
one.pack(side=LEFT)

two = Button(frame, text="2",width=width, bg="black", fg="white", command=twof)
two.pack(side=LEFT)

three = Button(frame, text="3",width=width, bg="black", fg="white", command=threef)
three.pack(side=LEFT)

four = Button(frame, text="4", width=width, bg="black", fg="white", command=fourf)
four.pack(side=LEFT)

five = Button(frame, text="5",width=width, bg="black", fg="white", command=fivef)
five.pack(side=LEFT)

six = Button(frame, text="6", width=width, bg="black", fg="white", command=sixf)
six.pack(side=LEFT)

seven = Button(frame, text="7", width=width, bg="black", fg="white", command=sevenf)
seven.pack(side=LEFT)

eight = Button(frame, text="8", width=width, bg="black", fg="white", command=eightf)
eight.pack(side=LEFT)

nine = Button(frame, text="9", width=width, bg="black", fg="white", command=ninef)
nine.pack(side=LEFT)

zero = Button(frame, text="0", width=width, bg="black", fg="white", command=zerof)
zero.pack(side=LEFT)

minus = Button(frame, text="-  _", width=width, bg="black", fg="white", command=minusf)
minus.pack(side=LEFT)

plus = Button(frame, text="=  +", bg="black", fg="white", command=plusf)
plus.pack(side=LEFT)

backspace = Button(frame, text="backspace", bg="black", fg="white", command=backf)
backspace.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack()

tab = Button(frame1, text="Tab", bg="black", fg="white", command=tabf)
tab.pack(side=LEFT)

q = Button(frame1, text="Q", bg="black", fg="white", command=qf)
q.pack(side=LEFT)

w = Button(frame1, text="W", bg="black", fg="white", command=wf)
w.pack(side=LEFT)

e = Button(frame1, text="E", bg="black", fg="white", command=ef)
e.pack(side=LEFT)

r = Button(frame1, text="R", bg="black", fg="white", command=rf)
r.pack(side=LEFT)

t = Button(frame1, text="T", bg="black", fg="white", command=tf)
t.pack(side=LEFT)

y = Button(frame1, text="Y", bg="black", fg="white", command=yf)
y.pack(side=LEFT)

u = Button(frame1, text="U", bg="black", fg="white", command=uf)
u.pack(side=LEFT)

i = Button(frame1, text="I", bg="black", fg="white", command=iff)
i.pack(side=LEFT)

o = Button(frame1, text="O", bg="black", fg="white", command=of)
o.pack(side=LEFT)

p = Button(frame1, text="P", bg="black", fg="white", command=pf)
p.pack(side=LEFT)

opbr = Button(frame1, text="{  [", bg="black", fg="white", command=opbrf)
opbr.pack(side=LEFT)

clbr = Button(frame1, text="}  ]", bg="black", fg="white", command=clbrf)
clbr.pack(side=LEFT)

slash = Button(frame1, text="\\  |", bg="black", fg="white", command=bcslashf)
slash.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

caps = Button(frame2, text="CapsLK", bg="black", fg="white", command=capsf)
caps.pack(side=LEFT)

a = Button(frame2, text="A", bg="black", fg="white", command=af)
a.pack(side=LEFT)

s = Button(frame2, text="S", bg="black", fg="white", command=sf)
s.pack(side=LEFT)

d = Button(frame2, text="D", bg="black", fg="white", command=df)
d.pack(side=LEFT)

f = Button(frame2, text="F", bg="black", fg="white", command=ff)
f.pack(side=LEFT)

g = Button(frame2, text="G", bg="black", fg="white", command=gf)
g.pack(side=LEFT)

h = Button(frame2, text="H", bg="black", fg="white", command=hf)
h.pack(side=LEFT)

j = Button(frame2, text="J", bg="black", fg="white", command=jf)
j.pack(side=LEFT)

k = Button(frame2, text="K", bg="black", fg="white", command=kf)
k.pack(side=LEFT)

le = Button(frame2, text="L", bg="black", fg="white", command=lf)
le.pack(side=LEFT)

semic = Button(frame2, text="; :", bg="black", fg="white", command=colmf)
semic.pack(side=LEFT)

aph = Button(frame2, text="' "+'"', bg="black", fg="white", command=aphf)
aph.pack(side=LEFT)

enter = Button(frame2, text="ENTER", bg="black", fg="white", command=enterf)
enter.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack()

shift = Button(frame3, text="Shift", bg="black", fg="white", command=shiftf)
shift.pack(side=LEFT)

z = Button(frame3, text="Z", bg="black", fg="white", command=zf)
z.pack(side=LEFT)

x = Button(frame3, text="X", bg="black", fg="white", command=xf)
x.pack(side=LEFT)

c = Button(frame3, text="C", bg="black", fg="white", command=cf)
c.pack(side=LEFT)

v = Button(frame3, text="V", bg="black", fg="white", command=vf)
v.pack(side=LEFT)

b = Button(frame3, text="B", bg="black", fg="white", command=bf)
b.pack(side=LEFT)

n = Button(frame3, text="N", bg="black", fg="white", command=nf)
n.pack(side=LEFT)

m = Button(frame3, text="M", bg="black", fg="white", command=mf)
m.pack(side=LEFT)

co = Button(frame3, text=",  <", bg="black", fg="white", command=grf)
co.pack(side=LEFT)

stop = Button(frame3, text=".  >", bg="black", fg="white", command=lessf)
stop.pack(side=LEFT)

sl = Button(frame3, text="/  ?", bg="black", fg="white", command=quesf)
sl.pack(side=LEFT)

shift = Button(frame3, text="Shift", bg="black", fg="white", command=shiftf)
shift.pack(side=LEFT)

up = Button(frame3, text="up", bg="black", fg="white")
up.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack()

exi = Button(frame4, text="exit", bg="black", fg="white", command=root.quit)
exi.pack(side=LEFT)

space = Button(frame4, text="space", width="15", bg="black", fg="white", command=space)
space.pack(side=LEFT)

left = Button(frame4, text="Left", bg="black", fg="white")
left.pack(side=LEFT)

down = Button(frame4, text="Down", bg="black", fg="white")
down.pack(side=LEFT)

right = Button(frame4, text="Right", bg="black", fg="white")
right.pack(side=LEFT)


root.mainloop()
