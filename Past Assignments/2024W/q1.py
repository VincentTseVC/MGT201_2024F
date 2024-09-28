prices = {600: 100, 250: 50, 50: 25, 10: 15}
data = {}

while True:
    empID = input('請輸入你的員工號碼: ')

    if empID not in data:
        data[empID] = {600: 0, 250: 0, 50: 0, 10: 0}

    com = int(input('請輸入 combination (600, 250, 50m 10): '))
    # if com < 0: ...

    data[empID][com] = data[empID][com] + 1
    # d1[k1][k2] = d1[k1][k2] + 1
    #   d2  [k2] =   d2  [k2] + 1


    print(data)
    quit = input('請問你要結束嗎? (y/n) ')
    if quit == 'y':
        break

# 如何顯示 summary
for impID in data:
    print(f'員工: {empID} 的數據如下: ')

    for com in data[empID]:
        amount = data[empID][com]
        total_prices = prices[com] * amount
        total_tickets = com * amount


        print(f'({com} tickets / ${prices[com]}) 組合 賣出:' )
        print(f' 一共 {amount} 的交易次數')
        print(f' 一共 {total_prices} 的總價格')
        print(f' 一共 {total_tickets} 的總票數量')