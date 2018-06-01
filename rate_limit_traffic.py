"""

The function can be tested by adding a line
below the function:

result = rate_limit_traffic("small.log")
    
Strategy used: 
1) The starting time stamp of a user is taken as reference
and stored in a dictionary with user IP address as key.The number of
requests made per second(taken wrt to reference) are counted and stored
in a dictionary. 

2) After one second, the time reference is updated and counts are
considered corresponding to the next second.

3) If a user has already completed his max limit in one second,
he is not allowed any more requests.
"""

import shlex
def rate_limit_traffic(log_path):
    """Implement your solution here.

    Arguments:
        log_path: String with path of Nginx access logfile.

    Returns:
        A list of integers, representing the IDs of the rejected requests.
    """
    
    #Maximum limit of requests per user per second is 10
    result = []
    max_limit = 10
    
    with open(log_path, "r") as in_file:
        """
        Creating dicitonaries to store the
        time references, request count and 
        next request allowance in next
        one second slot
        """
        dicty_time = {}
        dicty_cnt = {}
        dicty_next = {}
        for line in in_file:
            k = shlex.split(line)
            o = k[3].split(" ")
            """
            Handling the exceptional cases when IP address is
            "16.180.70.237" or the web address begins with 
            "/ops". These cases are not evaluated for requests
            limit.
            """ 
            if(k[1] == "16.180.70.237" or o[1].startswith("/ops/")):
                continue
            else:
                """
                If user IP address is not found in the dictionary,
                add his entry time reference to the dictionary
                and allot him the maximum limit - 1 requests.
                The one less request is because he is currently
                making one request.
                """ 
                if k[1] not in dicty_time:
                    dicty_time[k[1]] = float(k[2])
                    dicty_cnt[k[1]] = max_limit - 1
                else:
                    
                    """
                    If user already exists and the time duration with
                    respect to his time reference saved is less than 
                    one second, check if he already exceeded the 
                    maximum limit for this one second.
                
                    Append the integer id to result list,if he exceeded
                    else keep counting his requests.
    
                    """ 
                    if((float(k[2])-dicty_time[k[1]]) < 1.000):
                        if(dicty_cnt[k[1]] <= 0):
                            result.append(int(k[0]))
                        else:
                            dicty_cnt[k[1]] = dicty_cnt[k[1]] - 1
                    else:
                        """
                        After one second taken with respect to when user entered,
                        reset the time reference to the current timestamp.
            
                        """ 
                        dicty_time[k[1]] = float(k[2])
                        """
                        If user exceeded time limit and he doesn't have
                        a next request allowance, assign him
                        only 1 request in the next to next second.
                        
                        Appending the integer id to the result list
                        """ 
                        if(dicty_cnt[k[1]] == 0 and k[1] not in dicty_next):
                            dicty_next[k[1]] = 1
                            """
                            If user exceeded time limit and does have
                            a next request allowance, he can only make one 
                            more request in the next to next second.
                        
                            Appending the integer id to the result list
                            """ 
                            result.append(int(k[0]))
                        elif(dicty_cnt[k[1]] == 0 and k[1] in dicty_next):
                            dicty_cnt[k[1]] = dicty_next[k[1]] - 1  
                            result.append(int(k[0]))
                            """
                            If user didn't exceed time limit and doesn't have
                            a next request allowance, he is allowed to
                            make max limit(10) requests in the next to next
                            second
                            """ 
                        elif(dicty_cnt[k[1]] != 0 and k[1] not in dicty_next):
                            dicty_next[k[1]] = max_limit
                            """
                            If user didn't exceed time limit and does have
                            a next request allowance, he is allowed to
                            make max limit(10)-1 requests in the next
                            second, since he is using one request right now.
                            """ 
                        elif(dicty_cnt[k[1]] != 0 and k[1] in dicty_next):
                            dicty_cnt[k[1]] = dicty_next[k[1]] - 1
                    
    return result


            
