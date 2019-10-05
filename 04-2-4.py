numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
  value = counter.get(number)
  if( value != None):
    counter[number] = value + 1
  else:
    counter[number] = 1

print(counter)

character = {
  "name": "기사",
  "level": 12,
  "items": {
    "sword": "불꽃의 검",
    "armour": "풀플레이트"
  },
  "skill": ["베기", "세게 베기", "아주 세게 배기"]
}

for key in character:
  if type(character[key]) == str:
    print(key, ":", character[key])
  elif type(character[key]) == list:
    for l in character[key]:
      print(key, ":", l)
  elif type(character[key]) == dict:
    for key2 in character[key]:
      print(key2, ":", character[key][key2])