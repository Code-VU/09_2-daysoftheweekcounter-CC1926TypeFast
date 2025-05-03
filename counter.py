def countDayOfTheWeek():
    # This first line is provided for you


    file_name = input("Enter a file name: ")

    fhand = open(file_name)
    di = {}

    for line in fhand:
        line = line.rstrip()
        if line.startswith('From '):
            abc = line.split()
            day = abc[2]
            di[day] = di.get(day, 0) + 1
            
    print(di)



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
