import pandas as pd
from lxml import etree
import xml.etree.ElementTree as ET
import xmltodict

cols_manter = [
    'cUF_ide',
    'cNF_ide',
    'natOp_ide',
    'nNF_ide',
    'dhEmi_ide',
    'dhSaiEnt_ide',
    'CNPJ_emit',
    'xNome_emit',
    'xFant_emit',
    'CRT_emit',
    'enderEmit.xLgr_emit',
    'enderEmit.nro_emit',
    'enderEmit.xBairro_emit',
    'enderEmit.cMun_emit',
    'enderEmit.xMun_emit',
    'enderEmit.UF_emit',
    'enderEmit.CEP_emit',
    'enderEmit.cPais_emit',
    'enderEmit.xPais_emit',
    'enderEmit.fone_emit',
    'CNPJ_dest',
    'xNome_dest',
    'enderDest.xLgr_dest',
    'enderDest.nro_dest',
    'enderDest.xBairro_dest',
    'enderDest.cMun_dest',
    'enderDest.xMun_dest',
    'enderDest.UF_dest',
    'enderDest.CEP_dest',
    'enderDest.xPais_dest',
    'enderDest.fone_dest',
    '@nItem_det',
    'prod.xProd_det',
    'prod.uCom_det',
    'prod.qCom_det',
    'prod.vUnCom_det',
    'prod.vProd_det',
    'ICMSTot.vICMS_total',
    'ICMSTot.vProd_total',
    'ICMSTot.vFrete_total',
    'ICMSTot.vNF_total',
    'ICMSTot.vTotTrib_total',
    'modFrete_transp',
    'transporta.CNPJ_transp',
    'transporta.xNome_transp',
    'transporta.IE_transp',
    'transporta.xEnder_transp',
    'transporta.xMun_transp',
    'transporta.UF_transp',
    'vol.qVol_transp',
    'vol.esp_transp',
    'vol.pesoL_transp',
    'vol.pesoB_transp',
    'fat.vOrig_cobr',
    'fat.vDesc_cobr',
    'fat.vLiq_cobr',
    'detPag.vPag_pag',
    'nome_documento',
    'CNAE_emit',
    'email_dest',
    'enderEmit.xCpl_emit',
    'CNPJ_autXML',
    'CPF_autXML',
    'prod.comb.cProdANP_det',
    'prod.comb.descANP_det',
    'prod.comb.UFCons_det',
    'enderDest.xCpl_dest',
    'vol.marca_transp',
    'prod.vDesc_det',
    'NFref.refNFe_ide',
    'prod.veicProd.chassi_det',
    'CNPJ_retirada',
    'xLgr_retirada',
    'xCpl_retirada',
    'xBairro_retirada',
    'cMun_retirada',
    'xMun_retirada',
    'UF_retirada',
    'CNPJ_entrega',
    'xLgr_entrega',
    'nro_entrega',
    'xCpl_entrega',
    'xBairro_entrega',
    'cMun_entrega',
    'xMun_entrega',
    'UF_entrega',
    'CEP_entrega',
    'CNPJ_infIntermed'
]

dic_names = {
    'cUF_ide':'codigo_uf',
    'cNF_ide':'codigo_nf',
    'natOp_ide':'natureza_operacao',
    'nNF_ide':'numero_nf',
    'dhEmi_ide':'data_hora_emissao',
    'dhSaiEnt_ide':'dh_saida_emitente',
    'CNPJ_emit':'cnpj_emitente',
    'xNome_emit':'razao_social_emitente',
    'xFant_emit':'nome_fantasia_emitente',
    'CRT_emit':'crt_emitente',
    'enderEmit.xLgr_emit':'logradouro_emitente',
    'enderEmit.nro_emit':'numero_emitente',
    'enderEmit.xBairro_emit':'bairro_emitente',
    'enderEmit.cMun_emit':'cod_mun_emitente',
    'enderEmit.xMun_emit':'municipio_emitente',
    'enderEmit.UF_emit':'uf_emitente',
    'enderEmit.CEP_emit':'cep_emitente',
    'enderEmit.cPais_emit':'cod_pais_emitente',
    'enderEmit.xPais_emit':'pais_emitente',
    'enderEmit.fone_emit':'tel_emitente',
    'CNPJ_dest':'cnpj_destinatario',
    'xNome_dest':'nome_destinatario',
    'enderDest.xLgr_dest':'logradouro_destinatario',
    'enderDest.nro_dest':'numero_destinatario',
    'enderDest.xBairro_dest':'bairro_destinatario',
    'enderDest.cMun_dest':'cod_mun_destinatario',
    'enderDest.xMun_dest':'municipio_destinatario',
    'enderDest.UF_dest':'uf_destinatario',
    'enderDest.CEP_dest':'cep_destinatario',
    'enderDest.xPais_dest':'pais_destinatario',
    'enderDest.fone_dest':'tel_destinatario',
    '@nItem_det':'nr_do_item',
    'prod.xProd_det':'nome_produto',
    'prod.uCom_det':'unidade_produto',
    'prod.qCom_det':'quantidade_produto',
    'prod.vUnCom_det':'valor_unitario_produto',
    'prod.vProd_det':'valor_total_produto',
    'ICMSTot.vICMS_total':'vICMS_total',
    'ICMSTot.vProd_total':'vProd_total',
    'ICMSTot.vFrete_total':'vFrete_total',
    'ICMSTot.vNF_total':'vNF_total',
    'ICMSTot.vTotTrib_total':'vTotTrib_total',
    'modFrete_transp':'modalidade_frete',
    'transporta.CNPJ_transp':'CNPJ_trasportadora',
    'transporta.xNome_transp':'xNome_trasportadora',
    'transporta.IE_transp':'IE_trasportadora',
    'transporta.xEnder_transp':'xEnder_trasportadora',
    'transporta.xMun_transp':'xMun_trasportadora',
    'transporta.UF_transp':'UF_trasportadora',
    'vol.qVol_transp':'volume_trasnportado',
    'vol.esp_transp':'especificacao_tranporte',
    'vol.pesoL_transp':'peso_liquido_trasportado',
    'vol.pesoB_transp':'peso_bruto_transportado',
    'fat.vOrig_cobr':'valor_original_cobranca',
    'fat.vDesc_cobr':'desconto_cobranca',
    'fat.vLiq_cobr':'valor_liquido_cobranca',
    'detPag.vPag_pag':'vPag_pag',
    'nome_documento':'nome_documento',
    'CNAE_emit':'codigo_CNAE',
    'email_dest':'email_destinatario',
    'enderEmit.xCpl_emit':'complemento_emitente',
    'CNPJ_autXML':'CNPJ_aut_xml',
    'CPF_autXML':'CPF_aut_xml',
    'prod.comb.cProdANP_det':'codigo_produto_anp',
    'prod.comb.descANP_det':'descricao_produto_anp',
    'prod.comb.UFCons_det':'uf_destino_produto',
    'enderDest.xCpl_dest':'complemento_destinatario',
    'vol.marca_transp':'transportadora',
    'prod.vDesc_det':'valor_desconto_transp',
    'NFref.refNFe_ide':'chave_ref_nota',
    'prod.veicProd.chassi_det':'chassi_veiculo',
    'CNPJ_retirada':'cnpj_retirada',
    'xLgr_retirada':'logradouro_retirada',
    'xCpl_retirada':'complemento_retirada',
    'xBairro_retirada':'bairro_retirada',
    'cMun_retirada':'codigo_mun_retirada',
    'xMun_retirada':'municipio_retirada',
    'UF_retirada':'uf_retirada',
    'CNPJ_entrega':'cnpj_entrega',
    'xLgr_entrega':'logradouro_entrega',
    'nro_entrega':'numero_entrega',
    'xCpl_entrega':'complemento_entrega',
    'xBairro_entrega':'bairro_entrega',
    'cMun_entrega':'codigo_mun_entrega',
    'xMun_entrega':'nome_mun_entrega',
    'UF_entrega':'uf_entrega',
    'CEP_entrega':'cep_entrega',
    'CNPJ_infIntermed':'cnpj_intermediario'
}

class LerXML:
    @staticmethod
    def retorna_chave_acesso(xml_content: bytes) -> str:
        str_xml = etree.fromstring(xml_content)

        # Converte o XML do formato string para o uma Element Tree
        tree = ET.ElementTree(str_xml)

        # Extrai os valores para busca
        root = tree.getroot()

        # Defina o namespace do XML
        namespace = {'ns': 'http://www.portalfiscal.inf.br/nfe'}

        element = root.find('.//ns:infNFe', namespace)

        if element is not None:
            xCA = element.get('Id')
            if xCA is not None:
                xCA = xCA.replace('NFe','')
                return xCA
            else:
                xCA = 'Chave NFe não encontrada'
        else:
            element = root.find('.//ns:infEvento', namespace)
            if element is not None:
                xCA = element.get('Id')
            if xCA is not None:
                xCA = xCA.replace('ID','')
                return xCA
            else:
                xCA = 'Chave NFe não encontrada'
    @staticmethod
    def DataFrameFromXML(path: bytes, 
                         nome_documento: str = None, 
                         list_manter:list = cols_manter, 
                         dic_names: dict = dic_names ) -> pd.DataFrame:           
        # abre o arquivo xml
        with open(path, 'rb') as f:
                xml_content = f.read()

        # converte o arquivo xml em um dicionario
        xml_dict = xmltodict.parse(xml_content)
        
        # Acessa as etiqueta 'nfeProc', em seguida 'NFe' e por fim 'infNFe' do XML
        nfe = xml_dict['nfeProc']['NFe']['infNFe']

        # Cria dicionário
        inf_dict =[]

        # intera para cada um dos campos dento da marca infNFe do dicionário
        for i in nfe:
                # ignora as etiqueta que começam com NFe
                if not '@' in i:
                        # converte o dicionario em um pandas dataframe
                        norm = pd.json_normalize(nfe[i])
                        #acrescenta no nome da coluna a etiqueta no xml
                        norm.columns = [col +'_'+ i for col in norm.columns]
                        # filtra apenas as colunas informadas na lista
                        norm = norm.filter(list_manter)
                        # altera os nome das colunas para um novo mais fácil de ler
                        norm = norm.rename(columns=dic_names)
                        # adiciona a informação da marca no dicionário
                        inf_dict.append(norm.reset_index(drop=True))
        
        # une todas as informações do xml em um dataframe
        df = pd.concat(inf_dict, axis=1)
        
        if nome_documento is not None:
            # cria uma coluna com o nome do documento para servir de referência
            df['nome_documento'] = nome_documento
        
        # esta etapa esta em desenvolvimento >:(
        df['chave_acesso_xml'] = LerXML.retorna_chave_acesso(xml_content)
        return df