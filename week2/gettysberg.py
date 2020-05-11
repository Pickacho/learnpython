gettysburg_address = """
Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth. 
"""
gettysburg_address = gettysburg_address.replace("—"," ")
gettysburg_address = gettysburg_address.replace("-"," ")
#type(gettysburg_address)
print(len(gettysburg_address.split())) #the number of word in the gettysburg speech
#print(gettysburg_address.split())

dedicated_count = gettysburg_address.count('dedicated')
nation_count = gettysburg_address.count('nation')
great_count = gettysburg_address.count('great')
here_count = gettysburg_address.count('here')
we_count = gettysburg_address.count('we')

# How to calculate? sum the times of each word repeat itself in the speech and multiply by 100 and divide by number of words in speech
dedicated_percent = (gettysburg_address.count('dedicated') * 100) / len(gettysburg_address.split())
nation_percent = (gettysburg_address.count('nation') * 100) / len(gettysburg_address.split())
great_percent = (gettysburg_address.count('great') * 100) / len(gettysburg_address.split())
here_percent = (gettysburg_address.count('here') * 100) / len(gettysburg_address.split())
we_percent = (gettysburg_address.count('we') * 100) / len(gettysburg_address.split())

total_times = dedicated_count + nation_count + great_count + here_count + we_count
total_times_percent = total_times * 100 /  len(gettysburg_address.split())
print("If I sum up the words 'dedicated, 'nation', 'great', 'here', 'we' it\'s", total_times,"and it\'", total_times_percent, "%")
