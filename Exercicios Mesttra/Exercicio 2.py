SAL_MIN = float(input('informe o valor do sal�rio m�nimo'))

SAL = float(input('informe o valor do sal�rio do funcionario'))


if(SAL_MIN>SAL):

    print('O funcionaio ganha menos que um salario m�nimo!')

elif(SAL > SAL_MIN and SAL < (SAL_MIN*2)):

    print('O funcionario recebe 1-2 salarios minimo!')

else:

    print('O funcinario rebebe mais do que 2 salarios minimos!')