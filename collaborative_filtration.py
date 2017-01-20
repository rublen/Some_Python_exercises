students = {'st0' : {'gr0' : 10, 'gr1' : 7, 'gr2' : 5, 'gr3' : 3},
            'st1' : {'gr0' : 6, 'gr1' : 8, 'gr2' : 2, 'gr3' : 5},
            'st2' : {'gr0' : 4, 'gr1' : 6, 'gr2' : 6, 'gr3' : 4},
            'st3' : {'gr0' : 3, 'gr1' : 5, 'gr2' : 6, 'gr3' : 7},
            'st4' : {'gr0' : 9, 'gr1' : 6, 'gr2' : 6, 'gr3' : 4}}

def evkl_dist(a, b): #a, b - dictioaries
    s = 0
    for key in a:
        if key in b: s += (a[key] - b[key])**2
    from math import sqrt
    d = sqrt(s)
    return d

st_list = list(students.keys())
ed = {} #evklidova vidstan
mp = {} #mira podibnosti

for i in range(0, len(st_list)):
    for j in range(i+1, len(st_list)):
        stst = st_list[i] + ' and ' + st_list[j]
        dist = evkl_dist(students[st_list[i]], students[st_list[j]])
        ed[stst] = round(dist, 2)
        mira = round(1/(1+dist), 4)
        mp[stst] = mira
  
def sort_dict(d):
    d_list = list(d.items())
    d_sort = sorted(d_list, key = lambda x: x[1])
    for i in d_sort: print(i[0], ': ', i[1])
    
print('Sorted by evkl_dist: ')
sort_dict(ed)

print('Sorted by mira_podibnosti: ')
sort_dict(mp)
