# Nuvem Quiz

## Question 1
No modelo de responsabilidade compartilhada da computação em nuvem, o provedor de Infraestrutura como Serviço (IaaS) assume a gestão de quais camadas da arquitetura?

- [x] Virtualização, servidores físicos, rede e armazenamento.
- [ ] Sistemas operacionais, middlewares, runtime e dados.
- [ ] Aplicações de usuário final e controle de acesso a dados sensíveis.
- [ ] Ambientes de desenvolvimento, compiladores e bibliotecas de sistema.
- [ ] Segurança lógica de rede interna e patches do kernel do sistema operacional convidado.

**Hint:** Considere o nível mais baixo de abstração onde o hardware é transformado em recurso virtual.

## Question 2
A computação serverless, frequentemente associada ao modelo Function-as-a-Service (FaaS), apresenta características específicas de execução. Assinale a afirmativa tecnicamente correta sobre esse modelo.

- [x] O modelo baseia-se em programação stateless, onde o estado não é persistido nativamente entre execuções de funções.
- [ ] O provedor garante a persistência do estado (stateful) em memória volátil para otimizar o tempo de resposta em chamadas subsequentes.
- [ ] A cobrança no modelo FaaS é baseada em instâncias reservadas, independentemente do volume real de execuções mensais.
- [ ] O desenvolvedor deve configurar manualmente o auto-scaling dos servidores subjacentes para suportar picos de tráfego.
- [ ] O uso de contêineres é obrigatório e visível ao desenvolvedor, que deve gerenciar o orquestrador de pods durante o deploy.

**Hint:** Pense sobre a persistência de dados entre uma chamada de função e outra.

## Question 3
O NIST define cinco características essenciais para a computação em nuvem. Aquela que garante que os recursos sejam alocados e liberados de forma dinâmica e quase instantânea é a:

- [x] Elasticidade Rápida.
- [ ] Escalabilidade Vertical.
- [ ] Agrupamento de Recursos.
- [ ] Amplo Acesso à Rede.
- [ ] Autosserviço sob Demanda.

**Hint:** Esta característica está ligada à agilidade do sistema em 'esticar' ou 'encolher' conforme a necessidade.

## Question 4
Sobre os modelos de implantação de nuvem, a nuvem comunitária (Community Cloud) diferencia-se da nuvem privada principalmente pelo fato de que:

- [x] A infraestrutura é compartilhada por diversas organizações que possuem preocupações e requisitos comuns de conformidade ou missão.
- [ ] O acesso é aberto ao público geral mediante pagamento por uso, garantindo isolamento total por meio de criptografia.
- [ ] A gestão dos dados é obrigatoriamente realizada por um terceiro, sendo vedada a administração interna por qualquer membro da comunidade.
- [ ] Os recursos computacionais são fixos e não permitem elasticidade, visando garantir a soberania digital dos entes envolvidos.
- [ ] Trata-se de uma extensão da nuvem pública onde o provedor reserva hardware físico exclusivo para um único cliente corporativo.

**Hint:** Foque no perfil dos usuários e na razão do compartilhamento dos recursos.

## Question 5
O modelo Platform-as-a-Service (PaaS) é ideal para desenvolvedores de software. Nesse contexto, assinale a opção que descreve corretamente uma limitação ou responsabilidade do usuário nesse modelo.

- [x] O usuário possui controle sobre a configuração das aplicações e, ocasionalmente, do ambiente de hospedagem, mas não do sistema operacional.
- [ ] O desenvolvedor deve realizar a instalação e a atualização manual de patches de segurança do kernel Linux ou Windows Server.
- [ ] A elasticidade é inexistente, exigindo que o desenvolvedor solicite formalmente ao provedor o aumento de memória RAM via ticket de suporte.
- [ ] O usuário é responsável pela manutenção física dos servidores e pela refrigeração do data center onde a plataforma reside.
- [ ] O modelo PaaS restringe o uso de linguagens de programação, permitindo exclusivamente o desenvolvimento em HTML e CSS estáticos.

**Hint:** Pense no que o desenvolvedor deixa de gerenciar para ganhar produtividade.

## Question 6
Considere o conceito de agrupamento de recursos (Resource Pooling) do NIST. Qual é o mecanismo fundamental que permite que esse agrupamento ocorra mantendo a privacidade e segurança dos dados de diferentes clientes?

- [x] Multi-tenancy sustentado por tecnologias de virtualização e isolamento lógico.
- [ ] Uso de instâncias preemptivas que bloqueiam o acesso de outros usuários durante o processamento de dados sensíveis.
- [ ] Instalação de firewalls físicos dedicados para cada máquina virtual de cada cliente no data center.
- [ ] Replicação de dados em tempo real em nuvens de diferentes fornecedores (cloud bursting) para evitar vazamentos.
- [ ] Alocação de hardware exclusivo (Single-tenancy) como requisito obrigatório para qualquer serviço classificado como nuvem.

**Hint:** Lembre-se da metáfora de vários inquilinos morando em um mesmo prédio (infraestrutura).

## Question 7
Em relação aos custos na computação em nuvem, o modelo de 'Instâncias Reservadas' é comparado às 'Instâncias sob Demanda'. Sobre essa comparação, assinale a afirmativa correta.

- [x] Instâncias reservadas oferecem descontos significativos em troca de um compromisso de uso por longo prazo (1 a 3 anos).
- [ ] Instâncias reservadas são mais caras que instâncias sob demanda, pois garantem prioridade absoluta de CPU em casos de desastres globais.
- [ ] O modelo pay-as-you-go aplica-se apenas a instâncias reservadas, sendo as instâncias sob demanda cobradas por boletos fixos trimestrais.
- [ ] Instâncias reservadas podem ser desligadas pelo provedor a qualquer momento (preemptivas) caso haja alta demanda de outros usuários.
- [ ] A reserva de instâncias elimina a necessidade de monitoramento e de serviços mensuráveis, pois o custo torna-se fixo e ilimitado.

**Hint:** Pense no equilíbrio entre flexibilidade imediata e economia planejada.

## Question 8
Ao migrar sistemas legados para a nuvem, um conceito fundamental é o de 'Acoplamento Fraco' (Loosely Coupled). Por que essa abordagem é preferida em arquiteturas de nuvem?

- [x] Permite que os componentes do sistema operem de forma independente, facilitando a escalabilidade e a resiliência a falhas.
- [ ] Reduz a necessidade de conexões de internet, uma vez que os componentes legados passam a depender exclusivamente do hardware local.
- [ ] Garante que todos os dados sejam processados de forma stateful, mantendo a sessão do usuário fixa em um único servidor físico.
- [ ] Torna obrigatória a unificação de todas as funcionalidades em um único executável monolítico para otimizar o tempo de CPU.
- [ ] Elimina a necessidade de APIs, permitindo que as aplicações acessem diretamente a memória RAM umas das outras para maior velocidade.

**Hint:** Pense no que acontece com o sistema se um pedaço dele parar de funcionar.

## Question 9
Sobre a Nuvem Híbrida, o termo 'Cloud Bursting' refere-se a uma estratégia específica de gerenciamento de tráfego. Assinale a opção que a descreve corretamente.

- [x] Uma aplicação roda em nuvem privada e utiliza a nuvem pública para absorver picos de demanda temporários.
- [ ] Ocorre quando dados sensíveis de uma nuvem pública são 'explodidos' (deletados) automaticamente após o término de um contrato.
- [ ] Trata-se da migração definitiva e irreversível de todos os serviços de uma nuvem comunitária para uma nuvem pública gratuita.
- [ ] É o processo de sincronização de backups entre dois provedores de nuvem pública para garantir a durabilidade dos dados.
- [ ] Refere-se ao bloqueio total do acesso à internet quando o limite de custos mensais da nuvem híbrida é atingido.

**Hint:** Imagine uma represa (nuvem privada) que usa um canal extra (nuvem pública) quando o nível da água sobe demais.

## Question 10
No contexto da segurança e conformidade (LGPD) em ambientes de nuvem pública, qual é a responsabilidade do Controlador de dados ao contratar um provedor de nuvem (Operador)?

- [x] Garantir a base legal para o tratamento e selecionar provedores que ofereçam garantias de medidas técnicas e administrativas de segurança.
- [ ] O controlador fica isento de qualquer responsabilidade civil, uma vez que o provedor de nuvem assume os riscos integrais ao aceitar o contrato.
- [ ] Configurar fisicamente os firewalls de hardware e as câmeras de vigilância nos data centers do provedor de nuvem.
- [ ] A responsabilidade é transferida automaticamente para a ANPD (Autoridade Nacional de Proteção de Dados) assim que os dados sobem para a nuvem.
- [ ] Garantir que a nuvem seja privada e local, sendo vedada pela LGPD a transferência internacional de dados para provedores globais como AWS ou Azure.

**Hint:** Pense no dever de cuidado de quem 'dono' do dado ao escolher quem vai processá-lo.
