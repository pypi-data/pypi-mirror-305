
class Greatest:

    @staticmethod
    def setGreat(arg, n:int=None, listofchoice:list=None) -> int:
        if isinstance(arg, int):
            n=arg
            listofchoice=None
        elif isinstance(arg, list):
            listofchoice=arg
            n =None

        lists = []
        if listofchoice == None and n !=None:

            for i in range(n):
                a = int(input())

                lists.append(a)
        else:
            lists = listofchoice

        for j in range(len(lists)):
            list2 =[]

            for i in range(len(lists)):
                val1 = lists[i]
                val2 = lists[-i]
            
                if val1>=val2:
                    list2.append(val1) 
                else:
                    list2.append(val2)
            

            lists = list(set(list2))
        
        #This part is further done because our logic of using lists[i] and -i will comapre 0 index
        # twice and the next index also twice because there's only one left.(no matter how many iterations we use we get the same [a,b]) 
        if lists[0]>=lists[1]:
            return lists[0]
        else:
            return lists[1]

