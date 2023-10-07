import random
import array

LEN =int(input('Enter the lenth of the character: '))
NUM =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
UP_CASE =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J',
            'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y','Z']
LOW_CASE =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j',
             'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u',
             'v', 'w', 'x', 'y','z']
SPE_CASE =['!','@','#','€','$','%','&','*','?']
COMBINED = NUM+UP_CASE+LOW_CASE+SPE_CASE
rand_digits =random.choice(NUM)
rand_up =random.choice(UP_CASE)
rand_low =random.choice(LOW_CASE)
rand_spe =random.choice(SPE_CASE)
temp_pswd= rand_digits+rand_up+rand_low+rand_spe
for i in range(LEN-4):
    temp_pswd= temp_pswd+random.choice(COMBINED)
    temp_pswd_list = array.array('u', temp_pswd)
    random.shuffle(temp_pswd_list)
pswd = ""
for i in temp_pswd_list:
        pswd = pswd + i
print("YOUR PASSWORD IS ",pswd)
