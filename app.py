import connexion

# IN
# http :8080/arraytest names==dog,cat
# OUT is invalid!
# [
#     "Hello d",
#     "Hello o",
#     "Hello g",
#     "Hello ,",
#     "Hello c",
#     "Hello a",
#     "Hello t"
# ]

def arraytest(names):
    return ['Hello ' + name for name in names]

# IN
# http :8080/booltest mybool==false
# OUT is invalid!
# [true]
def booltest(mybool):
    return [mybool]

# IN
# http POST :8080/bodytest mybool=false names:='["i1","i2"]'
# OUT is correct!
def bodytest(body):
    return body



app = connexion.App(__name__, port=8080)
app.add_api('my_api.yaml')
app.run()
