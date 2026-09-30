def FibonacciSeries(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        series = [0,1]
        for i in range(2, n):
            curr_num = series[i-1] + series[i-2]
            series.append(curr_num)
        return series