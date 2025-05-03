import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name=0)


otv=[]

def voz(button_zavod):
    for fir in range(0,10):
        value = df.iloc[fir, 0]
        if value == button_zavod:
            otv = [df.iloc[fir, 1],df.iloc[fir, 2],f"photos//{[df.iloc[fir, 3]]}//"]
            break
    return(otv)




    # Получение значения из ячейки A1 (первая строка, первый столбец)
   # value = df.iloc[0, 0]
    #print(value)

    ## Вывод первых строк таблицы
    #print(df.head())
# Чтение файла
#df = pd.read_excel('example.xlsx', sheet_name=0)  # Можно указать `sheet_name=0` для первого листа