from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, time_window_seconds: int):
        self.max_requests = max_requests
        self.time_window = time_window_seconds
        self.client_logs = defaultdict(deque)

    def should_allow(self, client_id: str, current_time_seconds: int) -> bool:
        """Returns True if the request is allowed, False if rate limited."""
        cutoff_time = current_time_seconds - self.time_window

        while client_queue and client_queue[0] < cutoff_time:
          client_queue.popleft()
        
        if len(client_queue) >= self.max_requests
          return False
        
        client_queue.append(current_time_seconds)
        return True
