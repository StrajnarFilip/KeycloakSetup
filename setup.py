from os import urandom
def render(database_password: str,admin_password: str,management_password: str) -> str:
    return f"""services:
  postgresql-keycloak:
    image: postgres:14-alpine3.15
    restart: always
    environment:
      POSTGRES_USER: "postgres"
      POSTGRES_PASSWORD: "{database_password}"
      POSTGRES_DB: "postgres"
    volumes:
      - './postgres:/var/lib/postgresql/data'
  keycloak:
    image: docker.io/bitnami/keycloak:latest
    restart: always
    ports:
      - "49001:8080"
    environment:
      KEYCLOAK_DATABASE_HOST: postgresql-keycloak
      KEYCLOAK_DATABASE_PORT: 5432
      KEYCLOAK_DATABASE_NAME: postgres
      KEYCLOAK_DATABASE_USER: postgres
      KEYCLOAK_DATABASE_PASSWORD: "{database_password}"
      KEYCLOAK_CREATE_ADMIN_USER: true
      KEYCLOAK_ADMIN_USER: admin
      KEYCLOAK_ADMIN_PASSWORD: "{admin_password}"
      KEYCLOAK_MANAGEMENT_USER: manager
      KEYCLOAK_MANAGEMENT_PASSWORD: "{management_password}"
      
    depends_on:
      - postgresql-keycloak
    volumes:
      - './mynewtheme:/opt/bitnami/keycloak/themes/mynewtheme'"""


with open("docker-compose.yaml","w") as file:
    file.write(render(urandom(32).hex(),urandom(32).hex(),urandom(32).hex()))