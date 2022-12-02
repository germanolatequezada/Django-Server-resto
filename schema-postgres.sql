DROP TABLE IF EXISTS auth_user_user_permissions;
DROP TABLE IF EXISTS auth_user_groups;
DROP TABLE IF EXISTS authtoken_token;
DROP TABLE IF EXISTS auth_group_permissions;
DROP TABLE IF EXISTS auth_permission;
DROP TABLE IF EXISTS django_admin_log;
DROP TABLE IF EXISTS auth_group;
DROP TABLE IF EXISTS auth_user;
DROP TABLE IF EXISTS django_content_type;
DROP TABLE IF EXISTS django_session;
DROP TABLE IF EXISTS django_migrations;
DROP TABLE IF EXISTS jet_bookmark;
DROP TABLE IF EXISTS jet_pinnedapplication;
DROP TABLE IF EXISTS pedidos_cliente;
DROP TABLE IF EXISTS pedidos_ingrediente;
DROP TABLE IF EXISTS pedidos_mesa;
DROP TABLE IF EXISTS pedidos_modulo;
DROP TABLE IF EXISTS pedidos_plato;
DROP TABLE IF EXISTS pedidos_sucursales;
DROP TABLE IF EXISTS pedidos_usuario;
DROP TABLE IF EXISTS pedidos_comanda;
DROP TABLE IF EXISTS pedidos_comanda_detalle;


CREATE TABLE auth_group (
    id BIGSERIAL PRIMARY KEY,
    name varchar(150) NOT NULL UNIQUE
);

CREATE TABLE auth_user(
	id BIGSERIAL PRIMARY KEY,
	password varchar(128) NOT NULL,
	last_login	timestamp,
	is_superuser boolean NOT NULL,
	username varchar(150) NOT NULL UNIQUE,
	first_name varchar(150) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff boolean NOT NULL,
	is_active boolean NOT NULL,
	date_joined timestamp
);

/* ADD USER admin WITH PASS admin*/
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES
('pbkdf2_sha256$320000$qdBAYBozHfVYRtXzLY3hMp$sZD+L0yEbVW1FOCnBh48CDZxmA+xWcMnmQ4Epo9Ahk4=', NULL, true,
    'admin', 'Administrator', 'Administrator', 'admin@admin.cl', true, true, now());

SELECT COUNT(1) FROM auth_user;

CREATE TABLE django_content_type (
	id BIGSERIAL PRIMARY KEY,
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
   	CONSTRAINT django_content_type_app_label_model
	   UNIQUE (app_label, model)
);

INSERT INTO django_content_type (app_label, model) VALUES ('admin', 'logentry');
INSERT INTO django_content_type (app_label, model) VALUES ('auth', 'permission');
INSERT INTO django_content_type (app_label, model) VALUES ('auth', 'group');
INSERT INTO django_content_type (app_label, model) VALUES ('auth', 'user');
INSERT INTO django_content_type (app_label, model) VALUES ('contenttypes', 'contenttype');
INSERT INTO django_content_type (app_label, model) VALUES ('sessions', 'session');
INSERT INTO django_content_type (app_label, model) VALUES ('userapi', 'usuario');
INSERT INTO django_content_type (app_label, model) VALUES ('authtoken', 'token');
INSERT INTO django_content_type (app_label, model) VALUES ('authtoken', 'tokenproxy');
/* ADD CONTENT SCHEMA WEB_SHOPPING*/
--INSERT INTO django_content_type (app_label, model) VALUES ('web_shopping', 'billing_type');

SELECT COUNT(1) FROM django_content_type;


CREATE TABLE django_admin_log (
	id BIGSERIAL PRIMARY KEY,
	action_time timestamp NOT NULL,
	object_id text,
	object_repr varchar(200) NOT NULL,
	action_flag smallint NOT NULL CHECK (action_flag > 0),
	change_message text NOT NULL,
	content_type_id bigint,
	user_id bigint,
   	CONSTRAINT fk_django_admin_log_content_type_id
    	FOREIGN KEY(content_type_id) 
	 	REFERENCES django_content_type(id),
    	FOREIGN KEY(user_id) 
	 	REFERENCES auth_user(id)
);

CREATE TABLE django_session (
    session_key varchar(40) PRIMARY KEY,
    session_data text NOT NULL,
    expire_date timestamp NOT NULL
);

CREATE TABLE django_migrations (
    id BIGSERIAL PRIMARY KEY,
    app varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    applied timestamp NOT NULL
);

INSERT INTO django_migrations (app, name, applied) VALUES ('contenttypes', '0001_initial', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0001_initial', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('admin', '0001_initial', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('admin', '0002_logentry_remove_auto_add', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('admin', '0003_logentry_add_action_flag_choices', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('contenttypes', '0002_remove_content_type_name', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0002_alter_permission_name_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0003_alter_user_email_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0004_alter_user_username_opts', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0005_alter_user_last_login_null', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0006_require_contenttypes_0002', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0007_alter_validators_add_error_messages', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0008_alter_user_username_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0009_alter_user_last_name_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0010_alter_group_name_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0011_update_proxy_permissions', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('auth', '0012_alter_user_first_name_max_length', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('sessions', '0001_initial', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('authtoken', '0001_initial', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('authtoken', '0002_auto_20160226_1747', now());
INSERT INTO django_migrations (app, name, applied) VALUES ('authtoken', '0003_tokenproxy', now());

CREATE TABLE auth_permission (
    id BIGSERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename varchar(100) NOT NULL,
   	CONSTRAINT auth_permission_content_type_id_codename
	   UNIQUE (content_type_id, codename),
   	CONSTRAINT auth_permission_content_type_id
    	FOREIGN KEY(content_type_id) 
	 	REFERENCES django_content_type(id)
);

INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add log entry', 1, 'add_logentry');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change log entry', 1, 'change_logentry');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete log entry', 1, 'delete_logentry');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view log entry', 1, 'view_logentry');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add permission', 2, 'add_permission');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change permission', 2, 'change_permission');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete permission', 2, 'delete_permission');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view permission', 2, 'view_permission');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add group', 3, 'add_group');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change group', 3, 'change_group');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete group', 3, 'delete_group');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view group', 3, 'view_group');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add user', 4, 'add_user');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change user', 4, 'change_user');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete user', 4, 'delete_user');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view user', 4, 'view_user');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add content type', 5, 'add_contenttype');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change content type', 5, 'change_contenttype');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete content type', 5, 'delete_contenttype');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view content type', 5, 'view_contenttype');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add session', 6, 'add_session');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change session', 6, 'change_session');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete session', 6, 'delete_session');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view session', 6, 'view_session');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add usuario', 7, 'add_usuario');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change usuario', 7, 'change_usuario');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete usuario', 7, 'delete_usuario');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view usuario', 7, 'view_usuario');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add Token', 8, 'add_token');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change Token', 8, 'change_token');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete Token', 8, 'delete_token');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view Token', 8, 'view_token');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add token', 9, 'add_tokenproxy');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can change token', 9, 'change_tokenproxy');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can delete token', 9, 'delete_tokenproxy');
INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can view token', 9, 'view_tokenproxy');
/* ADD PERMISSION WEB_SHOPPING */
--INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('Can add Country', 
--    (select id FROM django_content_type WHERE app_label = 'web_shopping' and model = 'country'), 'add_country');


SELECT COUNT(1) FROM auth_permission;

CREATE TABLE auth_group_permissions (
    id BIGSERIAL PRIMARY KEY,
    group_id bigint NOT NULL,
    permission_id bigint NOT NULL,
   	CONSTRAINT auth_group_permissions_group_id_permission_id
	   UNIQUE (group_id, permission_id),
   	CONSTRAINT auth_group_permissions_group_id
    	FOREIGN KEY(group_id) 
	 	REFERENCES auth_group(id),
   	CONSTRAINT auth_group_permissions_auth_permission
    	FOREIGN KEY(permission_id) 
	 	REFERENCES auth_permission(id)     
);

CREATE TABLE auth_user_groups (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    user_id bigint NOT NULL,
    group_id bigint NOT NULL,
    CONSTRAINT auth_user_groups_user_id_group_id UNIQUE (user_id, group_id),
   	CONSTRAINT auth_user_groups_user_id
    	FOREIGN KEY(user_id) 
	 	REFERENCES auth_user(id),
   	CONSTRAINT auth_user_groups_group_id
    	FOREIGN KEY(group_id) 
	 	REFERENCES auth_group(id)
);

CREATE TABLE authtoken_token (
    key varchar(40) PRIMARY KEY,
    created timestamp NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id),
   	CONSTRAINT authtoken_token_user_id
    	FOREIGN KEY(user_id) 
	 	REFERENCES auth_user(id)
);

CREATE TABLE auth_user_user_permissions (
    id BIGSERIAL PRIMARY KEY,
    user_id bigint NOT NULL,
    permission_id bigint NOT NULL,
    CONSTRAINT auth_user_user_permissions_user_id_permission_id UNIQUE (user_id, permission_id),
   	CONSTRAINT auth_user_user_permissions_permission_id
    	FOREIGN KEY(permission_id) 
	 	REFERENCES auth_permission(id),
   	CONSTRAINT auth_user_user_permissions_user_id
    	FOREIGN KEY(user_id) 
	 	REFERENCES auth_user(id)
);

CREATE TABLE jet_bookmark(
    id BIGSERIAL PRIMARY KEY,
	url varchar(200) NOT NULL,
	title varchar(255) NOT NULL,
	user_id bigint NOT NULL,
	date_add timestamp NOT NULL
);

CREATE TABLE jet_pinnedapplication(
    id BIGSERIAL PRIMARY KEY,
	app_label varchar(255) NOT NULL,
	user_id bigint NOT NULL,
	date_add timestamp NOT NULL
);

CREATE TABLE  pedidos_cliente (
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	apellido_paterno varchar(30) NOT NULL,
	rut varchar(30) NOT NULL
);

INSERT INTO pedidos_cliente (nombre, apellido_paterno, rut) VALUES ('admin', 'admin', '1-9');
INSERT INTO pedidos_cliente (nombre, apellido_paterno, rut) VALUES ('Barbara', 'Farias', '1-1');

CREATE TABLE pedidos_ingrediente(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	unidad varchar(30) NOT NULL
);

/*MESAS */
INSERT INTO pedidos_ingrediente (nombre, unidad) VALUES ('Diente de Ajo', 30);
INSERT INTO pedidos_ingrediente (nombre, unidad) VALUES ('Cebollin', 30);
INSERT INTO pedidos_ingrediente (nombre, unidad) VALUES ('Lomo kg.', 10);
INSERT INTO pedidos_ingrediente (nombre, unidad) VALUES ('Pollo kg.', 30);

CREATE TABLE pedidos_mesa(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	capacidad int NOT NULL
);

/*MESAS */
INSERT INTO pedidos_mesa (nombre, capacidad) VALUES ('Mesa 9', 3);
INSERT INTO pedidos_mesa (nombre, capacidad) VALUES ('Mesa 1', 5);

CREATE TABLE pedidos_modulo(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL
);


CREATE TABLE pedidos_plato(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	tiempo_preparacion_min int NOT NULL,
	tipo varchar(30) NOT NULL,
	url_img varchar(80),
	precio bigint,
	id_ingrediente1 bigint,
	id_ingrediente2 bigint,
	id_ingrediente3 bigint,
	id_ingrediente4 bigint,
	id_ingrediente5 bigint
);
/*PLATOS TIPICOS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('biffe a lo pobre', 45, 'plato tipico', 'img/plato_tipico/biffe_a_lo_pobre.jpg', 12590);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('cazuela de vacuno', 45, 'plato tipico', 'img/plato_tipico/cazuela_de_vacuno.jpg', 3550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('empanada', 30, 'plato tipico', 'img/plato_tipico/empanada.jpg', 1980);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('humita', 30, 'plato tipico', 'img/plato_tipico/humita.jpg', 2550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('pantruca', 45, 'plato tipico', 'img/plato_tipico/pantruca.jpg', 3150);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('pastel de choclo', 60, 'plato tipico', 'img/plato_tipico/pastel_de_choclo.jpg', 5680);

/*SOPAS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('acelga', 30, 'sopa', 'img/sopa/acelga.jpg', 2550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('champiñones', 30, 'sopa', 'img/sopa/champiñones.jpg', 2550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('garbanzos', 30, 'sopa', 'img/sopa/garbanzos.jpg', 2550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('esparragos', 30, 'sopa', 'img/sopa/esparragos.jpg', 2550);
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('crema de porotos', 30, 'sopa', 'img/sopa/crema_de_porotos.jpg', 2550);

/*ENSALADAS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('ensalada mixta', 15, 'ensalada', 'img/ensalada/ensalada_mixta.jpg', 1800);

/*HELADOS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('barquillo', 15, 'helado', 'img/helado/barquillo.jpg', 2850);

/*MOUSSES*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('volcan de chocolate', 15, 'mousse', 'img/mousse/volcan_de_chocolate.jpg', 3560);

/*TORTAS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('pastel de trufa', 15, 'pastel', 'img/pastel/pastel_de_trufa.jpg', 3600);

/*CERVEZAS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('cerveza artesanal', 15, 'cerveza', 'img/cerveza/cerveza_artesanal.jpg', 2800);

/*BEBIDAS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('refresco ccu', 15, 'bebida', 'img/bebida/refresco_ccu.jpg', 1880);

/*JUGOS*/
INSERT INTO pedidos_plato(nombre, tiempo_preparacion_min, tipo, url_img, precio) VALUES ('jugo_natural', 15, 'jugo', 'img/jugo/jugo_natural.jpg', 3250);

CREATE TABLE pedidos_sucursales(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	direccion varchar(30) NOT NULL
);


CREATE TABLE pedidos_usuario(
    id BIGSERIAL PRIMARY KEY,
	nombre varchar(30) NOT NULL,
	apellido_paterno varchar(30) NOT NULL,
	rut varchar(30) NOT NULL
);


CREATE TABLE pedidos_comanda(
    id BIGSERIAL PRIMARY KEY,
	id_mesa bigint NOT NULL,
	id_usuario bigint NOT NULL,
	id_cliente bigint NOT NULL,
	fecha_inicio TIMESTAMP,
	fecha_fin TIMESTAMP
);

CREATE TABLE pedidos_comanda_detalle(
    id BIGSERIAL PRIMARY KEY,
	id_comanda bigint NOT NULL,
	id_plato bigint NOT NULL,
	cantidad int NOT NULL,
	precio int NOT NULL
);
