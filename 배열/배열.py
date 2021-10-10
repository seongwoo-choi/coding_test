def q1():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    data_list2 = []
    for i in range(0, 3):
        data_list2.append(data_list[2][i])

    for data in range(len(data_list2)):
        print(data_list2.pop())


def q2():
    dataset = ['Braund, Mr. Owen Harris',
               'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
               'Heikkinen, Miss. Laina',
               'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
               'Allen, Mr. William Henry',
               'Moran, Mr. James',
               'McCarthy, Mr. Timothy J',
               'Palsson, Master. Gosta Leonard',
               'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
               'Nasser, Mrs. Nicholas (Adele Achem)',
               'Sandstrom, Miss. Marguerite Rut',
               'Bonnell, Miss. Elizabeth',
               'Saundercock, Mr. William Henry',
               'Andersson, Mr. Anders Johan',
               'Vestrom, Miss. Hulda Amanda Adolfina',
               'Hewlett, Mrs. (Mary D Kingcome) ',
               'Rice, Master. Eugene',
               'Williams, Mr. Charles Eugene',
               'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
               'Masselmani, Mrs. Fatima',
               'Fynney, Mr. Joseph J',
               'Beesley, Mr. Lawrence',
               'McGowan, Miss. Anna "Annie"',
               'Sloper, Mr. William Thompson',
               'Palsson, Miss. Torborg Danira',
               'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
               'Emir, Mr. Farred Chehab',
               'Fortune, Mr. Charles Alexander',
               'Dwyer, Miss. Ellen "Nellie"',
               'Todoroff, Mr. Lalio']

    count_m = 0

    for index, data in enumerate(dataset):
        for num in range(len(data)):
            if data[num] == 'M':
                count_m += 1
    print(count_m)

q1()
q2()