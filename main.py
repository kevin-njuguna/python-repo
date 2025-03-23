def function1():
    x = 1
    def function2():
        x = 2
        print(x)
    function2()
    
function1()