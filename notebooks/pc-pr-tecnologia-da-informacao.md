# PC-PR TECNOLOGIA DA INFORMAÇÃO

- **Notebook ID:** `546f0cb3-6aab-4b5b-97ac-7e8c7adec19c`
- **Fontes:** 49
- **Consultar ao vivo:** `notebooklm ask "pergunta" -n 546f0cb3-6aab-4b5b-97ac-7e8c7adec19c`


## Resumo do NotebookLM

Os documentos fornecidos consistem em materiais educativos da **curso preparatório** voltados ao ensino de **Redes de Computadores** e **Informática**. O conteúdo detalha conceitos fundamentais como os tipos de conexões, direções de transmissão e a classificação de redes conforme sua **abrangência geográfica** ou arquitetura. Há uma explicação minuciosa sobre as **topologias de rede**, como estrela e barramento, além do funcionamento de meios físicos como **cabos de par trançado** e **fibra óptica**. Os textos também exploram o papel de equipamentos essenciais, incluindo **roteadores**, **switches** e **modems**, na infraestrutura da internet. Por fim, o material aborda padrões de comunicação **IEEE 802** e tecnologias de acesso à web, servindo como um guia técnico para estudantes e candidatos a concursos públicos.


## Índice hierárquico

Este notebook consolida a base conceitual e normativa de Tecnologia da Informação voltada para a preparação operacional em reta final de concurso. O escopo abrange o funcionamento lógico e físico de redes, computação em nuvem, ferramentas de produtividade, segurança cibernética ativa, bancos de dados, desenvolvimento web e a legislação digital correlata.

### Redes de Computadores e Internet
- Hardware de rede e conectividade
  Modems, roteadores e switches
  Cabeamento de par trançado, coaxial e fibra óptica
- Padrões de comunicação sem fio
  Diferença entre Wireless (termo genérico) e Wi-Fi (IEEE 802.11)
  Evolução dos padrões IEEE 802.11 e Bluetooth (IEEE 802.15)
- Arquitetura TCP/IP
  Modelo de referência em camadas (Aplicação, Transporte, Rede, Enlace)
  Protocolo IP (IPv4 de 32 bits e IPv6 de 128 bits)
  Regras de abreviação e compressão do IPv6
  Protocolo TCP (confiável, orientado à conexão) e UDP (não confiável, rápido)
  Protocolo ARP para mapeamento de IP para MAC (48 bits)
  Protocolo DNS para resolução de nomes e domínios
- Protocolos de aplicação e serviços
  SMTP para envio de mensagens
  POP3 e IMAP para recebimento e sincronização de correio eletrônico
  SSH (criptografado) vs. Telnet (texto claro) no acesso remoto

### Intranets, Extranets e VPNs
- Redes privadas e corporativas
  Conceito de Intranet e sua restrição de acesso lógico
  Extranets como canais de comunicação com parceiros e clientes externos
- Segurança em tráfego e acesso remoto
  VPN para tunelamento criptografado sobre redes públicas
  Protocolos IPSec, SSL/TLS e L2TP aplicados à VPN
  Acesso por Área de Trabalho Remota (RDP)

### Computação em nuvem
- Características essenciais segundo o NIST
  Resource Pooling (agrupamento de recursos multi-inquilino)
  Rapid Elasticity (elasticidade rápida e automática)
  Broad Network Access (amplo acesso de rede e ubiquidade)
  On-demand Self-service (autosserviço sob demanda)
  Measured Service (serviço medido e tarifado por consumo)
- Modelos de serviço de nuvem
  IaaS (Infraestrutura como Serviço): controle do SO, rede e armazenamento
  PaaS (Plataforma como Serviço): ambiente de desenvolvimento e compiladores
  SaaS (Software como Serviço): acesso a aplicações prontas via navegador
- Modelos de implantação de nuvem
  Nuvem Pública (aberta, multilocatária)
  Nuvem Privada (exclusiva para um único órgão ou organização)
  Nuvem Híbrida (integração entre modelos distintos)
  Nuvem Comunitária (compartilhamento por organizações com interesses comuns)

### Navegadores, Cookies e Cache
- Localizadores de recursos e navegação web
  Estrutura de URLs (esquema, domínio, porta, recurso)
  Uso de URLs de configuração interna (chrome://settings e equivalentes)
- Desempenho e persistência local
  Web Cache para armazenamento de elementos estáticos e aceleração de carregamento
  Cookies de sessão (temporários) vs. Cookies persistentes (mantidos em disco)
  Navegadores Google Chrome, Microsoft Edge e Mozilla Firefox
- Privacidade e segurança na navegação
  Modo de navegação anônima/InPrivate e suas limitações de rastreamento de rede
  Níveis de proteção do Google Chrome (reforçada, padrão e sem proteção)
  Arquitetura Sandbox para isolamento de processos de guias

### Correio Eletrônico
- Gerenciamento de caixas e pastas de e-mail
  Caixa de Entrada, Rascunhos, Caixa de Saída, Itens Enviados e Lixeira
- Clientes de e-mail locais (Mozilla Thunderbird)
  Procedimento de compactação de pastas para recuperação de espaço físico
  Diferenças práticas de tráfego entre protocolos POP3 e IMAP

### Redes sociais e plataformas digitais
- Compartilhamento de dados heterogêneos
  Mecanismos de privacidade, exposição de metadados e controle de perfis

### Segurança da Informação e Segurança Cibernética
- Pilares fundamentais da segurança
  Confidencialidade, Integridade e Disponibilidade (Tríade CID)
  Autenticidade e Não-repúdio (Irretratabilidade)
- Criptografia Simétrica
  Chave única compartilhada para cifrar e decifrar
  Algoritmos AES, DES, 3DES, Blowfish, RC4, IDEA
- Criptografia Assimétrica
  Par de chaves correspondentes (pública e privada)
  Algoritmo RSA
- Integridade e funções resumo
  Funções hash de via única (MD5 de 128 bits e SHA-256 de 256 bits)
- Assinatura Digital e Validação jurídica
  Cifragem do hash do documento com a chave privada do remetente
  Garantias de integridade, autenticidade e não-repúdio
- Certificados Digitais e padrão ICP-Brasil
  Autoridades Certificadoras (ACs) e Autoridades de Registro (AR)
  Lista de Certificados Revogados (LCR)
  Tipos de certificados e prazos de validade (A1/S1, A2/S2, A3/S3, A4/S4)
- Autenticação de dois fatores (2FA)
  Algoritmos baseados em tempo (TOTP) e baseados em contadores (HOTP)

### Ameaças Cibernéticas e Malwares
- Classificação de códigos maliciosos
  Vírus de computador (necessita de arquivo hospedeiro e ação direta do usuário)
  Worms (autônomos, autorreplicáveis na rede, esgotam largura de banda)
  Bots e criação de Botnets para ataques distribuídos de negação de serviço (DDoS)
  Cavalos de troia (Trojans) para abertura silenciosa de portas (backdoors)
  Spywares (Keyloggers para teclas físicas e Screenloggers para cliques de mouse)
  Rootkits nos níveis de Usuário e de Kernel
- Golpes, ataques e fraudes
  Ransomware (criptografia hostil e extorsão por criptomoedas)
  Phishing (falsificação de sites e e-mails para roubo de credenciais)
  Ataques de negação de serviço (DoS/DDoS) para afetar disponibilidade
  Baiting (iscas físicas, como pendrives contendo arquivos maliciosos)
  Ataque do Homem no Meio (Man-in-the-Middle)

### Segurança de Redes e Firewalls
- Controle e filtragem de perímetro
  Funcionamento básico de bloqueio e liberação de fluxos lógicos
- Mecanismos de filtragem de tráfego
  Filtro de pacotes (Stateless) baseado em cabeçalhos de portas e IPs isolados
  Firewall Stateful baseado no monitoramento em tabelas de estado de conexões ativas
  Firewall Proxy (Gateway de Aplicação) atuando na camada de aplicação
  Firewalls de nova geração (NGFW) com DPI e WAF (Web Application Firewall)

### Backup e Recuperação de Dados
- Controle lógico por atributos
  Funcionamento do Bit de Arquivamento (Archive Bit / Flag A)
- Rotinas e modalidades de backup
  Backup Completo (Normal/Total): copia todos os arquivos e zera o bit para 0
  Backup Incremental: copia novos ou alterados e zera o bit para 0
  Backup Diferencial: copia novos ou alterados desde o completo e mantém o bit em 1
  Backup de Cópia: cópia emergencial total sem afetar o bit de arquivamento
  Backup Diário: cópia baseada na data do sistema sem alterar o bit de arquivamento
- Estratégias físicas e operacionais
  Cold Backup (frio/offline) vs. Hot Backup (quente/online)
  Armazenamento seguro redundante off-site

### Prevenção e Resposta a Incidentes de Segurança
- Estruturas de reação a ataques
  Times CSIRT, ETIR e CERT para gerenciamento de crises cibernéticas
- Padrões normativos
  Diretrizes de tratamento de incidentes com base na norma ISO/IEC 27035

### Planilhas Eletrônicas: MS Excel e LibreOffice Calc
- Gerenciamento de referências em fórmulas
  Referências Relativas, Mistas e Absolutas (uso de \$)
  Comportamento geométrico das fórmulas na cópia e arrasto horizontal e vertical
- Funções, operadores e processamento de dados
  Uso de operadores matemáticos e lógicos padrão
  Ferramenta de Consolidação de Dados para agregar intervalos entre abas ou arquivos
- Interface de usuário do Calc
  Disposição física da Barra de Menus (Arquivo, Editar, Exibir, Inserir, Dados)

### Processadores de Texto: MS Word e LibreOffice Writer
- Gestão de documentos e revisão no Word
  Menu Backstage (Guia Arquivo) para tarefas do arquivo (imprimir, exportar, salvar)
  Controle de Alterações e exibição de revisões de forma visível (tachados e sublinhados)
- Padrões e formatos abertos
  Padrão ODF (Open Document Format) gerenciado pela OASIS
  Extensões nativas (.odt) e interoperabilidade com formatos proprietários (.docx, .doc, .pdf)

### Editores de Apresentação: MS PowerPoint e LibreOffice Impress
- Estrutura e suporte de slides
  Navegação de guias estruturais no PowerPoint e correspondências no Impress (.odp)

### Sistemas Operacionais: Windows 11
- Gestão hierárquica de arquivos e caminhos
  Estrutura em árvore de diretórios a partir do disco raiz C:\
  Delimitação física de caminhos de arquivos por meio de barras invertidas (\)
  Regras de nomenclatura e impedimento de homônimos de arquivo/pasta no mesmo nível
- Restrições e ações lógicas
  Nove caracteres terminantemente proibidos na nomeação: \ / : * ? " < > |
  Exclusão de arquivos enviando à Lixeira vs. Exclusão definitiva via Shift+Del
  Modos de exibição física no Explorador de Arquivos (Detalhes, Blocos, Lista, Ícones)
- Segurança e Otimização do sistema
  Desfragmentar e Otimizar Unidades (organização contígua de blocos físicos de HD)
  Criptografia total de partição lógica por meio de BitLocker
  Windows Defender Firewall com perfis de rede ativo (Domínio, Particular, Público)
  Ferramenta de Captura (Snipping Tool) com temporizador nativo

### Sistemas Operacionais Móveis: Android e iOS
- Arquitetura lógica do Android
  Base estruturada no Kernel Linux e camadas de bibliotecas nativas
  Compilação de aplicativos pelo Android Runtime (ART) na instalação
  Distribuição de software e arquivos de instalação no formato APK
- Blindagem criptográfica do iOS
  Coprocessador Secure Enclave para dados criptográficos de Face ID e Touch ID
- Gestão de privacidade e permissões
  Gerenciador de recursos nativos e recurso de Transparência no Rastreamento (ATT)

### Google Workspace
- Colaboração produtiva em nuvem
  Compartilhamento com níveis hierárquicos (Leitor, Comentarista, Editor)
  Edição cooperativa offline mediante ativação explícita de modo offline
  Recuperação automática por Histórico de Versões

### Fundamentos de Informática: Hardware e Software
- Estrutura e representação binária de dados
  Menor unidade de dados: bit (Binary Digit)
  Padrão de agrupamento de dados: 1 Byte correspondente a 8 bits
  Diferença de base binária de Bytes (1024) vs. base decimal de bits (1000)
- Componentes de hardware e hierarquia de memórias
  Dispositivos e periféricos de entrada, saída e de entrada/saída (E/S)
  Hierarquia física (registradores, cache, RAM, secundária)
  Unidades de memória de leitura (ROM, EPROM, EEPROM e Memória Flash)
  Mídias físicas secundárias (fita magnética de acesso sequencial, SSD e disco óptico)

### Lógica de Programação, Linguagens Web e APIs
- Lógica algorítmica e estruturas
  Operadores lógicos e operadores bit-a-bit (Bitwise Shift: << e >>)
  Passagem de parâmetros por Valor (cópia isolada) vs. por Referência (ponteiro)
  Estruturas de dados lineares: Vetores (estáticos) e Listas (dinâmicas)
  Estruturas lineares de acesso: Pilha (LIFO) e Fila (FIFO)
- Programação web front-end
  Estrutura de tags HTML e função informativa de tags metadados (<meta>)
  Uso de manifesto de cache (.appcache) na tag <html> para acesso offline
  Sintaxe CSS para estilização de cores, fundos e layouts
  JavaScript para interatividade com operadores de incremento pós/pré e controle lógico
- Persistência e Integração lógica
  Armazenamento local do navegador via localStorage (persistente) e sessionStorage (guia)
  Modelagem e arquitetura de integração por meio de APIs RESTful
  Propriedades das APIs RESTful: operação sem estado (stateless) e métodos HTTP

### Bancos de Dados
- Sistemas e independências físicas/lógicas
  Papel dos Sistemas Gerenciadores de Banco de Dados (SGBD)
  Independência lógica (alteração conceitual) e física (armazenamento físico)
- Propriedades rígidas de transações (ACID)
  Atomicidade (tudo ou nada)
  Consistência (obediência às regras estruturais de integridade)
  Isolamento (transações paralelas comportam-se de forma serial)
  Durabilidade (permanência do dado pós-commit diante de falhas de rede)
- Modelagem NoSQL e especiais
  Modelos de bancos de dados em memória (In-Memory)
  Modelos desestruturados Não-Relacionais (NoSQL): chave-valor, documentos, grafos e colunas

### Legislação Digital: Lei Geral de Proteção de Dados (LGPD)
- Definições legais estruturais (Art. 5º)
  Dado pessoal comum, sensível e anonimizado, tratamento e relatórios (RIPD)
- Princípios do tratamento de dados (Art. 6º)
  O princípio da Necessidade (limitação de tratamento ao mínimo necessário)
- Tratamento de vulneráveis e prazos
  Regras para dados de crianças (exigência de consentimento de responsável)
  Direito de acesso a dados em formato simplificado (imediato) ou completo (15 dias)
- Agentes de tratamento e responsabilidade
  Competências do Controlador (decisões) e Operador (execução sob instruções)
  Obrigatoriedade de registro de operações por ambos os agentes
  Regime de responsabilidade civil e indenização de prejuízos causados
- Fiscalização, multas e penalidades
  Multa simples de até 2% do faturamento limitada a R\$ 50 milhões por infração
  Suspensão temporária do tratamento (máximo 6 meses prorrogável)
  Regra de aplicação gradual de penalidades graves da ANPD

### Legislação Digital: Marco Civil da Internet
- Fundamentos normativos e terminologias (Arts. 2º, 3º, 5º)
  Conceito técnico de terminal, IP, registros de conexão e registros de aplicação
- Guarda compulsória de logs e prazos
  Provedores de conexão: guarda obrigatória de logs de conexão por 1 ano (12 meses)
  Provedores de conexão: proibição expressa de guarda de logs de aplicação
  Provedores de aplicação comercial/profissional: guarda de logs de aplicação por 6 meses
- Procedimento de preservação cautelar
  Extensão de guarda por requisição de autoridade e prazo decadencial de 60 dias para judicialização
  Reserva de jurisdição para disponibilização física de registros
- Responsabilidade civil e remoção de conteúdo de terceiros
  Isenção total dos provedores de conexão
  Responsabilidade de provedores de aplicação por notice and takedown judicial (Art. 19)
  Exceção para remoção imediata de pornografia não consensual por simples notificação da vítima (Art. 21)

### Legislação Digital: Crimes Informáticos
- Evolução típica de crimes digitais
  Redação original do Art. 154-A do Código Penal (Lei Carolina Dieckmann de 2012)
  Exigência de "violação de mecanismo de segurança" e pena de detenção de 3 meses a 1 ano
- Atualizações penais graves (Lei 14.155 de 2021)
  Exclusão da necessidade elementar de barreira ou violação física para configuração do crime
  Majoração da pena básica para reclusão de 1 a 4 anos, e multa
  Majoração de um sexto a dois terços se resultar em prejuízo econômico
  Invasão qualificada (§ 3º) com reclusão de 2 a 5 anos, e multa
- Condicionamento de Ação Penal
  Ação Pública Condicionada à Representação vs. Pública Incondicionada contra a Administração


## Conceitos-chave por tema

### Redes de Computadores e Internet

- **Protocolo IP (Internet Protocol)**: Protocolo da camada de rede que atua host-a-host. É considerado um protocolo não confiável (unreliable) e sem conexão, pois não garante a entrega, a integridade ou a ordem dos pacotes.
- **IPv4 vs. IPv6**: O IPv4 utiliza endereços de **32 bits** divididos em quatro octetos decimais pontuados. O IPv6 utiliza endereços de **128 bits** divididos em oito grupos hexadecimais de 16 bits separados por dois-pontos.
- **Regras de Abreviatura do IPv6**: Grupos sucessivos compostos apenas por zeros podem ser substituídos por **dois-pontos duplos (::)**, o que só é permitido **uma única vez** por endereço. Zeros à esquerda em qualquer grupo individual podem ser completamente omitidos.
- **Protocolo TCP (Transmission Control Protocol)**: Protocolo da camada de transporte orientado à conexão e confiável que opera **fim-a-fim** (ou processo-a-processo). Implementa controle de fluxo utilizando o mecanismo de **Janelas Deslizantes** e garante a entrega ordenada de segmentos.
- **Protocolo UDP (User Datagram Protocol)**: Protocolo da camada de transporte sem conexão e não confiável. Não possui controle de fluxo, não confirma recebimento de pacotes, não reordena segmentos e não faz retransmissões. É ideal para transmissões rápidas que toleram perdas, como streaming e VoIP.
- **Protocolo ARP (Address Resolution Protocol)**: Protocolo de camada de rede que traduz um endereço IP (lógico) em um endereço **MAC (físico/hardware) de 48 bits**.
- **DNS (Domain Name System)**: Protocolo da camada de aplicação responsável por traduzir nomes de domínios em endereços IP lógicos. No Brasil, o registro e manutenção de domínios nacionais são centralizados pelo **Registro.br**.
- **SMTP vs. POP3 vs. IMAP**: O SMTP é o protocolo da camada de aplicação responsável estritamente pelo **envio (saída)** de mensagens. O POP3 realiza o **download local** e apaga os e-mails do servidor por padrão. O IMAP permite a **sincronização** em tempo real das mensagens mantidas centralizadamente no servidor.

### Intranets e Redes Privadas Virtuais (VPN)

- **Intranet vs. Extranet**: Intranet é uma rede privada corporativa restrita aos funcionários de uma organização que utiliza a pilha de protocolos TCP/IP da internet. Extranet é a extensão controlada e autorizada de partes da intranet para **parceiros comerciais, clientes ou fornecedores** externos.
- **VPN (Virtual Private Network)**: Rede privada virtual criada sobre a infraestrutura de uma rede pública (como a internet). Utiliza técnicas de **tunelamento** (encapsulamento de um protocolo em outro) e criptografia para garantir a **confidencialidade e integridade** dos dados em trânsito.
- **Protocolos e Tipos de VPN**: Utiliza protocolos como **IPSec e L2TP** nas camadas de enlace ou rede. Divide-se em **Site-to-Site** (interconecta redes de escritórios distintos de forma roteador-a-roteador) e **Client-to-Site** (conecta um dispositivo individual a uma rede remota de forma cliente-a-gateway).

### Navegadores e Mecanismos de Navegação Web

- **Arquitetura Sandbox**: Recurso de segurança que isola as guias abertas. Cada guia funciona como um **processo separado e independente** no sistema operacional, o que evita que falhas ou códigos maliciosos de uma página comprometam outras guias ou o sistema hospedeiro.
- **Cache do Navegador (Web Cache)**: Armazenamento local de imagens e partes estáticas de páginas visitadas. Tem a função exclusiva de **acelerar o carregamento** das páginas em acessos futuros, poupando banda da rede.
- **Cookies**: Pequenos arquivos de texto gravados no computador do usuário para armazenar dados de estado e preferências. Dividem-se em **cookies de sessão** (apagados ao fechar o navegador) e **cookies persistentes** (gravados no disco rígido com data de expiração definida).
- **Navegação Anônima / Privativa**: Impede o salvamento local do histórico, pesquisas, dados de formulários e cookies após o encerramento da sessão. **Não impede o rastreamento** das atividades por provedores de acesso à internet, administradores de redes corporativas ou servidores de destino.
- **Níveis de Proteção do Google Chrome**:
  - *Proteção reforçada*: Envia dados adicionais e proativos para avaliar riscos de downloads, páginas e extensões, além de alertar sobre **vazamentos de senhas**.
  - *Proteção padrão*: Alerta contra ameaças conhecidas e sites perigosos de forma menos invasiva.
  - *Sem proteção*: Desativa as verificações de segurança nativas do navegador.

### Correio Eletrônico

- **Pastas de Correio**: A **Caixa de Saída** armazena temporariamente os e-mails em fila de processamento que ainda não foram transmitidos por falha ou atraso de envio. Os **Itens Enviados** arquivam mensagens que já foram transmitidas com sucesso ao servidor SMTP.
- **Compactação de Pastas (Mozilla Thunderbird)**: As mensagens excluídas no cliente local permanecem fisicamente no disco e são apenas ocultadas. A **compactação manual ou automática** é obrigatória para remover definitivamente os arquivos e recuperar espaço físico em disco.
- **Respostas de Férias e Regras**: Configuração na guia **Arquivo** (modo Backstage) do gerenciador de e-mails para responder automaticamente a remetentes durante períodos de indisponibilidade ou reencaminhar mensagens com base em filtros cadastrados.

### Segurança da Informação e Segurança Cibernética

- **Tríade CID e Atributos**:
  - *Confidencialidade*: Protege a informação contra acesso não autorizado. Garantida por criptografia.
  - *Integridade*: Protege a informação contra modificação não autorizada. Garantida por funções hash e assinaturas digitais.
  - *Disponibilidade*: Garante o acesso em tempo oportuno a usuários autorizados. Garantida por tolerância a falhas e rotinas de backup.
  - *Autenticidade*: Garante a real identidade da autoria de uma mensagem ou transação.
  - *Não-repúdio (Irretratabilidade)*: Impede que o autor negue a autoria de uma ação anteriormente validada.
- **Criptografia Simétrica**: Emprega a **mesma chave secreta** para cifrar e decifrar. Apresenta alta velocidade de processamento, mas **não garante o não-repúdio** e exige canal de transmissão seguro para compartilhamento da chave. Algoritmos: **AES, DES, 3DES, Blowfish, RC4, IDEA**.
- **Criptografia Assimétrica**: Emprega um **par de chaves matematicamente correlacionadas** (pública e privada). Cifrar com a chave pública do destinatário garante **confidencialidade** (apenas o dono da chave privada correspondente pode ler). Cifrar com a chave privada do emissor garante **autenticidade e não-repúdio** (assinatura digital). Algoritmos: **RSA**.
- **Função Hash**: Algoritmo que gera um resumo matemático de tamanho fixo e unidirecional a partir de dados de qualquer extensão. É usado para **garantir a integridade**. Algoritmos: **MD5 (saída de 128 bits)** e **SHA-256 (saída de 256 bits)**.
- **Assinatura Digital**: O remetente criptografa o hash da mensagem utilizando sua própria **chave privada**. Garante integridade, autenticidade e não-repúdio, mas **não garante sigilo/confidencialidade**, pois o corpo da mensagem pode trafegar em claro.
- **Certificados Digitais (ICP-Brasil)**: Documento assinado por uma Autoridade Certificadora (AC) que vincula um titular a uma chave pública. A **Lista de Certificados Revogados (LCR)** invalida certificados antes de seu vencimento. Prazos e Validades:
  - *A1/S1 (Software / Disco Rígido ou Pendrive)*: Validade máxima de **1 ano**.
  - *A2/S2 (Software / Smartcard ou Token)*: Validade máxima de **2 anos**.
  - *A3/S3 (Hardware / Smartcard ou Token USB)*: Validade máxima de **5 anos**.
  - *A4/S4 (Hardware / HSM)*: Validade máxima de **6 anos**.

### Ameaças Cibernéticas e Malwares

- **Vírus de Computador**: Código malicioso parasitário que insere cópias de si mesmo em outros arquivos. **Necessita de um programa ou arquivo hospedeiro** e da **ação direta do usuário** para se propagar e infectar a máquina.
- **Worm (Verme)**: Programa malicioso autônomo. **Não necessita de arquivo hospedeiro nem de ação do usuário**; propaga-se de forma automática pelas conexões de rede explorando vulnerabilidades. Seu principal impacto é o **alto consumo de largura de banda e recursos de processamento** de rede.
- **Bot**: Programa independente que, uma vez instalado, disponibiliza um canal de backdoor estável para que o invasor **controle o computador infectado (zumbi) remotamente**. Uma rede estruturada de bots forma uma **Botnet** para coordenar ataques de DDoS.
- **Spywares**: Softwares projetados para espionar e monitorar dados locais. Subdividem-se em:
  - *Keylogger*: Monitora e captura teclas digitadas fisicamente.
  - *Screenlogger*: Registra cliques do mouse e imagens da tela ao redor do cursor (anulando teclados virtuais).
- **Trojan (Cavalo de Troia)**: Programa aparentemente útil que traz uma carga maliciosa embutida para abrir portas (backdoors) sem o conhecimento do usuário. Não se propaga autonomamente.
- **Ransomware**: Malware de extorsão que criptografa os dados locais para torná-los inacessíveis e exige o pagamento de resgate (normalmente em criptomoedas como Bitcoin). O pagamento **não oferece nenhuma garantia** de devolução de chaves.
- **Técnicas de Fraude (Phishing, Baiting, Brute Force)**:
  - *Phishing*: Mensagens de engenharia social que falsificam entidades confiáveis para pescar dados pessoais.
  - *Baiting*: Uso de iscas físicas (como pendrives abandonados com malwares em áreas públicas) para induzir a conexão do hardware.
  - *Brute Force (Força Bruta)*: Ataque automatizado por software para adivinhar senhas por meio de tentativas repetidas de combinações lógicas.

### Segurança de Redes e Firewalls

- **Firewall de Filtragem de Pacotes (Stateless)**: Analisa cabeçalhos de pacotes individuais (IPs de origem/destino, protocolo e portas TCP/UDP) na camada de rede e transporte. Classificado como **stateless**, pois trata cada pacote de forma isolada, sem manter memória do contexto da conexão.
- **Firewall Stateful (Filtro de Estado)**: Mantém uma **tabela de estados** das conexões ativas na memória. É capaz de **verificar conexões TCP em andamento** antes de permitir a passagem de pacotes subsequentes, reduzindo significativamente o custo de processamento e aumentando a segurança.
- **Firewall Proxy (Gateway de Aplicação)**: Servidor intermediário (procurador) entre computadores da rede interna e serviços na internet pública. Opera na **camada de aplicação** e toma decisões com base no conteúdo (URLs, palavras-chave). Realiza armazenamento em **cache compartilhado para toda a rede**.
- **WAF (Web Application Firewall) e NGFW (Next-Generation)**:
  - *WAF*: Firewall especializado estritamente na inspeção e filtragem do tráfego HTTP/HTTPS direcionado a aplicações web (protegendo contra SQL Injection e XSS).
  - *NGFW*: Firewall de nova geração que incorpora **inspeção profunda de pacotes (DPI)**, identificação de aplicações independentemente da porta utilizada, antivírus de borda e sistemas de prevenção de intrusão (IPS) integrados.

### Backup e Recuperação de Dados

- **Mecanismo do Bit de Arquivamento (Flag Archive)**: Atributo lógico controlado pelo sistema operacional.
  - Quando um arquivo é criado ou alterado: Bit Archive = **1 (marcado)**, indicando que necessita de backup.
  - Quando passa por backup completo ou incremental: Bit Archive = **0 (desmarcado)**, indicando que já foi arquivado.
- **Tipos de Rotinas de Backup**:
  - **Backup Completo (Full / Normal / Total)**: Copia absolutamente **todos os arquivos** selecionados, independentemente de estarem marcados ou não, e **desmarca o bit de arquivamento (muda para 0)**.
  - **Backup Incremental**: Copia apenas os arquivos criados ou modificados (com Bit = 1) desde o último backup completo ou incremental anterior. Após a cópia, **desmarca o bit de arquivamento (muda para 0)**.
  - **Backup Diferencial (Incremental Cumulativo)**: Copia os arquivos criados ou modificados (com Bit = 1) desde o último backup completo ou incremental. Após a cópia, **NÃO desmarca o bit de arquivamento (mantém em 1)**.
  - **Backup de Cópia**: Copia todos os arquivos selecionados, mas **não altera nem remove o bit de arquivamento**.
  - **Backup Diário**: Copia apenas os arquivos gerados ou modificados na data da execução (baseando-se na data do sistema) e **não altera o bit de arquivamento**.
- **Hot vs. Cold Backup**:
  - *Hot Backup (Quente)*: Executado com o banco de dados ou sistema **ativo e em uso**, sem interromper a operação dos usuários.
  - *Cold Backup (Frio)*: Exige que o sistema ou banco de dados esteja **completamente fechado ou offline** para garantir a consistência física da cópia.

### Computação em Nuvem

- **Características Essenciais do NIST (NIST SP 800-145)**:
  - *Resource Pooling (Agrupamento de recursos)*: Recursos físicos/virtuais são agrupados de forma dinâmica para atender múltiplos clientes baseando-se no modelo de multi-tenancy.
  - *Rapid Elasticity (Elasticidade rápida)*: Recursos são provisionados ou liberados de forma automática e dinâmica para acompanhar variações rápidas de tráfego.
  - *Broad Network Access (Amplo acesso à rede)*: Serviços são disponibilizados em plataformas de rede padronizadas de amplo alcance geográfico (ubiquidade).
  - *On-demand Self-service (Autosserviço sob demanda)*: O cliente configura recursos computacionais (processamento, armazenamento) de maneira manual e automática, sem requerer intermediação humana do provedor.
  - *Measured Service (Serviço mensurável)*: O uso dos recursos é monitorado, controlado, tarifado e relatado com base no consumo efetivo (pay-per-use).
- **Modelos de Serviço (IaaS, PaaS, SaaS)**:
  - *IaaS (Infraestrutura)*: O provedor fornece capacidade física de processamento, servidores, virtualização, redes e armazenamento. O cliente gerencia e instala o **sistema operacional**, middlewares, dados e aplicações.
  - *PaaS (Plataforma)*: O provedor disponibiliza o hardware de infraestrutura corporativa e o sistema operacional, incluindo ambientes de desenvolvimento e bancos de dados. O cliente gerencia apenas os **dados gerados e as aplicações criadas**.
  - *SaaS (Software)*: O provedor gerencia toda a infraestrutura física e lógica. O cliente simplesmente acessa e utiliza a aplicação pronta via web browser.
- **Modelos de Implantação**:
  - *Pública*: A infraestrutura de nuvem é compartilhada e aberta ao uso de múltiplos inquilinos de forma aberta na internet.
  - *Privada*: A infraestrutura é operada de forma restrita e exclusiva para uma única organização.
  - *Híbrida*: Composta pela composição estruturada de duas ou mais nuvens distintas (pública, privada ou comunitária) que mantêm sua independência técnica.
  - *Comunitária*: Compartilhada de forma específica por organizações que possuem requisitos ou interesses comuns (por exemplo, órgãos de segurança pública).

### Suítes de Escritório: Excel e Calc

- **Operador Cifrão (\$) e Referências**:
  - `A1`: Referência relativa. Muda de linha e coluna se copiada ou arrastada.
  - `$A1`: Referência mista. Trava de forma absoluta a coluna A; a linha 1 permanece relativa.
  - `A$1`: Referência mista. Trava de forma absoluta a linha 1; a coluna permanece relativa.
  - `$A$1`: Referência absoluta. Congela tanto a linha quanto a coluna ao arrastar ou replicar a fórmula.
- **Menus e Interfaces do Calc**: A barra de menus do LibreOffice Calc é estruturada nos tópicos *Arquivo, Editar, Exibir, Inserir, Formatar, Estilos, Planilha, Dados, Ferramentas, Janela, Ajuda*.
- **Funções Matemáticas e de Agrupamento**: Ferramentas como **Consolidação de Dados** agregam tabelas dispostas em intervalos ou abas de planilhas heterogêneas, gerando somatórios, médias ou valores máximos unificados em um único intervalo de destino.

### Suítes de Escritório: Word e Writer

- **Modo Backstage do Word**: Interface ativada ao clicar na guia **Arquivo**. É usada para gerenciar o documento em nível estrutural externo (tarefas "com o arquivo", e não "no arquivo", como Imprimir, Salvar Como, Exportar PDF, Configurações e proteção de senha global).
- **Controle de Alterações**: Ferramenta de revisão que registra visualmente revisões colaborativas feitas no documento. Exclusões são formatadas com efeito visual **tachado** no modo de marcações e inserções ganham sublinhados ou cores destacadas.
- **Padrão ODF (Open Document Format)**: Formato de arquivo aberto baseado em XML desenvolvido pela organização **OASIS**. É o formato de salvamento nativo do LibreOffice Writer (`.odt`), Calc (`.ods`) e Impress (`.odp`).

### Sistemas Operacionais: Windows 11

- **Caracteres Proibidos em Arquivos/Pastas**: O Windows 11 veda de forma absoluta nomes de arquivos e pastas que contenham os caracteres: **`\ / : * ? " < > |`**.
- **Shift+Del**: Atalho de teclado para **excluir arquivos permanentemente**, sem passar pela retenção temporária na Lixeira. Arquivos excluídos com essa sequência não podem ser recuperados pelas funções nativas de restauração do sistema.
- **Windows Defender Firewall (Perfis de Rede)**: Fornece regras específicas para três tipos de perfis de rede:
  - *Domínio*: Ativo quando a máquina é autenticada em um controlador de domínio corporativo.
  - *Particular*: Ativo em redes internas conhecidas e confiáveis (domésticas ou corporativas sem domínio).
  - *Público*: Ativo em redes não confiáveis e abertas, como Wi-Fi públicos de aeroportos ou hotéis.
- **Ferramenta de Captura (Snipping Tool)**: Permite recortar imagens da tela do computador e inclui a funcionalidade de **temporizador (atraso de captura)** configurável para atrasar o registro da imagem por alguns segundos.
- **Criptografia com BitLocker**: Recurso nativo do Windows para **criptografar volumes inteiros** de unidades físicas de armazenamento (HDs e SSDs), impedindo a leitura indevida dos dados em caso de roubo físico do hardware.

### Sistemas Operacionais Móveis: Android e iOS

- **Arquitetura Modular do Android**: Baseado no kernel (núcleo) do Linux. Utiliza o ambiente de runtime **ART (Android Runtime)** para compilar aplicativos no momento da instalação física para melhor desempenho. Pacotes de aplicativos utilizam a extensão compactada **APK (Android Package Kit)**.
- **Segurança Blindada no iOS (Secure Enclave)**: Coprocessador físico de alta segurança responsável pelas operações criptográficas de biometria (Face ID e Touch ID). Os dados biométricos reais permanecem encriptados localmente no hardware do **Secure Enclave**, nunca sendo compartilhados com o sistema operacional principal ou enviados a servidores de nuvem (iCloud).
- **ATT (App Tracking Transparency)**: Funcionalidade de privacidade do iOS que exige autorização expressa do usuário (opt-in) antes que qualquer aplicativo monitore suas atividades de navegação em serviços de terceiros para fins de publicidade direcionada.

### Fundamentos de Informática (Hardware e Software)

- **Medidas de Armazenamento vs. Transmissão**:
  - *Bytes (B)*: Usam a representação de base binária (múltiplos de **1024**). 1 KB = 1024 Bytes. Empregados para medir capacidade física de memória.
  - *bits (b)*: Usam a representação de base decimal (múltiplos de **1000**). 1 Kb = 1000 bits. Empregados para medir taxas de transmissão e velocidade por segundo em redes.
  - *Conversão*: **1 Byte equivale estritamente a 8 bits**.
- **ROM (Read Only Memory) e Variações**: Memória não volátil cujos dados não são perdidos com a ausência de corrente elétrica.
  - *EPROM*: Permite apagamento por luz ultravioleta e regravação física.
  - *EEPROM*: Permite apagamento elétrico em nível de byte.
  - *Memória Flash*: Tecnologia que permite ciclos de apagamento elétrico em blocos de memória, servindo de base tecnológica para pendrives e unidades SSD.
- **Fita Magnética**: Mídia física de armazenamento secundário não volátil baseada no **acesso sequencial de dados**. Apresenta altíssima latência para leitura (pois exige o rebobinamento físico da fita até localizar a seção desejada), mas é amplamente utilizada para backups de longo prazo devido ao seu custo extremamente reduzido por gigabyte.

### Lógica de Programação, Linguagens Web e APIs

- **Estruturas de Dados**:
  - *Vetores*: Estrutura linear de armazenamento estático de dados, com tamanho fixo.
  - *Listas*: Estrutura linear dinâmica cujo tamanho se expande ou se contrai de forma flexível.
  - *Fila*: Estrutura que opera no padrão **FIFO (First-In, First-Out)**, em que o primeiro elemento inserido é o primeiro a ser retirado.
  - *Pilha*: Estrutura que opera no padrão **LIFO (Last-In, Last-Out)**, em que o último elemento inserido é obrigatoriamente o primeiro a ser retirado.
- **Passagem de Parâmetros**:
  - *Por Valor*: A sub-rotina recebe uma cópia isolada da variável original. Alterações feitas no método não afetam o valor da variável de origem.
  - *Por Referência*: A sub-rotina recebe o endereço físico de memória (ponteiro) da variável. Alterações se refletem instantaneamente no valor da variável de origem.
- **HTML5 Web Storage**:
  - *localStorage*: Persiste os dados de navegação localmente por domínio e protocolo, **sem data de validade definida**. Os dados sobrevivem ao fechamento das guias do navegador.
  - *sessionStorage*: Armazena dados de navegação apenas para a sessão atual. Os dados são **eliminados de forma definitiva assim que o usuário fecha a guia** do navegador.
- **Metadados em HTML**: A tag `<meta>` é inserida obrigatoriamente dentro da seção `<head>`. Ela armazena dados que descrevem informações estruturais da página (como viewport para responsividade móvel, autor e descrição) para navegadores e mecanismos de busca.
- **APIs RESTful**: Interfaces lógicas de comunicação de sistemas que utilizam verbos HTTP (`GET, POST, PUT, DELETE`) para manipular recursos identificados por URLs únicas. Uma API RESTful opera sob o pilar **stateless**, o que significa que cada requisição deve conter todas as informações para sua interpretação de forma isolada, sem dependência ou retenção de estado lógico no servidor.

### Bancos de Dados

- **Propriedades ACID**:
  - **Atomicidade**: A transação deve ser executada como uma unidade indivisível. Todas as operações são salvas (commit) ou, diante de qualquer falha, revertidas por completo (rollback).
  - **Consistência**: A transação deve mover o banco de dados de um estado íntegro para outro igualmente íntegro, respeitando todas as regras de integridade e restrições cadastradas.
  - **Isolamento**: Garante que transações executadas simultaneamente (concorrentes) não interfiram umas nas outras nem exponham estados parciais inconsistentes de dados.
  - **Durabilidade**: Garante que os dados modificados por uma transação confirmada (commit) permaneçam permanentemente gravados em meio físico estável, resistindo a falhas do sistema operacional ou quedas de energia.
- **Independência de Dados**:
  - *Independência Lógica*: Capacidade de alterar o esquema lógico conceitual do banco de dados (esquemas de tabelas, adição de atributos) sem a necessidade de reescrever ou alterar o código das aplicações de software que consomem os dados.
  - *Independência Física*: Capacidade de alterar o armazenamento físico do banco de dados (mudança de HDD para SSD, criação de índices lógicos) sem impactar o esquema conceitual ou o código das aplicações.
- **NoSQL (Bancos Não Relacionais)**: Bancos otimizados para grandes volumes de dados desestruturados ou semiestruturados. Estruturam dados em formato de **chave-valor, documentos, grafos ou colunas**.

### Legislação Digital: Lei Geral de Proteção de Dados (LGPD)

- **Vocabulário Legal da Lei (Art. 5º)**:
  - *Dado Pessoal*: Informação relacionada a pessoa natural identificada ou identificável.
  - *Dado Pessoal Sensível*: Informação que revela origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico.
  - *Controlador*: Pessoa natural ou jurídica a quem competem as decisões referentes ao tratamento de dados pessoais.
  - *Operador*: Pessoa natural ou jurídica que realiza o tratamento de dados pessoais em nome do controlador.
- **Princípios do Tratamento (Art. 6º)**: Destaca-se o princípio da **Necessidade**, que exige a limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência de dados não excessivos em relação aos objetivos originais.
- **Tratamento de Dados de Crianças (Art. 14)**: O tratamento de dados pessoais de crianças (até 12 anos incompletos) exige o **consentimento específico e em destaque dado por pelo menos um dos pais** ou pelo responsável legal.
- **Prazo de Exercício de Direitos (Art. 19)**: A confirmação de existência ou o acesso facilitado a dados cadastrais devem ser providenciados de forma imediata em formato simplificado ou, alternativamente, por meio de declaração clara e completa em até **15 dias** contados a partir da data de requerimento do titular.
- **Sanções Administrativas (Art. 52)**: Aplicadas exclusivamente pela ANPD. Variam de advertência simples à **multa simples de até 2% do faturamento** anual no Brasil, limitada ao teto de **R\$ 50.000.000,00 por infração**. Sanções graves (como suspensão de atividades ou proibição do tratamento) só podem ser aplicadas **após já ter sido imposta ao menos uma** das sanções menos severas (como advertência, multa simples, multa diária, publicização ou bloqueio de dados) para o mesmo caso concreto.

### Legislação Digital: Marco Civil da Internet (Lei nº 12.965/2014)

- **Vocabulário Técnico Legal (Art. 5º)**:
  - *Terminal*: Qualquer dispositivo que se conecte à internet.
  - *Registro de Conexão*: Log contendo a data e hora de início e término de uma conexão, sua duração e o endereço IP utilizado pelo terminal.
  - *Registro de Acesso a Aplicações*: Log contendo a data e hora de uso de uma aplicação de internet específica a partir de um IP.
- **Prazos Legais de Guarda de Logs**:
  - **Guarda de Conexão (Operadoras de Acesso)**: O administrador de sistema autônomo tem o dever de guardar os registros de conexão pelo prazo mínimo de **1 ano (12 meses)**, sob sigilo e ambiente controlado. **É expressamente vedado** ao provedor de conexão guardar registros de acesso a aplicações de internet de seus usuários.
  - **Guarda de Aplicação (Plataformas Web)**: Provedores de aplicação estruturados como pessoas jurídicas e operando profissionalmente com fins econômicos devem guardar registros de acesso a aplicações por no mínimo **6 meses**.
- **Procedimento Cautelar de Congelamento**: Autoridades policiais, administrativas ou o Ministério Público podem requerer cautelarmente que os registros de logs sejam mantidos guardados por mais tempo que o prazo legal. Contudo, a autoridade tem o prazo improrrogável de **60 dias** contados da data do pedido para protocolar o pedido judicial de acesso definitivo aos logs. A entrega dos registros aos investigadores **depende obrigatoriamente de ordem judicial**.
- **Responsabilidade Civil por Conteúdo de Terceiros**:
  - *Provedor de Conexão*: Não responde civilmente em nenhuma hipótese por danos decorrentes de conteúdos gerados por terceiros que trafegaram em sua rede.
  - *Provedor de Aplicação*: Só responde civilmente por danos de conteúdo gerado por terceiros se, após **ordem judicial específica contendo o endereço (URL) do material infringente**, não tomar as providências para torná-lo indisponível dentro do prazo determinado (notice and takedown judicial).
  - *Exceção de Nudez / Pornografia Não Consensual (Art. 21)*: O provedor de aplicação responde solidariamente caso não remova imagens, vídeos ou mídias contendo nudez ou atos sexuais de caráter privado após **notificação direta feita pela própria vítima** ou de seu representante legal, sem necessidade de decisão judicial prévia.

### Legislação Digital: Crimes Informáticos (Lei nº 12.737/2012 e Lei nº 14.155/2021)

- **Crime de Invasão de Dispositivo Informático (Art. 154-A do CP)**:
  - *Redação Original (Lei Carolina Dieckmann)*: Tipificava a conduta de invadir dispositivo de uso alheio mediante **violação indevida de mecanismo de segurança**, punindo o infrator com pena de detenção de 3 meses a 1 ano, e multa.
  - *Redação Atual (Lei 14.155/2021)*: Modificou a natureza da pena para **reclusão, de 1 a 4 anos, e multa**. **Excluiu-se a exigência elementar de "violação de mecanismo de segurança"**. A simples invasão sem consentimento já caracteriza o crime consumado.
  - *Aumento de Pena por Prejuízo*: Aumenta-se a pena de **um sexto a dois terços** se da invasão resulta prejuízo econômico concreto para a vítima (na redação original de 2012, o aumento de pena era de um sexto a um terço).
  - *Invasão Qualificada (Art. 154-A, § 3º)*: Ocorre quando a invasão resulta na obtenção de conteúdo de comunicações eletrônicas privadas, segredos comerciais ou industriais, informações sigilosas ou controle remoto do dispositivo. Pena atual: **reclusão de 2 a 5 anos, e multa**.
  - *Ação Penal*: A regra é a **Ação Penal Pública Condicionada à Representação** da vítima. O crime passa a ser processado mediante **Ação Penal Pública Incondicionada** se for cometido contra a administração pública direta ou indireta de qualquer esfera dos Poderes (União, Estados, DF, Municípios) ou contra concessionárias de serviços públicos.

***

`lacuna nas fontes: procedimentos práticos de auditoria de TI e técnicas avançadas de forense computacional (extração de imagens físicas, ferramentas específicas de perícia).`


## Pegadinhas, relações e lacunas

## Do que trata
O notebook reúne o material de preparação focado em Tecnologia da Informação para o concurso da Polícia Civil do Paraná (PCPR). Ele abrange conceitos básicos e avançados de redes de computadores, computação em nuvem, sistemas operacionais (Windows, Android, iOS) e suítes de escritório (Microsoft 365 e LibreOffice). Além disso, aprofunda-se em segurança da informação, programação web (HTML, CSS, JS), banco de dados, APIs e na legislação digital correlata, incluindo a LGPD, o Marco Civil da Internet e a Lei de Crimes Informáticos.

## Temas centrais
- **Segurança da Informação** — As fontes definem a segurança através dos pilares de Confidencialidade, Integridade e Disponibilidade (CID), além dos conceitos de autenticidade, não-repúdio e as diferenças entre criptografia simétrica (chave única compartilhada) e assimétrica (par de chaves pública e privada).
- **Malwares e Ameaças** — Códigos maliciosos são detalhados e classificados de acordo com sua propagação, destacando-se os vírus (que infectam arquivos e dependem de execução do usuário) e os worms (programas autônomos que se propagam pela rede explorando vulnerabilidades e consumindo largura de banda).
- **Computação em Nuvem** — A tecnologia é explicada com base no modelo do NIST que possui cinco características essenciais (serviços mensuráveis, elasticidade rápida, amplo acesso à rede, agrupamento de recursos e autosserviço sob demanda), três modelos de serviço (IaaS, PaaS, SaaS) e quatro modelos de implantação (pública, privada, híbrida e comunitária).
- **Legislação Digital (LGPD)** — A Lei 13.709/2018 regula o tratamento de dados pessoais por pessoas físicas ou jurídicas de direito público ou privado, com o intuito de proteger direitos fundamentais como a liberdade e a privacidade.
- **Legislação Digital (Marco Civil da Internet)** — A Lei 12.965/2014 estabelece princípios e garantias para o uso da rede no Brasil, regulando os prazos obrigatórios para guarda de logs (1 ano para registros de conexão mantidos por administradores de sistema autônomo e 6 meses para registros de acesso de provedores de aplicação).
- **Políticas de Backup** — Os procedimentos de cópia de segurança envolvem diferentes tipos de rotinas que manipulam o bit de arquivamento (Archive Bit), diferenciando o backup completo (copia tudo e desmarca o bit), o incremental (copia alterações desde o último backup e desmarca o bit) e o diferencial (copia alterações desde o último completo e não desmarca o bit).
- **APIs e Arquitetura Web** — As fontes descrevem o desenvolvimento e a integração de sistemas focando em APIs RESTful, as quais utilizam métodos HTTP padronizados (GET, POST, PUT, DELETE) e operam de forma stateless, sem guardar estado entre as requisições.
- **Sistemas Operacionais e Windows 11** — O sistema é tratado na gestão prática de arquivos, pastas e caminhos de diretório, além de recursos nativos como o BitLocker (criptografia de volume inteiro), o Windows Defender Firewall com perfis de rede específicos e ferramentas administrativas de otimização de discos.

## O que aparece com mais profundidade
- **Diferenciação e Mecanismos de Malwares**: As fontes dedicam extensas seções com tabelas detalhadas comparando a forma de obtenção, forma de instalação, forma de propagação e ações maliciosas de múltiplos códigos, tais como vírus, worms, bots, cavalos de troia, spywares (keyloggers e screenloggers), backdoors e rootkits.
- **Modelos de Responsabilidade Compartilhada na Nuvem**: Há uma forte insistência prática e teórica em distinguir quais recursos de infraestrutura (redes, armazenamento, servidores, virtualização, SO, middlewares, dados e aplicações) são gerenciados pelo cliente e quais são gerenciados pelo provedor de serviços nos arranjos de IaaS, PaaS e SaaS.
- **Princípios e Direitos na LGPD**: A Lei Geral de Proteção de Dados é destrinchada exaustivamente artigo por artigo, com destaque repetido para as obrigações dos agentes de tratamento (controlador e operador), os direitos de petição e retificação do titular, e o regime de responsabilidade civil em caso de vazamentos de dados.

## Nomes, normas e números que se repetem
- **Lei nº 13.709/2018 (LGPD)** e seus artigos fundamentais (como o Art. 5º que define o vocabulário básico, o Art. 6º que lista os 10 princípios e o Art. 7º que elenca os requisitos de tratamento).
- **Lei nº 12.965/2014 (Marco Civil da Internet)**, citando frequentemente seus conceitos de terminal, IP e os prazos obrigatórios de custódia de dados.
- **Prazos de guarda de logs do Marco Civil**: o prazo de **1 ano** (12 meses) para registros de conexão armazenados pelo administrador de sistema autônomo, e o prazo de **6 meses** para os registros de acesso a aplicações.
- **Padrões IEEE 802**: a recorrência de referências a protocolos como o **IEEE 802.3 (Ethernet)**, **IEEE 802.11 (Wi-Fi)** e **IEEE 802.15 (Bluetooth)**.
- **NIST SP 800-145**: a norma e framework norte-americano do National Institute of Standards and Technology citado repetidas vezes como o molde conceitual para o estudo da Computação em Nuvem.
- **Dados e Limites de Criptografia**: especificações de tamanhos de chaves e barramentos que se repetem, como chaves simétricas de 128, 192 e 256 bits no padrão **AES**, saídas de hashes em **MD5 (128 bits)** e **SHA-256 (256 bits)**.

## Lacunas
- **Auditoria de TI e Perícia Forense** — Embora conste o título da disciplina no edital/pasta, as fontes não trazem pouca ou nenhuma cobertura prática e detalhada sobre técnicas de forense computacional, cadeia de custódia digital de provas físicas, extração de imagens de discos (bit-stream) ou uso de ferramentas periciais específicas.
- **Cálculos Matemáticos de Sub-Redes (CIDR)** — O notebook foca amplamente na teoria das classes de IPs (A, B e C) e faixas privadas, mas há uma lacuna de conteúdo prático e didático sobre o cálculo de máscaras de sub-rede de tamanho variável (VLSM) e conversões binárias complexas para identificar IPs de rede e broadcast.


## Materiais baixados deste notebook

- [546f0cb3_quiz_nuvem-quiz_a712ac.md](../materiais/546f0cb3_quiz_nuvem-quiz_a712ac.md)


## Fontes

- Aula 00 - Internet, redes e tecnologias digitais - Resumo.pdf `(pdf)`
- Aula 00 - Internet, redes e tecnologias digitais - Simplificada.pdf `(pdf)`
- Aula 01 - Internet, redes e tecnologias digitais - Resumo.pdf `(pdf)`
- Aula 01 - Internet, redes e tecnologias digitais - Simplificada.pdf `(pdf)`
- Aula 02 - Intranet; VPN - Resumo.pdf `(pdf)`
- Aula 02 - Intranet; VPN - Simplificada.pdf `(pdf)`
- Aula 03 - Computação em nuvem; dispositivos e serviços em nuvem - Resumo.pdf `(pdf)`
- Aula 03 - Computação em nuvem; dispositivos e serviços em nuvem - Simplificada.pdf `(pdf)`
- Aula 04 - Navegadores; cookies; cache - Simplificada.pdf `(pdf)`
- Aula 05 - Correio eletrônico - Resumo.pdf `(pdf)`
- Aula 05 - Correio eletrônico - Simplificada.pdf `(pdf)`
- Aula 06 - Redes sociais; plataformas digitais - Simplificada.pdf `(pdf)`
- Aula 07 - Segurança da informação e segurança cibernética - Resumo.pdf `(pdf)`
- Aula 07 - Segurança da informação e segurança cibernética - Simplificada.pdf `(pdf)`
- Aula 08 - Vulnerabilidades; malware; ransomware; phishing - Resumo.pdf `(pdf)`
- Aula 08 - Vulnerabilidades; malware; ransomware; phishing - Simplificada.pdf `(pdf)`
- Aula 09 - Segurança em redes; Firewall - Simplificada.pdf `(pdf)`
- Aula 10 - Backup; recuperação de dados - Resumo.pdf `(pdf)`
- Aula 10 - Backup; recuperação de dados - Simplificada.pdf `(pdf)`
- Aula 11 - Prevenção e resposta a incidentes de segurança - Apostila completa.pdf `(pdf)`
- Aula 12 - Microsoft 365 (BR) - Excel - Resumo.pdf `(pdf)`
- Aula 12 - Microsoft 365 (BR) - Excel - Simplificada.pdf `(pdf)`
- Aula 13 - LibreOffice-BrOffice - Calc - Resumo.pdf `(pdf)`
- Aula 13 - LibreOffice-BrOffice - Calc - Simplificada.pdf `(pdf)`
- Aula 14 - Microsoft 365 (BR) - Word - Resumo.pdf `(pdf)`
- Aula 14 - Microsoft 365 (BR) - Word - Simplificada.pdf `(pdf)`
- Aula 15 - LibreOffice-BrOffice - Writer - Resumo.pdf `(pdf)`
- Aula 15 - LibreOffice-BrOffice - Writer - Simplificada.pdf `(pdf)`
- Aula 16 - Microsoft 365 (BR) - PowerPoint - Resumo.pdf `(pdf)`
- Aula 16 - Microsoft 365 (BR) - PowerPoint - Simplificada.pdf `(pdf)`
- Aula 17 - LibreOffice-BrOffice - Impress - Resumo.pdf `(pdf)`
- Aula 17 - LibreOffice-BrOffice - Impress - Simplificada.pdf `(pdf)`
- Aula 18 - Sistemas operacionais - Windows 11 (BR) - Resumo.pdf `(pdf)`
- Aula 18 - Sistemas operacionais - Windows 11 (BR) - Simplificada.pdf `(pdf)`
- Aula 19 - Android e iOS - instalação, configuração e segurança - Simplificada.pdf `(pdf)`
- Aula 20 - Google Workspace - Simplificada.pdf `(pdf)`
- Aula 21 - Fundamentos de informática - hardware e software - Resumo.pdf `(pdf)`
- Aula 21 - Fundamentos de informática - hardware e software - Simplificada.pdf `(pdf)`
- Aula 23 - Noções de lógica de programação - Apostila completa.pdf `(pdf)`
- Aula 24 - Aplicações web, HTML - Apostila completa.pdf `(pdf)`
- Aula 25 - CSS - Apostila completa.pdf `(pdf)`
- Aula 26 - Bancos de dados - Simplificada.pdf `(pdf)`
- Aula 27 - APIs - Simplificada.pdf `(pdf)`
- Aula 28 - JavaScript - Apostila completa.pdf `(pdf)`
- Aula 29 - Legislação e ética digital - LGPD - Resumo.pdf `(pdf)`
- Aula 29 - Legislação e ética digital - LGPD - Simplificada.pdf `(pdf)`
- Aula 30 - Marco Civil da Internet (Lei 12.965-2014) - Simplificada.pdf `(pdf)`
- Aula 31 - Lei dos Crimes Informáticos (Lei 12.737-2012) - Apostila completa.pdf `(pdf)`
- computação em nuvem `(markdown)`