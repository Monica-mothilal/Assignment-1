#unpack dictionary using function to generate your personal data
def print_personal_data(name, age, city, country):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Country:", country)

personal_data = {
    "name": "jemes",
    "age": 50,
    "city": "mumbai",
    "country": "India"
}
print("Personal Data:")
print_personal_data(**personal_data)
