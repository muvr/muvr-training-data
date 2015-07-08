%% Exercise set frequency
% Measures the period in a suspected set

%% Load data
% Load the CSV, filter out relevant rows

M = readtable('../../../labelled/back/jan-2/2.csv');
ads = table2array(M(:,[5,6,7]));
% title('Raw');
% subplot(4, 1, 1);
% plot(time, ads);

%% Smooth out the raw input
colours = ['r', 'g', 'b'];
for i = 1:3
    data = smooth(ads(:,i));
    [freq, period, power] = sigfft(data);
    m = fix(mean(data) / 100) * 100;
    s = std(data);
    
    hold on;
    subplot(5, 1, 1);
    plot(data, colours(i));
    hold off;
    
    hold on;
    subplot(5, 1, 2);
    plot(period, power, colours(i));
    hold off;
    
    hold on;
    subplot(5, 1, i + 2);
    bar([m, s], colours(i));
    hold off;
end
