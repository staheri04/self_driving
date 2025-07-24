scores = input("nomre ha ro ba fasele vared kon: ")
score_list = [int(s) for s in scores.split()]
high_scores = []
for s in score_list : 
	if s > 14:
		high_scores.append(s)

with open("high_scores.txt", "w") as f:
	for score in high_scores:
		f.write(str(score) + "\n")
