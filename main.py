def main():
    email = input('Enter your email: ')
    length = len(email)
    firstChar = email[0]
    
    if length<5 or length>30:
        return False
    
    if not firstChar.isalpha:
        return False
    
    if '@' not in email:
        return False
    else: 
        atId = email.find('@')
        postAt = email[atId:]
        
    if '.' not in postAt:
        return False   
        
    result = True

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    print(main())
