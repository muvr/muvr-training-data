%% Smoothes out the input data
%

function [data] = smooth(xs)
    windowSize = 50;
    b = (1 / windowSize) * ones(1, windowSize);
    a = 1;
    fd = filter(b, a, xs);    
    data = fd(windowSize:end);
end
