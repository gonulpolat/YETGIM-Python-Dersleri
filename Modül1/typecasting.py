
#Type Casting(Tip Dönüşümü)
int_val = 10
float_val = 10.5
string_val = "10.5"
bool_val = True
#int to float
float_val =float(int_val)
print("Float Değer",float_val)
print(type(float_val))

#int to boolean
bool_val = bool(int_val)
print("Boolean Değer",bool_val)
print(type(bool_val))

#float to int 
int_val_to_float = int(float_val)
print("Float to int",int_val_to_float)
print(type(int_val_to_float))

#float to boolean
bool_val_to_float = bool(float)
print("Float to boolean",bool_val_to_float)
print(type(bool_val_to_float))

#string to int
int_val_to_string = float(string_val)
print("String to int",int_val_to_string)
print(type(int_val_to_string))

#Trick
val = None
print(val)
print(type(val))

