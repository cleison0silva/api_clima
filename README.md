# api_clima
Exercício consulta de clima pelo nome da cidade

Mais um exercício usando uma API pública, agora para consultar o clima, passando o nome de uma cidade.

Inicialmente foram criadas duas funções, uma para fazer a requisição na API e a outra para fazer a impressão dos valores.

Nas linhas 4 até 11 foi criada a função requisicao onde se conecta a API pública.

Logo depois nas linhas 13 até 18 foi criada a função printar, onde duas variáveis vão coletar as informações da condição do clima e da temperatura.

Por fim nas linhas 21 até 32 temos um laço de repetição onde é solicitado para o usuário digitar o nome da cidade ou SAIR para finalizar o programa, armazenando a informação na variável op. Também é feito um teste para saber se o resultado da requisição é 404 onde o nome da cidade não é encontrada, por fim o resultado é mostrado no fim do programa.
