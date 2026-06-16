CREATE TABLE CTL_ESTOQUE.cliente (
    cd_cliente    NUMBER(7) NOT NULL,
    nr_cpf        CHAR(11 CHAR) NOT NULL,
    dt_nascimento DATE,
    tp_genero     CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.cliente_cd_idx ON
    CTL_ESTOQUE.cliente (
        cd_cliente
    ASC );

CREATE UNIQUE INDEX CTL_ESTOQUE.cliente_cpf_idx ON
    CTL_ESTOQUE.cliente (
        nr_cpf
    ASC );

ALTER TABLE CTL_ESTOQUE.cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( cd_cliente );

ALTER TABLE CTL_ESTOQUE.cliente ADD CONSTRAINT cliente_cpf_un UNIQUE ( nr_cpf );

CREATE TABLE CTL_ESTOQUE.endereco (
    cd_endereco   NUMBER(7) NOT NULL,
    nr_cep        CHAR(8 CHAR) NOT NULL,
    nm_logradouro VARCHAR2(50 CHAR) NOT NULL,
    nr_logradouro VARCHAR2(5 CHAR) NOT NULL,
    cd_municipio  SMALLINT NOT NULL
    cd_endereco    NUMBER(7) NOT NULL,
    nr_cep         CHAR(8 CHAR) NOT NULL,
    nm_logradouro  VARCHAR2(50 CHAR) NOT NULL,
    nr_logradouro  VARCHAR2(5 CHAR) NOT NULL,
    cd_municipio   SMALLINT NOT NULL,
    nm_bairro      VARCHAR2(25 CHAR) NOT NULL,
    ds_complemento VARCHAR2(100 CHAR)
);

CREATE UNIQUE INDEX CTL_ESTOQUE.endereco_cd_idx ON
    CTL_ESTOQUE.endereco (
CREATE UNIQUE INDEX endereco_cd_idx ON
    endereco (
cd_endereco
ASC );

@@ -37,63 +19,40 @@ ALTER TABLE CTL_ESTOQUE.endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( cd_end
CREATE TABLE CTL_ESTOQUE.estoque (
cd_estoque    SMALLINT NOT NULL,
nr_rua        SMALLINT NOT NULL,
    nr_prateleita SMALLINT NOT NULL,
    nr_prateleira SMALLINT NOT NULL,
nr_sequencia  CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.estoque_cd_idx ON
    CTL_ESTOQUE.estoque (
CREATE UNIQUE INDEX estoque_cd_idx ON
    estoque (
cd_estoque
ASC );

ALTER TABLE CTL_ESTOQUE.estoque ADD CONSTRAINT estoque_pk PRIMARY KEY ( cd_estoque );

CREATE TABLE CTL_ESTOQUE.fornecedor (
    cd_fornecedor  NUMBER(7) NOT NULL,
    nr_cnpj        CHAR(14 CHAR) NOT NULL,
    nm_razaosocial VARCHAR2(100 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.fornecedor_cd_idx ON
    CTL_ESTOQUE.fornecedor (
        cd_fornecedor
    ASC );

CREATE UNIQUE INDEX CTL_ESTOQUE.fornecedor_cnpj_idx ON
    CTL_ESTOQUE.fornecedor (
        nr_cnpj
    ASC );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cd_fornecedor );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_cnpj_un UNIQUE ( nr_cnpj );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_razsoc_un UNIQUE ( nm_razaosocial );

CREATE TABLE CTL_ESTOQUE.municipio (
cd_municipio SMALLINT NOT NULL,
nm_municipio VARCHAR2(50) NOT NULL,
nm_estado    VARCHAR2(50 CHAR) NOT NULL,
nm_pais      VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.municipio_cd_idx ON
    CTL_ESTOQUE.municipio (
CREATE UNIQUE INDEX municipio_cd_idx ON
    municipio (
cd_municipio
ASC );

ALTER TABLE CTL_ESTOQUE.municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( cd_municipio );

CREATE TABLE CTL_ESTOQUE.pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_pessoa  NUMBER(7) NOT NULL,
    tp_pedido  CHAR(1 CHAR) NOT NULL,
    dt_pedido  DATE DEFAULT sysdate NOT NULL,
    dt_entrega DATE
    cd_pedido  		   NUMBER(7) NOT NULL,
    cd_pessoa 		   NUMBER(7) NOT NULL,
    dt_pedido  		   DATE DEFAULT sysdate NOT NULL,
    dt_entregaprevista DATE
);

CREATE UNIQUE INDEX CTL_ESTOQUE.pedido_cd_idx ON
    CTL_ESTOQUE.pedido (
CREATE UNIQUE INDEX pedido_cd_idx ON
    CTL_ESTOQUE.pedido  (
cd_pedido
ASC );

@@ -107,22 +66,66 @@ CREATE TABLE CTL_ESTOQUE.pessoa (
nm_email    VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.pessoa_cd_idx ON
   CTL_ESTOQUE.pessoa (
CREATE UNIQUE INDEX pessoa_cd_idx ON
    pessoa (
cd_pessoa
ASC );

ALTER TABLE CTL_ESTOQUE.pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( cd_pessoa );

CREATE TABLE CTL_ESTOQUE.pessoa_fisica (
    cd_pessoa     NUMBER(7) NOT NULL,
    nr_cpf        CHAR(11 CHAR) NOT NULL,
    dt_nascimento DATE NOT NULL,
    tp_genero     CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX cliente_cd_idx ON
    CTL_ESTOQUE.pessoa_fisica (
        cd_pessoa
    ASC );

CREATE UNIQUE INDEX cliente_cpf_idx ON
    CTL_ESTOQUE.pessoa_fisica (
        nr_cpf
    ASC );

ALTER TABLE CTL_ESTOQUE.pessoa_fisica ADD CONSTRAINT cliente_pk PRIMARY KEY ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa_fisica ADD CONSTRAINT cliente_cpf_un UNIQUE ( nr_cpf );

CREATE TABLE CTL_ESTOQUE.pessoa_juridica (
    cd_pessoa      NUMBER(7) NOT NULL,
    nr_cnpj        CHAR(14 CHAR) NOT NULL,
    nm_razaosocial VARCHAR2(100 CHAR) NOT NULL
);

CREATE UNIQUE INDEX fornecedor_cd_idx ON
    CTL_ESTOQUE.pessoa_juridica (
        cd_pessoa
    ASC );

CREATE UNIQUE INDEX fornecedor_cnpj_idx ON
    CTL_ESTOQUE.pessoa_juridica (
        nr_cnpj
    ASC );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_cnpj_un UNIQUE ( nr_cnpj );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_razsoc_un UNIQUE ( nm_razaosocial );

CREATE TABLE CTL_ESTOQUE.produto (
cd_produto          SMALLINT NOT NULL,
nm_produto          VARCHAR2(50 CHAR) NOT NULL,
ds_produto          VARCHAR2(500 CHAR),
    tp_embalagemproduto CHAR(1 CHAR) NOT NULL
    tp_embalagemproduto CHAR(1 CHAR) NOT NULL,
    vl_produto          NUMBER(7, 2) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.produto_cd_idx ON
    CTL_ESTOQUE.produto (
CREATE UNIQUE INDEX produto_cd_idx ON
    produto (
cd_produto
ASC );

@@ -137,48 +140,26 @@ CREATE TABLE CTL_ESTOQUE.produto_estoque (
dt_produtoestoque DATE NOT NULL
);

ALTER TABLE CTL_ESTOQUE.produto_estoque ADD CONSTRAINT produto_estoque_pk PRIMARY KEY ( cd_estoque,
                                                                            cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_fonecedor (
    cd_produto    SMALLINT NOT NULL,
    cd_fornecedor NUMBER(7) NOT NULL,
    vl_produto    NUMBER(7, 2)
);

ALTER TABLE CTL_ESTOQUE.produto_fonecedor ADD CONSTRAINT produto_fonecedor_pk PRIMARY KEY ( cd_fornecedor,
                                                                                cd_produto );
ALTER TABLE CTL_ESTOQUE.produto_estoque ADD CONSTRAINT produto_estoque_pk PRIMARY KEY ( cd_estoque, cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_produto SMALLINT NOT NULL,
    qt_produto NUMBER(7, 2) NOT NULL
    cd_pedido       NUMBER(7) NOT NULL,
    cd_produto      SMALLINT NOT NULL,
    qt_produto      NUMBER(7, 2) NOT NULL
);

ALTER TABLE CTL_ESTOQUE.produto_pedido ADD CONSTRAINT produto_pedido_pk PRIMARY KEY ( cd_pedido );

CREATE TABLE CTL_ESTOQUE.transacao (
    cd_transacao NUMBER(7) NOT NULL,
    cd_estoque   SMALLINT NOT NULL,
    cd_produto   SMALLINT NOT NULL,
    cd_pedido    NUMBER(7) NOT NULL,
    tp_transacao CHAR(1 CHAR) NOT NULL,
    qt_produto   NUMBER(7, 2) NOT NULL,
    dt_transacao DATE DEFAULT sysdate NOT NULL
);
ALTER TABLE CTL_ESTOQUE.produto_pedido ADD CONSTRAINT produto_pedido_pk PRIMARY KEY ( cd_pedido, cd_produto );

ALTER TABLE CTL_ESTOQUE.transacao ADD CONSTRAINT transacao_pk PRIMARY KEY ( cd_transacao );

ALTER TABLE CTL_ESTOQUE.cliente
    ADD CONSTRAINT cliente_pessoa_fk FOREIGN KEY ( cd_cliente )
ALTER TABLE CTL_ESTOQUE.pessoa_fisica
    ADD CONSTRAINT cliente_pessoa_fk FOREIGN KEY ( cd_pessoa )
REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.endereco
ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( cd_municipio )
REFERENCES CTL_ESTOQUE.municipio ( cd_municipio );

ALTER TABLE CTL_ESTOQUE.fornecedor
    ADD CONSTRAINT fornecedor_pessoa_fk FOREIGN KEY ( cd_fornecedor )
ALTER TABLE CTL_ESTOQUE.pessoa_juridica
    ADD CONSTRAINT fornecedor_pessoa_fk FOREIGN KEY ( cd_pessoa )
REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pedido
@@ -189,14 +170,6 @@ ALTER TABLE CTL_ESTOQUE.pessoa
ADD CONSTRAINT pessoa_endereco_fk FOREIGN KEY ( cd_endereco )
REFERENCES CTL_ESTOQUE.endereco ( cd_endereco );

ALTER TABLE CTL_ESTOQUE.produto_fonecedor
    ADD CONSTRAINT prod_forn_forn_fk FOREIGN KEY ( cd_fornecedor )
        REFERENCES CTL_ESTOQUE.fornecedor ( cd_fornecedor );

ALTER TABLE CTL_ESTOQUE.produto_fonecedor
    ADD CONSTRAINT prod_forn_prod_fk FOREIGN KEY ( cd_produto )
        REFERENCES CTL_ESTOQUE.produto ( cd_produto );

ALTER TABLE CTL_ESTOQUE.produto_estoque
ADD CONSTRAINT produto_estoque_estoque_fk FOREIGN KEY ( cd_estoque )
REFERENCES CTL_ESTOQUE.estoque ( cd_estoque );
@@ -213,83 +186,92 @@ ALTER TABLE CTL_ESTOQUE.produto_pedido
ADD CONSTRAINT produto_pedido_produto_fk FOREIGN KEY ( cd_produto )
REFERENCES CTL_ESTOQUE.produto ( cd_produto );

ALTER TABLE CTL_ESTOQUE.transacao
    ADD CONSTRAINT transacao_pedido_fk FOREIGN KEY ( cd_pedido )
        REFERENCES CTL_ESTOQUE.pedido ( cd_pedido );

ALTER TABLE CTL_ESTOQUE.transacao
    ADD CONSTRAINT transacao_produto_estoque_fk FOREIGN KEY ( cd_estoque,
                                                              cd_produto )
        REFERENCES CTL_ESTOQUE.produto_estoque ( cd_estoque,
                                     cd_produto );

CREATE SEQUENCE ctl_estoque.sq_cd_municipio START WITH 1 NOCACHE ORDER;
DROP SEQUENCE CTL_ESTOQUE.sq_cd_endereco;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_endereco START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_municipio BEFORE
    INSERT ON ctl_estoque.municipio
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_endereco BEFORE
    INSERT ON CTL_ESTOQUE.endereco
FOR EACH ROW
    WHEN ( new.cd_municipio IS NULL )
    WHEN ( new.cd_endereco IS NULL )
BEGIN
    :new.cd_municipio := ctl_estoque.sq_cd_municipio.nextval;
    :new.cd_endereco := CTL_ESTOQUE.sq_cd_endereco.nextval;
END;
/

CREATE SEQUENCE ctl_estoque.sq_cd_endereco START WITH 1 NOCACHE ORDER;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_estoque START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_endereco BEFORE
    INSERT ON ctl_estoque.endereco
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_estoque BEFORE
    INSERT ON CTL_ESTOQUE.estoque
FOR EACH ROW
    WHEN ( new.cd_endereco IS NULL )
    WHEN ( new.cd_estoque IS NULL )
BEGIN
    :new.cd_endereco := ctl_estoque.sq_cd_endereco.nextval;
    :new.cd_estoque := CTL_ESTOQUE.sq_cd_estoque.nextval;
END;
/

 SEQUENCE ctl_estoque.sq_cd_pessoa START WITH 1 NOCACHE ORDER;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_municipio START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_pessoa BEFORE
    INSERT ON ctl_estoque.pessoa
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_municipio BEFORE
    INSERT ON CTL_ESTOQUE.municipio
FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
    WHEN ( new.cd_municipio IS NULL )
BEGIN
    :new.cd_pessoa := ctl_estoque.sq_cd_pessoa.nextval;
    :new.cd_municipio := CTL_ESTOQUE.sq_cd_municipio.nextval;
END;
/

CREATE SEQUENCE ctl_estoque.sq_cd_pedido START WITH 1 NOCACHE ORDER;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pedido START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_pedido BEFORE
    INSERT ON ctl_estoque.pedido
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pedido BEFORE
    INSERT ON CTL_ESTOQUE.pedido
FOR EACH ROW
WHEN ( new.cd_pedido IS NULL )
BEGIN
    :new.cd_pedido := ctl_estoque.sq_cd_pedido.nextval;
    :new.cd_pedido := CTL_ESTOQUE.sq_cd_pedido.nextval;
END;
/

CREATE SEQUENCE ctl_estoque.sq_cd_estoque START WITH 1 NOCACHE ORDER;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_estoque BEFORE
    INSERT ON ctl_estoque.estoque
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa BEFORE
    INSERT ON CTL_ESTOQUE.pessoa
FOR EACH ROW
    WHEN ( new.cd_estoque IS NULL )
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_estoque := ctl_estoque.sq_.nextval;
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa.nextval;
END;
/
--
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa_fisica START WITH 1 NOCACHE ORDER;

CREATE SEQUENCE ctl_estoque.sq_cd_produto START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_produto BEFORE
    INSERT ON ctl_estoque.produto
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa_fisica BEFORE
    INSERT ON CTL_ESTOQUE.pessoa_fisica
FOR EACH ROW
    WHEN ( new.cd_produto IS NULL )
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_produto := ctl_estoque.sq_cd_produto.nextval;
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa_fisica.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa_juridica START WITH 1 NOCACHE ORDER;

CREATE SEQUENCE ctl_estoque.sq_cd_transacao START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_transacao BEFORE
    INSERT ON ctl_estoque.transacao
CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa_juridica BEFORE
    INSERT ON CTL_ESTOQUE.pessoa_juridica
FOR EACH ROW
    WHEN ( new.cd_transacao IS NULL )
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa_juridica.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_produto START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_produto BEFORE
	INSERT ON CTL_ESTOQUE.produto
	FOR EACH ROW
	WHEN ( new.cd_produto IS NULL )
BEGIN
    :new.cd_transacao := ctl_estoque.sq_cd_transacao.nextval;
	:new.cd_produto := CTL_ESTOQUE.sq_cd_produto.nextval;
END;
/