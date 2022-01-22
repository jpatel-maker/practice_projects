#Leetcode problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 


price = [7,1,5,3,6,4]

def day_to_buy_stock (prices):

    buy_day = 1

    for index,value in enumerate ( prices):

       if index + 1 < len(prices):

           if value < prices [index + 1] and value < prices [buy_day -1]:
               buy_day = index +1

           #else: break

    return buy_day


def day_to_sell_stock(prices, buying_day):

    sell_day  = 1
    sell_list = prices[buying_day - 1:]

    for index, item in enumerate(sell_list):

        if index + 1 < len(sell_list) :

            if sell_list [index + 1] > item and sell_list[index+1] > sell_day:

                sell_day = index +2
                #print (sell_day)

            #else: break

    return sell_day






Buy = day_to_buy_stock(price)

Sell = day_to_sell_stock(price, Buy)
print(Buy)

print (Sell)