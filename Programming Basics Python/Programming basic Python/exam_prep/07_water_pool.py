obem = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

sum_pipes = (pipe1 + pipe2) * hours
overal_procent = sum_pipes / obem
first_pipe_procent = pipe1 * hours / sum_pipes
second_pipe_procent = pipe2 * hours / sum_pipes

if sum_pipes <= obem:
    print(f"The pool is {overal_procent:.2%} full. Pipe 1: {first_pipe_procent:.2%}. Pipe 2: {second_pipe_procent:.2%}.")
else:
    sum_pipes > obem
    print(f"For {hours} hours the pool overflows with {sum_pipes - obem} liters.")
