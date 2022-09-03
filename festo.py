def main():
    # data reading
    dataBase = []
    data = {}
    file = open(r"C:\Users\sipos\Downloads\office_database.txt")
    
    for line in file:
        data["username"] = line.split(',')[0].rstrip().lstrip()
        data["id"] = line.split(',')[1].rstrip().lstrip()
        data["accessKey"] = int(line.split(',')[2].rstrip().lstrip())
        data["firstLogin"] = line.split(',')[3].rstrip().lstrip()
        dataBase.append(data)
        data = {}
    
    print(dataBase)
    # puzzle 1: find the person who stole your mug
    # solution for puzzle 1
    countOfPossibleIDs = 0
    for i in range(0,len(dataBase)):
        if "814" in dataBase[i]["id"]:
            # print("contains " + dataBase[i]["id"])
            countOfPossibleIDs += int(dataBase[i]["id"])

    # solution to puzzle 1
    print(f"countOfPossibleIDs: {countOfPossibleIDs}")

    # puzzle 2: 
    # solution for puzzle 2
    # each person only has access to some part of the station
    # parts a person van enter are decoded in their access key
    # station has 8 modules (1,2,3...8)
    # for each module either has access (1) or has no access (0)
    # ex: person with access to module 3 and 7 will have a binary number 00100010.So this person's access key is 34 (the decimal representation of 00100010).
    # kitchen is in module 5.
    # return the sum of ID numbers who have access to module 5

    # acces key needs to be convert a binary number
    # ex 34 -> 100010 
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

if __name__ == "__main__":
    main()

