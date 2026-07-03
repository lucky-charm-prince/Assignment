subs=input("enter the subscription=").lower()
progress=85
score=65
if subs=="pre":
	if  progress>=80:
		if score>=70:
			print("unlock certificate")
		else:
			print("retry test")
	else:
		print("ask to complete the course")
elif subs=="basic":
	if progress>=50:
		print("allowed limited progress")
	else:
		print("lock content")
else:
	print("deny access")
	
