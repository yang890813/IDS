#Hw0 Problem2
#用來得到各項目位置之function
def get(key):
  return(col_name.index(key))
data_name = 'IMDB-Movie-Data.csv'
original_data = []
for i in open(data_name,'r'):
  original_data.append(i.split(','))
data = original_data[1:]
col_name = original_data[0]

#(1)
print('#(1)')
movie_2016 = {}
#整理出所有2016的電影和Rating
for i in data:
  if i[get('Year')]=='2016':
    movie_2016[i[get('Title')]]=i[get('Rating')]
print(sorted(movie_2016.items(),key = lambda movie:movie[1],reverse = True)[:3])
#(2)
print('#(2)')
all_rev = {}
#一個key為actor名字，value為包含其所有演過電影獲得revenue的list
for movie in data:
#在遇到缺失值因為float("")會報錯，進入except，則可忽略缺失值
  try:
    rev = float(movie[get('Revenue (Millions)')])
    actors = movie[get('Actors')]
    for actor in actors.split('|'):
      actor = actor.strip('')
      if actor in all_rev:
        all_rev[actor].append(rev)
      else:
        all_rev[actor]=[rev]
  except:
    continue
average_revenue = {}
#再從原始有所有revenue的dictionary整理出平均revenue的dictionary
for actor in  all_rev:
  ave_rev = sum(all_rev[actor])/len(all_rev[actor])
  average_revenue[ave_rev]=actor
print(sorted(average_revenue.items(),reverse = True)[0])

#(3)
print('#(3)')
ratings_emma = []
#建立所有Emma Watson演過電影的rating組成之list
for movie in data:
  if 'Emma Watson' in movie[get('Actors')]:
    ratings_emma.append(float(movie[get('Rating')]))
print(sum(ratings_emma)/len(ratings_emma))
#取平均
#(4)
print('#(4)')
collab_list = {}
#建立key為導演名稱，value為所有與其合作過演員的dictionary
for movie in data:
  actors = []
  for actor in movie[get('Actors')].split('|'):
    actors.append(actor.strip())
  director = movie[get('Director')]
  if director in collab_list:
    for actor in actors:
      collab_list[director].append(actor)
  else:
    collab_list[director]=actors
collab_list_setted={}
#從上面的dictionary建立下面相同key，value為合作演員數量的dictionary
for director in collab_list:
  collab_list_setted[director]=len(set(collab_list[director]))
print(sorted(collab_list_setted.items(),key = lambda dir:dir[1],reverse=True)[:4])
#(5)
print('#(5)')
genres = {}
#建立key為演員，value為演過的所有genre的dictionary
for movie in data:
  for actor in movie[get('Actors')].split('|'):
    if actor.strip() in genres:
      genres[actor.strip()]+=movie[get('Genre')].split('|')
    else:
      genres[actor.strip()]=movie[get('Genre')].split('|')
num_of_gen={}
#再建立value為所有演過genre數量的dictionary
for actor in genres:
  num_of_gen[actor] = len(set(genres[actor]))
print(sorted(num_of_gen.items(),key = lambda actor:actor[1],reverse = True)[:12])
#(6)
print('#(6)')
#先建立key為演員名稱，value為其gap year之dictionary
gap_year = {}
for movie in data:
  actors = movie[get('Actors')].split('|')
  for actor in actors:
    if actor.strip() in gap_year:
     continue
    else:
      years = []
      for i in range(len(data)):
        if actor.strip() in data[i][get('Actors')]:
          years.append(int(data[i][get('Year')]))
  gap_year[actor.strip()] = max(years)-min(years)
#若滿足value等於最大gap year(10)的演員則放入answer list
answer = []
for i in gap_year:
  if gap_year[i]==max(gap_year.values()):
    answer.append(i)
print(answer)
#(7)
print('#(7)')
answer = []
movie_to_delete = data
while True:
  ori_actors = ['Johnny Depp']
  new_actors = []
  for i,movie in enumerate(movie_to_delete):
    actors = movie[get('Actors')].split('|')
    for ori_actor in ori_actors:
      if ori_actor.strip() in movie[get('Actors')]:
        for actor in actors:
          new_actors.append(actor)
        del movie_to_delete[i]
      else:
        continue
    ori_actors = new_actors
  if len(new_actors) == 0:
    break