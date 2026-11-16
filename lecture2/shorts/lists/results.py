results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) # here we add a list inside of the list
results.remove(["Bowser", "Donkey Kong Jr."]) # remove elements in the list
results.extend(["Bowser", "Donkey Kong Jr."]) # extend methods allows to append multiple elements in the list

print(results)


results1 = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results1.remove("Bowser")
results1.insert(0, "Bowser") # insert method allows to insert an element in a specific index

results1.reverse() # reverse method allows to reverse the order of elements in the list

print(results1)