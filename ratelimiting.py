import time 
requests = 0
LIMIT = 5 
TIME_WINDOW = 60  # seconds
def is_allowed(user_id):
  current time = time.time()

  if user_id not in  requests:
    requests[user_id] = []
     #remove  old request
     requests[user_id] = [
       t for t in requests[user_id]
       if current_time -t < TIME_WINDOW
     ]
     if len(requests[user_id]) < LIMIT
    re [user_id].append(current_time)
    return True
  else:
    return False
     