def find(d):
    d2l = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def back(ans,i):
        if(len(ans) == len(d)):
            print(ans)
            return
        for c in d2l[d[i]]:
            back(ans+c,i+1)
    back("",0)
find("23")

