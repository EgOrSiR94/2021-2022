x = 10
y = 10
e = 200
v = 200
def setup():
    size(600,400)
def draw():
    global x,y,e,v
    background(10)
    rect(10,10,x,y)
    fill(random(0,255),random(0,200),random(0,100))
    rect(110,10,y,x)
    fill(random(0,255),random(0,200),random(0,100))
    rect(210,100,e,v)
    fill(random(0,255),random(0,200),random(0,100))
    rect(410,100,v,e)
    fill(random(0,100),random(0,200),random(0,255))
    x +=1
    y +=1
    e -=1
    v -=1
    
