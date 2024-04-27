import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leer los datos del archivo
    df = pd.read_csv("adult.data.csv")

    # Número de personas por raza
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje de personas con licenciatura
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # Filtrar el DataFrame para personas con y sin educación avanzada
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Porcentaje de personas con y sin educación avanzada que ganan más de 50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # Número mínimo de horas que una persona trabaja por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de personas que trabajan el número mínimo de horas por semana y tienen un salario de más de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # País con el mayor porcentaje de personas que ganan más de 50K y ese porcentaje
    country_earning_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_earning_percentage.idxmax()
    highest_earning_country_percentage = round(country_earning_percentage.max(), 1)

    # Ocupación más popular para aquellos que ganan más de 50K en India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Imprimir los resultados si se solicita
    if print_data:
        print("Número de personas por raza:\n", race_count)
        print("Edad promedio de los hombres:", average_age_men)
        print(f"Porcentaje con licenciatura: {percentage_bachelors}%")
        print(f"Porcentaje con educación avanzada que ganan más de 50K: {higher_education_rich}%")
        print(f"Porcentaje sin educación avanzada que ganan más de 50K: {lower_education_rich}%")
        print(f"Horas mínimas de trabajo por semana: {min_work_hours} horas/semana")
        print(f"Porcentaje de personas con salario >50K entre los que trabajan el mínimo de horas: {rich_percentage}%")
        print("País con el mayor porcentaje de personas que ganan más de 50K:", highest_earning_country)
        print(f"Porcentaje más alto de personas con salario >50K en ese país: {highest_earning_country_percentage}%")
        print("Ocupación más popular para aquellos que ganan más de 50K en India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
