
a = '00011'

def binary(decimal):
	binary = "";
	while decimal > 0:
		binary =  str(decimal%2) + binary
		decimal = int(decimal/2)
	return binary




def onesCompliment(binary):
	ocm = ""
	# get the compliments of each digit 
	for l in binary:
		if int(l) == 0:
			ocm = ocm + "1" 
		else:
			ocm = ocm + "0"  
	return ocm



def twosCompliment(ocm):
	tcm = ''
	i = len(ocm)-1
	
	carry = '0';
	if int(ocm[i]) + 1 == 2:
		carry = '1'
		tcm =  '0' + tcm  
	else:
		tcm =  tcm + '1'

	i = i -1 #

	while i >= 0:
		if int(ocm[i]) + int(carry) == 2:
			tcm = '0' + tcm 
		else:
			tcm = str(int(carry) + int(ocm[i])) + tcm
			carry = '0'
		i = i -1
	return tcm



decimal = 23
print('Decimal : ' + str(decimal))
bnr= binary(decimal)
print('Binary: ' + bnr)
ocm = onesCompliment(bnr)
print('One\'s Compliment: ' + ocm)
tcm = twosCompliment(ocm)
print('Two\'s compliment: ' + tcm)
			




