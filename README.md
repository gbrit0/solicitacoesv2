# Sistema de Solicitações V2

Recriação do sistema de solicitações ao Almoxarifado e ao Armazém. Aplicação de interface React criada com lovable e integração no backend com API's REST do Protheus e do GLPI.

```mermaid
   flowchart LR
      %% Usuário acessando o frontend
      User[Usuário] --> Frontend["Frontend (Web/App)"]

      %% Comunicação entre frontend e backend
      Frontend --> |API REST| Backend["Backend"]

      %% Backend se comunica com sistemas externos
      Backend --> |Autentição| GLPI[GLPI]
      Backend --> |Integração| Protheus[Protheus REST API]
```
