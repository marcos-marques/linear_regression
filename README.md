## REGRESSÃO

Regressão é uma forma estatística de análise de dados. O termo regressão foi utilizado pela primeira vez por Sir Francis Galton, por volta de 1880, para denotar a regressão à média da população observada. Em estatística a *Regressão à Média* trata de como os dados se equilibram, isto é, se uma variável for extrema na primeira vez que for medida, ela estará mais próxima da média na próxima vez que for medida.     

Analisamos um conjunto de dados com a finalidade de entender o comportamento dos dados e como estes estão organizados. Um conjunto de dados estruturados, isto é, organizado em linhas e colunas por exemplo é formado por grupos de informações que identificam alguma característica desse conjunto de dados. Uma tabela de dados que apresente duas colunas sendo uma a idade e a outra o peso de uma criança recém nascida pode ser representada do seguinte modo:


|idade em meses| peso médio em kg|
|--------------|-----------------|
|0             | 3,2             |
|1             | 4,2             |
|2             | 5,1             |
|3             | 5,8             |
|4             | 6,4             |
|5             | 6,9             |


### Variáveis dependentes e independentes  


Ao analisar a tabela de dados é possível verificar que a medida que a idade da criança aumenta o peso da criança também aumenta, isto indica que há uma relação entre os valores das colunas. É importante no entanto observar que é a idade que varia definindo o peso e não ao contrário. Tomando essa relação como exemplo, é possível então dizer que há uma depêndencia entre os dados das colunas, que aqui podemos chamar de variáveis, ou seja, a variável *peso* depende da variável *idade*. Então se a idade aumenta, teremos da mesma forma um aumento no peso, denotando dessa forma uma dependência entre a variável peso e a variável idade.  
Diante desse cenário podemos então afirmar que temos uma variável dependente e uma variável independente, uma vez que o peso depende da idade. Quando esse fenômeno acontece, podemos afirmar que temos uma relação linear entre as variáveis, isto porque o aumento de uma resulta no aumento linear da outra.  
O que queremos dizer com linear? Queremos dizer que é possível expressar ou representar essa relação linha reta que representa o comportamento entre essas duas variáveis. Essa relação pode ser representada do seguinte modo:

![dependencia entre variáveis](images/variable_dependencies.png)


### Regressão Linear

Ao observermos a linha verde percebemos que há dois pontos na cor azul que representa a relação entre as variáveis *peso médio* e *idade em meses*. É possível notar que a medida que o valor da variável *y* cresce também o valor da variável *x*. Essa relação representada pela linha verde, entre as duas variáveis é chamada de **linear**, uma vez que pode ser exprimida por meio de uma linha reta. De forma geral quando duas variáveis aumentam ou diminuem simultaneamente temos então uma regressão linear.

### Regressão Linear Simples

Quando temos uma relação entre apenas duas variáveis, uma dependente e outra independente dizemos que a regressão é do tipo simples, uma vez uma variável dependente, isto é o *y* (peso médio) esta sendo explicada pela independente, neste caso *x* (idade em meses). Uma regresão linear pode ter uma relação *positiva* ou *negativa*:

**Relação Linear Positiva:** quando uma variável aumenta e a outra também aumenta, temos uma relação linear positiva.

**Relação Linear Negativa:** quando uma variável aumenta e a outra diminui, temos uma relação linear negativa.   

### Fórmula da Regressão Linear Simples

Um modelo de **regressão linear** é uma equação  matemática que fornece uma relação linear entre duas variáveis, isto é uma linha reta expressa normalmente por *x* e *y* que pode ser representada da seguinte forma:

------------------------

#### COEFICIENTE DE CORRELAÇÃO DE PEARSON

É um teste que mede a relação estatística, entre duas variáveis continuas. O coeficiente de correlação de Pearson pode ter um intervalo de valores +1 e -1. Um valor zero(0), indica que não há associação entre as variáveis.


#### RELAÇÃO LINEAR FRACA OU INEXISTENE

Quando temos valores muito dispersos no gráfico ao traçarmos uma linha, identificamos que os valores estão muito longe da linha. Nesse caso a correlação pode ser muito fraca ou inexistente.


#### FUNÇÃO DE CUSTO

A diferença entre os valores previstos e a verdade fundamental. Para isso elevamos ao quadrado a diferença do erro, somamos todos os pontos de dados e dividimos esse valor pelo número total de pontos de dados.


