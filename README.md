# 🔐 Sistema de Login em Python
### Autor: Matheus Ruivo  
📅 Data: 17/10/2025  

---

## 🧠 Sobre o projeto
Este projeto foi criado com o objetivo de **praticar lógica de programação** em Python, especialmente:
- Estruturas condicionais (`if`, `elif`, `else`);
- Operadores lógicos (`and`, `or`);
- Estruturas de decisão baseadas em entrada do usuário;
- Conversão de tipos (`int`, `str`);
- Organização e fluxo de código.

O sistema permite que o usuário **cadastre um nome de usuário, senha e idade**, e depois **faça login** com as credenciais criadas.

---

## 🚀 Como funciona
1. O programa pergunta se o usuário quer **fazer login** ou **cadastro**;
2. Se escolher **cadastro**, ele pede:
   - Nome de usuário  
   - Senha  
   - Idade  
3. Se a idade for maior ou igual a 18 anos, o usuário pode continuar e **entrar no sistema**;
4. Se escolher **login**, basta digitar o nome e a senha para entrar (simulado no mesmo fluxo);
5. O sistema valida os dados e mostra mensagens de sucesso ou erro.

---

## 💻 Tecnologias usadas
- 🐍 **Python 3**
- `input()` para entrada de dados
- Estruturas condicionais
- Operador lógico `and`
- Comparações e validações

---

## 🧩 Exemplo de uso
```python
Você quer fazer login ou cadastro? cadastro
Digite um nome de usuário: matheus
Digite uma senha: 1234
Coloque sua idade: 20
Idade apropriada!
Quer entrar ou sair? entrar
Faça login!
Coloque seu nome de usuário: matheus
Coloque sua senha: 1234
Você entrou, parabéns!
