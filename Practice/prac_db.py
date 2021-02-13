from pymongo import MongoClient

# local에서 DB를 만드는 과정
client = MongoClient('localhost', 27017)
db = client.dbpractice

# 코딩 시작

# insert
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# doc = {'name':'john','age':27}
# db.users.insert_one(doc)
#
# doc = {'name':'smith','age':30}
# db.users.insert_one(doc)
#
# doc = {'name':'jane','age':21}
# db.users.insert_one(doc)


# find
# people = list(db.users.find({},{'_id':False}))
# for person in people :
#     print(person)
# print()
#
# # find에 조건을 걸어서 찾을수도 있다.
# ages_21 = list(db.users.find({'age':21},{'_id':False}))
# for person in ages_21 :
#     print(person)
# print()
#
# # 데이터를 한개만 찾을 때는 다음과 같이 한다.
# user = db.users.find_one({'name' : 'bobby'},{'_id':False})
# print(user)


# update
# db.users.update_one({'name' : 'bobby'}, {'$set':{'age' : 19}})
# db.users.update_many({'name' : 'bobby'}, {'$set':{'age' : 21}})


# delete
# db.users.delete_one({'name' : 'bobby'})
# db.users.delete_many({'name' : 'bobby'})

