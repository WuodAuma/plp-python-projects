def checkvowel(n):
    match n:
        case "a": return "Vowel alphabet"
        case "e": return "Vowel alphabet"
        case "i": return "Vowel alphabet"
        case "o": return "Vowel alpahbet"
        case "u": return "Vowel alphabet"
        case _: return "Simple alphabet"
print (checkvowel("t"))
print (checkvowel("o"))
print (checkvowel("w"))