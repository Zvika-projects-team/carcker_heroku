from abc import ABC, abstractmethod
import requests
import time
import math


class Cracker(ABC):
    MAX_LEN = 6
    # ?url = r'https://passwordserveritayron.herokuapp.com'
    url = r'http://127.0.0.1:5000/'
    #POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    POOL = "01HPKsta9"

    @abstractmethod
    def find_pass_len(self, password_start_len=1):
        pass

    @abstractmethod
    def find_password(self, length):
        pass

    @abstractmethod
    def find_pass_last_char(self, password):
        pass

    @staticmethod
    def timeit(url2check, repeat=1):
        tt = []
        for _ in range(repeat):
            start = time.time()
            requests.get(url2check, allow_redirects=True)
            end = time.time()
            tt.append(end - start)
        return tt

    def analize(self, check_len):
        checks = []
        delay_margin = 0.09
        while check_len < self.MAX_LEN:
            url1 = self.url + '/' + ("").ljust(check_len, '_')
            checks.append(min(self.timeit(url1, 1)))
            print(
                f'Checking password length {check_len}: min time {checks[-1]}')
            check_len += 1
        prev = checks[0]
        current = 0
        prev_delta = current - prev
        analisis = []
        for i in range(1, len(checks)):

            current = checks[i]
            current_delta = current - prev
            
            if(abs(current_delta - prev_delta) < delay_margin):
                analisis.append([0,prev,current])
            elif(current_delta > prev_delta + delay_margin):
                analisis.append([1, prev, current])
            elif(current_delta + delay_margin < prev_delta):
                analisis.append([-1, prev, current])
            prev_delta = current_delta
            prev = checks[i]
        return analisis   
    '''      
        check_for = ""
        
        up = False
        down = False
        first_val = ""
        enter_up_count = 0
        enter_down_count = 0
        for report in analisis:
            if up or down:
                if up and down and (report[0] != 0):
                    check_for = "further"
                    break
                elif up and not down:
                    if enter_up_count > 1:
                        break
                    enter_up_count += 1
                elif down and not up:
                    if enter_down_count > 1:
                        check_for = "further"
                        break

                    
                    
            else:
                if(report[0] == 1):
                    up = True
                    first_val = "up"
                
                    
                elif(report[0] == -1):
                    down = True
                    check_for = "down"
    def check_for_seq():
        pass
    '''