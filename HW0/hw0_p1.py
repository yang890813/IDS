#####在我寫完這些之後就一直覺得自己寫完了，直到要交作業的前一天才發現我寫成把各個括號兩兩相乘後再相加
#####然後在輸入polynomials時括號跟括號之間要有*號才可以運行
#####希望多少還是可以給我一些分數QQ
string = input('Input the polynomials: ')
pols = string[1:-1].split(')(')
N = len(pols)
ans = {}
for i, pol1 in enumerate(pols):
  #與所有未計算過的部分相乘
    for pol2 in pols[i + 1:N]:
        #因為來不及寫完所以只先用+來splitQQ
        for p in pol1.split('+'):
            for q in pol2.split('+'):
              #如果第一個字不為digit則係數為1
                if not p[0].isdigit():
                    p = '1*' + p
                if not q[0].isdigit():
                    q = '1*' + q
                #n1,n2 為係數，m1,m2 為剩餘之字串
                n1, m1 = p.split('*')
                n2, m2 = q.split('*')
                num = int(n1) * int(n2)
              #一個key為x,y等字母，value為其指數之dictionary
                dic = {}
                for j, m in enumerate(m1):
                    if m.isalpha():
                        try:
                            if m1[j + 1] == '^':
                                dic[m] = int(m1[j + 2])
                            else:
                                dic[m] = 1
                        except:
                            dic[m] = 1
              #同上
                for j, m in enumerate(m2):
                    if m.isalpha():
                        if m in dic:
                            try:
                                if m2[j + 1] == '^':
                                    dic[m] += int(m2[j + 2])
                                else:
                                    dic[m] += 1
                            except:

                                dic[m] += 1
                        else:
                            try:
                                if m2[j + 1] == '^':
                                    dic[m] = int(m2[j + 2])
                                else:
                                    dic[m] = 1
                            except:
                                dic[m] = 1
                out = ''
                for var in sorted(dic):
                    nv = var.replace('^1', '')
                    out = out + var + '^' + str(dic[var]) + '*'
                out = out[:-1]
                if out in ans:
                    ans[out] += num
                else:
                    ans[out] = num

output = ''
print(ans)
for var in ans:
    output += (str(ans[var]) + var + '+')
print('Output Result:', output[:-1])
