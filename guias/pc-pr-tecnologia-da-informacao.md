# GUIA DEFINITIVO DE ESTUDO: REDES DE COMPUTADORES E INTERNET (FOCO FGV)

Este guia foi estrategicamente elaborado para o candidato que não aceita ser enganado pela **Fundação Getulio Vargas (FGV)**. Como seu professor especialista, mapeei cada detalhe técnico exaustivo e as armadilhas recorrentes que a banca utiliza para desestabilizar o concorrente. Use este material como sua ferramenta definitiva de revisão.

---

## 1. Fundamentos e Conexões de Rede

### 1.1 Definição e Benefícios
Uma rede de computadores é um conjunto de terminais, equipamentos, meios de transmissão e comutação que, interligados, possibilitam a prestação de serviços e a troca de dados.

**Os 7 Benefícios Estratégicos (Mapeados pela FGV):**
1.  **Compartilhamento de Recursos:** Uso comum de hardware (impressoras) e software, reduzindo custos e redundância.
2.  **Comunicação Eficiente:** Troca rápida e segura de dados (e-mails, mensagens, videoconferências).
3.  **Acesso à Informação:** Obtenção organizada de dados para decisões ágeis.
4.  **Centralização de Dados:** Simplifica backups, gerenciamento e aumenta a segurança.
5.  **Redução de Custos:** Otimiza o uso de infraestrutura e reduz gastos operacionais.
6.  **Flexibilidade e Mobilidade:** Permite o trabalho remoto e acesso móvel à informação.
7.  **Escalabilidade e Integração:** Facilidade em adicionar novos dispositivos e usuários.

### 1.2 Tipos de Link/Enlace
O link (ou enlace) é o canal que permite o tráfego de dados.

| Tipo de Conexão | Descrição Técnica | Exemplo de Prova |
| :--- | :--- | :--- |
| **Ponto-a-Ponto** | Fornece um link dedicado e exclusivo entre dois dispositivos. | Controle remoto e TV. |
| **Ponto-Multiponto** | Link compartilhado por mais de dois dispositivos simultaneamente. | Redes Wi-Fi públicas ou Mainframe conectando várias estações. |

### 1.3 Direções e Modos de Transmissão
A banca FGV adora confundir sentido (fluxo) com destinatários.

**Direções de Transmissão (Fluxo):**
*   **Simplex:** Comunicação unidirecional. Papéis de transmissor e receptor nunca se invertem (Ex: TV, Rádio, Teclado).
*   **Half-Duplex:** Bidirecional, mas não simultânea. Ambos transmitem e recebem, porém um por vez (Ex: Walkie-talkie).
*   **Full-Duplex:** Bidirecional e simultânea. Alta eficiência (Ex: Celular, VoIP).

**Modos de Transmissão (Destinatários):**
*   **Unicast:** Um para um. Destinatário único e específico.
*   **Multicast:** Um para vários. Envio para um grupo selecionado.
*   **Broadcast:** Um para todos. Mensagem enviada para todos os nós da rede.
*   **Anycast:** (Conceito de rodapé) Comunicação de um remetente para o destinatário mais próximo dentro de um grupo.

> **Pegadinha de Ouro:** A FGV tenta desestabilizar o candidato ao usar o termo "Ponto-a-Ponto" em dois contextos. No **Tipo de Conexão**, refere-se ao link dedicado. Na **Arquitetura**, refere-se ao modelo P2P (Par-a-par), onde não há servidor centralizado e as máquinas são iguais.
>
> **Questões da Banca:** Costumam pedir a modalidade que permite fala e escuta simultânea (Full-Duplex) e a diferença prática entre Broadcast técnico (enviar para todos os endereços) vs. redes sociais.

---

## 2. Dimensão e Abrangência Geográfica

### 2.1 Classificação PAN, LAN, MAN e WAN
A classificação baseia-se estritamente no espaço físico interligado.

*   **PAN (Personal Area Network):** Rede pessoal (celular, fones, mouse).
    *   *Cobertura:* Centímetros a poucos metros.
    *   *Tecnologias:* Bluetooth, USB.
*   **LAN (Local Area Network):** Redes de lares, escritórios ou edifícios.
    *   *Cobertura:* Centenas de metros a alguns quilômetros.
    *   *Tecnologias:* Ethernet, Wi-Fi.
*   **MAN (Metropolitan Area Network):** Abrange uma cidade ou área metropolitana (matriz e filiais).
    *   *Cobertura:* Dezenas de quilômetros.
    *   *Tecnologias:* Fibra óptica, WiMAX.
*   **WAN (Wide Area Network):** Grande área (cidades distantes, países ou continentes).
    *   *Cobertura:* Dezenas a milhares de quilômetros.
    *   *Tecnologia:* Internet.

**Tabela Resumo de Abrangência:**

| Sigla | Extensão Típica | Foco de Aplicação |
| :--- | :--- | :--- |
| **PAN** | Centímetros a metros | Dispositivos pessoais de curto alcance. |
| **LAN** | Metros a quilômetros | Redes locais (escritórios, escolas). |
| **MAN** | Dezenas de quilômetros | Conectar redes locais em uma cidade. |
| **WAN** | Milhares de quilômetros | Comunicação global (Internet). |

**O Prefixo "W" (Wireless):** Para redes sem fio, utiliza-se WPAN, WLAN, WMAN e WWAN.

> **Pegadinha da FGV:** O examinador pode omitir o "W" e chamar uma rede Wi-Fi doméstica simplesmente de "LAN". Fique atento: o critério geográfico prevalece sobre o meio físico no enunciado.

---

## 3. Arquitetura e Topologia de Redes

### 3.1 Arquitetura P2P vs. Cliente/Servidor
*   **Ponto-a-Ponto (P2P/Par-a-par):** Modelo não hierárquico. Todos são iguais (pares/peers).
    *   *Puro:* Totalmente descentralizado (BitTorrent).
    *   *Híbrido:* Utiliza **supernós** para coordenação e indexação de dados.
*   **Cliente/Servidor:** Modelo hierárquico centralizado. Servidores dedicados oferecem serviços; clientes os consomem.

**Tabela Comparativa de Arquitetura:**

| Critério | Ponto-a-Ponto (P2P) | Cliente/Servidor |
| :--- | :--- | :--- |
| **Custo** | Baixo (sem servidor dedicado) | Alto (exige máquinas potentes) |
| **Gerenciamento** | Difícil e descentralizado | Fácil e centralizado |
| **Segurança** | Menor (difícil aplicar políticas) | Maior (políticas no servidor) |
| **Escalabilidade** | Limitada em grandes redes | Alta (fácil adicionar clientes) |

### 3.2 Topologias Físicas e Lógicas
*   **Física:** Layout real dos cabos e nós.
*   **Lógica:** Fluxo real ou percurso dos dados.

**As 4 Topologias Básicas:**
1.  **Barramento (Bus):** Todos ligados a um único cabo central (**backbone**). Uma ruptura no cabo derruba toda a rede. Usa conectores BNC.
2.  **Anel (Ring):** Círculo fechado. Transmissão unidirecional (Simplex). O controle de acesso é feito pelo **Token** (passe). Sem colisões.
3.  **Estrela (Star):** Todas ligadas a um nó central (Hub/Switch). Enlace estação-nó é Ponto-a-Ponto. Falha em um cabo não afeta os outros.
4.  **Malha (Mesh):** Múltiplos caminhos.
    *   *Full Mesh:* Todos conectados a todos.
    *   *Fórmulas:* Cabos = $n(n-1)/2$; Portas/Placas = $n(n-1)$.

> **Pegadinha Clássica do Hub:** Fisicamente é **Estrela** (layout dos cabos), mas logicamente é **Barramento**. Por ser um **Meio Compartilhado**, ele se comporta como um barramento onde apenas um pode falar por vez, causando colisões.

---

## 4. Meios de Transmissão (Guiados e Não-Guiados)

### 4.1 Cabos de Cobre
*   **Cabo Coaxial:** Fio central de cobre, blindagem metálica. Uso em TV a cabo e redes antigas.
    *   **Conectores BNC:** Existem três tipos: **Padrão** (conexão final), **T-BNC** (divisão da conexão/splitting) e **Terminador** (instalado no fim do cabo para impedir a reflexão do sinal).
*   **Cabo de Par Trançado:** Fios entrelaçados para reduzir interferência. Usa conector **RJ-45**.
    *   *UTP:* Sem blindagem. *STP:* Com blindagem.

**Tabela Técnica de Categorias (CAT):**
| Categoria | Largura de Banda | Taxa Máxima |
| :--- | :--- | :--- |
| **CAT3** | 16 MHz | 10 Mbps |
| **CAT5e** | 100 MHz | 1 Gbps |
| **CAT6/6A** | 250/500 MHz | 10 Gbps |
| **CAT7** | **600 MHz** | 10 Gbps |
| **CAT7A** | **1000 MHz** | 10 Gbps |
| **CAT8** | 2000 MHz | 40 Gbps |

### 4.2 Fibra Óptica
Transmite luz através de um núcleo (vidro/plástico) e uma casca.
*   **Monomodo (Single mode):** Um caminho de luz. Longas distâncias (WAN), Laser. **Baixo índice de refração e baixa atenuação.**
*   **Multimodo (Multimode):** Vários caminhos de luz. Curtas distâncias (LAN), LED. **Alto índice de refração e alta atenuação.**

### 4.3 Meios Não-Guiados (Wireless)
*   **Rádio:** Omnidirecional, atravessa obstáculos.
*   **Infravermelho:** Exige **linha de visada** direta (curto alcance).
*   **Micro-ondas:** Transmissão via antenas ou satélite.

> **Pegadinha da FGV:** Diferença entre **Largura de Banda** (capacidade teórica máxima) e **Taxa de Transferência/Throughput** (velocidade real prática, limitada por ruídos e atrasos).

---

## 5. Equipamentos de Interconexão

### 5.1 Dispositivos de Camada 1 e 2
*   **Placa de Rede (NIC):** Camada 2. Possui o **Endereço MAC** (48 bits/6 bytes), físico e único.
*   **Hub (Concentrador):** Camada 1. "Burro": apenas repete o sinal para todas as portas via Broadcast. Cria um único domínio de colisão.
*   **Bridge (Ponte):** Camada 2. Filtra dados pelo endereço MAC. Divide a rede em domínios de colisão menores. Processamento via software (lenta).
*   **Switch (Comutador):** Camada 2 (ou L3 se for roteador). Inteligente. Usa **autoaprendizado** (tabela MAC) e **autonegociação**. Elimina colisões em Full-Duplex. Processamento via hardware (rápida).

### 5.2 Roteadores e Modems
*   **Router (Roteador):** Camada 3. Interliga redes diferentes (LAN e WAN) usando endereços **IP**. Decide a melhor rota.
*   **Modem (Modulador/Demodulador):** Converte sinal Digital (computador) em Analógico (linha telefônica) e vice-versa.
*   **Gateway:** Tradutor universal. Interliga redes com arquiteturas e protocolos incompatíveis. Atua em todas as camadas do modelo TCP/IP.

---

## 6. Padrões IEEE e Tecnologias Sem Fio

### 6.1 Ethernet (802.3) e Token Ring (802.5)
*   **Ethernet (802.3):** Redes cabeadas. Utiliza o método **CSMA/CD** (Detecção de Colisão).
    *   **Backoff:** Quando ocorre uma colisão, o dispositivo espera um tempo **aleatório** (Backoff) antes de tentar retransmitir para evitar novas colisões.
*   **Token Ring (802.5):** Topologia lógica em anel. Uso de um "token" (passe) para transmitir. Sem colisões.

### 6.2 Wi-Fi (802.11)
**Evolução dos Padrões:**

| Padrão | Nome Comercial | Frequência | Taxa Máxima |
| :--- | :--- | :--- | :--- |
| 802.11b | - | 2.4 GHz | 11 Mbps |
| 802.11a | - | 5 GHz | 54 Mbps |
| 802.11g | Wi-Fi 3 | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 / 5 GHz | Até 600 Mbps |
| 802.11ac | Wi-Fi 5 | **5 GHz (Exclusivo)** | 6.9 Gbps |
| 802.11ax | Wi-Fi 6 | 2.4 / 5 GHz | 9.6 Gbps |
| **802.11ax-E** | **Wi-Fi 6E** | **2.4 / 5 / 6.0 GHz** | 9.6 Gbps |
| 802.11be | Wi-Fi 7 | 2.4 / 5 / 6.0 GHz | > 40 Gbps |

**Segurança:** WEP (Fraco/Obsoleto) → WPA → WPA2 (AES) → WPA3 (Forte).

### 6.3 Outros Padrões IEEE
*   **IEEE 802.15 (Bluetooth):** WPAN.
    *   **Piconet:** 1 Mestre + até 7 Escravos ativos (8 totais).
    *   **Classes de Potência:** Classe 1 (100m), Classe 2 (10m), Classe 3 (1m).
*   **IEEE 802.16 (WiMAX):** WMAN. Longo alcance (até 40 km).
*   **IEEE 802.20 (Mobile-Fi):** WWAN. Conexão de banda larga para dispositivos em movimento (veículos).

> **Mnemônico Estratégico:** Para decorar a ordem Wi-Fi: **"BAGUNÇA"**
> (**B**-802.11b, **A**-802.11a, **G**-802.11g, **UN**-802.11n, **CA**-802.11ac).

---

## 7. Internet e Tecnologias Web

### 7.1 Comutação e Protocolos
*   **Comutação por Circuito:** Caminho dedicado (Telefonia). Ineficiente para dados (canal ocupado em silêncio).
*   **Comutação por Pacotes:** Base da Internet. Dados divididos em pacotes com rotas variadas.
*   **TCP/IP:** O IP cuida do endereçamento ("para onde vai"); o TCP cuida do controle e entrega ("como chega").

### 7.2 Camadas da Web
*   **Surface Web:** Indexada (Google). Pública.
*   **Deep Web:** Não indexada. Exige autenticação (e-mails, bancos, sistemas internos). **Não é necessariamente ilegal.**
*   **Dark Web:** Oculta propositalmente. Exige o software **Tor** (The Onion Router - Roteador Cebola). Foco em anonimato total (.onion).

### 7.3 Internet das Coisas (IoT)
Conexão de objetos cotidianos à rede.
*   **Metáfora para memorizar:** Sensores são os **"olhos"** (coleta) e Atuadores são as **"mãos"** (ação).
*   **Tecnologias:** Zigbee (baixa potência), Bluetooth Low Energy (BLE).

---

## 8. Tecnologias de Acesso e ISPs

### 8.1 Métodos de Conexão Residencial
*   **ADSL:** Banda larga via telefone. É **assimétrica** (Download > Upload). O "A" significa Asymmetric. Diferente da Dial-up, permite usar telefone e internet ao mesmo tempo por frequências diferentes.
*   **HFC (Hybrid Fiber-Coax):** Fluxo arquitetural: A Fibra parte do **Backbone**, passa pelos postes até um **Receptor Óptico**, e dali o **Cabo Coaxial** distribui para as casas.
*   **PLC (Power Line Communication):** Internet via rede elétrica. No Brasil, embora autorizada, possui **baixo investimento por razões estratégicas e econômicas**.
*   **Satélite:** Cobertura global. **Curiosidade Técnica:** A Lua pode ser usada como satélite? Teoricamente sim, mas prefere-se satélites artificiais que permitem regenerar o sinal.

### 8.2 Hierarquia de Provedores (ISPs)
*   **Tier 1:** Provedores de backbone mundial. Não pagam trânsito a ninguém (fazem *peering* direto).
*   **Tier 2:** Provedores regionais/nacionais (Vivo, Claro). Compram acesso do Tier 1.
*   **Tier 3:** Provedores locais (de bairro). Dependem totalmente dos níveis superiores.

> **Perguntas da FGV:** A banca costuma cobrar qual nível de ISP não paga pelo tráfego de dados (Tier 1) e o significado da assimetria no ADSL.