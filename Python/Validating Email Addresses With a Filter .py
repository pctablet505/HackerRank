def fun(s):
    '''It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is
. '''
    username,sep,webext=s.rpartition('@')
    websitename,sep,extension=webext.rpartition('.')
    if username and websitename and extension:
        if (username+'@'+websitename+'.'+extension)==s:
           if websitename.isalnum() and 1<=len(extension)<=3:
                if username.replace('-','').replace('_','').isalnum():
                    return True
                
    return False

     
    
    # return True if s is a valid email, else return False

