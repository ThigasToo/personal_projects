# Carrossel de Mensagens Especiais ❤️

Este é um pequeno projeto pessoal e afetivo: uma página web de arquivo único (`.html`) que exibe um carrossel 3D animado e interativo. Foi criado para compartilhar uma série de mensagens de uma forma criativa e especial.

O projeto é construído inteiramente com HTML, CSS e JavaScript vanilla, sem a necessidade de bibliotecas externas.

![Demo do Carrossel](https://i.imgur.com/link-para-seu-gif-ou-imagem.gif)
*(Sugestão: grave um GIF da tela para colocar aqui e mostrar o efeito!)*

## 🚀 Como Funciona

A interação com o carrossel é simples e fluida. O usuário pode navegar pelas mensagens de três maneiras:
* **Roda do Mouse (Scroll):** Role para cima ou para baixo para avançar ou retroceder.
* **Arrastar (Drag):** Clique e arraste os cartões para os lados.
* **Clicar:** Clique diretamente em um cartão para trazê-lo para o foco.

## 🎨 Como Personalizar

Você pode facilmente alterar tanto as mensagens quanto adicionar suas próprias imagens aos cartões.

### Alterando os Textos
Para mudar as mensagens, abra o arquivo `moça_bonita_git.html` em um editor de texto e edite o conteúdo dentro das `divs` com a classe `"title"`.

**Exemplo:**
```html
<div class="carousel-item">
    <div class="carousel-box">
        <div class="title">Sua nova mensagem incrível aqui ✨</div> 
        <div class="num">01</div>
        <img src=""/>
    </div>
</div>
```
### Adicionando Imagens Locais (com Base64)
Os cartões estão prontos para receberem imagens de fundo. Para adicionar uma imagem do seu próprio computador sem precisar hospedá-la em um site, você pode convertê-la para o formato Base64 e colar o código diretamente no HTML.
Siga estes passos:
1. Escolha sua imagem no computador (formatos como .jpg, .png, .gif funcionam bem).
2. Acesse um conversor online. Uma ótima opção é o base64.guru.
3. Faça o upload da sua imagem no site.
4. O site irá gerar um longo código de texto. Copie o código completo que aparece no campo de resultado. Ele começará com data:image/jpeg;base64,... (ou similar).
5. Cole o código copiado dentro das aspas do atributo src="" da tag <img> no cartão desejado.

 - Antes: 
```HTML
<div class="carousel-item">
    <div class="carousel-box">
        <div class="title">Somos fodas juntos 🎀</div>
        <div class="num">03</div>
        <img src="">
    </div>
</div>
```
 - Depois (exemplo com código Base64 abreviado):
```HTML
<div class="carousel-item">
    <div class="carousel-box">
        <div class="title">Somos fodas juntos 🎀</div>
        <div class="num">03</div>
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QAiRXhpZgAASUkqAAgAAA....(código muito longo)...">
    </div>
</div>
```

Repita o processo para cada cartão que desejar personalizar com uma imagem!

## 💻 Como Visualizar
Nenhuma instalação ou servidor é necessário. Basta salvar o arquivo moça_bonita_git.html e abri-lo em qualquer navegador de internet (como Google Chrome, Firefox ou Microsoft Edge).
