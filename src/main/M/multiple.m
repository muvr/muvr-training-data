range = 1:34;
dir = '/Users/janmachacek/Muvr/muvr-preclassification/training-data/jan-chest-12-06/';

for i = range
    % Prepare file names
    fileName = strcat(strcat(dir, num2str(i)), '.csv');
    imageName = strcat(strcat(dir, num2str(i)), '.png');
    
    % Load the CSV
    M = readtable(fileName);
    ads = table2array(M(:,[6,7,8]));

    % Simple smoothing
    windowSize = 50;
    b = (1 / windowSize) * ones(1, windowSize);
    a = 1;
    adsf = filter(b, a, ads);
    adsf = adsf(windowSize:end,:);

    % Save the figure
    titleCell = M{1,1:2};
    fig = figure('name', strcat(strcat(titleCell{1}, ' '), titleCell{2}));
    time = 1:length(adsf);
    plot(time, adsf);
    print(fig, imageName, '-dpng');
    close(fig);
end
