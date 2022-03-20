
#print(int(15/2))



def binary(decimal):
	binary = "";
	while decimal > 0:
		binary =  str(decimal%2) + binary
		decimal = int(decimal/2)
	return binary

#
def onesCompliment(binary):
	ocm = ""
	# get the compliments of each digit 
	for l in binary:
		if int(l) == 0:
			ocm = ocm + "1" 
		else:
			ocm = ocm + "0"  
	return ocm

def towsCompliment(ocm):
	tcm = ""
	for l in ocm:
		if 


		#




	
def typeofInput(num):
	if num >=0 && num <= 225:
		return 'unsignedInt'
	elif num >= -127 && num <= 127
		return 'onesComplimnet '
	elif num >= -128 && num <=127
		return 'towsCompliment'

		


	

print(binary(128))