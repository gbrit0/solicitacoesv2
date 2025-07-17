# Implementação do Backend para o Sistema de Solicitações

O backend atuará na aplicação como orquestrador dos serviços sendo o ponto de entrada dos dados do frontend, controlado a autenticação junto ao GLPI, gerenciando os tokens de acesso JWT da aplicação e do Protheus, e repassando as solicitações à REST do Protheus.

## API Rest GLPI

A implementação do backend se baseia na documentação da API do GLPI e usa dois endpoints, init e kill Session. A ideia é utilizar o cadastro de usuário GLPI como login padrão para a aplicação. O endpoint valida usuário e senha e retorna um token de sessão para acessos ao GLPI. Entretanto, como o interesse é somente validar o usuário, logo após a confirmação, recebendo o token, a sessão é encerrada no GLPI. O sistema de solicitações, contudo, gerará um JWT para si a fim de manter um tempo limite de login e facilitar a lógica de logout. O token será gravado no cache do navegador, quando o usuário sair da aplicação, será apagado. Caso exceda o limite de tempo de 15 minutos, a solicitação não será aceita pelo sistema e o usuário terá de logar novamente.

* ### Init session

   * URL: apirest.php/initSession/

   * Description: Request a session token to uses other API endpoints.

   * Method: GET

   * Parameters: (Headers)

      * a couple login & password: 2 parameters to login with user authentication. You should pass this 2 parameters in http basic auth. It consists in a Base64 string with login and password separated by ":" A valid Authorization header is:

         ```"Authorization: Basic base64({login}:{password})"```

   * Returns:

      * 200 (OK) with the session_token string.

      * 400 (Bad Request) with a message indicating an error in input parameter.

      * 401 (UNAUTHORIZED)

   * Example:

      ```bash
      $ curl -X GET \
         -H 'Content-Type: application/json' \
         -H "Authorization: Basic Z2xwaTpnbHBpasdf84qwe546asdf465weda5" \
         'http://path/to/glpi/apirest.php/initSession'
      ```

* ### Kill session

   * URL: apirest.php/killSession/

   * Description: Destroy a session identified by a session token.

   *  Method: GET

   * Parameters: (Headers)

      * Session-Token: session var provided by initSession endpoint. Mandatory.

   * Returns:

      * 200 (OK).

      * 400 (Bad Request) with a message indicating an error in input parameter.

   * Example :

      ```bash
      $ curl -X GET \
      -H 'Content-Type: application/json' \
      -H "Session-Token: 83af7e620c83a50a18d3eac2f6ed05a3ca0bea62" \
      'http://path/to/glpi/apirest.php/killSession'
      ```

## API Rest Protheus

A implementação da API Rest do Protheus neste orquestrador consiste basicamente da réplica dos endpoints da API original, com exceção da autenticação que será feita, na primeira camada com o Glpi. A segunda camada usará um usuário único para todas as solicitações e lidará com a autenticação junto ao Protheus. A lógica de autenticação do Protheus implementa tokens de acesso Bearer token. Esse token é resultado de um POST no endpoint /token e tem uma validade de curta duração. Seu contexto de acesso pode variar de acordo com o usuário que está se autenticando.

* ###  Token

   * URL: /rest/api/oauth2/v1/token/

   * Description: Request a session token to uses other API endpoints.

   * Method: POST

   * Query Parameters:

      * grant_type: 'password'

   * Headers

      * password: senha do usuário

      * username: usuário do sistema (Protheus)

   * Returns:

      ```bash
         {
            "access_token": "eyJhbGciOiJIUzI1Ni...",
            "refresh_token": "YEv3dtFbNCisITD3y...",
            "scope": "default",
            "token_type": "Bearer",
            "expires_in": 3600,
            "hasMFA": false
         }
      ```

De posse então do access_token, basta fazer a requisição à API desejada incluindo no cabeçalho a parâmetro Authorization com o valor Bearer mais o token de acesso.

* ### A atualização do token

Após a expiração do token de acesso, ao tentar requisitar alguma API protegida, será retornado o status 401 de não autorizado, como se não houvesse sido enviado um token de acesso.

É o momento então de requisitar para a mesma API de token a atualização conforme o exemplo abaixo:

   * URL: /rest/api/oauth2/v1/token/

   * Description: Request a session token to uses other API endpoints.

   * Method: POST

   * Query Parameters:

      * grant_type: 'refresh_token'
      * refresh_token: Toke recebido na requisição anterior

   * Headers

      * password: senha do usuário

      * username: usuário do sistema (Protheus)

   * Returns:

      ```bash
      {    
         "access_token": "eyJhbGciOiJIUzI1NiIsInR...",
         "refresh_token": "YEv3dtFbNCisMST1yztKi5...",
         "scope": "default",
         "token_type": "Bearer",
         "expires_in": 3600,
         "hasMFA": false
      }
      ```

## Para iniciar o backend

```uvicorn app.main:app # --reload ```