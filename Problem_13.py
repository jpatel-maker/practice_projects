
#find path through grid given certain rules

grid = {1:[1,2,3,4], 2: [2,5,6,7], 3:[3,8,9,4], 4 : [4,3,2,1]}
numbers = []

def get_next_row (whole_grid,current_column):

    next_row_list = []

    next_row_list = whole_grid.get(current_column +1)

    return next_row_list


def get_previous_row (whole_grid,current_column):

    previous_row_list = []

    previous_row_list = whole_grid.get(current_column -1)

    return

    



def get_product (number_list):


    product_final = 1
    for numb in number_list:

        product_final = product_final * numb



    return product_final

# get the largest right product for all elements in the grid

def get_right_product(whole_grid,number):

    largest_product = 1
    next_row = True

    for key, value in whole_grid.items():

        list = value


        for index,item in enumerate(list):

            if next_row == True:

                print(number)
                product = get_product(number)

                if product >= largest_product:

                    largest_product = product


                number.clear()

                for next_index in range(index,index+4):

                    if next_index < len(list):
                        number.append(list[next_index])

#if out of range of current row

                    if next_index >= len(list) :



                        list_next_row = get_next_row(grid, key)

                        if list_next_row:

                            next_row = True
                            for items in range(0,4 - (4-index)):

                                number.append(list_next_row[items])


                            break

                        else:
                                next_row = False
                                break




    return largest_product


# get largest left product for all the elements in the list

def get_left_product (whole_grid, number):

    largest_product = 1
    previous_row = True
    next_row = True

    if next_row:
        print(numbers)

    for key,value in whole_grid.items():

        list = value

        for index, items in enumerate(list):



                print(number)
                product = get_product(number)

                if product >= largest_product:
                    largest_product = product

                number.clear()


 # get the previous elements and add to list number
                for previous_index in range(index, index-4,-1):


                    if previous_index >= 0 :
                        number.append(list[previous_index])


                    if previous_index < 0:

                        previous_row_list = get_previous_row(whole_grid,key)
                        next_row_list = get_next_row(whole_grid,key)


                        if previous_row_list:

                            previous_row = True

                            for items in range(((index+1)-4),0):

                                number.append(previous_row_list[items])

                            if next_row_list:
                                next_row = True

                            else:
                                next_row = False
                            break

                        else:
                            previous_row = False

                            break

    if next_row == False:


        print(numbers)

        product = get_product(number)

        if product >= largest_product:
            largest_product = product

        number.clear()

    return largest_product

    
#up-down
















#diagonally











final_right_product = get_right_product(grid,numbers)
print(final_right_product)

final_left_product = get_left_product(grid,numbers)
print(final_left_product)

