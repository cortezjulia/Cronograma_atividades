from datetime import datetime, date,timedelta
import os
from datetime import time
voltar_int=0

while True:
    os.system('cls')
    if voltar_int==1 or voltar_int==0: #DADOS INICIAIS
        nome_grupo=input('Insira o nome do Grupo Escoteiro: ')
        nome_ramo=input('Insira o Ramo Escoteiro: ')
        cidade=input('Insira a cidade: ')
        estado=input('Insira o estado: ')
        local=input('Insira o local: ')
    

    if voltar_int==3 or voltar_int==0: #ESCOLHA DE ATIVIDADES
        lista_atividades=[]
        while True:
            os.system('cls')
            try:
                quantidade_atividade=int(input('Quantas atividades você quer inserir: '))
                break
            except:
                print('Insira só números inteiros!')
                continue
        if voltar_int==3:
            if limite_ati!=quantidade_atividade:
                print(f'Aqui você só pode editar as {limite_ati} atividades inseridas, não pode remover nem adicionar!')
                quantidade_atividade=limite_ati

        for i in range(quantidade_atividade):
            atividade = input('Atividade: ')
            lista_atividades.append(atividade)
            

        for indice,nome in enumerate(lista_atividades):
            indice_final=indice+1
            print(indice_final,nome)

    if voltar_int==6 or voltar_int==0: #ESCOLHA DE DATA       
        
        data_atual=date.today()

        data_atual_em_texto = data_atual.strftime('%d/%m/%Y')
        #

        
        while True: 
            os.system('cls')
            print('O dia de hoje é = ',data_atual_em_texto)
            print('Podemos considerar essa data atual?')
            alterar_data=input('Para aceitar digite "sim" e para alterar digite "nao": ')
            if alterar_data.lower().startswith('n') and alterar_data.lower().endswith('o'):
                while True: 
                    os.system('cls')
                    print('Insira no seguinte formato: XX/XX/XXXX')
                    nova_data_entrada=input('Insira: ')
                    barra=0
                    dia_s=''
                    ano_s=''
                    mes_s=''
                    barra_indice=[]

                    if len(nova_data_entrada)!=10:
                        print('Você ultrapassou o limite de caracteres desse formato!')
                        continue
                    tamanho_data=len(nova_data_entrada)
                    j=0
                    while j<tamanho_data:
                        if nova_data_entrada[j]=='/':
                            barra+=1
                            barra_indice.append(j)
                        j+=1
                    soma_barra_indice=0
                    
                    for k in barra_indice:
                        soma_barra_indice+=k
                
                
                    if (barra!=2) or soma_barra_indice!=7:
                        print('Insira como na formatação indicada!')
                        continue

                    i=0
                    while i<len(nova_data_entrada):
                        if i==0 or i==1:
                            dia_s+=nova_data_entrada[i] 
                        
                        elif i==3 or i==4:
                            mes_s+=nova_data_entrada[i]
                        elif i>5:
                            ano_s+=nova_data_entrada[i]
                        i+=1
                    
                    
                    try:
                        dia_int=int(dia_s)
                        mes_int=int(mes_s)
                        ano_int=int(ano_s)
                    except:
                        print('Insira apenas números!')
                        continue
                    if dia_int>31:
                        print('Você inseriu um dia inválido! Tente novamente.')
                        continue
                    if mes_int>12:
                        print('Você inseriu um mês inválido! Tente novamente.')
                        continue
                    
                    nova_data_final=date(ano_int,mes_int,dia_int)
                
                    break
                    
                    
                data_atual_em_texto=nova_data_final.strftime('%d/%m/%Y')
                print(data_atual_em_texto)
                break

                            


            elif alterar_data.lower().startswith('s') and alterar_data.lower().endswith('m'):
                print('Você escolheu não alterar a data!')
                break

            else:
                    print('Insira [s]im ou [n]ao!')
                    continue

        print('***Definição de data concluída!***')
        os.system('cls')

    if voltar_int==2 or voltar_int==0: #HORA DE INICIO DAS ATIVIDADES
        while True: 
            os.system('cls')       
            print('Insira agora a hora de início das atividades!')
            print('Insira no seguinte formato:XX:XX:XX')
            hora_inicio=input('Insira: ')

            if len(hora_inicio)!=8:
                print('Você ultrapassou o limite de caracteres desse formato!')
                continue
            a=0
            pontos=0
            pontos_indice=[]
            while a<len(hora_inicio):
                if hora_inicio[a]==':':
                    pontos+=1
                    pontos_indice.append(a)
                a+=1
                
            soma_pontos_indice=0    
            for f in pontos_indice:
                soma_pontos_indice+=f
                
                
            if (pontos!=2) or soma_pontos_indice!=7:
                print('Insira como na formatação indicada!')
                continue

            d=0
            hora_s=''
            min_s=''
            seg_s=''
        
            while d<len(hora_inicio):
                if d==0 or d==1:
                    hora_s+=hora_inicio[d] 
                        
                elif d==3 or d==4:
                    min_s+=hora_inicio[d]
                elif d>5:
                    seg_s+=hora_inicio[d]
                d+=1
                    
                    
            try:
                hora_int=int(hora_s)
                min_int=int(min_s)
                seg_int=int(seg_s)
            except:
                print('Insira apenas números!')
                continue
            if hora_int>24:
                print('Você inseriu as horas de forma inválida! Tente novamente.')
                continue
            if min_int>60:
                print('Você inseriu os minutos de forma inválida! Tente novamente.')
                continue
            if seg_int>60:
                print('Você inseriu os segundos de forma inválida! Tente novamente.')
                continue
            
            nova_hora=str(time(hora_int,min_int,seg_int))
            
            break
        

    if voltar_int==4 or voltar_int==0: #DURAÇÃO DAS ATIVIDADES
        while True:
            os.system('cls')
            print('Vamos inserir agora a duração das atividades!')
            print('Insira no seguinte formato:XX:XX:XX')
            duraçoes=[]
            duraçoes.clear()
            flag_libera=0
            for indice,atividade in enumerate(lista_atividades):
                indice_novo=indice+1
                print(indice_novo,'-',atividade,':')
                entrada_duracao=input('Insira a duração: ')
                if len(entrada_duracao)!=8:
                    print('Você ultrapassou o limite de caracteres desse formato!')
                    flag_libera=1
                    break
                a=0
                pontos=0
                pontos_indice=[]
                while a<len(entrada_duracao):
                    if entrada_duracao[a]==':':
                        pontos+=1
                        pontos_indice.append(a)
                    a+=1
                
                soma_pontos_indice=0    
                for f in pontos_indice:
                    soma_pontos_indice+=f
                
                
                if (pontos!=2) or soma_pontos_indice!=7:
                    print('Insira como na formatação indicada!')
                    flag_libera=1
                    break

                d=0
                duracao_hora_s=''
                duracao_min_s=''
                duracao_seg_s=''
        
                while d<len(entrada_duracao):
                    if d==0 or d==1:
                        duracao_hora_s+=entrada_duracao[d] 
                        
                    elif d==3 or d==4:
                        duracao_min_s+=entrada_duracao[d]
                    elif d>5:
                        duracao_seg_s+=entrada_duracao[d]
                    d+=1
                    
                    
                try:
                    duracao_hora_int=int(duracao_hora_s)
                    duracao_min_int=int(duracao_min_s)
                    duracao_seg_int=int(duracao_seg_s)
                except:
                    print('Insira apenas números!')
                    flag_libera=1
                    break
                if duracao_hora_int>24:
                    print('Você inseriu as horas de forma inválida! Tente novamente.')
                    flag_libera=1
                    break
                if duracao_min_int>60:
                    print('Você inseriu os minutos de forma inválida! Tente novamente.')
                    flag_libera=1
                    break
                if duracao_seg_int>60:
                    print('Você inseriu os segundos de forma inválida! Tente novamente.')
                    flag_libera=1
                    break
                duraçoes.append(entrada_duracao)
            
            if flag_libera==1:
                continue
            else:
                break
    if voltar_int==2 or voltar_int==4 or voltar_int==0:#SOMATORIO DO HORARIO INICIAL COM OS HORARIOS DAS ATIVIDADES
        
        somatorio_duracoes=[]
        hora_int2=hora_int
        min_int2=min_int
        seg_int2=seg_int
        for indice,tempo in enumerate(duraçoes):

            
            tempo_1=timedelta(hours=hora_int2,minutes=min_int2,seconds=seg_int2)
            tempo_2=datetime.strptime(tempo,"%H:%M:%S")

            
            soma_tempo_12=tempo_1+tempo_2
            str_tempo_12=soma_tempo_12.strftime("%H:%M:%S")
        
            somatorio_duracoes.append(str_tempo_12)
            hora_int2,min_int2,seg_int2=map(int,str(str_tempo_12).split(':'))

    if voltar_int==5 or voltar_int==0: #NOME DE RESPONSÁVEL  
        os.system('cls') 
        print('Vamos inserir o nome do Escotista responsável por cada atividade!')
        nomes_chefes=[]
        for indice,atividade in enumerate(lista_atividades):
            indice_novo=indice+1
            print(indice_novo,'-',atividade,':')
            nome_chefe_entrada=input('Insira o nome do responsável: ')
            nomes_chefes.append(nome_chefe_entrada)

    if voltar_int==7 or voltar_int==0:#AREAS DE DESENVOLVIMENTO
        os.system('cls')
        print('Por favor, Insira agora a área de desenvolvimento das atividades!')

        areas=[]
        for indice,atividade in enumerate(lista_atividades):
            indice_novo=indice+1
            print(indice_novo,'-',atividade,':')
            area_dese=input('Insira a área de desenvolvimento: ')
            areas.append(area_dese)
    
    if voltar_int==8 or voltar_int==0:#MATERIAS USADOS NAS ATIVIDADES
        
        while True:
            os.system('cls')
            materiais=[]
            print('Você deseja inserir os materiais usados nas atividades?')
            pular_etapa=input('Insira "sim" ou "nao": ')
            
            if pular_etapa.lower().startswith('s') and pular_etapa.lower().endswith('m'):
                for indice,atividade in enumerate(lista_atividades):
                    indice_novo=indice+1
                    print(indice_novo,'-',atividade,':')
                    material=input('Insira os materias para a atividade apresentada: ')
                    materiais.append(material)

            elif pular_etapa.lower().startswith('n') and pular_etapa.lower().endswith('o'):
                break
            else:
                print('Insira [sim] ou [nao]!')
                continue
            break

    os.system('cls')
    print('**********************************')
    print('Grupo escoteiro:', nome_grupo)
    print('**********************************')
    print('Ramo:', nome_ramo)
    print('**********************************')
    print('Cidade:', cidade)
    print('**********************************')
    print('Estado:',estado)
    print('**********************************')
    print('Data:',data_atual_em_texto)
    print('**********************************')
    print('Hora de início:',nova_hora)
    print('**********************************')

    tamanho_atividades=len(lista_atividades)
    ind=0
    print('--------------------------------------------------------------------------------')
    print('Horário','------->','Atividades','------->','Responsável','------->','Áreas de Desenvolvimento','------->', 'Materiais') 
    print('--------------------------------------------------------------------------------')      
           

    if len(materiais)!=0:
        while ind < tamanho_atividades:
            
            print(somatorio_duracoes[ind],'------->',lista_atividades[ind],\
            '------->',nomes_chefes[ind],'------->', areas[ind],\
            '------->',materiais[ind])
            ind+=1
    else:
        while ind < tamanho_atividades:
            print(somatorio_duracoes[ind],'------->',lista_atividades[ind],\
            '------->',nomes_chefes[ind],'------->', areas[ind])
            ind+=1
    flag=0
    while True:
        flag=0
        print('*****************************************')
        print('*****************************************')
        print('Você quer sair ou editar algum parâmetro?')
        sair=input('Digite "e" para editar e "s" para sair:' )
        if sair.lower().startswith('e'):
            print('**********************************')
            print('**********************************')
            print('Insira o que você deseja alterar:')
            print('Dados Iniciais: [1]')
            print('Hora inicial:[2]')
            print('Atividades: [3]')
            print('Duração das atividades: [4]')
            print('Responsáveis: [5]')
            print('Data: [6]')
            print('Área de desenvolvimento: [7]')
            print('Materiais: [8]')
            print('Todos: [0]')
            voltar=input('Insira o número corresponde: ')
            try:
                voltar_int=int(voltar)
                if (voltar_int>=0) and (voltar_int<=8):
                    if voltar_int==3:
                        limite_ati=len(lista_atividades)
                    flag=1
                    break
            except:
                continue
            
        elif sair.lower().startswith('s'):
            break

        else:
            continue
   
    if flag==1:
        continue
    else:
        break




           
           
       
       
    






    
    

    




    
    







