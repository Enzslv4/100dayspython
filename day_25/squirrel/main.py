import pandas

squirrels = pandas.read_csv('day_25/squirrel/squirrel_data.csv')

squirrels_colors = squirrels['Primary Fur Color']

len_gray = len(squirrels_colors[squirrels_colors == 'Gray'])
len_cinnamon = len(squirrels_colors[squirrels_colors == 'Cinnamon'])
len_black = len(squirrels_colors[squirrels_colors == 'Black'])

data_colors = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [len_gray, len_cinnamon, len_black]
}

data = pandas.DataFrame(data_colors)

data.to_csv('day_25/squirrel/squirrel_count.csv')