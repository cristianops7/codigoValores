a31=[6,	0,	-6,	6,	0,	-6,	0	,0]	;
a7=[24,	6,	6	,-6,	-6,	6,	-6,	-24];
a11=[16,20,	4,	-4,	10,	-16,	-10,	-20];
a13=[12,12,18,12,	-12,-12,-12,-18];
a17=[4,-4,16,14,4,-4,-16,-14];
a19=[0,18,0,0,12,0,-18,-12];
a23=[22,2,-2,2,-2,8,-22,-8];
a29=[10,8,10,-10,-8,-10,2,-2];
g=[7,11,13,17,19,23,29,31];
function  calequal(borda,ajz) 
  g=[7,11,13,17,19,23,29,31];
  multiplos=1;
  for m=1:borda
    multiplos*=g(m);
  endfor
  #fim=multiplos*30+multiplos;  
  u=[];
  fim=g(borda)*g(borda)*4+multiplos*30;
  for i=1:(borda-1)
    naoPrimo=[g(i)*(g(i)+ajz(i)):g(i)*30:fim];  #ajustes
    u=union(u,naoPrimo);
  endfor
  naoPrimoBorda=[g(borda)*(g(borda)+ajz(borda)):g(borda)*30:fim];   #ajustes
  diferentes=setdiff(naoPrimoBorda,u);
  primeiro=diferentes(1);
  ultimo=multiplos*30+primeiro;
  i=1;
  subsetdiffes=[];
  while (diferentes(i)<ultimo)    
    subsetdiffes=union(subsetdiffes,diferentes(i));
    i+=1;
  endwhile
  nome=["Resto29",'-',num2str( g(borda)),'-',num2str( multiplos),".txt"];  #ajustes
  #csvwrite(nome,subsetdiffes);
  
  
  
  passos=multiplos*30;
  gerador=g(borda);
  quantidade=length(subsetdiffes);
  ultimo=subsetdiffes(quantidade);
  
   #passos=termos(1);
   #gerador=termos(2);
   #quantidade=length(termos);
  printf(" %d; %d ; %d ; %d\n",passos , gerador, quantidade, ultimo); 
endfunction


maxBorda=6

for borda=2:maxBorda
  calequal(borda,a7);  
  calequal(borda,a11); 
  calequal(borda,a13); 
  calequal(borda,a17); 
  calequal(borda,a19); 
  calequal(borda,a23); 
  calequal(borda,a29); 
  calequal(borda,a31); 
endfor
printf("passos;gerador;quantidade;ultimo\n");



