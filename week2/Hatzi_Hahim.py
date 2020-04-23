"""
חצי חיים
קבלו מהמשתמש מילה מסוימת ומשפט.
בדקו שתחילת המילה מופיעה לפני החצי של המשפט.
היעזרו בדוגמאות כדי לבדוק את עצמכם.
    המילה Love במשפט I Love Chocolate תחזיר True, כיוון שהמילה Love מתחילה במקום 2, ואורך חצי המשפט הוא 8.
    המילה salad במשפט This is the best salad in town תחזיר False, כיוון שהמילה salad מתחילה במקום 17, ואורך חצי המשפט הוא 15.
    המילה Meow במשפט "All you need is Love" תחזיר False, כיוון שהמילה Meow לא נמצאת בשירים של הביטלס (וחבל שכך).

"""
sentence = input("Enter the sentence")
word_to_look_for_its_index = input("Enter the word you wish to tell if it shows before the middle of the sentence")
if sentence.find(word_to_look_for_its_index) == -1:
    print("False")
elif (len(sentence) / 2 - 1) > sentence.find(word_to_look_for_its_index):
    print("True")
else:
    print("False")
