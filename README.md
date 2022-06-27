# Template-Services-Linux
Template para monitoramento de serviços Linux via discovery 

# Dependencias 

- Zabbix 4.4
- Python3

# Como utilizar

- Insira os scripts no diretório /etc/zabbix/scripts
- Insira o arquivo userparameter no diretório /etc/zabbix/zabbix_agentd.d
- Restart o zabbix-agent

Ir em configurações, templates e clique em importar

# Opção de filtragem de serviços

Em *Discovery rules* selecione o *Discovery Services* clique em *Filters* insira o filtro desejado exemplo abaixo:

```
{#SERVICENAME} => matches => NOME-SERVIÇO
```
