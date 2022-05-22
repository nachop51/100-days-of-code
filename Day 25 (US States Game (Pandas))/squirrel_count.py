import pandas

squirrels = pandas.read_csv("squirrel.csv")

gray = len(squirrels[squirrels['Primary Fur Color'] == "Gray"])
cinnamon = len(squirrels[squirrels['Primary Fur Color'] == "Cinnamon"])
black = len(squirrels[squirrels['Primary Fur Color'] == "Black"])

print(gray, cinnamon, black)

data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data_dict = pandas.DataFrame(data)
data_dict.to_csv("squirrel_count.csv")
