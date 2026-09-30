def maxOverlaps(intervals): 
    if len(intervals) == 0: 
        return 0
  
    # Sort intervals according to their starting time 
    intervals.sort(key = lambda x: x[0])
  
    # Creating an array that stores the number of 
    # overlapping intervals for each interval 
    result = [0] * len(intervals) 
  
    # Initialising result[0] (as the first interval is always 
    # non-overlapping as it has no previous intervals) 
    result[0] = 1
  
    # Initializing the endpoint variable for comparison 
    endpoint = intervals[0][1] 
  
    for i in range(1, len(intervals)): 
        # If the current interval's start time is less 
        # than or equal to the endpoint, it's overlapping 
        if intervals[i][0] <= endpoint: 
            # Store the maximum number of overlapping 
            # intervals 
            result[i] = result[i - 1] + 1
        else: 
            result[i] = 1
          
        # Update the endpoint 
        endpoint = max(endpoint, intervals[i][1]) 
  
    # Finding the maximum number of overlapping intervals 
    maximum_overlaps = max(result) 
  
    return maximum_overlaps