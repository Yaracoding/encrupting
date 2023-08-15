letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message= input("What is the message you would like to send?").lower()
encr = ""
k = 3
for l in message:
    location = letters.index(l)
    print(location)
    encr = encr+letters[location+k]

print(encr)
