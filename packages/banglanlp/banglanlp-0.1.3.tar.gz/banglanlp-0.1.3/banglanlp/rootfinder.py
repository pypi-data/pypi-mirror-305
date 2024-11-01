import json
import pkg_resources
import pandas as pd

# Reading from a JSON file and load in list

abc = ['অ','আ','ই','ঈ','উ','ঊ','ঋ','এ','ঐ','ও','ঔ','ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য','য়','র','ল','শ','ষ','স','হ','ড়','ঢ়']
list = []

def load_dataset(filename):
    dataset_path = pkg_resources.resource_filename(__name__, f'data/{filename}')
    with open(dataset_path, 'r') as file:
        return json.load(file)


for i in abc:
    x = f"dict{i}.json"
    try:
        y = load_dataset(x)
        list.append(y)  
    except ValueError as e:
        print(f"Error loading {x}: {e}")  

latter_uniqueness = load_dataset('latter_uniqueness.json')

def replace_য়(string):

  old_char = "়"
  new_char = ["য়","ড়"]
  result = ""
  prev_char = None
  for char in string:
    if char == '়' and prev_char == 'য':
      result = result[0:-1]
      result += new_char[0]
    elif char == '়' and prev_char == 'ড':
      result = result[0:-1]
      result += new_char[1]
    else:
      result += char
    prev_char = char
  return result


# function for make word unique value dimention

def uniqueness(text):  
    li1 = []
    for i in text:
        for a,b in latter_uniqueness.items():
            if i==a:
                li1.append(b)
    return li1

two_latter_word = {}
for i in list:
    for key,value in i.items():
        if len(key)==2:
            two_latter_word[key] = value
    
    
    
# find best match from dict

def find_best_matching_key(text,dict):
    max_matches = 0
    best_key = None

    li = uniqueness(text)
    best_keys = []
    for key, value_list in dict.items():
        matches = 0
        for i in range(min(len(li), len(value_list))):
            if li[i] == value_list[i]:
                matches += 1
            else:
                break


        if matches > max_matches:
            max_matches = matches
            if max_matches>2:
                best_keys = [key]
            else:
                best_keys = [li]
        elif matches == max_matches:  # jodi same match hoi sob akta list e rekhe sob theke soto ta print korbe
          best_keys.append(key)
        


    
    x = min(best_keys, key=len)
    if len(x) >= len(text):         # text er theke match word boro hole text return korbe
        x = text
    elif (max_matches<3) and (len(text)>=4):  # text remove korar por akdom soto hole original text retunr korbe
        x = text
    elif (max_matches<4) and (len(text)>=5):  # text remove korar por akdom soto hole original text retunr korbe
        x = text
       
            

    return x

# its for only noun to remonve prefix

# ['কে', 'দের', 'ই', 'ও', 'রে', 'রাও','রা' ,'সহ',"তে",',ে' ]
suffix_list = [[28,7], [45,7,55], [19], [26], [7, 55], [55, 1, 26], [55, 1], [59, 60],[43,7],[38, 1, 28, 7], [30, 4, 56, 9],[30, 4, 56, 3, 55],[30, 4, 56, 3],[30, 4, 56, 9, 55],[30, 4, 56, 3, 55],[30, 4, 56, 3,27,7],[30, 4, 56, 9],[30, 4, 56, 9, 28, 7],[38, 3],[38,1]]
m = [18, 52, 1]


def make_noun_list(text):
  result = uniqueness(text)     #noun er uniqueness korbe
  list = uniqueness(text)
    
  for sublist in suffix_list:
    sublist_len = len(sublist)
    list_len = len(list)

    if list_len >= sublist_len:
      for i in range(sublist_len):
        if sublist[-i-1] != list[-i-1]:     # sublist thakle remove korbe
            break
      else: 
          if len(result)<=3:
              break
          else:
              result = result[:-sublist_len] 
              if len(result)>=3:
                  break
              elif len(result)<=2:
                  for key, value in two_latter_word.items():
                    if value == result:
                        return result
                  if result==[43,1]:
                      result = list
               
  for i in range(len(list)):
      if (list[i]==13):
          if (list[i+1]==28):
              result = list


    
  count = 0
  for i in range(len(list) - len(m) + 1):
    if list == m[i:i+len(list)]:
      count +=1
  if count==3:
      result = list
  return result



def find_key_depend_on_list_letter(search_value):
  for key, value in latter_uniqueness.items():
    if value == search_value:
      return key
        
def noun_original_form(text):
    list_of_values = make_noun_list(text)
    list_of_keys = []
    for i in list_of_values:
        list_of_keys.append(find_key_depend_on_list_letter(i))    # list theke word a convert
    
    result = "".join(list_of_keys)
    return result


def find_from_dataset(text):    # dataset theke data extract korbe first latter anujayi
    match text[0]:
        case 'অ':
            x = find_best_matching_key(text,list[0])
            return x
        case 'আ':
            x = find_best_matching_key(text,list[1])
            return x
        case 'ই':
            x = find_best_matching_key(text,list[2])
            return x
        case 'ঈ':
            x = find_best_matching_key(text,list[3])
            return x
        case 'উ':
            x = find_best_matching_key(text,list[4])
            return x
        case 'ঊ':
            x = find_best_matching_key(text,list[5])
            return x
        case 'ঋ':
            x = find_best_matching_key(text,list[6])
            return x
        case 'এ':
            x = find_best_matching_key(text,list[7])
            return x
        case 'ঐ':
            x = find_best_matching_key(text,list[8])
            return x
        case 'ও':
            x = find_best_matching_key(text,list[9])
            return x
        case 'ঔ':
            x = find_best_matching_key(text,list[10])
            return x
        case 'ক':
            x = find_best_matching_key(text,list[11])
            return x
        case 'খ':
            x = find_best_matching_key(text,list[12])
            return x
        case 'গ':
            x = find_best_matching_key(text,list[13])
            return x
        case'ঘ':
            x = find_best_matching_key(text,list[14])
            return x
        case 'ঙ':
            x = find_best_matching_key(text,list[15])
            return x
        case 'চ':
            x = find_best_matching_key(text,list[16])
            return x
        case 'ছ':
            x = find_best_matching_key(text,list[17])
            return x
        case 'জ':
            x = find_best_matching_key(text,list[18])
            return x
        case 'ঝ':
            x = find_best_matching_key(text,list[19])
            return x
        case 'ঞ':
            x = find_best_matching_key(text,list[20])
            return x
        case 'ট':
            x = find_best_matching_key(text,list[21])
            return x
        case 'ঠ':
            x = find_best_matching_key(text,list[22])
            return x
        case 'ড':
            x = find_best_matching_key(text,list[23])
            return x
        case 'ঢ':
            x = find_best_matching_key(text,list[24])
            return x
        case 'ণ':
            x = find_best_matching_key(text,list[25])
            return x
        case 'ত':
            x = find_best_matching_key(text,list[26])
            return x
        case 'থ':
            x = find_best_matching_key(text,list[27])
            return x
        case 'দ':
            x = find_best_matching_key(text,list[28])
            return x
        case 'ধ':
            x = find_best_matching_key(text,list[29])
            return x
        case 'ন':
            x = find_best_matching_key(text,list[30])
            return x
        case 'প':
            x = find_best_matching_key(text,list[31])
            return x
        case 'ফ':
            x = find_best_matching_key(text,list[32])
            return x
        case 'ব':
            x = find_best_matching_key(text,list[33])
            return x
        case 'ভ':
            x = find_best_matching_key(text,list[34])
            return x
        case 'ম':
            x = find_best_matching_key(text,list[35])
            return x
        case 'য':
            x = find_best_matching_key(text,list[36])
            return x
        case 'য়':
            x = find_best_matching_key(text,list[37])
            return x
        case 'র':
            x = find_best_matching_key(text,list[38])
            return x
        case 'ল':
            x = find_best_matching_key(text,list[39])
            return x
        case 'শ':
            x = find_best_matching_key(text,list[40])
            return x
        case 'ষ':
            x = find_best_matching_key(text,list[41])
            return x
        case 'স':
            x = find_best_matching_key(text,list[42])
            return x
        case 'হ':
            x = find_best_matching_key(text,list[43])
            return x
        case 'ড়':
            x = find_best_matching_key(text,list[44])
            return x
        case 'ঢ়':
            x = find_best_matching_key(text,list[45])
            return x
        case _:
            x = text
            return x
        
        
def bstem(text):  # final step
    
    # make a list of givent input text
    list = []
    li = text.split()
    for i in li:
        x = replace_য়(i)
        list.append(x)
        

    # make two list one for noun and one for other
    list1 = []
    list2 = []
    for i in list:
        x = noun_original_form(i)
        if len(i) <= len(x):
            list2.append(i)  # input text jodi soto hoi tahole otai print korbe
        else:
            list1.append(x)
            
    # find other root word and make one main list
    for i in list2:
        list1.append(find_from_dataset(i))

    string = ' '.join(list1)
    return string
    
