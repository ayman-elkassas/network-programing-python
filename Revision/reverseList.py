class reverseList:
    def reverse(List):
        count = len(List) - 1
        swap_var = 0
        i = 0
        for i in range(int(count / 2)):
            if i <= count / 2:
                swap_var = List[i]
                List[i] = List[count - i]
                List[count - i] = swap_var
        return  List
        