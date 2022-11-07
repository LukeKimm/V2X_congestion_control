import matplotlib.pyplot as plt

data_f = open("V2X_variables_10s.csv",'r', encoding='utf-8-sig')

TIMEs = []
CBRs = []
ITTs = []

for line in data_f:
    (TIME, CBR, ITT) = line.split(',')
    TIMEs.append(TIME)
    CBRs.append(CBR)
    ITTs.append(ITT)
    
data_f.close()

# 첫번째 열에 항목이 있을 경우 사용
# TIMEs = TIMEs[1:]
# CBRs = CBRs[1:]
# ITTs = ITTs[1:]

TIMEs = [float (i) for i in TIMEs]
CBRs = [float (i) for i in CBRs]
ITTs = [float (i) for i in ITTs]

ITTs.insert(0, 0)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(TIMEs, CBRs, color='magenta', marker='o', linestyle='dashed', label='CBR')
plt.title("CBR stabilizing")
plt.xlabel("TIME")
plt.ylabel("CBR")
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig('V2X_variables_10s_CBR.png')