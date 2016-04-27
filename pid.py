from time import time


########################################################################
class PID:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, P, I, D, setpoint, initial, when = None):
        """Constructor"""
        self.gains = (float(P), float(I), float(D))
        self.setpoint = [float(setpoint)]
        
        if when is None:
            self.previous_time = time()
        else:
            self.previous_time = float(when)
            
        self.previous_error = self.setpoint[-1] - float(initial)
        self.integrated_error = 0.0
        
    #----------------------------------------------------------------------
    def calculate_response(self, value, now = None):
        """"""
        if now is None:
            now = time()
        else:
            now = float(now)
            
        P, I, D = self.gains
        err = self.setpoint[-1] - value
        result = P + err
        delta = now - self.previous_time
        self.integrated_error += err * delta
        result += I * self.integrated_error
        result += D * (err - self.previous_error) / delta
        
        self.previous_error = err
        self.previous_time = now
        
        return result