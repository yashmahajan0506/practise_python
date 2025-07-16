# Tickets Sold 
# Price Per Ticket 
# Calculate: 
# Total earnings for each movie 
# Movie with the highest earnings 
# example: 
# movies = [ 
# ["Avengers", 500, 10], 
# ["Inception", 300, 12], 
# ["Titanic", 400, 8] 
# ] 
# Output:- Total Earnings: [['Avengers', 5000], ['Inception', 3600], ['Titanic', 3200]] 
# Highest Earning Movie: ['Avengers', 5000] 
# Take movies data dynamic.

# movie=input("Enter the movie name:")

# for i in movie:

#     total=[]
#     high_earnign=[]

# movies = [ 
# ["Avengers", 500, 10], 
# ["Inception", 300, 12], 
# ["Titanic", 400, 8] 
# ] 

n=int(input("Enter Number of movie :"))

movies=[]
for i in range(n):
    movie_name=input("Enter the Name of movie:")
    price=int(input("Enter the Price  of movie:"))
    sold_ticket=int(input("Enter the Ticket price of movie:"))
    movies.append([movie_name,price,sold_ticket])

print("movies",movies)

earning_list=[]

for i in movies:
    movie_name=i[0]
    total_earnigs=i[1]*i[2]
    earning_list.append([movie_name,total_earnigs])

# highest = max(total_earnigs,key=lambda x: x[1])
highest = max(earning_list,key=lambda x :x[1])
print(highest)
# [['Avengers', 5000], ['Inception', 3600], ['Titanic', 3200]] 