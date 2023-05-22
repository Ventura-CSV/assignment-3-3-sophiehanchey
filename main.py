def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = True

    if not email[0].isalpha():
        result = False

    elen = len(email)
    if elen <= 5 or elen >= 30:
        result = False

    atidx = email.find('@')
    if atidx == -1:
        result = False
    else:
        if email[atidx:].find('.') == -1:
            result = False

    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
