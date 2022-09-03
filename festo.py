def main(path):
    # data reading
    dataBase = []
    data = {}
    file = open(fr"{path}")
    print(";;;;;;;;;;;;")
    for line in file:
        data["username"] = line.split(',')[0].rstrip().lstrip()
        data["id"] = int(line.split(',')[1].rstrip().lstrip())
        data["accessKey"] = int(line.split(',')[2].rstrip().lstrip())
        data["firstLogin"] = line.split(',')[3].rstrip().lstrip()
        dataBase.append(data)
        data = {}
    
    # puzzle 1: find the person who stole your mug
    # solution for puzzle 1
    countOfPossibleIDs = 0
    for i in range(0,len(dataBase)):
        if "814" in str(dataBase[i]["id"]):
            # print("contains " + dataBase[i]["id"])
            countOfPossibleIDs += int(dataBase[i]["id"])

    # solution to puzzle 1
    print(f"countOfPossibleIDs: {countOfPossibleIDs}")

    # puzzle 2: 
    # solution for puzzle 2
    # access key is a number
    # convert it to binary and every one means that the person has access to that room or st
    # sum of the id numbers where the fifth digit is 1
    
    sumOfDecimal = 0
    sum = 0
    uj = 0
    kell = []
    megint = []
    for i in range(0,len(dataBase)):
        print(f"dataBase[i]: {dataBase[i]}")
        # ez van alapbol: 00100010 (ez binaris)
        # dataBase[i]["accessKey"] needs to be converted to decimal, to find the 5. digit
        print(f"dataBase[i]['accessKey']: {dataBase[i]['accessKey']}")
        decimal = format(int(dataBase[i]['accessKey']), "b")
        # the conversion is good, the logic is not working i think
        try:
            print(f"decimal: {decimal}, 5.th: {decimal[4]}")
            print(dataBase[i]['id'] not in megint)
            if int(decimal[4]) == 1 and dataBase[i]['id'] not in megint:
                print("RE")
                megint.append(dataBase[i]['id'])
                sumOfDecimal += int(dataBase[i]['id'])
                kell.append(sumOfDecimal)
                
        except IndexError:
            pass
    
    print(sumOfDecimal)
    print(uj)
    print(sum)
    print(len(kell))

    # skipped it lol idk what is this

    # puzzle 3
    # at 7.14 the mug was already stolen
    # so it was stolen before that
    # if person has not yet logged in today, the time is 99:99
    # sum of the id numbers who logged in before 7:14
    sumagain = 0
    cuccc = []
    
    for i in range(0, len(dataBase)):
        hour = int(dataBase[i]["firstLogin"].split(":")[0])
        minute = int(dataBase[i]["firstLogin"].split(":")[1])
        if hour <= 7:
            # ez nem jo sztem
            if minute < 14:
                print("7.14 elotti")
                print(dataBase[i])
                try:
                    print("ff")
                    print(str(format(int(dataBase[i]['accessKey']), "b"))[4])
                    if str(format(int(dataBase[i]['accessKey']), "b"))[4] == 1:
                        sumagain += dataBase[i]["id"]
                        if dataBase[i]["id"] not in cuccc:
                            cuccc.append(dataBase[i]["id"])
                except IndexError:
                    pass
    print(sumagain)
    print(len(cuccc))

if __name__ == "__main__":
    file = 'C:\\Users\\sipos\\Downloads\\office_database.txt' # path should be formatted with double backslashes
    main(file)

