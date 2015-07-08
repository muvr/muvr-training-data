function [data] = averageWindow(xs, windowSize)
    s = fix(length(xs) / windowSize);
    segments = mean(reshape(xs(1:s * windowSize), s, [])');
    data = repelem(segments, windowSize);
end
