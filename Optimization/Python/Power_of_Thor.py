a,b,x,y=map(int,raw_input().split())
while 1:print[["","S"][y<b],"N"][y>b]+[["","E"][x<a],"W"][x>a];y+=y<b;y-=y>b
