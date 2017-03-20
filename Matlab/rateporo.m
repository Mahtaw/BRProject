function rateporo( NoO)
format long
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

load('dataTransfer1.mat')
load('Timepoints1.mat')
for ii=NoO
        rateN=['rate' num2str(ii) '.out'];
        rate_ith = RateImporter(rateN, 5, size(rateN));
        RateBrpoints(:,ii)=rate_ith(:,3);
        PorosityN=['porosity' num2str(ii) '.out'];
        porosity_ith = PorosityImporter(PorosityN, 5, 40004);
        porositypoints(:,ii)=porosity_ith(:,3);
end
AverageRate1=mean(RateBrpoints);
AveragePorosity1=mean(porositypoints);
     



data=[data1 AverageRate1(end) AveragePorosity1(end)];

 dlmwrite('data.csv', data, 'delimiter', ',', 'precision', 9);

end

