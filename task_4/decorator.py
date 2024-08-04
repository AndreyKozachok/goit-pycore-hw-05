
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone pleas."
        except KeyError:
            return "Contact not exist."
        except IndexError:
            return "Enter name."
            
    return inner


