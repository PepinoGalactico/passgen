from secrets import choice

mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mins = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symb = ['"', "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", """'""", "", "^", "_", """`""", "{", "|", "~"]

def lon():
    while True:
        try:
            lon = int(input("Longitud de la Contraseña: "))
            if lon >= 64:
                print("El máximo es de 64 caracteres")
            else:
                return lon
        except ValueError:
            print("Debes ingresar un número entero")

lon = lon()
all = mayus + nums + symb + mins
contraseña = "".join(choice(all) for i in range(lon))
print(f"Contraseña: {contraseña}")