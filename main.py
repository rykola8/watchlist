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
     print("1. pievienot filmu norādot nosaukumu un reitingu, atzīmēt filmu kā skatīto/neskatīto ") 
     print("2. dzēst filmu no saraksta")
     print("3. atspoguļot top 10 filmas pec reitinga")
     print("4. iztukšot sarakstu")
     print("5. meklēt filmu pēc nosaukuma daļas")
     print("6. atfiltrēt noskatītas/nenoskatītas filmas")
     print("7. import json")
     print("8. Exit")
     command = input("Choose command: ") #lietotājs ievada savu izvēli.

     if command == "1": #ja viņš izvēlējās 1, tiek izpildīts šis kods.
       dictionary_films = {}
       
       name = input('Enter the film name: ')
       if len(name) < 2: #teikts, ka, ja nosaukumā ir mazāk par divām rakstzīmēm, tiks ģenerēta "kļūda"
            print("Error")
            continue
       if len(name) > 120: #teikts, ka, ja nosaukumā ir vairāk nekā simt divdesmit rakstzīmju, tiks ģenerēta "kļūda"
            print("Error")
            continue
       dictionary_films["name"] = name

       rating = input('Enter the film rating: ')
       if not rating.isdigit(): #pārbauda, vai tas ir vesels skaitlis 
            print("Error")
            continue
       if int(rating) < 1 or int(rating) > 10: #pārbauda, vai tas ir mazāks par 1 vai lielāks par 10.
            print("Error")
            continue
       dictionary_films["rating"] = int(rating)

       reviewed_yes_or_no = input('Have you seen this movie?(yes or no): ')
       dictionary_films["reviewed"] = reviewed_yes_or_no

       films.append(dictionary_films)
       print(films) 

     if command == "2": #ja viņš izvēlējās 2, tiek izpildīts šis kods.
        number_delete = int(input("enter number of film: "))
        del films[number_delete]
        print(films)
        pass 
     
    
     if command == "3": #ja viņš izvēlējās 3, tiek izpildīts šis kods.
          def my_func(films):
            return films["rating"]
            
          films.sort(key = my_func, reverse = True)
          print(films[0:9])

     if command == "4": #ja viņš izvēlējās 4, tiek izpildīts šis kods.
            films.clear()
            print(films)
            pass
    
     if command == "5": #ja viņš izvēlējās 5, tiek izpildīts šis kods.
            name_film = input('Enter the film name: ')
            new_films = []
            # izvēlos katru vārdnīcu no saraksta 
            for film in films:
                if film['name'] == name_film:  #pārbaudu, vai filmas nosaukums vārdnīcā sakrīt ar lietotāja rakstīto nosaukumu
                    new_films.append(film)     #Ja tas atbilst, es to pievienoju new_films
            print(new_films)

     if command == "6": #ja viņš izvēlējās 6, tiek izpildīts šis kods.
            reviewed = input("yes or no: ")
            new_films = []
            # izvēlos katru vārdnīcu no saraksta  
            for film in films:
                if film['reviewed'] == reviewed: #pārbaudīt, vai filma ir skatīta vai nē (atkarībā no lietotāja izvēles)
                    new_films.append(film)
            print(new_films) 

    
     if command == "7": #ja viņš izvēlējās 7, tiek izpildīts šis kods.
          import json
          with open('films.json', 'w') as file:
            json.dump(films, file)

          with open('films.json', 'r') as file:
            films_data = json.load(file)
            print(films_data)

     if command == "8": #ja viņš izvēlējās 8, tiek izpildīts šis kods.
            print("Exiting...")
            break 

    


   
   
   
   

    
    
    
  
   
    
 
      
    
    


