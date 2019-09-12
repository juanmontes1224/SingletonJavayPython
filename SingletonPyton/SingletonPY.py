import singleton
class PatronSingleton:

   def __new__(obj):

        try:
            obj.instance
            
        except AttributeError:

            obj.instance = super(PatronSingleton, obj).__new__(obj)

        return obj.instance


x = singleton.PatronSingleton()
y = singleton.PatronSingleton()

print("LA INSTANCIA  "+str(x)+ " ")
print("ES IGUAL A LA INSTANCIA "+str(y)+" ")
