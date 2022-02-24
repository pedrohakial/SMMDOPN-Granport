from flask_wtf import FlaskForm
from wtforms import (
    TextField, 
    PasswordField,
    IntegerField, 
    SelectMultipleField, 
    DateTimeField, 
    RadioField,
    SubmitField,
    StringField,
    SelectField,
    SelectMultipleField

)

from wtforms.validators import InputRequired, Email, DataRequired


class CadastroTermoDeOcorrênciaForm(FlaskForm):                       # Formulário para o Termo de Ocorrência
    formalização_da_reclamação = SelectMultipleField('Formalização da Reclamação'   ,id='formalizacao_da_reclamacao_create'             ,validators=[DataRequired()]                ,choices=['Telefone', 'E-mail', 'Site' ,'Outros'])
    primeira_vez = SelectMultipleField('Primeira Vez da Ocorrência?'                ,id='primeira_vez_create'                           ,validators=[DataRequired()]                ,choices=['Sim' ,'Não'])
    localidade = SelectMultipleField('Localidade'                                   ,id='localidade_create'                             ,validators=[DataRequired()]                ,choices=['SSZ' ,'SPO' ,'SUA' ,'MAO' ,'Outra'])
    data = DateTimeField('Data da Ocorrência'                                       ,id='data_da_ocorrencia_create'                     ,format='%d-%m-%Y')
    cnpj = TextField('CNPJ'                                                         ,id='cnpj_create'                                   ,validators=[DataRequired()])
    nome_empresa = TextField()
    nota_fiscal = IntegerField()
    CTe = IntegerField()
    trânsito_da_carga = RadioField('Trânsito da Carga'                     ,choices=[])
    cliente_identificou = RadioField(''         ,choices=[])
    granport_foi_acionada = RadioField(''           ,choices=[])
    manifestou_ocorrência = RadioField(''           ,choices=[])
    posterior_ao_recebimento = RadioField(''            ,choices=[])
    ainda_no_veículo = RadioField(''            ,choices=[])
    ato_descarga = RadioField(''            ,choices=[])
    descrição_relato = TextField()
    # por enquanto os RadioFields vão ficar no lugar dos Switches que vem com o Bootstrap 5 
    carga = RadioField('Carga', choices=['Falta','Avariada', 'Acréscimo', 'Inclusão', 'Cubagem', 'Outros' ])
    containers = RadioField('Containers', choices=['Amassado', 'Cortado', 'Portas', 'Piso', 'Sujo', 'Furado', 'Outros'])
    embalagem = RadioField('Embalagem', choices=['Rasgada', 'Amassada', 'Cortada', 'Arranhada', 'Molhada', 'Úmida', 'Outros' ])
    veículos = RadioField('Veículos', choices=['Incompatível com a Carga', 'Atrasado', 'Adiantado', 'Avariado', 'Sem Lona', 'Sem Peiação', 'Outros'])
    motorista = RadioField('Motorista', choices=['Sem EPI', 'Sem Uniforme', 'Indisciplinado', 'Não Atende Segurança', 'Desrespeitoso', 'Outros'])
    tipo_de_carga = RadioField('Tipo de Carga', choices = ['Eletrônica', 'Siderúrgica', 'Alimentos', 'Máquinas', 'Tintas', 'Cerâmica', 'Tubos', 'Móveis', 'Químico', 'Linha Branca', 'Metalúrgica', 'Farmacêutica', 'Combustíveis', 'Commodities', 'Automobilísticos', 'Materiais de Construção', 'Produtos de Limpeza'])
    tipo_de_embalagem = RadioField('Tipo de Embalagem', choices = ['Big bag', 'Sacos', 'Caixa', 'Lata', 'Baldes', 'Paletizada', 'Tambores', 'Bombonas', 'Bobinas de Aço', 'Bobinas de Madeiras', 'Bobinas de Papel', 'Amarrados'])
    considerações_finais = TextField()
    submit = SubmitField("Cadastrar")


class EscopoDeServicoForm(FlaskForm):
    empresa_cliente = SelectField()
    cidade_origem = TextField('Cidade de Origem'                             ,id='cidade_origem_create'          ,validators=[DataRequired()])
    estado_origem = SelectField(
        'Estado', 
        choices=[
        'São Paulo', 
        'Minas Gerais', 
        'Rio de Janeiro',
        'Acre',
        'Alagoas',
        'Amapá',
        'Amazonas',
        'Bahia',
        'Ceará',
        'Distrito Federal',
        'Goiás',
        'Maranhão',
        'Mato Grosso',
        'Mato Grosso do Sul',
        'Pará',
        'Paraiba',
        'Paraná',
        'Pernambuco',
        'Piauí',
        'Rio Grande do Sul',
        'Rondônia',
        'Roraima',
        'Santa Catarina',
        'Sergipe',
        'Tocantins'
        ],
        id='estado_create',
        validators=[DataRequired()]

        )
    estado_destino = SelectField(
        'Estado', 
        choices=[
        'São Paulo', 
        'Minas Gerais', 
        'Rio de Janeiro',
        'Acre',
        'Alagoas',
        'Amapá',
        'Amazonas',
        'Bahia',
        'Ceará',
        'Distrito Federal',
        'Goiás',
        'Maranhão',
        'Mato Grosso',
        'Mato Grosso do Sul',
        'Pará',
        'Paraiba',
        'Paraná',
        'Pernambuco',
        'Piauí',
        'Rio Grande do Sul',
        'Rondônia',
        'Roraima',
        'Santa Catarina',
        'Sergipe',
        'Tocantins'
        ],
        id='estado_create',
        validators=[DataRequired()]

        )
    cidade_destino = TextField('Cidade Destino'                             ,id='cidade_destino_create'         ,validators=[DataRequired()])
    tipo_de_operação = SelectField(
            'Operação',
            choices=[
                'Pier-Porta',
                'Porta-Porta',
                'Porta-Pier',
                'Pier-Pier'
                ],
            id='operação_create',
            validators=[DataRequired()]
            )
    tipo_embalagem = SelectMultipleField(
            'Tipo de Embalagem',
            choices = [
                ('Pallet','Pallet'),
                ('Sacaria','Sacaria'),
                ('Latas','Latas'),
                ('Caixas','Caixas'),
                ('Bombonas','Bombonas'),
                ('Tambor','Tambor'),
                ('Amarrados','Amarrados'),
                ('Baldes', 'Baldes'),
                ('Big Bag', 'Big Bag'),
                ('Bobina de Aço', 'Bobina de Aço'),
                ('Bobinas de Papel', 'Bobinas de Papel'),
                ('Bobinas de Madeira', 'Bobinas de Madeira'),
                ('Atados', 'Atados')
                ],
            id='tipo_embalagem_create',
            validators=[DataRequired()]
            )
    tipo_de_carga = SelectMultipleField(
            'Tipo de Carga',
            choices = [
                ('Alimentícios','Alimentícios'),
                ('Produtos de Limpeza','Produtos de Limpeza'),
                ('Móveis','Móveis'),
                ('Duas Rodas','Duas Rodas'),
                ('Automobilístico','Automobilístico'),
                ('Siderúrgico','Siderúrgico'),
                ('Metalúrgico','Metalúrgico'),
                ('Cerâmica','Cerâmica'),
                ('Químico','Químico'),
                ('Papel','Papel'),
                ('Linha Branca','Linha Branca'),
                ('Químico Perigoso','Químico Perigoso'),
                ('Eletrônicos','Eletrônicos'),
                ('Elétricos','Elétricos'),
                ('Isotank Vazio e Limpo','Isotank Vazio e Limpo')
                ],
            id='tipo_de_carga_create',
            validators=[DataRequired()]
            )
    
    quantidade_volumes = TextField()
    peso_total_carga = TextField('Pesto Total em KG')
    cubagem_total_carga = TextField()
    dimensões_volume = TextField()
    carga_excedente = SelectField(
            'Carga Excedente?',
            choices = [
                'Sim',
                'Não'
                ],
            id = 'carga_excedente_create'
            )

    dimensões_carga_excedente = TextField()
    valor_mercadoria = TextField()

    seguro_cliente = SelectField(
            'Seguro por conta do Cliente?',
            choices = [
                'Sim',
                'Não'
                ],
            )
    seguro_fornecedor = SelectField(
            'Seguro por conta do Fornecedor?',
            choices = [
                'Sim',
                'Não'
                ],
            )
    seguro_transportador = SelectField(
            'Seguro por conta do Transportador?',
            choices = [
                'Sim',
                'Não'
                ],
            )
    armazenagem = SelectField(
            'Armazenagem',
            choices = [
                'Sim',
                'Não'
                ],
            )
   
    maquinário_mov = SelectMultipleField(
            'Maquinário de Movimentação das cargas Origem e Destino:',
         choices = [
                ('EP Pequeno Porte','EP Pequeno Porte'),
                ('EP Médio Porte','EP Médio Porte'),
                ('EP Grande Porte','EP Grande Porte'),
                ('Meclift','Meclift'),
                ('Patola','Patola'),
                ('Clamps','Clamps'),
                ('Ariete','Ariete'),
                ('Abafador','Abafador')
                ]
            )
    pontos_atenção = SelectMultipleField(
            'Pontos de Atenção:',
            choices = [
                ('Exposição a Chuva','Exposição a Chuva'),
                ('Exposição ao Sol','Exposição ao Sol'),
                ('Umidade','Umidade'),
                ('Poeira','Poeira'),
                ('Óleo/Graxa','Óleo/Graxa')
                ]
            )

    remonte_mercadoria = SelectField(
            'É Permitido o Remonte das Mercadorias?',
            choices = [
                'Sim',
                'Não'
                ],
            )
    max_remonte = SelectField(
            'Quantidade Máxima Remonte',
            choices = [
                'Primeira Altura',
                'Segunda Altura',
                'Terceira Altura'
                ],
            )
    transporte_origem = SelectField(
            'Trasnporte na Origem:',
            choices = [
                'Sim',
                'Não'
                ],
            )
    tipo_transporte = SelectField(
            'Tipo de Transporte',
            choices = [
                'Coleta -> Fracionada',
                'Coleta -> Lote Único',
                'Entrega -> Fracionada',
                'Entrega -> Lote Único'
                ]
            )
    tipo_veículo = SelectField(
            'Tipo de Veículo:',
            choices = [
                'Container',
                'Carreta Aberta',
                'Sider',
                'Baú',
                'Toco',
                'Truck'
                ]
            )
    material_coleta = SelectMultipleField(
            'Envio Material para Coleta',
            choices = [
               ('Madeirite', 'Madeirite'),
                ('Cabo Aço','Cabo Aço'),
                ('Catracas','Catracas'),
                ('Lonas','Lonas'),
                ('Cordas','Cordas'),
                ('Pallets','Pallets'),
                ('Strech','Strech'),
                ('EPI','EPI'),
                ('Cunhas','Cunhas'),
                ('Pontalete','Pontalete'),
                ('Kit Emergência','Kit Emergência'),
                ('Corrente','Corrente')
                ]
            )
    peiação = SelectField(
            'Peiação',
            choices = [
                'Fornecedor',
                'Granport',
                'Cliente'
                ]
            )
    dessecantes = SelectField(
            'Dessecantes',
            choices = [
                'Sim',
                'Não'
                ]
            )
    ifyes_dessecantes = TextField(
            'Quantos Dessecantes?',
            )
    tmp_livre_carregamento = TextField(' Período a Disposição para Carregamento:')
    
    op_cavalo_atrelado = SelectField(
            'Operação com Cavalo Mecânico Atrelado:',
            choices = [
                'Sim',
                'Não'
                ]
            )

    tmp_cavalo_atrelado = TextField(
            'Período a Disposição para Operação com o Cavalo Mecânico Atrelado:',
            )

    ajudantes = SelectField(
            'Enviar Ajudantes:',
            choices = [
                'Sim',
                'Não'
                ]
            )

    ifyes_ajudantes = TextField(
            'Quantos?',
            )

    consolidação_origem = SelectField(
            'Consolidação na Origem',
            choices = [
                'Granport',
                'Cliente',
                'Fornecedor'
                ]
            )
    tipo_estufagem = SelectField(
            'Tipo de Estufagem',
            choices = [
                'Mecânica',
                'Manual'
                ]
            )
    qnt_ajudantes = TextField(
            'Quantidade de Ajudantes',
            )
    dessecant_cont = SelectField(
            'Incluir Dessecantes no Container?',
            choices = [
                'Sim',
                'Não'
                ]
            )
    ifyes_dessecant_cont = TextField(
            'Se Sim, Quantos?',
            )
    material_estufagem = SelectMultipleField(
            'Material para Estufagem',
            choices = [
                ('Madeirite','Madeirite'),
                ('Cabo Aço','Cabo Aço'),
                ('Stretch','Stretch'),
                ('Cunhas','Cunhas'),
                ('Pontalete','Pontalete'),
                ('Catracas','Catracas'),
                ('Lonas','Lonas'),
                ('Corrente','Corrente'),
                ('Cordas','Cordas'),
                ('Pallets','Pallets')
                ]
            )
    tipo_de_container = SelectMultipleField(
            'Tipo de Container',
            choices = [
                (' HC',' HC'),
                (' Seacell',' Seacell'),
                (' Dry',' Dry'),
                (' Open Top',' Open Top'),
                (' Flat Rack',' Flat Rack'),
                (' Reefer',' Reefer'),
                (' Isotank Vazio e Limpo',' Isotank Vazio e Limpo'),
                (' Testado ',' Testado '),
                (' Padrão Alimento ',' Padrão Alimento '),
                (' Carga Geral ',' Carga Geral '),
                (' Idade Máxima cont 10 Anos',' Idade Máxima cont 10 Anos')
                ]
            )
    tamanho_container = SelectField(
            'Tamanho do Container:',
            choices = [
                '20 pés',
                '40 pés'
                ]
            )
    operação_contratada_destino = SelectField(
            'Operação Contratada Destino',
            choices = [
                'Entrega Direta em Container - Porto x Cliente',
                'Entrega Postergada - Porto x Granport x Cliente',
                'Desovar Carga x Entrega Cliente'
                ]
            )
    transporte_destino = SelectField(
            'Transporte no Destino',
            choices = [
                'Sim',
                'Não'
                ]
            )
    tipo_coleta_destino = SelectField(
            'Tipo de Transporte Destino',
            choices = [
                'Coleta -> Fracionada',
                'Coleta -> Lote Único',
                'Entrega -> Fracionada',
                'Entrega -> Lote Único'
                ]
            )
    tipo_veículo_dest = SelectField(
            'Tipo de Veículo Destino',
            choices = [
                'Container',
                'Carreta Aberta',
                'Toco',
                'Truck',
                'Baú',
                'Sider'
                ]
            )
    período_disposição_dest = TextField(
            'Período a Disposição para Descarregamento',
            )
    operação_cavalo_dest = SelectField(
            'Operalão com Cavalo Mecânico Atrelado?',
            choices = [
                'Sim',
                'Não'
                ]
            )
    periodo_cavalo_dest = TextField(
            'Período a Disposição para Descarregamento:',
            )
    op_munck = SelectField(
            'Operação com Veículo Munck?',
            choices = [
                'Sim',
                'Não'
                ]
            )
    periodo_op_munck = TextField(
            'Período a Disposição para Operação com Veículo Munck',
            )
    ajudantes_dest = SelectField(
            'Enviar Ajudantes:',
            choices = [
                'Sim',
                'Não'
                ]
            )
    ifyes_ajudantes_dest = TextField('Quantidade de Ajudantes:')

    conferentes_dest = SelectField(
            'Enviar Conferente?',
            choices = [
                'Sim',
                'Não'
                ]
            )

    ifyes_conferentes_dest = TextField('Quantidade de Conferentes:')
    escolta = SelectField(
            'Escolta:',
            choices = [
                'Sim',
                'Não'
                ]
            )

    desconsolidação_dest = SelectField(
            'Desconsolidação no Destino:',
            choices = [
                'Sim',
                'Não'
                ]
            )

    resp_retirada_mercadoria_dest = SelectField(
            'Responsável pela Retirada da Mercadoria',
            choices = [
                'Granprot',
                'Cliente',
                'Destinatário'
                ]
            )
    temp_livre_armazenamento_dest = TextField(
            'Tempo Livre para Armazenamento na Granport Destino',
            )
    
    tipo_desova_dest = SelectField(
            'Tipo de Desova:',
            choices = [
                'Mecânica',
                'Manual'
                ]
            )
    ajudantes_dest_desova = TextField(
            'Quantidade de Ajudantes na Desova'
            )

    submit = SubmitField("Cadastrar")


    # Cadastro dos nossos contatos e responsáveis nos clientes
class CadastroContatoClienteForm(FlaskForm):                    
    nome_contato_cliente = TextField('Nome Do Contato No Cliente'          ,id='nome_contato_cliente_create'    ,validators=[DataRequired()])
    cargo = TextField('Cargo/Função'                                        ,id='cargo_create'                   ,validators=[DataRequired()])
    telefone = TextField('Telefone'                                        ,id='telefone_create'                ,validators=[DataRequired()])
    e_mail = TextField('E-mail'                                            ,id='e_mail_create'                  ,validators=[DataRequired(), Email()])
    submit = SubmitField("Cadastrar")

# Perfil Operacional / Escopo de Serviço
class CadastroOperacionalForm(FlaskForm):                                        
    porto_origem = SelectMultipleField('Porto Origem'                       ,id='porto_origem_create'                          ,validators=[DataRequired()]        ,choices=['SSZ', 'SUA', 'FOR', 'MAO'])                          # ( SSZ SUA FOR MAO)
    porto_destino = SelectMultipleField('Porto Destino'                     ,id='porto_destino_create'                         ,validators=[DataRequired()]        ,choices=['SSZ', 'SUA', 'FOR', 'MAO'])                         # porto de destino ( SSZ SUA FOR MAO)
    local_de_entrega = SelectMultipleField('Local de Entrega'               ,id='local_de_entrega_create'                      ,validators=[DataRequired()]        ,choices=['GPT', 'Cliente'])                      # Cliente ou GPT?
    endereço_de_entrega = TextField('Endereço de Entrega'                   ,id='endereco_de_entrega_create'                   ,validators=[DataRequired()])                             # ou é GPT ou é o endereço do cliente
    cidade_de_origem = TextField('Cidade de Origem'                         ,id='cidade_de_origem_create'                      ,validators=[DataRequired()])                                # qual a cidade que o cliente vai entregar a carga? ou é GPT ou é o endereço do cliente
    embalagens = TextField('Embalagem'                                      ,id='embalagem_create'                             ,validators=[DataRequired()])                            # tipos de embalagens
    # RESPONSA DA OPERAÇÃO tipo_de_caminhão = SelectMultipleField('Tipo de Caminhão'               ,validators=[DataRequired()])                      # tipos de caminhão LS, L por ai...
    # não precisa para o comercial quem define é a operação tipo_de_semi_reboque = SelectMultipleField()                  # tipo de semi reboque que a carreta precisa puxar
    apoio_na_coleta = TextField('Apoio na Coleta'                           ,id='apoio_na_coleta_create'                       ,validators=[DataRequired()])                       # precisa de ajudante? guindaste?
    peso_da_carga = IntegerField('Peso da Carga'                            ,id='peso_da_carga_create'                         ,validators=[DataRequired()])
    tipo_de_container = SelectMultipleField('Tipo de Container'             ,id='tipo_de_container_create'                     ,validators=[DataRequired()])
    submit = SubmitField("Cadastrar")

class PropostaComercialForm(FlaskForm):                             
    nome_empresa = SelectField('Empresa:', validators=[DataRequired()], choices=[], render_kw={"placeholder": "Owner company *"})
    valor_ton = IntegerField('Valor da Tarifa por Tonelada'          ,id='valor_tarifa_ton_create' , render_kw={"placeholder": "R$0.000,00"}      ,validators=[DataRequired()])
    valor_m3 = IntegerField('Valor da Tarifa por M³'                ,id='valor_m3_create' , render_kw={"placeholder": "R$0.000,00"}             ,validators=[DataRequired()]) 
    frete_rodo = IntegerField('Valor do Frete'                          ,id='valor_do_frete_create' , render_kw={"placeholder": "R$0.000,00"}                       ,validators=[DataRequired()])
    validade =  DateTimeField('Data de Validade'                       ,id='validade_create'                           ,validators=[DataRequired()])
    submit = SubmitField("Cadastrar")

class CadastroFornecedorForm(FlaskForm):                              # Cadastro dos fornecedores de serviços
    estado = TextField('Estado'                                             ,id='estado_create'                                 ,validators=[DataRequired()])
    tipo = TextField('Tipo de Cliente'                                      ,id='tipo_de_cliente_create'                        ,validators=[DataRequired()])   
    cnpj = IntegerField('CNPJ'                                              ,id='cnpj_create'                                   ,validators=[DataRequired()])
    razão_social = TextField('Razão Social'                                 ,id='razao_social_create'                           ,validators=[DataRequired()])
    nome_fantasia = TextField('Nome Fantasia'                               ,id='nome_fantasia_create'                          ,validators=[DataRequired()])
    cep = IntegerField('CEP'                                                ,id='cep_create'                                    ,validators=[DataRequired()])
    endereço = TextField('Endereço'                                         ,id='endereco_create'                               ,validators=[DataRequired()])
    complemento = TextField('Complemento'                                   ,id='complemento_create'                            ,validators=[DataRequired()])
    bairro = TextField('bairro'                                             ,id='bairro_create'                                 ,validators=[DataRequired()])
    município = TextField('Município'                                       ,id='municipio_create'                              ,validators=[DataRequired()])
    telefone = IntegerField('Telefone'                                      ,id='telefone_create'                               ,validators=[DataRequired()])
    inscrição_estadual = IntegerField('Inscrição Estadual'                  ,id='inscricao_estadual_create'                     ,validators=[DataRequired()])
    país = TextField('País'                                                 ,id='pais_create'                                   ,validators=[DataRequired()])
    e_mail = TextField('E-mail'                                             ,id='e_mail_create'                                 ,validators=[DataRequired(), Email()])
    submit = SubmitField("Cadastrar")
    


class CRMForm(FlaskForm):
    nome = StringField("Nome do Contato", validators=[DataRequired()])
    cargo = StringField("Cargo")
    telefone = StringField("Telefone")
    e_mail = TextField('E-mail'                                             ,id='e_mail_create'                                 ,validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")

# Cadastro das empresas que são clientes
class CadastroClientesForm(FlaskForm):                           
    cnpj = IntegerField('CNPJ'                                             ,id='cnpj_create'                    , validators=[DataRequired()])                                        # CPNJ da empresa 
    inscrição_estadual = IntegerField('Inscrição Estadual'                  ,id='inscricao_estadual_create'      , validators=[DataRequired()])
    cep = IntegerField('CEP'                                               ,id='cep_create'                     , validators=[DataRequired()])
    # Rua, bairro número
    segmento_mercado = TextField('Segmento de Mercado'                      ,id='segmento_mercado_create'        ,validators=[DataRequired()])
    endereço = TextField('Endereço'                                        ,id='endereco_create'                ,validators=[DataRequired()])                                      
    bairro = TextField('Bairro'                                            ,id='bairro_create'                  ,validators=[DataRequired()])
    complemento = TextField('Complemento'                                  ,id='complemento_create'             ,validators=[DataRequired()])
    nome_empresa = TextField('Nome Fantasia'                               ,id='nome_fantasia_create'           ,validators=[DataRequired()])
    razão_social = TextField('Razão Social'                                ,id='razao_social_create'            ,validators=[DataRequired()])
    cidade = TextField('Cidade'                                           ,id='cidade_create'                  ,validators=[DataRequired()])
    estado = SelectField(
        'Estado', 
        choices=[
        'São Paulo', 
        'Minas Gerais', 
        'Rio de Janeiro',
        'Acre',
        'Alagoas',
        'Amapá',
        'Amazonas',
        'Bahia',
        'Ceará',
        'Distrito Federal',
        'Goiás',
        'Maranhão',
        'Mato Grosso',
        'Mato Grosso do Sul',
        'Pará',
        'Paraiba',
        'Paraná',
        'Pernambuco',
        'Piauí',
        'Rio Grande do Sul',
        'Rondônia',
        'Roraima',
        'Santa Catarina',
        'Sergipe',
        'Tocantins'
        ],
        id='estado_create',
        validators=[DataRequired()]

        )
    país = TextField('País'                                                ,id='pais_create'                    ,validators=[DataRequired()])
    tipo_de_empresa = TextField('Tipo de Empresa'                          ,id='tipo_empresa_create'            ,validators=[DataRequired()])
    submit = SubmitField("Cadastrar")
# O escopo de serviço na parte do formulário, só vou adicionar
# alguns campos que vão ser renderizados em HTML mas outros
# como modelo de operação e itens do escopo vou deixar fora
# em uma base de dados dedicada assim os Controladores podem modificar
