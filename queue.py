print("queue implementaton")
queue=[]
while True:
    print("what operation would you like to perform?\n 1.enqueue,2.dequeue,3.size checking,4.emptiness,5.exit")
    a=int(input())
    if a==1:
        print("enter the element to be inserted:")
        l=input()
        queue.append(l)
        print("the element in the queue are",queue)
    elif a==2:
        if queue==[]:
            print("the queue is empty")
        else:
            queue.pop(0)
            print("the element in the queue are",queue)
    elif a==3:
        print("the size of the queue is",len(queue))
        print("the element in the queue are",queue)
    elif a==4:
        if queue==[]:
            print("the queue is empty")
        else:
            print("the elements in the queue are",queue)
        
    elif a==5:
        print("exit")
        break
