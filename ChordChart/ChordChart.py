import pandas as pd

# Carregar el fitxer CSV
df = pd.read_csv("Student_Attitude_and_Behavior.csv")

# Modificar els departaments per noms més llegibles
df['Department'] = df['Department'].replace({
    'BCA': 'Computer science',
    'B.com ISM': 'Information technology',
    'B.com Accounting and Finance ': 'Finance'
})

# Agrupar per Department i hobbies, i comptar quants estudiants hi ha en cada grup
agrupat = df.groupby(['Department', 'hobbies']).size().reset_index(name='count')

# Canviar els noms de les columnes
agrupat.columns = ['Categoria A', 'Categoria B', 'count']

# Duplicar les files intercanviant les columnes de les categories
invertit = agrupat.rename(columns={'Categoria A': 'Categoria B', 'Categoria B': 'Categoria A'})
duplicat = pd.concat([agrupat, invertit], ignore_index=True)

# Exportar el resultat a un fitxer .csv
duplicat.to_csv('StudentHobbies_per_Department.csv', index=False)
