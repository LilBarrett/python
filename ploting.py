import pandas as pd
import plotly.express as px

# Pobieramy plik xlsx
plik_xlsx = 'Statystyki z lat 2000-2023.xlsx'
df = pd.read_excel(plik_xlsx, sheet_name='PM2,5')

# Filtrujemy dane
years = range(2010, 2024)
df = df[
    (df['Czas uśredniania'] == '24g') &
    (df['Rok'].isin(years))
]

# Grupujemy po Kodzie stacji
stations = df.groupby('Kod stacji')['Rok'].nunique()

# Wykres 1: Wykres liniowy
full_data_stations = stations[stations == len(years)].index
full_stations_df = df[df['Kod stacji'].isin(full_data_stations)] # Użyjemy tylko stacji które mają pełne dane la lat 2010-2023
stacja1, stacja2 = full_data_stations[:2]
linear = full_stations_df[full_stations_df['Kod stacji'].isin([stacja1, stacja2])].groupby(['Rok', 'Kod stacji'])['Średnia'].mean().reset_index()

fig1 = px.line(linear, x='Rok', y='Średnia', color='Kod stacji',
               title='Średnie roczne stężenie PM2,5 dla dwóch stacji pomiarowych',
               labels={'Średnia': 'Średnie stężenie PM2,5 [µg/m³]', 'Rok': 'Rok'})
fig1.update_layout(legend_title_text='Kod stacji')
fig1.show()

# Wykres 2: Wykres pudełkowy
fig2 = px.box(df, x='Rok', y='Średnia',
              title='Rozkład średnich stężeń PM2,5 (2010-2023)',
              labels={'Średnia': 'Średnie stężenie PM2,5 [µg/m³]', 'Rok': 'Rok'})
fig2.show()

# Wykresy 3: Liczba przekroczeń normy
WHO_norm = 25
df['Przekroczenie normy'] = df['Średnia'] > WHO_norm
overflows = df.groupby(['Województwo', 'Rok'])['Przekroczenie normy'].sum().reset_index()
procentages = df.groupby(['Województwo', 'Rok'])['Przekroczenie normy'].mean().reset_index()

overflows_sum = overflows.groupby('Województwo')['Przekroczenie normy'].sum().reset_index()
fig3 = px.bar(overflows_sum, x='Województwo', y='Przekroczenie normy',
              title='Sumaryczna liczba przekroczeń normy PM2,5 w latach 2010–2023',
              labels={'Przekroczenie normy': 'Liczba przekroczeń', 'Województwo': 'Województwo'})
fig3.show()

# Procent przekroczeń
procentages_avg = procentages.groupby('Województwo')['Przekroczenie normy'].mean().reset_index()
procentages_avg['Przekroczenie normy'] *= 100
fig4 = px.bar(procentages_avg, x='Województwo', y='Przekroczenie normy',
              title='Procent pomiarów z przekroczoną normą PM2,5 (2010–2023)',
              labels={'Przekroczenie normy': 'Procent przekroczeń [%]', 'Województwo': 'Województwo'})
fig4.show()

