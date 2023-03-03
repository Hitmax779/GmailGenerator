import random
def mailgenerate():
    global rand_set 
    glas = ['a','e','i','j','o','u']
    sogl = ['b','c','d','f','g','h','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    nums = [1,2,3,4,5,6,7,8,9,0]
    result = [] 
    length = random.randint(5,10)  
    rand_set = random.choices(nums,k=4) 
    result2 = []                                                                            
    while len(result) < length: 
        rand_sogl = ''.join(random.choices(sogl,k=1)) 
        rand_glas = ''.join(random.choices(glas,k=1)) 
        result.append(rand_sogl) 
        result.append(rand_glas) 
    result2.append(rand_set) 
    letter_set = ''.join(map(str,result)) 
    setter = ''.join(map(str,rand_set)) 
    mail = letter_set + setter + '@gmail.com' 
    return mail
print(mailgenerate()) 
