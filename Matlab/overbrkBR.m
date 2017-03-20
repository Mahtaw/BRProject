function  overbrkBR(isRandom,FlowRate, path)
format long
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
   cd (path)
   path;
   P= 0.35;
   V=400;%cm3
   
for ii=1:200
    brekthroughN=['breakthrough' num2str(ii) '.out'];
    breakthrough_ith = BreakthroughImporter(brekthroughN, 3,size(brekthroughN));
    if ii==1
        BreakthroughTime=breakthrough_ith(:,1);
    end

    BreakthroughBr(:,ii)=breakthrough_ith(:,2);

end
velocityOutlet = VelocImporter('velocity1.out', 5, 40004);
velocityOutletYdirection=velocityOutlet(end-199:end,4)';
for ii=1:size(BreakthroughBr,1)
    BrekathroughBrOverall(ii,1)=sum(BreakthroughBr(ii,:).*velocityOutletYdirection)/sum(velocityOutletYdirection);

end
PoreVolume=[((BreakthroughTime*60)*FlowRate)/140];
 brk=[BreakthroughTime,BrekathroughBrOverall];
if isRandom
    randbrk =randsample(1:size(brk),1000);
    R=brk(randbrk,:);
    RandSortBrk=sort (R);
    dlmwrite(['R' '.csv'],R, 'delimiter', ',', 'precision', 9)
    dlmwrite(['RandSortBrk' '.csv'],RandSortBrk, 'delimiter', ',', 'precision', 9)
end
dlmwrite(['brk' '.csv'],brk, 'delimiter', ',', 'precision', 9)
end

