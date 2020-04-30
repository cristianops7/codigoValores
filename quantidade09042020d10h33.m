########################################
# author: Cristiano Porfirio da Silva
# written: 09/04/2020
# Script: quantidade09042020d10h33.m
#          para números não primos
########################################
function qtnp1 = qt2023(index31x)
  %quantidade a cada 30 números
  % os pares, os multiplos de 3 e 5; 
  % e sete dos oitos multiplos de 7 {  49    77     119   133   161   203   217}
  % ficou de fora o 91 que também é multiplo de 7.
  qtnp1=20+23*index31x;
  
endfunction

function qtnp2 = qt91(index31x) 
 qtnp2=floor((index31x-2+7)/7); % quantidade relacionana ao número 91
endfunction

function  qtj=qtjresto(index31x,a,resto)
  g=[7,11,13,17,19,23,29,31];
  qtj=0;
  for i=1:8
    start=floor((g(i)*(g(i)+a(i))-resto)/30);
    qtj=floor( (-(2*g(i)+a(i))+sqrt(4*(index31x-start)+(2*g(i)+a(i))^2))/2);
  endfor
endfunction


function j=qtjMaxj(index31x)

 a7=[24,	6,	6	,-6,	-6,	6,	-6,	-24];
 a11=[16,20,	4,	-4,	10,	-16,	-10,	-20];
 a13=[12,12,18,12,	-12,-12,-12,-18];
 a17=[4,-4,16,14,4,-4,-16,-14];
 a19=[0,18,0,0,12,0,-18,-12];
 a23=[22,2,-2,2,-2,8,-22,-8];
 a29=[10,8,10,-10,-8,-10,2,-2];
  a31=[6,	0,	-6,	6,	0,	-6,	0	,0]	;
 j=qtjresto(index31x,a7,7);
 j+=qtjresto(index31x,a11,11);
 j+=qtjresto(index31x,a13,13);
 j+=qtjresto(index31x,a17,17);
 j+=qtjresto(index31x,a19,19);
 j+=qtjresto(index31x,a23,23);
 j+=qtjresto(index31x,a29,29);
  j+=qtjresto(index31x,a31,31);
endfunction

function qtnp3 = qtnp731(index31x)
  lprimos=1500
  p1=vlprimos(lprimos);
  p2=[1;(p1-1)];
  i=2;  % os primeiros multiplos de 11 -> 1*6/(7*11);
  qtnp3=0;
  temp=floor((8*index31x*prod(p2(1:i))/prod(p1(1:i))));
  while (temp>=8)&&(i<lprimos) % minimo a ser considerado pode  variar?
      qtnp3+=temp;
      temp=floor(8*index31x*(prod(p2(1:i))/prod(p1(1:i))));
      i+=1;
  endwhile
endfunction

function p = vlprimos(lprimos)
  #números primos
  g=[7,11,13,17,19,23,29,31];
  p=zeros((lprimos+1),8);
  p+=g;
  gp=30*[0:(lprimos)];
  p=p+gp';
  p=p(:);
  p=setdiff(isprime(p).*p,[0]);
endfunction

numero=1000000000;
#numero= 7919
#numero=541
index31=floor((numero-2)/30);
qtprimos=numero -qt2023(index31) - qtnp731(index31) -qt91(index31);
p1=qtjMaxj(index31);