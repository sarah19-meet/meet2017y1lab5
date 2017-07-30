def fib (n):
    back1=1
    back2=1
    for i in range(3,n+1):
       this_fib=back1
       back2=back1
       back1=this_fib
    return back1
       
       
        
        
        
