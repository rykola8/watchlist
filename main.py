# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

films = []



#izveidoju bezgalīgu cilpu, lai sniegtu izvēli, līdz tiek izpildīts nosacījums, kas to izbeigs.
while True: 
    command = input("\nChoose command: 1. pievienot filmu norādot nosaukumu un reitingu, 2. dzēst filmu no saraksta, 3. atspoguļot top 10 filmas pec reitinga, 4. iztukšot sarakstu, 5. meklēt filmu pēc nosaukuma daļas, 6. atzīmēt filmu kā skatīto, 7. atzīmēt filmu kā neskatīto, 8.atfiltrēt noskatītas/nenoskatītas filmas: ")
    if command == "1":
       dictionary_films = {}
       
       name = input('Enter the film name: ')
       dictionary_films["name"] = name

       rating = input('Enter the film rating: ')
       dictionary_films["rating"] = int(rating)

       films.append(dictionary_films)
       print(films) 
    if command == "2":
        
        number_delete = int(input("enter number of film: "))
        del films[number_delete]
        print(films)
        pass
    
    if command == "3":
        def my_func(films):
            return films["rating"]
        
        films.sort(key = my_func, reverse = True)
        print(films[0:9])
        
    if command == "4":
        films.clear()
        print(films)
        pass
    if command == "5":
        name_film = input('Enter the film name: ')
        new_films = []
        # izvēlos katru vārdnīcu no saraksta 
        for film in films:
            if film['name'] == name_film:  #pārbaudu, vai filmas nosaukums vārdnīcā sakrīt ar lietotāja rakstīto nosaukumu
                new_films.append(x)     #Ja tas atbilst, es to pievienoju new_films

        print(new_films)

    if command == "6":
        name_film = input('Enter the film name: ')
        # izvēlos katru vārdnīcu no saraksta   
        for film in films:
            if film['name'] ==  name_film:  #pārbaudu, vai filmas nosaukums vārdnīcā sakrīt ar lietotāja rakstīto nosaukumu
                film['reviewed'] = "yes"  #ja tas atbilst, es pievienoju ['pārskatīts'] = "jā".
        print(films)   
    
    if command == "7":  
        name_film = input('Enter the film name: ')
        # izvēlos katru vārdnīcu no saraksta  
        for film in films:
            if film['name'] ==  name_film: #pārbaudu, vai filmas nosaukums vārdnīcā sakrīt ar lietotāja rakstīto nosaukumu
                film['reviewed'] = "no"  #ja tas atbilst, es pievienoju ['pārskatīts'] = "nē".
        print(films)   
    if command == "8":
        reviewed = input("yes or no: ")
        new_films = []
        # izvēlos katru vārdnīcu no saraksta  
        for film in films:
            if film['reviewed'] == reviewed: #pārbaudīt, vai filma ir skatīta vai nē (atkarībā no lietotāja izvēles)
                new_films.append(x)
        print(new_films)
    
    
    if command == "e":
        print("Exiting...")
        break



import json
f = open('films.json',) 
data = json.load(f)


