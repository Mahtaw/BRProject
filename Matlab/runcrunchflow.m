function [] = runcrunchflow( FlowRate, MajordirectionAnisotropy, MinordirectionAnisotropy, direc)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
% Sand Always need to be shown as 0 in the GRDCL file
cd(direc)
inputFile = 'InputTemplate.in';
generatedInputFile = 'magnesite.in';
%FlowRate=25; %flow rate in ml/min
%MajordirectionAnisotropy=50; % Enter the major direction Anisotropy you inserted into Petrel
%MinordirectionAnisotropy=1; % Enter the minor direction Anisotropy you inserted into Petrel
Porosity=0.35; % Please enter porosity used in CrunchFlow
highPressure = 10.0; %Initial highpressure in the Template input file
copyfile(inputFile, generatedInputFile);
permMatrix = Petrel2permMatrix;
PermXmatrix=permMatrix;
PermYmatrix=permMatrix;


PermXmatrix(:,1)=0;
PermXmatrix(:,size(permMatrix, 1))=0;
PermXmatrixGhost=zeros(size(permMatrix, 1),size(permMatrix, 1)+2);
PermXmatrixGhost(:,2:size(permMatrix, 1)+1)=PermXmatrix;
fidPermX = fopen('PermField.x', 'w');
for ii=1:size(permMatrix, 1)
    for jj=1:size(permMatrix, 1)+2
        fprintf(fidPermX,'%.3e\n', PermXmatrixGhost(ii,jj));
    end
end
fclose(fidPermX);
        


PermYmatrixGhost=zeros(size(permMatrix, 2)+2,size(permMatrix, 2));
PermYmatrixGhost(1,:)=PermYmatrix(1,:);
PermYmatrixGhost(end,:)=PermYmatrix(end,:);
PermYmatrixGhost(2:size(permMatrix, 2)+1,:)=PermYmatrix;
fidPermY = fopen('PermField.y', 'w');
for ii=1:size(permMatrix, 2)+2
    for jj=1:size(permMatrix, 2)
        fprintf(fidPermY,'%.3e\n', PermYmatrixGhost(ii,jj));
    end
end
fclose(fidPermY);

%Open the input file
fidInput = fopen(generatedInputFile);
tline2 = fgets(fidInput);
%Find the line with time points
while ~isempty(tline2)
    if ~isempty(strfind(tline2, 'spatial_profile'))
        gt=strsplit(strtrim(tline2));
        break
    end
    tline2 = fgets(fidInput);
end
for ii=2:length(gt)
    TimePoints(ii-1)=str2double(gt(ii));
end
fclose(fidInput);


%Run the first run in Matlab to find velocities for a short time.
fid3 = fopen(generatedInputFile, 'r');
fidTmp3 = fopen('tmp3.in', 'w');
tline3 = fgets(fid3);
while ischar(tline3)
    if ~isempty(strfind(tline3, 'spatial_profile'))
        FinalLine=tline3;
        fprintf(fidTmp3,'spatial_profile           0.001\n');
    else
        fprintf(fidTmp3,'%s',tline3);
    end
    tline3 = fgets(fid3);
end

fclose(fid3);
fclose(fidTmp3);
delete(generatedInputFile);
movefile('tmp3.in', generatedInputFile);




data1=[FlowRate  MajordirectionAnisotropy MinordirectionAnisotropy  Porosity];
save('dataTransfer1.mat','data1')
save('Timepoints1.mat','TimePoints')


system('CrunchFlow2007.exe');

%closing the spatial distribution figure.
close(figure(1))



%Putting back the timepoints for the final run.
fid4 = fopen(generatedInputFile, 'r');
fidTmp4 = fopen('tmp4.in', 'w');
tline4 = fgets(fid4);
while ischar(tline4)
    if ~isempty(strfind(tline4, 'spatial_profile'))
        fprintf(fidTmp4,'%s',FinalLine);
    else
        fprintf(fidTmp4,'%s',tline4);
    end
    tline4 = fgets(fid4);
end

fclose(fid4);
fclose(fidTmp4);
delete(generatedInputFile);
movefile('tmp4.in', generatedInputFile);


%Changing velocity based on the data acquired in the initial run.
velocity1 = VelocImporter('velocity1.out', 5, 40004);
Velocoutlet=velocity1(end-199:end,4);
v=(sum(Velocoutlet))/365/24/60*10;
highPressure = highPressure*FlowRate/v;
fid = fopen(generatedInputFile, 'r');
fidTmp = fopen('tmp5.in', 'w');
tline = fgets(fid);
while ischar(tline)
    idx = regexp(tline, {'pressure', 'zone', '1-200', '0-0', 'fix'});
    compFlag = 1;
    for i = 1 : 5
        if isempty(idx{i})
            compFlag = 0;
        end
    end
    if compFlag == 0
        fprintf(fidTmp,'%s',tline);
    else
        fprintf(fidTmp, 'pressure %.2f    zone  1-200 0-0       1-1 fix\n', highPressure);
    end
    tline = fgets(fid);
end

fclose(fid);
fclose(fidTmp);
delete(generatedInputFile);
movefile('tmp5.in', generatedInputFile);


FlowRate
MajordirectionAnisotropy
MinordirectionAnisotropy

%system('CrunchFlow2007.exe');
!CrunchFlow2007.exe &

end

