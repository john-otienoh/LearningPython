travel_log = []
def main():
    add_new_country('Germany', 5, ['Berlin', 'Hamburg', 'Stuttgatt'])
    add_new_country("Russia", 2, ['Moscow', 'Saint Petersburg', ])

def add_new_country(country, visits, cities):
    new_country = {}
    new_country['Country'] = country
    new_country['Visits'] = visits
    new_country['Cities'] = cities
    travel_log.append(new_country)
main()
print(travel_log)