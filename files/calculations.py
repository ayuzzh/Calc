from multiprocessing import Process
from time import sleep

def calc(equation):
	if equation == "":
		result = ""
	
	try:
		result = str(eval(equation))
	
	except NameError:
		result = "Clear the screen"
	
	except SyntaxError:
		result = "Invalid Syntax"
	
	except ZeroDivisionError:
		result = "Complex Number"
	
	
	file = open("result.txt", "a")
	print(result)
	file.write(result)
	file.close()
	


def wait_and_kill(process):
	sleep(0.1)
	process.terminate()
	print("Tried to kill the Calculation process and seems to succended")


def calculate(equation):
	calc_process = Process(target=calc, args=(equation,))
	calc_process.start()
	killer = Process(target=wait_and_kill, args=(calc_process,))
	killer.start()
	calc_process.join()
	killer.join()
	result = open("result.txt", "r").read()
	open("result.txt", "w").close()
	if result == "":
		return "Lack of Memory"
	elif len(result) >= 20:
		print("Number too large to display")
		return "Value too big"
	else:
		return result


if __name__ == "__main__":
	sys.exit()
