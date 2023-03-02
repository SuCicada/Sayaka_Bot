def my_decorator(name):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Error: {e}")
                # Handle error or retry logic here
        return wrapper
    return _wrapper

from retry import retry

@my_decorator(name="my_function")
@retry(exceptions=Exception, tries=3, delay=1)
def my_function():
    # code here
    print("Hello world!")
    a = 1 / 0

my_function()