import hashlib
import json
import math
import os
import random
# You may NOT alter the import list!!!!


class CryptoProject(object):

    def __init__(self):
        # TODO: Change this to YOUR Georgia Tech student ID!!!
        # Note that this is NOT your 9-digit Georgia Tech ID
        self.student_id = 'ychang363' 

    def get_student_id_hash(self):
        return hashlib.sha224(self.student_id.encode('UTF-8')).hexdigest()

    def get_all_data_from_json(self, filename):
        data = None
        base_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(base_dir, filename), 'r') as f:
            data = json.load(f)
        return data

    def get_data_from_json_for_student(self, filename):
        data = self.get_all_data_from_json(filename)
        name = self.get_student_id_hash()
        if name not in data:
            print(self.student_id + ' not in file ' + filename)
            return None
        else:
            return data[name]

    # TODO: OPTIONAL - Add helper functions below
    # BEGIN HELPER FUNCTIONS
    '''    
    def get_multiplicative_inverse(self,a,m):

        #if gcd(a,m)!=1:
         #   return None
        u1,u2,u3 = 1,0,a
        v1,v2,v3 = 0,1,m
        while v3!=0:
            q = u3//v3
            v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
        return u1%m
    '''
    def find_root(self, cube):
        up = 1
        while (up ** 3<=cube):
            up *= 2
        low = up//2
        while(low<up):
            mid = (up+low)//2
            if (up>mid and mid**3>cube):
                up = mid
            elif (low<mid and mid**3<cube):
                low = mid
            else:
                return int(mid)
        return int(mid+1)
    
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def get_multiplicative_inverse(self, m, a):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    
    # END HELPER FUNCTIONS
    
    def decrypt_message(self, N, e, d, c):
        # TODO: Implement this function for Task 1
        m = pow(c,d,N)
        print("task1 returns: ", hex(m).rstrip('L'))
        return hex(m).rstrip('L')

    def crack_password_hash(self, password_hash, weak_password_list):
        # TODO: Implement this function for Task 2
        password = ''
        salt = ''
        for s in weak_password_list:
            for p in weak_password_list:
                hashed_password = hashlib.sha256(p.encode() + s.encode()).hexdigest()
                if (hashed_password == password_hash):
                    password = p
                    salt = s
                    break
        print ("task2: password = ", password)
        print ("salt = ", salt)
        return password, salt

    def get_factors(self, n):
        # TODO: Implement this function for Task 3
        #return (0,0)
        p = 0
        q = 0
        if (n%2 == 0):
            p=2
            q=n//2
        else:
            p = int(math.sqrt(n))
            if (p%2 == 0):
                p += 1
            while (p>0 and not n%p == 0):
                p -= 2
            q = n//p
        print("taske, n = ", n)
        print("p*q = ", p*q)
        print("task3, p, q = ", p, q)
        return (p,q)        

    def get_private_key_from_p_q_e(self, p, q, e):
        # TODO: Implement this function for Task 3
        #return 0
        d = 0
        phi = (p-1)*(q-1)
        tem = 1
        while(not tem%e == 0):
            tem += phi
        d = tem//e
        print("task3, d = ", d)
        return d
    
    def is_waldo(self, n1, n2):
        # TODO: Implement this function for Task 4
        # Public key of yours and Waldo's share a common factor
        #return False
        if (n1<n2):
            r = [n2,n1]
        else: r = [n1,n2]
        while (not r[1]==0):
            tem = r[0] % r[1]
            r[0] = r[1]
            r[1] = tem
        result = (not r[0] == 1)
        
        return result

    def get_private_key_from_n1_n2_e(self, n1, n2, e):
        #return 0
        # TODO: Implement this function for Task 4
        d = 0
        if (n1<n2):
            r = [n2,n1]
        else: r = [n1,n2]
        while (not r[1]==0):
            tem = r[0] % r[1]
            r[0] = r[1]
            r[1] = tem
        common_factor = r[0]
        p = common_factor
        q = n1//p
        phi = (p-1)*(q-1)
        d = self.get_private_key_from_p_q_e(p, q, e)
        
        return d

    def recover_msg(self, N1, N2, N3, C1, C2, C3):
        # TODO: Implement this function for Task 5
        # return 42        
        # Note that 'm' should be an integer
        
        n1_i = self.get_multiplicative_inverse(N1, N2*N3)
        n2_i = self.get_multiplicative_inverse(N2, N1*N3)
        n3_i = self.get_multiplicative_inverse(N3, N2*N1)
        alpha = n1_i*N2*N3
        beta = n2_i*N1*N3
        gamma = n3_i*N1*N2
        m_cube = (C1*alpha + C2*beta + C3*gamma) % (N1*N2*N3)
        
        m = self.find_root(m_cube)
        return m

    def task_1(self):
        data = self.get_data_from_json_for_student('keys4student_task_1.json')
        N = int(data['N'], 16)
        e = int(data['e'], 16)
        d = int(data['d'], 16)
        c = int(data['c'], 16)

        m = self.decrypt_message(N, e, d, c)
        return m

    def task_2(self):
        data = self.get_data_from_json_for_student('hashes4student_task_2.json')
        password_hash = data['password_hash']

        # The password file is loaded as a convenience
        weak_password_list = []
        base_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(base_dir, 'top_passwords.txt'), 'r', encoding='UTF-8-SIG') as f:
            pw = f.readline()
            while pw:
                weak_password_list.append(pw.strip('\n'))
                pw = f.readline()

        password, salt = self.crack_password_hash(password_hash, weak_password_list)

        return password, salt

    def task_3(self):
        data = self.get_data_from_json_for_student('keys4student_task_3.json')
        n = int(data['N'], 16)
        e = int(data['e'], 16)

        p, q = self.get_factors(n)
        d = self.get_private_key_from_p_q_e(p, q, e)
        print("task3: ", hex(d).rstrip('L'))
        return hex(d).rstrip('L')

    def task_4(self):
        all_data = self.get_all_data_from_json('keys4student_task_4.json')
        student_data = self.get_data_from_json_for_student('keys4student_task_4.json')
        n1 = int(student_data['N'], 16)
        e = int(student_data['e'], 16)

        d = 0
        waldo = 'Dolores'

        for classmate in all_data:
            if classmate == self.get_student_id_hash():
                continue
            n2 = int(all_data[classmate]['N'], 16)

            if self.is_waldo(n1, n2):
                waldo = classmate
                d = self.get_private_key_from_n1_n2_e(n1, n2, e)
                break
        print("task4: ", hex(d).rstrip("L"))
        print("task4: waldo = ", waldo)
        return hex(d).rstrip("L"), waldo

    def task_5(self):
        data = self.get_data_from_json_for_student('keys4student_task_5.json')
        N1 = int(data['N0'], 16)
        N2 = int(data['N1'], 16)
        N3 = int(data['N2'], 16)
        C1 = int(data['C0'], 16)
        C2 = int(data['C1'], 16)
        C3 = int(data['C2'], 16)

        m = self.recover_msg(N1, N2, N3, C1, C2, C3)
        #print(hex(m))
        # Convert the int to a message string
        #msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')
        print(msg)
        return msg
