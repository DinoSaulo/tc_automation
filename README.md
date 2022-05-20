# Desafio QA Nutcache

### Modulo 1

- Website: http://www.republicavirtual.com.br/cep/exemplos.php

- In this challenge, try to enter a valid brazilian zip code and wait a few seconds for the address to be filled.
After that, ensure that the address fields (UF, etc) are actually filled in.

- Zip code format: 8 number digits, without “-”. I.e: “71608900”

## --------------//--------------//--------------

<!--- Utilizando o exemplos do repositório https://github.com/iuricode/readme-template para esse README.md --->

###  📝 Ferramentas utilizadas
| Linguagem         | Framework           | Ferramenta de Gerenciamento | Navegador                             |
|-------------------|---------------------|-----------------------------|---------------------------------------|
| Python 3.10.4     | Selenium Web Driver | PIP 22.0.4                  | Google Chrome (versão 101.0.4951.67)  |

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Possuir o `Python` instalado na versão 3.10.4 ou superior;
    * Possuir o `PIP` intalado no Python
* Possuir o `Google Chrome` instalado na versão instalado;
* Possuir o `Git` instalado.

## 🚀 Clonar o projeto

Para clonar o projeto, execute o seguinte comando no terminal:


``` bash
git clone https://github.com/DinoSaulo/tc_automation_module1.git
```

## ☕ Executando o projeto

Para executar o projeto basta fazer os seguintes passos:

```bash
cd tc_automation_module2
```

### Executar pela primeira vez

#### Instalar o env

```bash
pip install virtualenv
virtualenv env
```

#### Executando o env

- Windows
```bash
env\Scripts\activate
```

- Linux/MacOS
```bash
source ./env/bin/activate
```

#### Executar os testes

```bash
behave
```

### Executar demais vezes

```bash
behave
```

## ❔ Dúvidas

Pode entrar em contato comigo pelo e-mail: saulbpt@gmail.com