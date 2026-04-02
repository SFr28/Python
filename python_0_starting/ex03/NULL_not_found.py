def NULL_not_found(object: any) -> int:
	match object:
		case None:
			print("Nothing :", object, type(object))
			return 0
		case float() if object != object:
			print("Cheese :", object, type(object))
			return 0
		case int() if object == 0:
			print("Zero :", object, type(object))
			return 0
		case str() if object == "":
			print("Empty :", object, type(object))
			return 0
		case bool() if object == False:
			print("Fake :", object, type(object))
			return 0
		case _:
			print("Type not found")
			return 1