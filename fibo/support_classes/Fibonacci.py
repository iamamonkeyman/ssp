import allure


@allure.step
def generateFibonacci_ForLoop(num):

    if not isinstance(num, int):
        return "please, enter int number"

    final_li=[]
    n=n1=1
    num = abs(num)

    if num < 3:
        for i in range(num):
            final_li.append(1)
        return final_li
    else:
        final_li.append(1)
        for i in range(num-1):
            k=n+n1
            n=n1
            n1=k
            final_li.append(n)
        return final_li




def start_me_up():
    li2 = generateFibonacci_ForLoop(11)
    li3 = generateFibonacci_ForLoop(22)
    print("\n", li2, "\n", li3)



	
if __name__ == "__main__":
    start_me_up()