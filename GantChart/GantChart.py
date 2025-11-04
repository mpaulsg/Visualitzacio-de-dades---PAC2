import pandas as pd
import plotly.express as px

def generar_df_resum(input_path):
    # Carreguem les dades d'input en un DataFrame
    df_final = pd.read_csv(input_path, sep=',')
    # Generem un DF de resum agrupant les dades per països i quedant-nos només
    # amb la primera i la última temporada
    df_paisos_anys = df_final.groupby('Country').agg(
        First=('Season', 'min'),
        Last=('Season', 'max')
    ).reset_index()

    # Ens quedem només amb el primer any de cada temporada
    df_paisos_anys['First'] = df_paisos_anys['First'].astype(str).str[:4]
    df_paisos_anys['Last'] = df_paisos_anys['Last'].astype(str).str[:4]
    return df_paisos_anys

def generar_diagrama_gantt(df_paisos_anys):
    # Crear diagrama de Gantt
    fig = px.timeline(
        df_paisos_anys,
        x_start='First',
        x_end='Last',
        y='Country',
        title='Intervals en els que els països han tingut equips guanyadors de la Champions League',
        labels={'Country': 'País', 'First': 'Primera Temporada', 'Last': 'Última Temporada'}
    )
    
    # Ajustar el orden de las barras
    fig.update_yaxes(autorange="reversed")
    fig.write_image('Gantt_paisosChampions.png')


def main():
    input_path = 'UCL_Finals_1955-2023.csv'
    df_paisos_anys = generar_df_resum(input_path)
    generar_diagrama_gantt(df_paisos_anys)
    return None


main()
