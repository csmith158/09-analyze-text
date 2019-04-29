un# Remember to reach out for help after your own due diligence

def analyze_text(text):
    e_count = 0
    for i in (text):
        if i == "e":
            e_count = e_count + 1
        elif i == "E":
            e_count = e_count +1
    
    total_count = 0
    
    for i in (text):
        if i.isalpha():
            total_count = total_count + 1
        elif i.islower():
            total_count = total_count + 1
    
    percent = (e_count/total_count)*100
    
    answer = "The text contains {0} alphabetic characters, of which {1} (%.2f%) are ‘e’" %percent
    print(answer.format(total_count, e_count)
