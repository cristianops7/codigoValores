gerador=[7,11,13,17,19,23,29,31];
for i=1:length(gerador)
  for j=1:length(gerador)
    g=gerador(i);
    ajuste=gerador(j)-gerador(i);
    inicio=gerador(j)*gerador(i);
    resto=mod(inicio,30);
    printf("%d ;%d;%d;%d\n",resto,g,inicio,ajuste);
  endfor
endfor
