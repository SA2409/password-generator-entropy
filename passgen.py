import string
import secrets
import math

def calc_entropy(length, pool_size): #This function is math pure and help me to estimate the entropy.
    if pool_size > 0 and length > 0:
        return round(length * math.log2(pool_size), 2)
    return 0

def rank_strength(entropy): #Generate a system to later classify passwords. (based on entropy).
    "classifies the strength of the password according to entropy bits."
    if entropy < 50:
        return "🔴 Very Weak (Insecure against modern brute-force attacks)"
    elif entropy < 60:
        return "🟡 Moderate (Acceptable for secondary accounts, but could be improved)"
    elif entropy < 80:
        return "🟢 Strong (Very safe for everyday use)"
    else:
        return "🛡️ Excellent / Military Grade (Virtually impossible to break)"


def passw_gen():
    try:
        length = int(input('Enter the length of the password:  '))
        
        if length <= 0:
            print('❌ Error: The length must be greater than 0')

        chars = string.ascii_letters + string.digits + string.punctuation #We enter the symbols we want to use for password generator
        poolsize = len(chars) #Get a number == total of different characters we have

        password = ''.join(secrets.choice(chars) for i in range (length)) #For each turn of the cycle, one character is added
        
        entropy = calc_entropy(length, poolsize)
        strength = rank_strength(entropy)

        print("\n" + "="*40)
        print(f'🔑 Password generated: {password}')
        print(f'📊 Estimated entropy:  {entropy} bits')
        print(f'💪 Strength state:  {strength}')
        print("="*40)
    
    except ValueError:
        print('❌ Error: Please enter a valid integer.')

if __name__ == '__main__':
    passw_gen()