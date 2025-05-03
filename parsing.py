import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name=0)




def voz(button_zavod):
    st3 = ""
    otv=[]
    for fir in range(0,100):
        value = df.iloc[fir, 0]
        if value == button_zavod:
            photo= df.iloc[fir, 3].split(";")
            for i in range(len(photo)):
                st3 += "photos/" +  photo[i]+";"
            otv = [df.iloc[fir, 1],df.iloc[fir, 2],st3.split(";")]
            break
    return(otv)




    # Получение значения из ячейки A1 (первая строка, первый столбец)
   # value = df.iloc[0, 0]
    #print(value)

    ## Вывод первых строк таблицы
    #print(df.head())
# Чтение файла
#df = pd.read_excel('example.xlsx', sheet_name=0)  # Можно указать `sheet_name=0` для первого листа