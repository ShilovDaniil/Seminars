st, dct = input(), {}
for i in st.split():
    if (n := dct.setdefault(i,0)) > 0:
        print(f'{i}_{n}', end= ' ')
    else:
        print(f'{i}', end= ' ')
    dct[i] += 1