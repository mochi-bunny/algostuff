
#div n conq for rotation
#WORKING CODE

def shift_rotate(arr, shift_amount):
    length = len(arr)
    awe= arr
    if length>1:
        temp_arr = [None] * length
    
        for i in range(length):
            new_index = (i + shift_amount) % length
            temp_arr[new_index] = arr[i]
    
        for i in range(length):
            awe[i] = temp_arr[i]
    return awe 
    
def reverse_shift_rotation(arr, s):
    return shift_rotate(arr, -s)


def splitt(arn, coder, val):
    leng=len(arn)
    arr=arn
    # if leng>1:
    #     s= 0
    #     e= leng-1
    #     mid= (s+e)//2
    #     a1,a2= a[:mid],a[mid:]
    #     print(a1,a2)
    if coder== 'y': #rotate values
        # shift_rotate(a1,val)
        # shift_rotate(a2,val)
        shift_rotate(arr,val)
        #shift_rotate(a2, len(a1))
    if coder=='n': #reverse rotate to og
      # reverse_shift_rotation(a1, val)
      # reverse_shift_rotation(a2, val)
        reverse_shift_rotation(arr, val)
        #reverse_shift_rotation(a2, len(a1))

    
    #return a1+[arr[mid]]+a2
    return arr


#call func to shift rotate arr
def recursive(l,finar): 
    t1=[]
    t2=[]
    #finar= []
    if len(l)>=2 and l is not None:
        middle = len(l) // 2
        print('middle: #######',middle, '\nt1:',l[:middle], '\nt2',l[middle:])
        if middle>= 3 :
            
            t1 = splitt(l[:middle],'y',len(l[:middle])-1)
            t2= splitt(l[middle:],'y',len(l[middle:])-1)
            #left = recursive(t1)
            #right = recursive(t2)
            #print(left,right)
            print('tot ', len(t1), t1, len(t2), t2)
         
            print('/////////////////////////')
            recursive(t1,finar)
            recursive(t2,finar)
            print('/////////////////////////')
            
        else:   
            t1 = splitt(l[:middle],'y',len(l[:middle])-1)
            t2 = splitt(l[middle:],'y',len(l[middle:])-1)
            print('tot ', len(t1), t1, len(t2), t2)

            print('ASSSDDDSDDD', middle)
                    
            finar.extend(t1)
            finar.extend(t2)
            print('finar:  ',finar, len(finar))
            f = finar + [1111]
            return f
            
    else:
         print('intruuuu')
         return splitt(l,'y',len(l)-2)
         
 

a= []
for i in range(8):
    a.append(i) 
print('og array: ', a)
ans=[]
recursive(a,ans)
 
#to split into minor modules
def reversive(l,finar): 
    t1=[]
    t2=[]
    #finar= []
    if len(l)>=2 and l is not None:
        middle = len(l) // 2
        print('middle: #######',middle, '\nt1:',l[:middle], '\nt2',l[middle:])
        if middle>=4 :
            
            t1 = l[:middle]
            t2= l[middle:]
            #left = recursive(t1)
            #right = recursive(t2)
            #print(left,right)
            print('tot ', len(t1), t1, len(t2), t2)
         
            print('/////////////////////////')
            recursive(t1,finar)
            recursive(t2,finar)
            print('/////////////////////////')
            
        else:   
            t1 = l[:middle]
            t2 = l[middle:]
            print('tot ', len(t1), t1, len(t2), t2)

            print('ASSSDDDSDDD', middle)
                 
            finar.append([t1])
            finar.append([t2])
            print("FINAR:  ",finar) 
            
            
    else:
         print('intruuuu')
         return splitt(l,'y',len(l)-2)


t=ans
trash = []
print('kkae: ',ans )
print('-----------')
x= reversive(t,trash)
