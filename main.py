def main():
    email = input('Enter your email: ')
    length = len(email)
    firstChar = email[0]
    result = True
    
    if length<5 or length>30:
        result = False
    
    if not firstChar.isalpha():
        result = False
    
    if '@' not in email:
        result = False
    else: 
        atId = email.find('@')
        postAt = email[atId:]
        
    if '.' not in postAt:
        result = False
        
    print(result)   

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
