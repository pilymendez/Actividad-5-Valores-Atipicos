#########################3Finción para cargar un archivo como un dataframe############

def cargar_dataset(archivo):
    import pandas as pd
    import os

#si se desea agrefar un input se coloca:
    #Archivo = input("Favor ingresa el nombre del archivo")
    extension = os.path.splitext(archivo)[1].lower()   #Al archivo se le saca la extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df =pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return (df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
    
#FUNCION ISNULL
def valores_nulos(df):
    #Valores nulos por columna
    valores_nulos_cols = df.isnull().sum()
    #valores nulos por dataframe
    valores_nulos_df = df.isnull().sum().sum()

    return("Valores nulos por columna",valores_nulos_cols,
           "Valores nulos por dataframe",valores_nulos_df)


#FUNCION FFILL
#Sustituir valores nulos por valores no nulos hacia adelante "forward fill" ffill
#Filtro por columnas ESPECÍFICAS los valores suelen mantenerse constantes
def sustitucion_ffill(df,col):
    #Sustituir valores nulos con promedio o media, las numéricas
    df[col] = df[col].fillna(method='ffill')

    return(df)

#FUNCIÓN BFILL
#Sustituir valores cualitativos tipo object y category 
def sustitución_bfill(df):
    #Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object','category'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas.fillna(method="bfill")
    #Fusionar los cambios en el df original
    df[cualitativas.columns] = cualitativas

    return(df)

#STRING CONCRETO
#Sustituir valores cualitativos tipo object y category 
def sustitucion_string(df,col):
    df[col] = df[col].fillna("Información no disponible")
    return(df)

#PROMEDIO
#Sustituir valores cuantitativos tipo float e int
def promedio(df, col):
    Data_type = df[col].dtype
    if (Data_type == 'int64') | (Data_type == 'float64'):
    #Sustituir valores nulos con promedio o media
        df[col] = df[col].fillna(round(df[col].mean(),1))
        return(df)
    else:
        raise ValueError(f"La variable no es numerica, es de tipo: {Data_type}")

#MEDIANA
#Columnas numéricas donde hay valores extremos y el promedio podría estar distorsionado
def mediana(df):
    #Separo columnas cuantitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64','float','int','int64'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.median(),1))
    #Fusionar los cambios en el df original
    df[cuantitativas.columns] = cuantitativas

    return(df)

#CONSTANTE
def constante (df,col,col2,col3,value):
    df[col] = df[col].fillna(value)
    df[col2] = df[col2].fillna(value)
    df[col3] = df[col3].fillna(value)
    return df

#CONVERTIR A CSV
def convertir_a_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo)

#EL DF COMPLETO LIMPIO
def sustitucion_completa(df):
    import pandas as pd
    #Separar columnas cuantitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64', 'int64','float','int'])
    #Separar columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(000)
    cualitativas = cualitativas.fillna('Sin datos')

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

