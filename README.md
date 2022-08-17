# Desafio-Crawler---Leonardo-Alcantara
A biblioteca utilizada foi o Selenium, o código entra no site e localiza a partir do XPATH do HTML.
Foi utilizado também a biblioteca time, pois dependendo da conexão ou do processamento do computador, pode ser que o tempo não seja suficiente para carregar a página e 
o crawler não consiga identificar corretamente o XPATH, além disso, o XPATH foi encontrado a partir da página automatizada, pois em alguns sites o HTML pode mudar e ele 
encontra o erro "NoSuchElementException", ou seja, o elemento não foi encontrado.
O crawler segue o passo a passo do vídeo apresentado, entra na aba de pesquisa, coloca "Congresso Nacional - Brasília" e abre a aba, logo depois ele encontra o valor de 
"4.5" da avaliação e a quantidade de avaliações, seu texto precisa ser formatado, por isso utilizei o split, adicionando os valores a uma lista e printando apenas o 
primeiro valor desta. Logo depois ele printa o valor formatado da forma que foi pedido.
