def to_json(input_str):
    lst = [i.split(',') for i in input_str.split(' ')]
    titles = [i[0] for i in lst]
    values = [[lst[j][i] for j in range(len(lst))]for i in range(1,len(lst[0]))]
    return [dict(zip(titles, values[i])) for i in range(len(values))]

print(to_json("""name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""))
