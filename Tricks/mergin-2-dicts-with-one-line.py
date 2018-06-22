"""
Efficent way to merge 2 dictionaries with one line
"""
d1 = { 'Tomato': 8, 'Potato': 2.22 }
d2 = { 'Tuna': 2.5, 'ApplePenApplePen': 30}

merge_dics = {**d1, **d2} 
print(merge_dics)

