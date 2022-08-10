#list or array
student_name = ["John", "Kim", "Song" ]
print(student_name[0])
student_name[1] = "Tom"
print(student_name)


#tuple - same as list - immutable 
student_family_name = ("Kim", "Song", "Lee")
print(student_family_name[2])

#student_family_name[1] = "TTTTom" #Error - tuple contents cannot be changed


#dictionary
#korean["apple"] -> "사과"
kims_score_dict = {"english": 100 , "math": 90 , "art": 95}
print(kims_score_dict["english"]) # 100
print(kims_score_dict["art"])
kims_score_dict["math"] = 95
print(kims_score_dict["math"])
print(kims_score_dict)

#math 90 -> 95

mykeys = kims_score_dict.keys()
print(mykeys)

myvalues = kims_score_dict.values()
print(myvalues)


#dictionary 3 EA

#song_score_dict : keys = "english", "math", "art"
song_score_dict = {"english":100, "math":95, "art":90}

lee_score_dict = {"english":85, "math":91, "art":88}

john_score_dict = {"english":67, "math":95, "art":70}

#1. print "english" score of lee
print(lee_score_dict["english"])

#2. print "math" score of john
print(john_score_dict["math"])


def get_average(dict):
  average = (dict["english"] + dict["math"] +dict["art"])/len(dict)
  return average

  
#3. print songs average score of english,math,art
average = (song_score_dict["english"] + song_score_dict["math"] + song_score_dict["art"])/len(song_score_dict)

song_average = get_average(song_score_dict)
print(song_average)


