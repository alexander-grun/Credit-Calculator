import argparse
import math
import sys

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Incorrect parameters")
    return ivalue

parser = argparse.ArgumentParser(description='Credit calc')
parser.add_argument('--type', required=True)
parser.add_argument('--principal', type = check_positive)
parser.add_argument('--periods', type = check_positive)
parser.add_argument('--interest')#, type = check_positive)
parser.add_argument('--payment', type = check_positive)
args = vars(parser.parse_args())

if args['type'] in ["annuity", "diff"]:
	pass
else:
	print('Incorrect parameters')


if args['interest'] is None:
	print('Incorrect parameters')
elif float(args['interest']) < 0:
	print('Incorrect parameters')
elif args['interest'] is not None:
	if args['type'] == 'annuity':
		if ((args['principal'] != None) & (args['periods'] != None) & (args['interest'] != None)):
			p = int(args['principal'])
			n = int(args['periods'])
			i = float(args['interest'])
			i_nom = (i / (12 * 100))
			one_plus_i = math.pow(1 + i_nom, n)
			a = p * ((i_nom * one_plus_i) / (one_plus_i - 1))
			a_rounded = math.ceil(a)
			print("Your annuity payment = {}!".format(a_rounded))
			total = a_rounded * n 
			print("Overpayment = ", total - p)
		elif ((args['payment'] != None) & (args['periods'] != None) & (args['interest'] != None)):
			a = int(args['payment'])
			n = int(args['periods'])
			i = float(args['interest'])
			i_nom = (i / (12 * 100))
			one_plus_i = math.pow(1 + i_nom, n)
			p = a / ((i_nom * one_plus_i) / (one_plus_i - 1))
			p = math.floor(p)
			print("Your credit principal = {}!".format(p))
			total = a * n
			print("Overpayment = ", total - p)
		elif ((args['payment'] != None) & (args['principal'] != None) & (args['interest'] != None)):
			p = int(args['principal'])
			a = int(args['payment'])
			i = float(args['interest'])
			i_nom = (i / (12 * 100))
			log_arg = (a / (a - i_nom* p))
			n = math.log(log_arg, (1 + i_nom))
			n_ceil = math.ceil(n)
			month = n_ceil % 12
			years = n_ceil // 12
			if years == 0:
				print("You need {} months to repay this credit!".format(month))
			elif month == 0:
				print("You need {} years to repay this credit!".format(years))
			else: 
				print("You need {} years and {} months to repay this credit!".format(years, month))
			total = a * n_ceil
			print("Overpayment = ", total - p)
		else:
			print("Incorrect parameters")
	elif args['type'] == 'diff':
		if ((args['principal'] != None) & (args['periods'] != None) & (args['interest'] != None)):
			p = int(args['principal'])
			n = int(args['periods'])
			i = float(args['interest'])
			i_nom = (i / (12 * 100))
			total = 0
			for m in range(1, n + 1):
				month = p / n + i_nom * (p - (p * (m - 1)) / n)
				month = math.ceil(month)
				print ("Month {}: paid out {}".format(m, month))
				total += month
			print("Overpayment = ", total - p)	
		else:
			print("Incorrect parameters")
	else:
		print("Incorrect parameters")

