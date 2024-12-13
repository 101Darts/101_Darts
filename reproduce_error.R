library(pracma)

fp <- function(d,r){
	rt = 1/(sqrt(2*pi)*e1)*exp(-1*(r*cos(d)-u1)^2/(2*(e1^2)))
	rt = rt*1/(sqrt(2*pi)*e2)*exp(-1*(r*sin(d)-u2)^2/(2*(e2^2)))
	rt = rt*r	
	return(rt)
}

u1=0; u2=7.5; e1=1.5; e2=8.6;
d1=2.67; d2=2.985; r1=2.1; r2=10.1;


#AIM SC12 (-4.410, 6.070) => OBJ SC5 dg(1.728,2.042) Radius(2.100, 10.100) 
u1=-4.41; u2=6.07; e1=0.1; e2=0.2;
d1=1.728; d2=2.042; r1=2.1; r2=10.1;

#AIM SC5 (-2.320, 7.130) => OBJ D20 dg(1.414,1.728) Radius(17.300, 19.100) 
u1=-2.32; u2=7.13; e1=0.1; e2=0.4;
d1=1.414; d2=1.728; r1=17.3; r2=19.1;



val=integral2(fp,d1,d2,r1,r2);





pb=val[['Q']];
cat(sprintf("%.4f\n",pb)); 