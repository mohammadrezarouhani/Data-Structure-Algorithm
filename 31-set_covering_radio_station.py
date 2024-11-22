# we have some sypothetical radio station each of them covering some state in unoted state
# the problem is how can we select a minimum number of raio station that cover all of the state
# we call this problem set covering problems, this problem solving easily with greedy algorithm 

# gridy algorithm

states={'wa','mt','id','or','ca','nv','ut','ca','az'}

state_cover={}
state_cover['one']={'id','mt','uv'}
state_cover['two']={'wa','mt','id'}
state_cover['tree']={'or','ca','nv'}
state_cover['four']={'nv','ut'}
state_cover['five']={'ca','az'}

result=[]

while states:
    best_station=None
    state_covered=0
    for key in state_cover.keys():
        state_covered=states and state_cover[key]
        if len(state_covered)>state_covered:
            best_station=key
    else:
        states-=state_covered
        result.append(best_station)


print(result)