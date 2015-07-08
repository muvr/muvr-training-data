%% Computes FFT and power of the signal in xs
% Returns the most significant frequency, and period and powed, which 
% can be used to plot the data
%
% Examples usage is 
% [freq, period, power] = sigfft(table2array(xs(:,2)));
% plot(period, power);

function [freq, period, power] = sigfft(xs)
    %% 
    % Exercise activity is cyclical, and there is typically a major component
    % that falls in the range of 1 to 5 seconds.
    % The samples we have are noisy, we apply a moving average filter on the
    % windows of the given ``windowSize``.

    windowSize = 10;
    b = (1/windowSize)*ones(1,windowSize);
    a = 1;
    relNums = filter(b, a, xs);

    %%
    % Take FFT of the xs. The first component of Y, Y(1), is simply the sum of 
    % the data, and can be removed.

    Y = fft(relNums);
    Y(1) = [];

    %%
    % The complex magnitude squared of Y is called the power, and a plot of power
    % versus frequency is a "periodogram".
    n = length(Y);
    power = abs(Y(1:floor(n/2))).^2;
    nyquist = 1/2;
    freq = (1:n/2)/(n/2)*nyquist;

    period = 1./freq;

    index = power == max(power);

    freq = period(index);

end
