print("stack implementaton")
stack=[]
while True:
    print("what operation would you like to perform?\n 1.insertion,2.deletion,3.size checking,4.emptiness,5.exit")
    a=int(input())
    if a==1:
        print("enter the element to be inserted:")
        l=input()
        stack.append(l)
        print("the element in the stacks are",stack)
    elif a==2:
        if stack==[]:
            print("the stack is empty")
        else:
            stack.pop()
            print("the element in the stacks are",stack)
    elif a==3:
        print("the size of the stack is",len(stack))
        print("the element in the stacks are",stack)
    elif a==4:
        if stack==[]:
            print("the stack is empty")
        else:
            print("the elements in the stacks are",stack)
        
    elif a==5:
        print("exit")
        break
 
