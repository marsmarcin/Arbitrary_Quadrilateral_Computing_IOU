import numpy as np 

def line_slope(x1,y1,x2,y2,x3,y3,x4,y4):
        k1=(y2-y1)/(x2-x1)
        k2=(y3-y2)/(x3-x2)
        k3=(y4-y3)/(x4-x3)
        k4=(y1-y4)/(x1-x4)
        return k1,k2,k3,k4

gx2=923.65
gy2=308.27
gx3=758.05
gy3=342.11
gx4=741.83
gy4=262.68
gx1=907.42
gy1=228.85

# tx1=867.00
# ty1=224.00
# tx2=899.00
# ty2=292.00
# tx3=776.00
# ty3=346.00
# tx4=739.00
# ty4=277.00

# tx1=893.00
# ty1=226.00
# tx2=925.00
# ty2=303.00
# tx3=766.00
# ty3=352.00
# tx4=741.00
# ty4=278.00

tx1=908.00
ty1=215.00
tx2=934.00
ty2=312.00
tx3=752.00
ty3=355.00
tx4=728.00
ty4=252.00

tk1,tk2,tk3,tk4=line_slope(tx1,ty1,tx2,ty2,tx3,ty3,tx4,ty4)

tx=[tx1,tx2,tx3,tx4]
ty=[ty1,ty2,ty3,ty4]

tx_min=int(np.min(tx))
tx_max=int(np.max(tx))
ty_min=int(np.min(ty))
ty_max=int(np.max(ty))


t_ax=[]
t_ay=[]
t_gx=[]
t_gy=[]
st=0

for i in range(tx_min,tx_max+1):
        for j in range(ty_min,ty_max+1):
                l1=int(tk1*(i-tx1)+ty1)
                l2=int(tk2*(i-tx2)+ty2)
                l3=int(tk3*(i-tx3)+ty3)
                l4=int(tk4*(i-tx4)+ty4)
                if((l1<=j)&(l2>=j)&(l3>=j)&(l4<=j)):
                        st=st+1
                        t_ax.append(i)
                        t_ay.append(j)
                

print(st)
gk1,gk2,gk3,gk4=line_slope(gx1,gy1,gx2,gy2,gx3,gy3,gx4,gy4)

gx=[gx1,gx2,gx3,gx4]
gy=[gy1,gy2,gy3,gy4]

gx_min=int(np.min(gx))
gx_max=int(np.max(gx))
gy_min=int(np.min(gy))
gy_max=int(np.max(gy))

sg=0

for i in range(gx_min,gx_max+1):
        for j in range(gy_min,gy_max+1):
                l1=int(gk1*(i-gx1)+gy1)
                l2=int(gk2*(i-gx2)+gy2)
                l3=int(gk3*(i-gx3)+gy3)
                l4=int(gk4*(i-gx4)+gy4)
                if((l1<=j)&(l2>=j)&(l3>=j)&(l4<=j)):
                        sg=sg+1
                        t_gx.append(i)
                        t_gy.append(j)
                
print(sg)

t_a=[[0,0] for i in range(0,len(t_ax))]
t_g=[[0,0] for i in range(0,len(t_gx))]

for num in range(0,len(t_ax)):
        t_a[num][0]=t_ax[num]
        t_a[num][1]=t_ay[num]
for num in range(0,len(t_gx)):
        t_g[num][0]=t_gx[num]
        t_g[num][1]=t_gy[num]

# if(t_a[0]==t_g[0]):
#         print("aaa")
# else:
#         print("bbb")
iu=0
for m in range(0,len(t_ax)):
        for n in range(0,len(t_gx)):
                if(t_a[m]==t_g[n]):
                        iu=iu+1
iou=iu/(st+sg-iu)

print(iou)




