
Math=int(input('Enter your Math marks '))
Physics=int(input('Enter your Physics marks '))
English=int(input('Enter your English marks '))
Urdu=int(input('Enter your Urdu marks '))
Chemistry=int(input('Enter your Chemistry marks '))
total_marks=Math+Physics+English+Urdu+Chemistry
print('Your Total marks are '+ str(total_marks))
percentage=(total_marks/500)*100
percentage=round(percentage,2)
print('Your Percentage for total marks are ' +str(percentage) + ' %')
if Math<60 or Physics<60 or English < 60 or Urdu < 60 or Chemistry<60 or percentage<=60:
    print('Your are Fail because of low marks or percentage 92 and grade is \"F\"')
elif percentage >=61 and percentage <= 69:
    print('Your percentage is low and grade is \"C\"')
elif percentage >=70 and percentage <=79:
    print('Your percentage is normal and grade is\"B\"')
elif percentage >=80 and percentage <=89:
    print('Your percentage is High and grade is \"A\"')
elif percentage >=90 and percentage<=100:
    print('Your percentage is very High and grade is \"A+\"')