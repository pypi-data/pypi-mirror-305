# Pacote Ler XML SETRABH python - lerxmlspy

## Sobre o Pacote
O pacote consta com duas funções principais sendo:

1. retorna_chave_acesso:
   1. Esta função recebe apenas um argunto, o "xml_content" no qual deve ser informado a variável que contém o xml logo após ser aberto
   
   #### Exemplo

   ```python
   with open(arquivo_xml, 'rb') as f:
        xml_content = f.read()
   lerxmlspy.retorna_chave_acesso()

2. DataFrameFromXML:
   1. Esta função contém 4 argumentos, sendo apenas um obrigatorio obrigatórios
      1. path (obrigatório) bytes: Caminho do arquivo XML
      2. nome_documento (opcional) string: Inseri coluna com o nome do documento xml
      3. list_manter (opcional) list: Se não for informada utiliza a lista padronizada
      4. dic_names (opcional) dict: Se não for informada utiliza o dicionário padrão

   ### Exemplo
   ```python
   lerxmlspy.DataFrameFromXML(caminho_arquivo)