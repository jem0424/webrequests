import json, os


def jsonimport():
    with open(os.path.join(os.path.dirname(__file__),"SystemViewController.json"), 'r') as jsonfile:
        data = json.load(jsonfile)
        k = [data.keys()]
        subviews = data["subviews"] #list 
        return subviews
        # x = subviews[0] # dict
        # y = x["subviews"] # list
        # z = y[0] # dict
        # a = z["class"]

def function(subviews):
    for x in range(len(subviews)): 
        if 'subviews' not in subviews[x].keys():
            return
        else:
            if subviews[x]['class'] == "StackView":
                print(subviews[x].keys(),x)
                subviews=subviews[x]['subviews']
            function(subviews)

    # view1 = subviews[0]
    # print(view1.keys())

if __name__ == "__main__":
    subviews = jsonimport()
    function(subviews)


    #print(type(data["subviews"]))
    # for sub in subviews:
    #     if sub['class'] == 'StackView':
    #         # print(sub['class'],sub['classNames'])
    #         sub['class'] = 'JoelView'



    #     #print(sub['classNames'])
    # newString=json.dumps(subviews, indent=2, sort_keys=True)
    # # print(newString)

    # with open('newJSONFile.json', 'w') as file:
    #     json.dump(subviews, file, indent=2)

# import json 
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

# print(source)
    


    

