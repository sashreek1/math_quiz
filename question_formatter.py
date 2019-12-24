que_file = open("/home/sashreek/PycharmProjects/GCI/math_app_ques", 'r')
new_file = open('/home/sashreek/PycharmProjects/GCI/math_app_ques_csv','w')
text = que_file.read()
text = text.split('\n')
string = ''
for i in text:
    txt = i+'\t\t,\t\t'
    string+=txt
new_file.write(string)
new_file.close()
que_file.close()