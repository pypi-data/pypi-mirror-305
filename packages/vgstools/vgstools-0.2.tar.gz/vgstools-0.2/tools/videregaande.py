# passord styrkesjekker
# input passord
# sjekker passord
# hvis den ikke er sterk nok så gir man tips
# tips: bruk tegn, nummer, bokstaver
import re

def validate_password(password):    
    if len(password) < 8:
        return "Passordet ditt er ikke langt nok, øk lengden!"

    if not re.search(r'[A-Z]', password):
        return "Du mangler store bokstaver, legg til noen store bokstaver!"
        
    if not re.search(r'[a-z]', password):
        return "Du mangler små bokstaver i passordet, legg til noen små bokstaver for å få ett sterkere passord!"
    
    if not re.search(r'\d', password):
        return "Du mangler tall i passordet, legg til noen tall så får du et sterkere passord!"
    
    if not re.search(r"[.,?£$?=&!@%-]", password): # dette er det jeg brukte for alle tegnene https://owasp.org/www-community/password-special-characters noen er eksludert
        return "Passordet mangler tegn, prøv ett av disse tegnene i passordet!\n. , ? £ $ ? = & ! @  % -"
    
    else:
        return "Passordet ditt er sterkt!"
    
def decrypt(string): # Funksjon for å dekryptere den gitte stringen 
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    key = len(string) # Finner ut hvilken key den bruker
    result = "" # lagrer resultatet

    for letter in string:
        if letter in upper_alphabet:
            letter_index = (upper_alphabet.find(letter) - key) % len(upper_alphabet)
            result += upper_alphabet[letter_index]
        elif letter in lower_alphabet: 
            letter_index = (lower_alphabet.find(letter) - key) % len(lower_alphabet)
            result += lower_alphabet[letter_index]
        else:
            result += letter 
 
    return result # returnerer result til starten

def load_words(word_list): # loads words into a list
    wordlist = list() 
    try:    
        with open(word_list, encoding="utf-8") as f: # specify encoding aswell
            for line in f:
                wordlist.append(line.strip('\n'))
        return wordlist
    except IOError:
        print("Error 1: Filen eksister ikke, vennligst prøv en annen fil")

def decrypt_words(word_list): # for ordlisten
    
    decrypted_wordlist = [] # liste for å lagre alle ordene som blir dekryptert
    for word in word_list: # kjører gjennom hver eneste ord i ordlisten
        decrypted_word = decrypt(word) # lagrer dekryptert ord i en variabel
        decrypted_wordlist.append(decrypted_word) # appender det til en liste
        
    return decrypted_wordlist # sender tilbake listen som ble sendt inn
