from countryinfo import CountryInfo
try:
    count = input("Enter your country: ")
    country = CountryInfo(count)
    
    print("The capital is ", country.capital())
    print("Currencies is ", country.currencies())
    print("Languages is ", country.languages())
    print("Borders is ", country.borders())
    print("Other names :",country.alt_spellings())
except KeyError:
    print("This is not a country")
