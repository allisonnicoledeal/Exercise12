'''

'''
def rounding_to_nearest_int(number):
    base = int(number) #truncates number at decimal (5.9 --> 5 and 5.2 --> 5)
    if number - base >= 0.5:
        return base+1 #rounds up if number.5 or greater
    else:
        return base

    
def mystery2(inp):
    if not inp:
        return 0
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    return num

#finds length of third triangle side with other lengths a and b given
def pythagorean_theorem(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    
#reverses the order of items in a given list ([a, b, c, d] --> [d, c, b, a])
def reverse_list(my_list):
    size = len(my_list)
    for i in range(len(my_list)/2):
        temp = my_list[i]
        my_list[i] = my_list[size-i-1]
        my_list[size-i-1] = temp
        
    return

    
def mystery5():
    inp = open("sample_input.txt")
    ws = inp.split()
    h = dict()
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)

def mystery6(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = inp[i]
                swapped = True
