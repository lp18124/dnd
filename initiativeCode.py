def main():
    print("~~~~~~~~~~~~~~~~")
    print("Enter Initiative")
    print("~~~~~~~~~~~~~~~~")

    def init():
        azar = eval(input("Azar Ember: "))
        if azar < 0:
            azar = eval(input("Please enter a value above 0: "))
        ben = eval(input("Ben O'verbich: "))
        if ben < 0:
            ben = eval(input("Please enter a value above 0: "))
        monster1 = eval(input("Monster 1: "))
        if monster1 < 0:
            monster1 = eval(input("Please enter a value above 0: "))
        monster2 = eval(input("Monster 2: "))
        if monster2 < 0:
            monster2 = eval(input("Please enter a value above 0: "))
        monster3 = eval(input("Monster 3: "))
        if monster3 < 0:
            monster3 = eval(input("Please enter a value above 0: "))
        
        initList = [azar, ben, monster1, monster2, monster3]
        initList.sort(reverse=True)
        print(initList)
    init()
main()    