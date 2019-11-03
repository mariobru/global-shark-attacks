def year_range():
    
    year_list = []
    
    try:
        first = int(input("Please choose the first year of the year range: \n"))
        last = int(input("Now choose the last one: \n"))
        if (first >= 1900 and first <= 2016)  and (last >= 1900 and last<= 2016):
            if first < last:
                for i in range(first, last + 1):
                    year_list.append(i)
            elif first >= last:
                print("The first number should be smaller than the last one.")
        else:
            print("You should introduce an integer between 1900 and 2016.")
    except:
        print("You should introduce an integer between 1900 and 2016.")
        
        
    return year_list