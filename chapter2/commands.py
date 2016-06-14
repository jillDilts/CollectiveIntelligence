# Commands used to demonstrate / use functions created in Collective Intelligence
import recommendations
from recommendations import critics

# pg 9:
critics['Lisa Rose']['Lady in the Water']
critics['Toby']['Snakes on a Plane'] = 4.5
critics['Toby']

# pg 11
recommendations.sim_distance( recommendations.critics, 'Lisa Rose', 'Gene Seymour' )

# pg 14
recommendations.sim_pearson( recommendations.critics, 'Lisa Rose', 'Gene Seymour' )

# pg 15
recommendations.topMatches( recommendations.critics, 'Toby', n = 3 )

# pg 17
recommendations.getRecommendations(recommendations.critics, 'Toby')

recommendations.getRecommendations(recommendations.critics, 'Toby', similarity = recommendations.sim_distance)

movies = recommendations.transformPrefs( recommendations.critics )

recommendations.topMatches(movies, 'Superman Returns')

recommendations.getRecommendations(movies, 'Just My Luck')
