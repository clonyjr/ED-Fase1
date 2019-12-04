INSTRUÇÕES E ESCLARECIMENTOS PARA UTILIZAR O PROGRAMA QUE PERMITE VER OS GRÁFICOS QUE RESPONDEM ÀS PERGUNTAS ELABORADAS

**** ESCLARECIMENTOS ****
O programa foi desenvolvido na linguagem Pyhton®. Os dados foram tratados e extraídos para dois arquivos CSV (queryBestFare.csv e queryWeather.csv) As queries utilizadas estão no arquivo ED-ANALYSIS-QUERIES-final.sql

**** INSTRUÇÕES DE EXECUÇÃO ****
Ao descompactar o arquivo zipado, será criada uma pasta denominada Lab5_exercise. O conteúdo dessa pasta possui os arquivos csv's, o arquivo com as queries (conforme mencionado na seção ESCLARECIMENTOS) e um script/programa em python chamado connect.py e um arquivo para instalação das dependências para o script/programa em Python chamado installDependencies.bat onde contém comandos que verifica se no computador onde será executado o programa existe a instalação da linguagem python e instala as dependências para o programa. Como o programa em python connect.py utiliza de bibliotecas para gerar gráfico, bibliotecas para apresentação dos dados no browser e outra biblioteca para acessar o banco de dados, é necessário instalar as dependências, isto é, as bibliotecas para o correto funcionamento da aplicação.

**** EXECUÇÃO DO ARQUIVO installDependencies.bat ****
Esse arquivo deve ser chamado pelo prompt da linha de comando do windows de dentro da pasta Lab5_exercise, ou seja, a diretoria exibida na linha de comando do windows deve exibir o caminho onde a pasta Lab5_exercise foi descompactada/criada. A partir daí deve digitar installDependencies e pressionar o botão <ENTER>. O bat vai verificar se o python está instalado, caso esteja instalado ele fará as instalações das dependências automaticamente e, ao seu término, executará o programa connect.py. A seguir o programa abre o browser e 3 abas. A primeira aba é do servidor web a segunda aba exibe o gráfico da resposta da primeira pergunta e a terceira aba exibe o gráfico da resposta para a segunda pergunta. ATENÇÃO, SE NÃO EXISTIR A INSTALAÇÃO DO PYTHON O ARQUIVO NÃO REALIZA AÇÃO ALGUMA E APENAS EXIBE UMA INFORMAÇÃO DA NECESSIDADE DE INSTALAR O PYTHON, TERMINANDO A EXECUÇÃO DO .BAT.

**** EXECUÇÃO DO ARQUIVO connect.py ****
Caso já haja instalação do python e se deseje executar o arquivo connect.py diretamente, basta acessar pela linha de comando na diretoria do arquivo e digitar o comando python connect.py para as versões 2.X do python. Caso a versão do python instalada seja a 3.X.X deve digitar o comando python3 connect.py

