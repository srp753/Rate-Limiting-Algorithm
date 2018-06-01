# Rate-Limiting-Algorithm

This code defines a function "rate_limit_traffic" which takes in the path of a log file containing
user activity.

The aim is to limit user requests to the API to 10 per second.
The algorithm uses a sliding window fashion over the time
series log data to output the times when the user exceeded
the request limit. 

You can test the function by adding a line after the function as
follows:

result = rate_limit_traffic("small.log")

The log files are available in the inputs folder.
   


