continua = True
valido = True
bissexto = None

while continua:



  mes = int(input("Entre com o mes:"))
  while (mes <1 or mes >12) and valido == True:
      if mes == -1:
          print ("\n bye bye!")
          
          valido = False
          continua = False
      else:
          print ("Mes invalido!")
          mes = int(input("Entre com o mes:"))



  if mes > 0:
    ano = int(input("Entre com o ano:"))
    while ano <1800 or ano >2099:
          print ("Ano invalido!")
          ano = int(input("Entre com o ano:"))

    

                
  def QuantidadeDiasMes():


            if (ano%4==0) and (not(ano%100==0) or (ano%400==0)):
                bissexto = True
            else:
                bissexto = False

            if mes == 2 and bissexto:
                qtd_dias = 29
            else:
                qtd_dias = 28

            if mes in (1,3,5,7,8,10,12):
                qtd_dias = 31

            elif mes in (4,6,9,11):
                qtd_dias = 30
            return qtd_dias


  qtd = QuantidadeDiasMes()
  #determinar o dia da semana em que começa o mes
  def DeterminarSemanaInicial():

        century_digits = ano //100
        year_digits = ano % 100

        value = year_digits + (year_digits // 4)

        if century_digits == 18:
            value = value + 2
        elif century_digits == 20:
            value = value + 6
        if mes == 1 and not bissexto:
            value = value + 1
        elif mes == 2:
            if bissexto:
                value = value + 3
            else:
                value = value + 4
        elif mes == 3 or mes == 11:
            value = value + 4
        elif mes == 5:
            value  = value + 2
        elif mes == 6:
            value = value + 5
        elif mes == 8:
            value = value + 3
        elif mes == 9 or mes == 12:
            value = value + 6
        elif mes == 10:
            value = value + 1

        day_of_week = (value + 1) %7

        return day_of_week 


  #determinar o nome do dia da semana
  def DeterminarNomeDia(y=DeterminarSemanaInicial()):
        m=y
        if m == 1:
            dia_nome = "Domingo"
        elif m == 2:
            dia_nome = "Segunda"
        elif m == 3:
            dia_nome = "Terça"
        elif m == 4:
            dia_nome = "Quarta"
        elif m == 5:
            dia_nome = "Quinta"
        elif m == 6:
            dia_nome = "Sexta"
        else:
            dia_nome = "Sabado"
            
        return dia_nome

  #determinar o nome do mes
  def DeterminarNomeMes():

        if mes == 1:
            mes_nome = "Janeiro"
        elif mes == 2:
            mes_nome = "Fevereiro"
        elif mes == 3:
            mes_nome = "Março"
        elif mes == 4:
            mes_nome = "Abril"
        elif mes == 5:
            mes_nome = "Maio"
        elif mes == 6:
            mes_nome = "Junho"
        elif mes == 7:
            mes_nome = "Julho"
        elif mes == 8:
            mes_nome = "Agosto"
        elif mes == 9:
            mes_nome = "Setembro"
        elif mes == 10:
            mes_nome = "Outubro"
        elif mes == 11:
            mes_nome = "Novembro"
        else:
            mes_nome = "Dezembro"

        return mes_nome

        
  z = DeterminarNomeMes()
  y=DeterminarSemanaInicial()
  #apresentar linhas de dias
  def LinhasDeDias():

        if z == 0:
            col_inicial = 7
        else:
            col_inicial = y

        col_atual = 1
        col_largura = 4
        espaco = " "
        coluna_vazia = format (espaco, str(col_largura))
    
        while col_atual < col_inicial:
            print(coluna_vazia, end = '')
            col_atual = col_atual + 1

        dia_atual = 1
        

        while dia_atual <= qtd:

            if dia_atual < 10:
                print (format(espaco, '3') + str (dia_atual), end = '')
            else:
                print (format(espaco, '2') + str (dia_atual), end = '')

            if col_atual < 7:
                col_atual = col_atual + 1
            else:
                col_atual = 1
                print()

            dia_atual = dia_atual + 1

        print("\n")




  if mes > 0 :
    print ('Quantidade de dias do mês de %s de %d = '%(DeterminarNomeMes(),ano),QuantidadeDiasMes())
    print ('Dia da semana em que o mês se inicia = %s'%DeterminarNomeDia())
    print (' | D | S | T | Q | Q | S | S |')
    print (LinhasDeDias())


