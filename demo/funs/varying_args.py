def print_names(*names, message='Hello'):
    for n in names:
        print(f'{message} {n}')


print_names('Scott', 'Steve', "Job", message="Hi")
print_names('Andy', 'Mike')
