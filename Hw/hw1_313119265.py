SUBMISSION_IDS = ["313119265" ,"314631979", "208419671", "325713576"]
#Question 4a
def max_word_len(text):
    words = str.split(text)
    maxnum = 0
    for word in words:
        maxnum = max (maxnum,len(word))
    return maxnum
    
#Question 4b
def frequent_word(text):
        spltex = text.split()
        count = 0
        maxnum = 0
        maxword = ""
        for i in range(len(spltex)):
            for j in range(len(spltex)):
                if(spltex[i]==spltex[j]):
                    count+=1
            if(count > maxnum):
                maxnum = count
                maxword = spltex[i]
            count = 0
        return maxword
            

#Question 4c
def vc_ratio(text):
    letters_in_text = text.replace(' ', '')
    vowels = 'aeiou'
    vowels_cnt = 0
    consonants_cnt = 0
    for letter in letters_in_text:
        if letter in vowels:
            vowels_cnt += 1
        else:
            consonants_cnt += 1
    return vowels_cnt / consonants_cnt

#Question 5
def calc(expression):
    expression = expression.split()
    num = int(expression[0])
    for i in range(2, len(expression), 2):
        if expression[i-1] == "**":
            num = num**int(expression[i])
        elif expression[i-1] == "*":
            num = num*int(expression[i])
        elif expression[i-1] == "//":
            num = num//int(expression[i])
        elif expression[i-1] == "+":
            num = num + int(expression[i])
        else:
            num = num - int(expression[i])
    return num

#Question 6
def max_div_seq(n, k):
    count = 0
    maxc = 0
    while(n > 0):
        if((n%10)%k == 0):
            count+=1
            if(count>maxc):
                maxc = count
        else:
            count=0
        n = n//10

    return maxc

########
# Tester
########

def test():
    #testing Q4
    st = "the quick brown fox jumps over the lazy dog"
    if max_word_len(st) != 5:
        print("Error in max_word_len")
    if frequent_word(st) != "the":
        print("Error in frequent_word")
    if vc_ratio(st) != 11/24:
        print("Error in vc_ratio")

    #testing Q5
    if calc("2 ** 2 ** 2 ** 2") != 256:
        print("Error in calc")
    if calc("20 // 3") != 6:
        print("Error in calc")
        
    #testing Q6
    l = max_div_seq(23300247524689, 2)
    if l != 4:
        print("Error in max_div_seq")

    if not SUBMISSION_IDS:
        print("The list of IDs is empty")
        
    if not type(SUBMISSION_IDS) == list:
        print("The list of IDs is not a list type")

    if SUBMISSION_IDS and not all(type(x)==str for x in SUBMISSION_IDS):
        print("The list of IDs contains elments that are not strings")
