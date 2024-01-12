import mlflow

def calculator(x,y,operation=None):
    if operation == 'add':
        return x+y
    if operation == 'sub':
        return x-y
    if operation == 'mult':
        return x*y
    if operation == 'div':
        return x/y

if __name__ == "__main__":
    x=17
    y=37
    operation = "add"
    with mlflow.start_run():
        result = calculator(x, y,operation)
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_param("operation",operation)
        print(f"my result for {operation} is  : {result}")
        mlflow.log_param('result', result)