import connexion

# IN
# http :8080/arraytest names==dog,cat
# OUT
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
# OUT
# [true]
def booltest(mybool):
    return [mybool]

app = connexion.App(__name__, port=8080)
app.add_api('my_api.yaml')
app.run()
