col1 = ('a','b','c')
col2 = ('d','e','f')
col3 = ('g','h','i')
col4 = ('j','k','l')
col5 = ('a','b','e')

allCols = [col1,col2,col3,col4, col5]
layouts = []
for col1 in allCols:
    for col2 in allCols[1:]:
        doubles = set(col1).intersection(set(col2))
        if len(doubles) > 0:
            continue

        approach = {col1,col2}
        if frozenset(approach) not in layouts and len(approach) == 2:
            layouts.append(approach)
            print(approach)


