function summaryMaker2( searchPath )
    %addpath(genpath('S:\MahtaMatlab\yao'))
    addpath(genpath('R:\Research\GeologicalScience\sdm\Source\Matlab'))
    [out,isDirectory]=glob(searchPath);
    for i=1:size(out,1)
        out{i}
        if isDirectory(i)==1
            summary(10,out{i})
        else
            print 'not directory'
        end
    end
end