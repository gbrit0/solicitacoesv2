# Implementação do Backend para o Sistema de Solicitações

O backend atuará na aplicação como orquestrador dos serviços sendo o ponto de entrada dos dados do frontend, controlado a autenticação junto ao GLPI, gerenciando os tokens de acesso JWT da aplicação e do Protheus, e repassando as solicitações à REST do Protheus.

## API Rest GLPI

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


uvicorn app.main:app --reload 