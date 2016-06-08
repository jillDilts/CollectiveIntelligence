#-----------------------------------------------------------------------------------
# recommendations.py
# file is taken from Toby Segaran's "Programming Collective Intelligence" First edition
#-----------------------------------------------------------------------------------

# A dictionary of movie critics and their ratings of a small set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 
        'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 
        'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, 'The Night Listener': 4.5,
        'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 
        'Superman Returns': 3.0, 'You, Me and Dupree': 2.0, 'The Night Listener': 3.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0, 
        'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
    'Toby': {'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0}}

#------------------------------------------------------------------------------------------
# Similarity Functions
#------------------------------------------------------------------------------------------
from math import sqrt


#------------------------------------------------------------------------------------------
# function sim_distance
# arguments: 
#    prefs: nested dictionary of preference rating scores
#    person1, person2: strings of names of people whose preferences to compare
# Returns a Euclidian distance-based similarity score for person1 and person2
#  (returns 0 if person1 and person2 have no ratings in common)
#------------------------------------------------------------------------------------------
def sim_distance(prefs, person1, person2):
    #Get the list of items shared by person1 and person2
    shared_items = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            shared_items[item] = 1
    
    #if the persons have no ratings in common, return 0
    if len(shared_items) == 0: return 0
    
    #Add up the squares of all the differences
    sum_of_squares = sum( [ pow( prefs[person1][item] - prefs[person2][item], 2 ) for item in shared_items ] )
    
    return 1 / (1 + sqrt(sum_of_squares) )
    
